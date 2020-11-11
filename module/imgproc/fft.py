"""FFT処理
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
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
OK fft
OK ifft
-- high pass filter
-- low pass filter
-- band pass filter
"""

def fft_2d(src:np.ndarray, is_shift:bool=True) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    ２次元フーリエ変換
    :param src:
    :param is_shift:
    :param is_show_degree:
    :return: 変換した振幅, 表示用の振幅, 変換した位相
    """
    assert src.ndim == 2, "src must be grayscale; 2dim."

    # fft
    img_fft = np.fft.fft2(src)

    # 低周波を画像中心に移動
    if is_shift:
        img_fft = np.fft.fftshift(img_fft)

    # 画像表示用のスペクトラム log2(re**2 + im**2)
    magnitude_spectrum = 20 * np.log(np.abs(img_fft))

    # 位相
    img_angle = np.angle(img_fft, deg=False) # [-pi, +pi]

    # plus
    ang_rad_plus = np.copy(img_angle)
    ang_rad_plus[ang_rad_plus[:, :] < 0] = 0

    # minus
    ang_rad_minus = np.copy(img_angle)
    ang_rad_minus[ang_rad_minus[:, :] > 0] = 0
    ang_rad_minus[ang_rad_minus[:, :] < 0] += 2 * np.pi # [-pi, +pi] -> [0, +2pi]

    img_angle = np.rad2deg(ang_rad_plus + ang_rad_minus)

    return img_fft, magnitude_spectrum, img_angle


def ifft_2d(src:np.ndarray, is_shift:bool=True) -> np.ndarray:
    """
    2次元逆フーリエ変換
    :param src: 複素数(振幅＋位相)
    :param is_shift:
    :return: 画像
    """
    assert src.ndim == 2, "src must be grayscale; 2dim."

    if is_shift:
        src = np.fft.ifftshift(src)

    # 逆フーリエ変換
    img_ifft = np.fft.ifft2(src)
    dst = np.abs(img_ifft) # 振幅だけ
    dst = dst.astype(np.uint8)

    return dst



