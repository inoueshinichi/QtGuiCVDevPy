"""シェーディング"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, TypeVar, NoReturn, Generic)
from collections import namedtuple

# サードパーティ
import numpy as np
import scipy as sp
from scipy.ndimage import filters
import cv2
from PIL import Image
import skimage

# 自作


"""
OK シェーディング補正(輝度ムラを取り除く処理)
-- シフト処理
"""


def shading_correction(master:np.ndarray, base:np.ndarray, gain:float=1.0) -> np.ndarray:
    """
    シェーディング補正
    :param master: 輝度ムラがある補正対象画像(前景が写ってる)
    :param base: 補正に使用する全体的な明暗変化を表した明暗分布画像(およそ補正対象画像の背景成分が強い画像)
    :return:
    """
    assert master.ndim == 2, "master must be grayscale; 2dim."
    assert base.ndim == 2, "base must be grayscale; 2dim."
    assert master.shape == base.shape, \
        "master and base must be same shape. master:{0}, base:{1}".format(master.shape, base.shape)

    tmp_master = master.astype(np.float64)
    tmp_base = base.astype(np.float64)

    # 画素値1.0以下を1.0に制限
    tmp_master[tmp_master < 1.0] = 1.0
    tmp_base[tmp_base < 1.0] = 1.0

    # シェーディング補正
    diff_element = (tmp_master / tmp_base) * 128.0 - 128.0 # base画像に対してmaster画像の変化が大きな輝度成分だけを取り出す
    dst = 128.0 + diff_element * gain
    dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)

    return dst

def shift_shading(src:np.ndarray, shift_value:int, shift_direct:str, emphasize:float):
    """
    シフトシェーディング処理
    :param src:
    :param shift_value: 1, 2, 3, ...
    :param shift_direct: 左:'left', 上:'top', 右:'right', 下:'bottom', 左上:'left-top', 右上:'right-top',
                        右下:'right-bottom', 左下:'left-bottom', 上下左右:'cross', 8方向:'all'
    :param emphasize: 強調係数
    :return:
    """
    assert shift_value > 0, "shift_value must be > 0. given is {0}".format(shift_value)

    if src.ndim == 2:
        src_ = src.reshape(src.shape[0], src.shape[1], 1)
        height, width = src_.shape[:2]
        channels = 1
        img_tmp = np.zeros((height + shift_value * 2, width + shift_value * 2, 1), dtype=np.float32)
    elif src.ndim == 3:
        height, width, channels = src.shape
        img_tmp = np.zeros((height + shift_value * 2, width + shift_value * 2, channels), dtype=np.float32)
    else:
        assert False, "shape of src must be (N,M) or (N,M,C). given is {0}".format(src.shape)

    # 淵が黒の画像
    img_tmp[shift_value:shift_value+height, shift_value:shift_value+width] = src_.copy()

    # 淵を平均値で埋める
    # img_left = img_tmp[:, 0:shift_value]
    # img_right = img_tmp[:, -shift_value:]
    # img_up = img_tmp[0:shift_value, :]
    # img_bottom = img_tmp[-shift_value:, :]

    img_left_chunk = img_tmp[:, shift_value:shift_value*2]
    img_left_mean = np.mean(img_left_chunk, axis=1)[:, None, :] # (N,shift_value,C) -> (N,1,C)
    img_tmp[:, 0:shift_value] = img_left_mean # Broadcast

    img_right_chunk = img_tmp[:, shift_value+width:]
    img_right_mean = np.mean(img_right_chunk, axis=1)[:, None, :]
    img_tmp[:, shift_value+width:] = img_right_mean

    img_top_chunk = img_tmp[0:shift_value, :]
    img_top_mean = np.mean(img_top_chunk, axis=0)[None, :, :] # (shift_value,M,C) -> (1,M,C)
    img_tmp[0:shift_value, :] = img_top_mean # Broadcast

    img_bottom_chunk = img_tmp[height+shift_value:, :]
    img_bottom_mean = np.mean(img_bottom_chunk, axis=0)[None, :, :]
    img_tmp[-shift_value:, :] = img_bottom_mean

    # シフト処理
    if shift_direct == "left":
        img_shift = src_ - img_tmp[shift_value:shift_value+height, 0:width]
        pass
    elif shift_direct == "top":
        img_shift = src_ - img_tmp[0:height, shift_value:shift_value+width]
        pass
    elif shift_direct == "right":
        img_shift = src_ - img_tmp[shift_value:shift_value+height, -width:]
        pass
    elif shift_direct == "bottom":
        img_shift = src_ - img_tmp[-height:, shift_value:shift_value+width]
        pass
    elif shift_direct == "left-top":
        img_shift = src_ - img_tmp[0:height, 0:width]
        pass
    elif shift_direct == "right-top":
        img_shift = src_ - img_tmp[0:height, shift_value*2:]
        pass
    elif shift_direct == "right-bottom":
        img_shift = src_ - img_tmp[-height:, shift_value*2:]
        pass
    elif shift_direct == "left-bottom":
        img_shift = src_ - img_tmp[-height:, 0:width]
        pass
    elif shift_direct == "cross":
        img_left = img_tmp[shift_value:shift_value+height, 0:width]
        # img_right = img_tmp[shift_value:shift_value+height, -width:]
        # img_top = img_tmp[0:height, shift_value:shift_value+width]
        # img_bottom = img_tmp[-height:, shift_value:shift_value+width]

        img_shift = np.zeros_like(img_left)
        for i in range(img_left.shape[0]):
            for j in range(img_left.shape[1]):
                lum_c = img_tmp[shift_value + i + 0, shift_value + j + 0] # center
                lum_t = img_tmp[shift_value + i - shift_value, shift_value + j + 0] # top
                lum_b = img_tmp[shift_value + i + shift_value, shift_value + j + 0] # bottom
                lum_l = img_tmp[shift_value + i + 0, shift_value + j - shift_value] # left
                lum_r = img_tmp[shift_value + i + 0, shift_value + j + shift_value] # right

                ans_1 = 2 * lum_c - (lum_t + lum_b)
                ans_2 = 2 * lum_c - (lum_l + lum_r)

                if abs(ans_1) > abs(ans_2):
                    ans = ans_1
                else:
                    ans = ans_2

                ans = ans / 2

                img_shift[i, j] = ans

        # 上のプログラムの結果と違う;;;
        # 原因わからず
        # img_shift = np.zeros_like(img_left)
        # for c in range(channels):
        #     src_slice = src_[:, :, c]
        #     img_left = img_left[:, :, c]
        #     img_right = img_right[:, :, c]
        #     img_top = img_top[:, :, c]
        #     img_bottom = img_bottom[:, :, c]
        #
        #     img_shift_lr = 2 * src_slice - (img_left + img_right)
        #     img_shift_lr_abs = np.abs(img_shift_lr)
        #     img_shift_tb = 2 * src_slice - (img_top + img_bottom)
        #     img_shift_tb_abs = np.abs(img_shift_tb)
        #
        #     img_shift_lr_mask = img_shift_lr_abs > img_shift_tb_abs
        #     img_shift_tb_mask = np.logical_not(img_shift_lr_mask)
        #     img_shift_lr_mask = img_shift_lr_mask.astype(np.uint8)
        #     img_shift_tb_mask = img_shift_tb_mask.astype(np.uint8)
        #
        #     img_shift[:, :, c] = img_shift_lr * img_shift_lr_mask + img_shift_tb * img_shift_tb_mask

        # img_shift = 4 * src_ - (img_left + img_right + img_top + img_bottom)
        img_shift = img_shift / 2
        pass
    elif shift_direct == "all":
        img_left = img_tmp[shift_value:shift_value + height, 0:width]
        # img_right = img_tmp[shift_value:shift_value + height, -width:]
        # img_top = img_tmp[0:height, shift_value:shift_value + width]
        # img_bottom = img_tmp[-height:, shift_value:shift_value + width]

        img_shift = np.zeros_like(img_left)
        for i in range(img_left.shape[0]):
            for j in range(img_left.shape[1]):
                lum_c = img_tmp[shift_value + i + 0, shift_value + j + 0]  # center
                lum_t = img_tmp[shift_value + i - shift_value, shift_value + j + 0]  # top
                lum_b = img_tmp[shift_value + i + shift_value, shift_value + j + 0]  # bottom
                lum_l = img_tmp[shift_value + i + 0, shift_value + j - shift_value]  # left
                lum_r = img_tmp[shift_value + i + 0, shift_value + j + shift_value]  # right

                lum_lt = img_tmp[shift_value + i - shift_value, shift_value + j - shift_value] # left-top
                lum_lb = img_tmp[shift_value + i + shift_value, shift_value + j - shift_value] # left-bottom
                lum_rt = img_tmp[shift_value + i - shift_value, shift_value + j + shift_value] # right-top
                lum_rb = img_tmp[shift_value + i + shift_value, shift_value + j + shift_value] # right-bottom

                ans_1 = 2 * lum_c - (lum_t + lum_b)
                ans_2 = 2 * lum_c - (lum_l + lum_r)

                if abs(ans_1) > abs(ans_2):
                    ans_3 = ans_1
                else:
                    ans_3 = ans_2

                ans_4 = 2 * lum_c - (lum_lt + lum_rb)
                ans_5 = 2 * lum_c - (lum_lb + lum_rt)

                if abs(ans_4) > abs(ans_5):
                    ans_6 = ans_4
                else:
                    ans_6 = ans_5

                if abs(ans_3) > abs(ans_6):
                    ans_7 = ans_3
                else:
                    ans_7 = ans_6

                ans = ans_7 / 2

                img_shift[i, j] = ans

        # 上のプログラムの結果と違う;;;
        # 原因わからず
        # img_left = img_tmp[shift_value:shift_value+height, 0:width]
        # img_right = img_tmp[shift_value:shift_value+height, -width:]
        # img_top = img_tmp[0:height, shift_value:shift_value+width]
        # img_bottom = img_tmp[-height:, shift_value:shift_value+width]
        # img_left_top = img_tmp[0:height, 0:width]
        # img_right_top = img_tmp[0:height, shift_value*2:]
        # img_right_bottom = img_tmp[-height:, shift_value*2:]
        # img_left_bottom = img_tmp[-height:, 0:width]
        #
        # img_shift_lr = 2 * src_ - (img_left + img_right)
        #
        # img_shift_tb = 2 * src_ - (img_top + img_bottom)
        # img_shift_ltrb = 2 * src_ - (img_left_top + img_right_bottom)
        # img_shift_rtlb = 2 * src_ - (img_right_top + img_left_bottom)
        #
        # img_shift_lr_abs = np.abs(img_shift_lr)
        # img_shift_tb_abs = np.abs(img_shift_tb)
        # img_shift_ltrb_abs = np.abs(img_shift_ltrb)
        # img_shift_rtlb_abs = np.abs(img_shift_rtlb)
        #
        # img_shift_1 = np.where(img_shift_lr_abs > img_shift_tb_abs, img_shift_lr, img_shift_tb)
        # img_shift_2 = np.where(img_shift_ltrb_abs > img_shift_rtlb_abs, img_shift_ltrb, img_shift_rtlb)
        # img_shift_1_abs = np.abs(img_shift_1)
        # img_shift_2_abs = np.abs(img_shift_2)
        #
        # img_shift = np.where(img_shift_1_abs > img_shift_2_abs, img_shift_1, img_shift_2)
        img_shift = img_shift / 2
        pass
    else:
        assert False, "shift_direct is invalid. given is {0}".format(shift_direct)


    img_dst = emphasize * img_shift + 128 # 輝度値128をベースに変化量だけを強調する
    img_dst = np.clip(img_dst, a_min=0, a_max=255)
    img_dst = img_dst.astype(np.uint8)

    if src.ndim == 2:
        img_dst = np.squeeze(img_dst)

    return img_dst




