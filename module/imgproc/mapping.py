"""濃淡変換を行う処理
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

"""
OK ガンマ補正
OK 線形濃淡変換
-- clip_mapping???

"""

def gamma_mapping(src:np.ndarray, gamma:int=100) -> np.ndarray:
    """
    ガンマ補正
    :param src:
    :param gamma: 100%スケール
    :return:
    """
    dst = 255.0 * pow(src / 255.0, 100.0 / gamma)
    dst = np.clip(dst, a_min=0, a_max=255)
    dst = dst.astype(np.uint8)
    return dst


def linear_mapping(src:np.ndarray, alpha:float = 1.0, beta:float = 0.0) -> np.ndarray:
    """
    線形濃淡変換
    :param src:
    :param alpha: 明るい輝度の変化量を大きく
    :param beta:  画像全体のベースを変更
    :return: alpha * src + beta
    """
    dst = alpha * src + beta
    dst = np.clip(dst, a_min=0, a_max=255)
    dst = dst.astype(np.uint8)
    return dst


def clip_mapping(src:np.ndarray, lum_low:int = 0, lum_high:int = 255, is_contrast_up:bool = True) -> np.ndarray:
    """
    クリップマッピング?
    :param src:
    :param lum_low: 輝度の下限
    :param lum_high: 輝度の上限
    :return:
    """
    if lum_low < 0:
        lum_low = 0
    if lum_high > 255:
        lum_high = 255

    # 線形変換
    if is_contrast_up:
        alpha = 255.0 / (lum_high - lum_low)
        beta = -255.0 * lum_low / (lum_high - lum_low)
    else:
        alpha = (lum_high - lum_low) / 255.0
        beta = lum_low

    dst = alpha * src + beta

    # 輝度値の範囲を low <= I <= high にクリッピング
    dst = np.clip(dst, a_min=lum_low, a_max=lum_high)
    dst = dst.astype(np.uint8)

    return dst