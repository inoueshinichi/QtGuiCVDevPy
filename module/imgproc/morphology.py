"""モルフォロジー演算
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from collections import namedtuple
from typing import (List, Dict, Tuple, Union, Callable, Any, TypeVar, NoReturn, Generic, NamedTuple)

# サードパーティ
import numpy as np
import scipy as sp
import cv2
from PIL import Image
import skimage

# 自作



"""
OK 膨張処理
OK 収縮処理
OK オープニング
OK クロージング
OK 輪郭線抽出
-- 細線化
OK 矩形マスク
OK 楕円マスク
OK 十字マスク
"""


def dilation(src:np.ndarray, ksize:int, iterations:int=1) -> np.ndarray:
    """
    膨張処理
    :param src:
    :param ksize:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    for c in range(_src.shape[0]):
        dst[c] = cv2.dilate(src=_src[c], kernel=kernel, iterations=iterations)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def erosion(src:np.ndarray, ksize:int, iterations:int=1) -> np.ndarray:
    """
    収縮処理
    :param src:
    :param ksize:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    for c in range(_src.shape[0]):
        dst[c] = cv2.erode(src=_src[c], kernel=kernel, iterations=iterations)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def opening(src:np.ndarray, ksize:int, iterations:int=1) -> np.ndarray:
    """
    オープニング(収縮 x n -> 膨張 x n): ノイズ除去
    :param src:
    :param ksize:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    for c in range(_src.shape[0]):
        dst[c] = cv2.morphologyEx(src=_src[c], op=cv2.MORPH_OPEN, kernel=kernel, iterations=iterations)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def closing(src:np.ndarray, ksize:int, iterations:int=1) -> np.ndarray:
    """
    クロージング(膨張 x n -> 収縮 x n): 前景領域の中の小さな穴(黒点)を埋める
    :param src:
    :param ksize:
    :param iterations:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    for c in range(_src.shape[0]):
        dst[c] = cv2.morphologyEx(src=_src[c], op=cv2.MORPH_CLOSE, kernel=kernel, iterations=iterations)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def outline(src:np.ndarray, ksize:int, iterations:int=1) -> np.ndarray:
    """
    輪郭線抽出(膨張画像と収縮画像の差分)
    :param src:
    :param ksize:
    :param iterations:
    :return:
    """
    _src = src.copy()
    if _src.ndim == 2:
        _src = _src[:, :, np.newaxis]

    _src = _src.transpose(2, 0, 1)
    dst = np.zeros_like(_src)

    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    for c in range(_src.shape[0]):
        dst[c] = cv2.morphologyEx(src=_src[c], op=cv2.MORPH_GRADIENT, kernel=kernel, iterations=iterations)

    dst = dst.transpose(1, 2, 0)
    dst = np.squeeze(dst)
    return dst


def rectangle_mask(ksize:Tuple[int, int]) -> np.ndarray:
    """
    矩形マスク 前景:1, 背景:0(なし)
    :param ksize:
    :return:
    """
    return cv2.getStructuringElement(cv2.MORPH_RECT, ksize)


def ellipse_mask(ksize:Tuple[int, int]) -> np.ndarray:
    """
    楕円マスク 前景:1, 背景:0
    :param ksize:
    :return:
    """
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)


def cross_mask(ksize:Tuple[int, int]) -> np.ndarray:
    """
    十字マスク 前景:1, 背景:0
    :param ksize:
    :return:
    """
    return cv2.getStructuringElement(cv2.MORPH_CROSS, ksize)





