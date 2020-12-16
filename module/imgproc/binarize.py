"""2値化
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
import cv2
from PIL import Image
import skimage

# 自作


"""
OK ２値化
OK 大津の２値化(判別分析法)
OK 適応的２値化
"""


def binarize(src:np.ndarray, thresh:int) -> np.ndarray:
    """
    ２値化
    :param src:
    :param thresh:
    :return:
    """
    dst = np.where(src < thresh, 0, 255)
    return dst


def otsu_binarize(src:np.ndarray) -> Tuple[List[int], np.ndarray]:
    """
    大津の２値化(判別分析法)
    :param src:
    :return:
    """

    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    thresholds = []
    for c in range(_src.shape[0]):
        thresh, dst[c] = cv2.threshold(_src[c], -1, 255, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        thresholds.append(thresh)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return thresholds, dst


def adaptive_binarize(src:np.ndarray, patch_size:int=3, sub_thresh_bias:int=0) -> np.ndarray:
    """
    適用的２値化
    :param src:
    :param patch_size:
    :param sub_thresh_bias:
    :return:
    """
    assert patch_size % 2 != 0, "patch_size must be odd."

    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    for c in range(_src.shape[0]):
        dst[c] = cv2.adaptiveThreshold(src=_src[c], maxValue=255,
                                       adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       thresholdType=cv2.THRESH_BINARY,
                                       blockSize=patch_size,
                                       C=sub_thresh_bias)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst

