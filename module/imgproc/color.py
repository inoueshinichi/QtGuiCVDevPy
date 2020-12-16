"""画像カラー変換を行う関数群
"""

# 標準
import time
from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Callable,
    Any,
    NewType
)

# サードパーティ
import numpy as np
import scipy as sp
from scipy import ndimage
import skimage
import cv2
from PIL import Image
from matplotlib import pyplot as plt

# 自作

# 関数リスト
"""
OK rgb2gray
OK gray2rgb
OK rgb2hsv
OK hsv2rgb
"""


def rgb2gray(src:np.ndarray) -> np.ndarray:
    """
    RGB -> Grayscale(1ch)
    :param src:
    :return:
    """
    if src.ndim == 2:
        return src

    dst = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    return dst


def gray2rgb(src:np.ndarray) -> np.ndarray:
    """
    Grayscale(1ch) -> RGB(ColorMap-Jet)
    :param src:
    :return:
    """
    dst = cv2.applyColorMap(src, colormap=cv2.COLORMAP_JET)
    return dst


def rgb2hsv(src:np.ndarray) -> np.ndarray:
    """
    RGB -> HSV
    :param src:
    :return:
    """
    dst = cv2.cvtColor(src, cv2.COLOR_RGB2HSV)
    return dst


def hsv2rgb(src:np.ndarray) -> np.ndarray:
    """
    HSV -> RGB
    :param src:
    :return:
    """
    dst = cv2.cvtColor(src, cv2.COLOR_HSV2RGB)
    return dst