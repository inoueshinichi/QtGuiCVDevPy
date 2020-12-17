"""3次元ビジョン関係
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
-- 基礎行列Fの推定
-- 基本行列Eの推定
-- エピポーラ線の推定
-- 三角測量による2D→3Dの推定
-- 特徴点検出→特徴点マッチング→基礎行列Fの推定、基本行列Eの推定, 三角測量 (Structure From Motion パターン１)
-- 因子分解法によるStructure From Motion パターン２
-- LookAt方式によるカメラ位置姿勢の計算
-- 回転行列(rot_x, rot_y, rot_z)
-- オイラー角(ZXY)⇔回転行列
-- 回転行列⇔回転ベクトル
-- 回転行列⇔クォータニオン
-- クォータニオン⇔回転ベクトル
-- 右手座標系⇔左手座標系
-- 3D座標変換
-- ステレオ視による視差マップの生成
-- 複数視点で撮影された画像をある指定した位置での画像に変換する(平行化処理)
"""