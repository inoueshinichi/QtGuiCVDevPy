"""先鋭化処理
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
OK 先鋭化フィルタ
"""


def sharpen_filter(src:np.ndarray, ksize:int, sigma:float, strong:float) -> np.ndarray:
    """
    先鋭化フィルタ
    :param src:
    :param sigma:
    :param strong: 先鋭強度
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src, dtype=np.float64)

    for c in range(_src.shape[0]):
        g = cv2.GaussianBlur(_src[c], ksize=(ksize, ksize), sigmaX=sigma)
        diff = _src[c].astype(np.int32) - g
        dst[c] = _src[c].astype(np.int32) + strong * diff

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)

    # クリップ
    dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
    return dst