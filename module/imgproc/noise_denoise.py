"""ノイズ付加/ノイズ除去
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
OK Uniform Noise
OK Standard Noise
OK ROF Denoise
"""

def noise_uniform(src:np.ndarray, lower:int, upper:int, random_state:np.random.RandomState) -> np.ndarray:
    """
    一様分布に基づくノイズ付加
    :param src:
    :param lower:
    :param upper:
    :return:
    """
    src = src.astype(np.int32)
    dst = src + random_state.random_integers(low=lower, high=upper, size=src.shape)
    dst = np.clip(a=dst, a_min=0, a_max=255)
    return dst


def noise_standard(src:np.ndarray, mean:float, sigma:float, random_state:np.random.RandomState) -> np.ndarray:
    """
    正規分布に基づくノイズ付加
    :param src:
    :param mean:
    :param sigma:
    :param random_state:
    :return:
    """
    src = src.astype(np.float32)
    dst = src + random_state.normal(loc=mean, scale=sigma, size=src.shape)
    dst = np.clip(a=dst, a_min=0, a_max=255)
    dst = dst.astype(np.uint8)
    return dst


def denoise_rof(src:np.ndarray, u_init:np.ndarray, tolerance:float=0.1,
                step:float=0.125, tv_weight:int=100) -> Tuple[np.ndarray, np.ndarray]:
    """
    A. Chambolle(2005)の数式(11)記載の計算手順に基づく
    Rudin-Osher-Fatemi(ROF)ノイズ除去モデルの実装.
    https://link.springer.com/chapter/10.1007/11585978_10

    :param src:       ノイズのある入力画像(Grayscale)
    :param u_init:    Uの初期ガウス分布
    :param tolerance: 終了判断基準の許容誤差
    :param step:      ステップ長(tau)
    :param tv_weight: TV正規化項の重み
    :return:          ノイズ除去された画像, 残余テクスチャ
    """
    assert src.ndim == 2, "src must be grayscale, thus 2dim."

    m, n = src.shape

    # 初期化
    u = u_init
    px = src # 双対領域でのx成分
    py = src # 双対領域でのy成分
    error = 1

    while (error > tolerance):
        u_old = u

        # 主変数の勾配
        grad_ux = np.roll(u, -1, axis=1) - u # uの勾配のx成分
        grad_uy = np.roll(u, -1, axis=0) - u # uの勾配のy成分

        # 双対変数を更新
        px_new = px + (step / tv_weight) * grad_ux
        py_new = py + (step / tv_weight) * grad_uy
        norm_new = np.maximum(1, np.sqrt(px_new ** 2 + py_new ** 2))

        px = px_new / norm_new # 双対変数のx成分を更新
        py = py_new / norm_new # 双対変数のy成分を更新

        # 主変数を更新
        px_rx = np.roll(px, 1, axis=1) # x成分の右回りの変換
        py_ry = np.roll(py, 1, axis=0) # y成分の右回りの変換

        div_p = (px - px_rx) + (py - py_ry) # 双対領域の発散

        u = src + tv_weight * div_p # 主変数を更新

        # 誤差を更新
        error = np.linalg.norm(u - u_old) / math.sqrt(n*m)

    return u, src - u # ノイズ除去画像と残余テクスチャ

