"""解像度に関する処理
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
OK 低解像度化
-- アップサンプリング
OK ガウシアン画像ピラミッドの作成
OK ラプラシアン画像ピラミッドの作成
"""

def down_sampler(src:np.ndarray, n_octave:int=1, is_same_size:bool=True) -> np.ndarray:
    """
    低解像度化
    出力画像のサイズは入力サイズと同じ
    OpenCVを使っているので，ダウンサンプリング後は注目画素と上下の合計5画素によるガウシアンブラーがかかる.
    :param src:
    :param n_octave: 解像度を下げる回数. 1octaveで解像度は1/4だけ低下する.
    :param is_same_size: 出力画像サイズを入力画像と同じにする
    :return:
    """
    divide_img = src
    low_resolve_img = src
    for _ in range(n_octave):
        divide_img = cv2.pyrDown(src=divide_img)
        if is_same_size:
            low_resolve_img = cv2.pyrUp(src=divide_img)
        else:
            low_resolve_img = divide_img
        divide_img = low_resolve_img
    dst = low_resolve_img

    return dst

def up_sampler(src:np.ndarray, n_octave:int=1) -> np.ndarray:
    """
    アップサンプリング
    :param src:
    :param n_octave: 画像サイズを大きくする回数. 1回の処理で縦横2倍になる.
    :return:
    """
    big_img = src
    for _ in range(n_octave):
        big_img = cv2.pyrUp(src=big_img)
    dst = big_img

    return dst


def gaussian_pyramid(src:np.ndarray, n_octave:int=1, is_same_size:bool=True) -> List[np.ndarray]:
    """
    低解像度化による画像ピラミッドを作成.
    OpenCVを使っているので，ダウンサンプリング後は注目画素と上下の合計5画素によるガウシアンブラーがかかる.
    :param src:
    :param n_octave: 解像度を下げる回数. 1octaveで解像度は1/4だけ低下する.
    :param is_same_size: 出力画像サイズを入力画像と同じにする
    :return:
    """
    lower_resolutions = []
    divide_img = src
    for _ in range(n_octave):
        divide_img = cv2.pyrDown(src=divide_img)
        if is_same_size:
            low_resolve_img = cv2.pyrUp(src=divide_img)
        else:
            low_resolve_img = divide_img
        divide_img = low_resolve_img
        lower_resolutions.append(low_resolve_img)
    return lower_resolutions


def laplacian_pyramid(src:np.ndarray, n_octave:int=1, is_same_size:bool=True) -> List[np.ndarray]:
    """
    ラプラシアン画像ピラミッドを作成.
    :param src:
    :param n_octave:
    :param is_same_size:
    :return: 出力リストの画像はfloat64型
    """
    gauss_pyramid = gaussian_pyramid(src, n_octave + 1, is_same_size=is_same_size)

    # laplacian =  higher_resolve_img - lower_resolve_img
    laplacians = []
    for i in range(len(gauss_pyramid) - 1):
        if is_same_size:
            img_diff = gauss_pyramid[i].astype(np.float64) - gauss_pyramid[i + 1].astype(np.float64)
        else:
            img_diff = gauss_pyramid[i].astype(np.float64) - cv2.pyrUp(gauss_pyramid[i + 1]).astype(np.float64)
        laplacians.append(img_diff)

    return laplacians
