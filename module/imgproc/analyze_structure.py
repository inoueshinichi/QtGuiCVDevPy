"""構造解析
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
OK ラベリング
OK 主軸角度
-- 周囲長
-- 円形度
-- 輪郭線抽出
-- 面積
-- 重心
-- 外接面積
-- 指定エリアの標準偏差
-- 指定エリアの2値画像個数
"""

def labeling(src:np.ndarray) -> Tuple[int, np.ndarray, List[NamedTuple]]:
    """
    ラベリング
    :param src: ２値画像
    :return:  ラベル数, ラベリング画像, List[namedTuple(label, center, x, y, w, h, size), ...] ※ cx, cyは, float型
    """
    assert src.ndim == 2, "Dimension of src must be 2 dim."

    n_labels, label_images, data, centers = cv2.connectedComponentsWithStats(src)

    # 背景の情報を除外
    label_count = n_labels - 1 # 背景を除く
    data = np.delete(data, 0, 0)
    centers = np.delete(centers, 0, 0)

    features = []
    for i in range(len(data)):
        feat = namedtuple("Feature", [
            'label',
            'x',
            'y',
            'w',
            'h',
            'area',
            'center'
        ])
        features.append(feat(i, data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], tuple(centers[i])))

    return (label_count, label_images, features)


def principal_axes_angle(src_labeling:np.ndarray, label:int) -> Tuple[float, List[Tuple[int, int]]]:
    """
    主軸角度を計算
    :param src_labeling: ラベリング画像 背景:0, 前景:1, 2, 3, ...,で画素値が分類された画像
    :param label: ラベル番号: 1~N
    :return: 主軸角度:[deg], 主軸角度を持つ直線と画像縁との交点座標: [(x1,y1), (x2,y2)]
    """
    assert label != 0, "label must be > 0."
    assert src_labeling.ndim == 2, "Dimension of src_labeling must be 2 dim."

    # ラベルで指定したオブジェクトだけを前景にもつ２値画像
    img_target_binary = np.copy(src_labeling)
    img_target_binary[img_target_binary != label] = 0
    img_target_binary[img_target_binary == label] = 255
    img_target_binary = img_target_binary.astype(np.uint8)

    # 前景に対するモーメント値から主軸角度を計算
    # http://opencv.jp/opencv-2svn/cpp/structural_analysis_and_shape_descriptors.html
    moment = cv2.moments(img_target_binary)
    area = moment['m00']
    x_g = moment['m10'] / area
    y_g = moment['m01'] / area
    angle_rad = 0.5 * math.atan2(2.0 * moment['mu11'], moment['mu20'] - moment['mu02'])
    angle_deg = math.degrees(angle_rad)

    # 直線
    line_points = None
    height, width = img_target_binary.shape
    if angle_deg == 90:
        line_points = [(int(x_g), 0), (int(x_g), height - 1)]
    elif angle_deg == 0:
        line_points = [(0, int(y_g)), (width - 1, int(y_g))]
    else:
        cx = x_g
        cy = y_g
        x1 = 0
        y1 = math.tan(angle_rad) * (x1 - cx) + cy
        pt1 = tuple()
        pt2 = tuple()

        # pt1決定
        if y1 < 0:
            y1 = 0
            x1 = (y1 - cy) / math.tan(angle_rad) + cx
            pt1 = (int(x1), int(y1)) # 確定
        elif y1 < height:
            pt1 = (int(x1), int(y1)) # 確定
        else:
            y1 = height - 1
            x1 = (y1 - cy) / math.tan(angle_rad) + cx
            pt1 = (int(x1), int(y1))  # 確定

        # pt2決定
        x2 = width - 1
        y2 = math.tan(angle_rad) * (x2 - cx) + cy
        if y2 < 0:
            y2 = 0
            x2 = (y2 - cy) / math.tan(angle_rad) + cx
            pt2 = (int(x2), int(y2))  # 確定
        elif y2 < height:
            pt2 = (int(x2), int(y2))  # 確定
        else:
            y2 = height - 1
            x2 = (y2 - cy) / math.tan(angle_rad) + cx
            pt2 = (int(x2), int(y2))  # 確定

        line_points = [pt1, pt2]

    return angle_deg, line_points



