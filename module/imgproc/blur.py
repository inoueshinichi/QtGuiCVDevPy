"""フィルタ処理
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
OK 画像形状を3Dフィルタ処理しやすい形状に変換(im2col_3d)
OK 3Dフィルタ処理したあとの形状を画像形状に戻す(col2img_3d)
-- 2Dフィルタのim2col_2d
-- 2Dフィルタのcol2im_2d
-- 畳み込み演算
OK ガウシアンフィルタ
OK 平均値フィルタ
OK メディアンフィルタ
OK バイラテラルフィルタ
OK モザイクフィルタ
-- ノンローミカルフィルタ
-- 分散フィルタ
-- 最大最小フィルタ
-- 任意のカーネルの線形畳み込みフィルタ
"""

def im2col_3d(input_data, filter_h, filter_w, stride=1, pad=0):
    """
    畳み込み演算高速化関数
    画像を畳み込みしやすい行列に変換
    大規模データに対しても一定数の速度を出せる。
    逆に小規模データでは遅い。
    Parameters
    ----------
    input_data : (データ数, チャンネル, 高さ, 幅)の4次元配列からなる入力データ
    filter_h : フィルターの高さ
    filter_w : フィルターの幅
    stride : ストライド
    pad : パディング
    Returns
    -------
    col : 2次元配列
    """
    N, C, H, W = input_data.shape
    out_h = (H + 2*pad - filter_h) // stride + 1
    out_w = (W + 2*pad - filter_w) // stride + 1

    img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    return col


def col2im_3d(col, input_shape, filter_h, filter_w, stride=1, pad=0):
    """
    畳み込み演算高速化逆関数
    Parameters
    ----------
    col :
    input_shape : 入力データの形状（例：(10, 1, 28, 28)）
    filter_h :
    filter_w
    stride
    pad
    Returns
    -------
    畳み込み演算後の画像
    """
    N, C, H, W = input_shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1
    col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

    img = np.zeros((N, C, H + 2*pad + stride - 1, W + 2*pad + stride - 1))
    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

    return img[:, :, pad:H + pad, pad:W + pad]


def average_blur(src:np.ndarray, kernel:Tuple[int, int]) -> np.ndarray:
    """
    平均値平滑化フィルタ
    :param src:
    :param kernel:
    :return:
    """
    dst = cv2.blur(src, ksize=kernel)
    return dst


def gaussian_blur(src:np.ndarray, kernel:Tuple[int, int], sigma:Tuple[float, float]) -> np.ndarray:
    """
    ガウシアン平滑フィルタ
    :param src:
    :param kernel: (k_x, k_y)
    :param sigma: (std_x, std_y)
    :return:
    """
    dst = cv2.GaussianBlur(src, ksize=kernel, sigmaX=sigma[0], sigmaY=sigma[1])
    return dst


def median_blur(src:np.ndarray, kernel:int) -> np.ndarray:
    """
    メディアンフィルタ(正方形)
    :param src:
    :param kernel: k_xy
    :return:
    """
    dst = cv2.medianBlur(src, ksize=kernel)
    return dst


def bilateral_blur(src:np.ndarray, kernel:int, sigma_space:float, sigma_luminance:float) -> np.ndarray:
    """
    バイラテラルフィルタ(エッジを残しつつのガウシアン平滑化)
    :param src:
    :param kernel:
    :param sigma_space:
    :param sigma_luminance:
    :return:
    """
    dst = cv2.bilateralFilter(src, d=kernel, sigmaColor=sigma_luminance, sigmaSpace=sigma_space)
    return dst


def mosaic_blur(src:np.ndarray, block:Tuple[int, int]) -> np.ndarray:
    """
    モザイク処理
    :param src:
    :param block: (b_x, b_y)
    :return:
    """
    if src.ndim == 2:
        src = src[:, :, np.newaxis]
    height, width, channels = src.shape
    block_mod_x = width % block[0]
    block_mod_y = height % block[1]

    if block_mod_x > 0:
        diff_x = block[0] - block_mod_x
        border_x = np.zeros((src.shape[0], diff_x, channels), np.uint8)
        border_x[:,:] = np.mean(src[:, -diff_x:], axis=1).reshape(src.shape[0], 1, channels)
        src = np.concatenate([src, border_x], axis=1)

    if block_mod_y > 0:
        diff_y = block[1] - block_mod_y
        border_y = np.zeros((diff_y, src.shape[1], channels), np.uint8)
        border_y[:,:] = np.mean(src[-diff_y:, :], axis=0).reshape(1, src.shape[1], channels)
        src = np.concatenate([src, border_y], axis=0)

    block_chunk_x = src.shape[1] // block[0]
    block_chunk_y = src.shape[0] // block[1]
    dst = np.copy(src).astype(dtype=np.float32)
    for j in range(0, block_chunk_y):
        for i in range(0, block_chunk_x):
            patch = src[j*block[1]:(j+1)*block[1], i*block[0]:(i+1)*block[0]]
            mean = np.mean(patch, axis=0)
            mean = np.mean(mean, axis=0)
            dst[j*block[1]:(j+1)*block[1], i*block[0]:(i+1)*block[0]] = mean

    dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)
    dst = dst[:height, :width]
    if channels == 1:
        dst = dst.reshape(dst.shape[0], dst.shape[1])
    return dst
