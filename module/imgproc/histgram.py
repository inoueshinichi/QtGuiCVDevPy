"""ヒストグラム処理
"""

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
OK ヒストグラム平坦化
-- Self-Quotient
"""

def gen_histogram(src_list:List[np.ndarray]) -> List[List[Any]]:
    """
    ヒストグラムを生成
    :param src:
    :return:
    """
    hist_features = []
    HistFeature = namedtuple("HistFeature", ['hist', 'bin', 'cdf', 'normalized_cdf'])
    for src in src_list:
        _src = src.copy()
        if _src.ndim == 2:
            _src = _src[:, :, np.newaxis]
        _src = _src.transpose(2, 0, 1)

        hist_colors = []
        for c in range(_src.shape[0]):
            hist, _bin = np.histogram(_src[c].ravel(), 256, [0, 256])
            cdf = hist.cumsum()
            normalized_cdf = cdf * hist.max() / cdf.max()
            feature = HistFeature(hist=hist, bin=_bin, cdf=cdf, normalized_cdf=normalized_cdf)
            hist_colors.append(feature)
        hist_features.append(hist_colors)

    return hist_features


def flat_histogram(src:np.ndarray) -> np.ndarray:
    """
    ヒストグラム平坦化
    :param src: (H, W, C)
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    for c in range(_src.shape[0]):
        hist, bins = np.histogram(_src[c].ravel(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0)
        cdf = cdf.astype(np.uint8)
        dst[c] = cdf[_src[c]]

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst
