"""複数画像を用いた処理
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from collections import namedtuple
from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Callable,
    Any,
    TypeVar,
    NoReturn,
    Generic
)


# サードパーティ
import numpy as np
import scipy as sp
from scipy.ndimage import filters
import cv2
from PIL import Image
import skimage

# 自作
from module.imgproc.binarize import otsu_binarize
from module.imgproc.color import rgb2gray


"""
OK 画像加算(dst = src1 + src2)
OK 画像減算(dst = src1 - src2)
OK 画像掛算(dst = src1 * src2)
OK 画像割算(dst = src1 / src2)
OK 画像加算(dst = src + add)
OK 画像減算(dst = src - sub)
OK 画像掛算(dst = src * mul)
OK 画像割算(dst = src / div)
OK 平均画像(dst = avg(src1, src2, ...srcN))
OK ブレンド合成(dst = ratio * src1 + (1 - ratio) * src2 + bias)
-- クロマキー合成
-- 固有画像(画像をベクトルと見立てて，分散共分散行列の固有値を算出) 
"""

def add_two_imgs(src1:np.ndarray, src2:np.ndarray, is_clip:bool = False) -> np.ndarray:
    """
    画像加算(dst = src1 + src2)
    :param src1:
    :param src2:
    :return:
    """
    assert src1.shape == src2.shape, f"Shape of src2 must be the same as src1. Given is {src2.shape}."
    src1 = src1.astype(np.float32)
    src2 = src2.astype(np.float32)
    dst = src1 + src2
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def sub_two_imgs(src1:np.ndarray, src2:np.ndarray, is_clip:bool = False) -> np.ndarray:
    """
    画像減算(dst = src1 - src2)
    :param src1:
    :param src2:
    :return:
    """
    assert src1.shape == src2.shape, f"Shape of src2 must be the same as src1. Given is {src2.shape}."
    src1 = src1.astype(np.float32)
    src2 = src2.astype(np.float32)
    dst = src1 - src2
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def mul_two_imgs(src1:np.ndarray, src2:np.ndarray, is_clip:bool = False) -> np.ndarray:
    """
    画像掛算(dst = src1 * src2)
    :param src1:
    :param src2:
    :return:
    """
    assert src1.shape == src2.shape, f"Shape of src2 must be the same as src1. Given is {src2.shape}."
    src1 = src1.astype(np.float32)
    src2 = src2.astype(np.float32)
    dst = src1 * src2
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def div_two_imgs(src1:np.ndarray, src2:np.ndarray, is_clip:bool = False) -> np.ndarray:
    """
    画像割算(dst = src1 / src2)
    :param src1:
    :param src2:
    :return:
    """
    assert src1.shape == src2.shape, f"Shape of src2 must be the same as src1. Given is {src2.shape}."
    src1 = src1.astype(np.float32)
    src2 = src2.astype(np.float32)

    is_zero_div = np.sum((src2 == 0).astype(np.int64))
    assert is_zero_div == 0, f"Zero Division Error. Content of src2 have zero value."

    dst = src1 / src2
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def add_img(src:np.ndarray, add:float, is_clip:bool = False) -> np.ndarray:
    """
    画像加算(dst = src + add)
    :param src1:
    :param add:
    :param is_clip:
    :return:
    """
    src = src.astype(np.float32)
    dst = src + add
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def sub_img(src:np.ndarray, sub:float, is_clip:bool = False) -> np.ndarray:
    """
    画像減算(dst = src - sub)
    :param src1:
    :param add:
    :param is_clip:
    :return:
    """
    src = src.astype(np.float32)
    dst = src - sub
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def mul_img(src:np.ndarray, mul:float, is_clip:bool = False) -> np.ndarray:
    """
    画像掛算(dst = src * mul)
    :param src1:
    :param add:
    :param is_clip:
    :return:
    """
    src = src.astype(np.float32)
    dst = src * mul
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def div_img(src:np.ndarray, div:float, is_clip:bool = False) -> np.ndarray:
    """
    画像掛算(dst = src * mul)
    :param src1:
    :param add:
    :param is_clip:
    :return:
    """
    src = src.astype(np.float32)
    assert div != 0, f"Zero Division Error. Given is {div}"

    dst = src / div
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def average_of_imgs(src_list:List[np.ndarray], is_clip:bool = False) -> np.ndarray:
    """
    平均画像(dst = avg(src1, src2, ...srcN))
    :param src_list:
    :param is_clip:
    :return:
    """
    assert len(src_list) > 0, f"Length of src_list must be > 0. Given is {len(src_list)}."
    # tmp_imgs = list(map(lambda x: x.astype(np.float32), src_list))
    # sum_img = sum(tmp_imgs)
    # dst = sum_img / len(tmp_imgs)
    dst = np.mean(np.array(src_list).astype(np.float32), axis=0) # 速い
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def blend_two_imgs(src1:np.ndarray, src2:np.ndarray, ratio:float=0.5, bias: float=0, is_clip:bool = False) -> np.ndarray:
    """
    ブレンド合成(dst = ratio * src1 + (1 - ratio) * src2 + bias)
    :param src1:
    :param src2:
    :param ratio:
    :param bias:
    :return:
    """
    assert src1.shape == src2.shape, f"Shape of src2 must be the same as src1. Given is {src2.shape}."
    src1 = src1.astype(np.float32)
    src2 = src2.astype(np.float32)

    dst = cv2.addWeighted(src1=src1, src2=src2, alpha=ratio, beta=(1 - ratio), gamma=bias)
    if is_clip:
        dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    return dst


def chromakey(src1:np.ndarray, src2:np.ndarray, pos:Tuple[int,int]) -> np.ndarray:
    """
    クロマキー合成
    :param src1:
    :param src2:
    :param pos:
    :param hist_low_limit:
    :param hist_high_limit:
    :return:
    """
    assert src1.ndim == src2.ndim, f"Dimension of src2 must be the same as src1. " \
                                   f"Givens are src1.ndim: {src1.ndim}, src2.ndim: {src2.ndim}."

    src1_h, src1_w = src1.shape[0], src1.shape[1]
    src2_h, src2_w = src2.shape[0], src2.shape[1]
    assert src1_h >= src2_h, f"Must be src1_h >= src2_h, Givens are src1_h: {src1_h}, src2_h: {src2_h}."
    assert src1_w >= src2_w, f"Must be src1_w >= src2_w, Givens are src1_w: {src1_w}, src2_w: {src2_w}."

    x, y = pos
    assert 0 <= x < src1_w, f"Must be 0 <= pos[0](x) < src1_w, Given is {x}."
    assert 0 <= y < src1_h, f"Must be 0 <= pos[1](y) < src1_h, Given is {y}."

    # chromakey_patch_size
    patch_w = src2_w if x + src2_w < src1_w else src2_w - x
    patch_h = src2_h if y + src2_h < src1_h else src2_h - y
    patch_src1 = src1[y:y+patch_h, x:x+patch_w]
    patch_src2 = src2[0:patch_h, 0:patch_w]

    patch_src2_gray = rgb2gray(patch_src2)

    _, src2_binary = otsu_binarize(patch_src2_gray)
    if src1.ndim != 1:
        tmp_src2_binary = np.copy(src2_binary)
        for i in range(src1.shape[-1] - 1):
            src2_binary = np.dstack((src2_binary, tmp_src2_binary))

    src2_mask = src2_binary > 0                       # True or False
    src2_inv_mask = np.logical_not(src2_mask)         # True or False
    src2_mask = src2_mask.astype(np.uint8)
    src2_inv_mask = src2_inv_mask.astype(np.uint8)

    # src1 background
    bg_src1 = patch_src1 * src2_inv_mask
    # src2 foreground
    fg_src2 = patch_src2 * src2_mask

    # mixture of chromakey
    patch_dst = bg_src1 + fg_src2

    dst = np.copy(src1)
    dst[y:y+patch_h, x:x+patch_w] = patch_dst
    return dst



