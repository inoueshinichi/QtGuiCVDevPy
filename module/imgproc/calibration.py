"""カメラキャリブレーション"""

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
-- PnP Solver
-- Zhang Calibration
-- 
-- 
"""


def pnp_solver(img_points: np.ndarray, obj_points: np.ndarray) -> Union[np.ndarray, None]:
    """
    6組以上の2次元点(画像点)と3次元点の対応点を与えて、DLT(Direct Linear Transform)Ax=bの
    最小二乗解をムーアペンローズの疑似逆行列を用いて解く
    :param img_points: (N,2) [u,v]
    :param obj_points: (N,3) [x_w, y_w, z_w]
    :return: 透視投影変換行列 (3,4)
    """

    # DLT法
    A = np.zeros((obj_points.shape[0] * 2, 11), dtype=np.float64)
    b = np.zeros((obj_points.shape[1] * 2, 1), dtype=np.float64)
    for row in range(0, obj_points.shape[0], 2):
        # 偶数行目
        A[row, 0:3] = obj_points[row, 0:3] # (x_w, y_w, z_w)
        A[row, 3] = 1.0
        A[row, 8] -= img_points[row, 0] * obj_points[row, 0]  # -u * x_w
        A[row, 9] -= img_points[row, 0] * obj_points[row, 1]  # -u * y_w
        A[row, 10] -= img_points[row, 0] * obj_points[row, 2] # -u * z_w
        b[row, 0] = img_points[row, 0] # u

        # 奇数行目
        A[row + 1, 4:7] = obj_points[row, 0:3] # (x_w, y_w, z_w)
        A[row + 1, 7] = 1.0
        A[row + 1, 8] -= img_points[row, 1] * obj_points[row, 0]  # -v * x_w
        A[row + 1, 9] -= img_points[row, 1] * obj_points[row, 1]  # -v * y_w
        A[row + 1, 10] -= img_points[row, 1] * obj_points[row, 2]  # -v * z_w
        b[row + 1, 0] = img_points[row, 1] # v


    # SVDを用いてAx=bの最小二乗解を求める
    is_success, core_projection = cv2.solve(src1=A, src2=b, flags=cv2.DECOMP_SVD)
    if not is_success:
        print("Failed to SVD decompose Ax=b in DLT method.")
        return None
    else:
        print(f"")
