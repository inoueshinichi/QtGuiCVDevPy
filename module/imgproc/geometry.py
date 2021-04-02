"""幾何学的変換処理
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
OK フリップ
OK 拡大・縮小
OK 平行移動
OK 回転
OK アフィン変換
OK アフィン変換(行列指定)
-- 対応点(最低3組)からアフィン変換行列を生成
-- 透視変換
-- 透視変換(行列指定)
-- 対応点(最低4組)から透視変換行列を生成して透視変換を実行
-- 画像の位置合わせ(分割アフィンワーピング: 長方形画像を三角形に分割してアフィン変換. 指定の位置・角度に貼り付ける)
"""


def flip(src:np.ndarray, flip_pattern: str) -> np.ndarray:
    """
    フリップ操作
    :param src:
    :param flip_pattern: 'h': 垂直軸回転, 'v': 水平軸回転, 'b': 両軸回転
    :return:
    """
    flip_code = 0
    if flip_pattern.lower() == 'v':
        flip_code = 0
    elif flip_pattern.lower() == 'h':
        flip_code = 1
    elif flip_pattern.lower() == 'b': # both
        flip_code = -1
    else:
        assert False, f"Invalid flip_code."

    dst = cv2.flip(src=src, flipCode=flip_code)
    return dst


def resize(src:np.ndarray, size:Tuple[int,int], interpo:int=1) -> np.ndarray:
    """
    画像の拡大・縮小処理
    :param src:
    :param size: (w,h)
    :param interporation: 0: Nearest Neighber, 1: Liner Interpo, 2: Cubic Interpo
    :return:
    """
    assert 0 <= interpo <= 2, f"Invalid Interporation Method; {interpo}"

    dst = cv2.resize(src=src, dsize=size, interpolation=interpo)
    return dst


def translate(src:np.ndarray, trans:Tuple[int,int]) -> np.ndarray:
    """
    画像の平行移動
    :param src:
    :param trans: (tx,ty)
    :return:
    """
    dst = np.zeros_like(src, dtype=src.dtype)
    height, width = src.shape[:-1]
    tx, ty = trans
    if tx == 0 and ty == 0:
        return src

    if tx > 0 and ty > 0:
        crop = src[:-ty, :-tx]
        dst[ty:, tx:] = crop

    if tx < 0 and ty < 0:
        crop = src[-ty:, -tx:]
        crop_h = height + ty
        crop_w = width + tx
        dst[:crop_h, :crop_w] = crop

    if tx > 0 and ty == 0:
        crop = src[:, :-tx]
        dst[:, tx:] = crop

    if tx < 0 and ty == 0:
        crop = src[:, -tx:]
        crop_w = width + tx
        dst[:, :crop_w] = crop

    if tx == 0 and ty > 0:
        crop = src[:-ty, :]
        dst[ty:, :] = crop

    if tx == 0 and ty < 0:
        crop = src[-ty:, :]
        crop_h = height + ty
        dst[:crop_h, :] = crop

    return dst


def rotate(src: np.ndarray, deg: float = 0.0, center: Tuple[int, int] = (0, 0)) -> np.ndarray:
    """
    画像の回転
    :param src:
    :param deg:
    :param center:
    :param interpo:
    :return:
    """
    # 回転行列の作成(2x3)
    M = cv2.getRotationMatrix2D(center=center, angle=deg, scale=1.0)
    height, width = src.shape[:2]
    dst = cv2.warpAffine(src, M, (width, height))
    return dst


def affine2d(src: np.ndarray,
             deg: float = 0.0,
             tran: Tuple[int, int] = (0, 0),
             scale: Tuple[float, float] = (0, 0),
             center: Tuple[int,int] = (0, 0))\
        -> np.ndarray:
    """
    アフィン変換
    :param src:
    :param deg:
    :param tran:
    :param scale:
    :param center:
    :return:
    """
    # 指定位置での回転と並進をする行列を作成
    rad = math.radians(deg)
    r11 = scale[0] * math.cos(rad)
    r12 = scale[1] * math.sin(rad)
    r13 = (1 - r11) * center[0] - r12 * center[1] + tran[0]
    r21 = -r12
    r22 = r11
    r23 = r12 * center[0] + (1 - r11) * center[1] + tran[1]
    M = np.float64([[r11, r12, r13], [r21, r22, r23]])
    # M = cv2.getRotationMatrix2D(center=center, angle=deg, scale=scale)

    height, width = src.shape[:2]
    dst = cv2.warpAffine(src, M, (width, height))
    return dst


def affine2d_M(src:np.ndarray, M:np.ndarray) -> np.ndarray:
    """
    指定した行列に沿ってアフィン変換を実行
    :param src:
    :param M:
    :return:
    """
    height, width = src.shape[:2]
    dst = cv2.warpAffine(src, M, (width, height))
    return dst





