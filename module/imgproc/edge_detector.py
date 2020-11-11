"""エッジ検出
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, TypeVar, NoReturn, Generic)

# サードパーティ
import numpy as np
import scipy as sp
from scipy.ndimage import filters
import cv2
from PIL import Image
import skimage

# 自作

"""
OK 微分フィルタ
OK プレウィットフィルタ
OK ソベルフィルタ
OK ラプラシアンフィルタ
OK ROGフィルタ
OK DOGフィルタ
-- XDOGフィルタ
OK ゼロ点交差
OK キャニー
"""

def base_diff_filter(src:np.ndarray, kernel:np.ndarray) -> np.ndarray:
    """
    微分系フィルタの雛形
    :param src:
    :param kernel:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        dst[c] = cv2.filter2D(_src[c], ddepth=cv2.CV_64F, kernel=kernel)


    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def differential_filter(src:np.ndarray, dir:str) -> np.ndarray:
    """
    微分フィルタ
    :param src:
    :param dir: 微分方向 'h', 'v', 'ut', 'dt'
    :return:
    """
    kernel = np.zeros((3, 3), np.float64)

    if dir == 'v':
        kernel[0, 1] = -0.5
        kernel[2, 1] = 0.5

    elif dir == 'h':
        kernel[1, 0] = -0.5
        kernel[1, 2] = 0.5

    elif dir == 'ut':
        kernel[0, 2] = 0.5
        kernel[2, 0] = -0.5

    elif dir == 'dt':
        kernel[0, 0] = -0.5
        kernel[2, 2] = 0.5

    else:
        assert False, "dir must be h, v, ut or dt."

    dst = base_diff_filter(src, kernel)
    return dst


def prewitt_filter(src:np.ndarray, dir:str) -> np.ndarray:
    """
    プレウィットフィルタ
    :param src:
    :param dir: 微分方向 'h', 'v', 'ut', 'dt'
    :return:
    """
    kernel = np.zeros((3, 3), np.float64)

    if dir == 'v':
        kernel[0, :] = -1
        kernel[2, :] = 1

    elif dir == 'h':
        kernel[:, 0] = -1
        kernel[:, 2] = 1

    elif dir == 'ut':
        kernel[0, 1] = 1
        kernel[0, 2] = 1
        kernel[1, 2] = 1
        kernel[1, 0] = -1
        kernel[2, 0] = -1
        kernel[2, 1] = -1

    elif dir == 'dt':
        kernel[0, 0] = -1
        kernel[0, 1] = -1
        kernel[1, 0] = -1
        kernel[1, 2] = 1
        kernel[2, 1] = 1
        kernel[2, 2] = 1

    else:
        assert False, "dir must be h, v, ut or dt."

    # 定義通り1/6する
    kernel /= 6

    dst = base_diff_filter(src, kernel)
    return dst


def sobel_filter(src:np.ndarray, dir:str) -> np.ndarray:
    """
    ソベルフィルタ
    :param src:
    :param dir: 微分方向 'h', 'v', 'ut', 'dt'
    :return:
    """
    kernel = np.zeros((3, 3), np.float64)

    if dir == 'v':
       kernel[0, 0] = -1
       kernel[0, 1] = -2
       kernel[0, 2] = -1
       kernel[2, 0] = 1
       kernel[2, 1] = 2
       kernel[2, 2] = 1

    elif dir == 'h':
        kernel[0, 0] = -1
        kernel[1, 0] = -2
        kernel[2, 0] = -1
        kernel[0, 2] = 1
        kernel[1, 2] = 2
        kernel[2, 2] = 1

    elif dir == 'ut':
        kernel[0, 1] = 1
        kernel[0, 2] = 2
        kernel[1, 2] = 1
        kernel[1, 0] = -1
        kernel[2, 0] = -2
        kernel[2, 1] = -1

    elif dir == 'dt':
        kernel[0, 0] = -2
        kernel[0, 1] = -1
        kernel[1, 0] = -1
        kernel[1, 2] = 1
        kernel[2, 1] = 1
        kernel[2, 2] = 2

    else:
        assert False, "dir must be h, v, ut or dt."

    # 定義通り1/8する
    kernel /= 8

    dst = base_diff_filter(src, kernel)
    return dst


def laplacian_filter(src:np.ndarray, ksize:int) -> np.ndarray:
    """
    ラプラシアンフィルタ
    :param src:
    :param kernel: カーネルサイズ
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        dst[c] = cv2.Laplacian(_src[c], ddepth=cv2.CV_64F, ksize=ksize)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def log_filter(src:np.ndarray, ksize:int, sigma:float) -> np.ndarray:
    """
    LOGフィルタ(Laplaican Of Gaussian)
    :param src:
    :param ksize: カーネルサイズ
    :param sigma:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        mid = cv2.GaussianBlur(_src[c], ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
        dst[c] = cv2.Laplacian(mid, ddepth=cv2.CV_64F, ksize=ksize)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def dog_filter(src:np.ndarray, ksize:int, sigma:float=1.3, k:float=1.6, gamma:float=1) -> np.ndarray:
    """
    DOG(Differencial Of Gaussian)フィルタ
    :param src:
    :param ksize: カーネルサイズ
    :param k: ガウシアンフィルタのシグマの倍率
    :param gamma: 差分時のスケール(通常1)
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        g_prior = cv2.GaussianBlur(_src[c], ksize=(ksize, ksize), sigmaX=sigma)
        g_later = cv2.GaussianBlur(_src[c], ksize=(ksize, ksize), sigmaX=k*sigma)
        dst[c] = g_prior - gamma * g_later

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def xdog_filter(src:np.ndarray, p:float, ksize:int, eps:float, phi:float, sigma:float=1.3, k:float=1.6) -> np.ndarray:
    """
    拡張DOG
    https://www.kyprianidis.com/p/cag2012/winnemoeller-cag2012.pdf
    https://qiita.com/Shirataki2/items/813fdade850cc69d1882
    :param src:
    :param ksize:
    :param sigma:
    :param k:
    :param gamma:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        g_prior = cv2.GaussianBlur(_src[c], ksize=(ksize, ksize), sigmaX=sigma)
        g_later = cv2.GaussianBlur(_src[c], ksize=(ksize, ksize), sigmaX=k * sigma)
        mid = (1 + p) * g_prior - p * g_later
        mid /= mid.max()
        e = 1 + np.tanh(phi * (mid - eps))
        e[e >= 1] = 1
        dst[c] = e

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def zero_crossing(src:np.ndarray) -> np.ndarray:
    """
    ゼロ点交差処理によるエッジ抽出(細線化?)
    ※遅くて使い物にならないので，暇があれば高速化すること
    :param src:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64) # zero_cross

    for c in range(_src.shape[0]):
        height = dst.shape[1]
        width = dst.shape[2]
        for j in range(1, height - 1):
            for i in range(1, width - 1):
                # 各ピクセルについて，注目点の8近傍のpos_pxlとneg_pxlを数える
                count_neg_pxl = 0
                count_pos_pxl = 0

                # 8近傍
                neighborhoods = list(_src[c][j-1:j+2, i-1:i+2].flatten())
                del neighborhoods[4] # 3x3の中心ピクセルを削除
                neighborhoods = np.array(neighborhoods)

                # max/min in 8 neighborhoods
                d = neighborhoods.max()
                e = neighborhoods.min()

                # count neg_pxl/pos_pxl
                count_neg_pxl = np.sum(neighborhoods < 0)
                count_pos_pxl = np.sum(neighborhoods > 0)

                # 注目ピクセル近傍にpos_pxlとneg_pxlがある場合，ゼロ点交差の可能性あり
                if count_neg_pxl > 0 and count_pos_pxl > 0:
                    tar_pxl = _src[c][j, i]
                    if tar_pxl > 0:
                        dst[c][j, i] = tar_pxl + np.abs(e)
                    elif tar_pxl < 0:
                        dst[c][j, i] = np.abs(tar_pxl) + d

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def canny(src:np.ndarray, hysterisis_upper:int, hysterisis_lower:int) -> np.ndarray:
    """
    キャニーエッジ検出
    :param src:
    :param hysterisis_upper: ヒステリシス上限しきい値　この値より大きな微分値はエッジとみなす
    :param hysterisis_lower: ヒステリシス下限しきい値　この値より小さな微分値はエッジではない
    ※中間領域は注目点と近傍の微分値から適応的に判断する
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        dst[c] = cv2.Canny(_src[c], threshold1=hysterisis_upper, threshold2=hysterisis_lower)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst