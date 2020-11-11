"""図形
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
OK 直線
-- 楕円
-- 矩形

"""

def line(src:np.ndarray, pt1:Tuple[int, int], pt2:Tuple[int, int], color=Union[int, Tuple[int, int, int]], thickness:int=1) -> np.ndarray:
    """
    直線の描画
    :param src:
    :param pt1: 点1 (x,y)
    :param pt2: 点2 (x,y)
    :param color: 色 (r, g, b) or 明度(int) 0-255
    :param thickness: 直線の幅
    :return:
    """
    dst = cv2.line(src, pt1=pt1, pt2=pt2, color=color, thickness=thickness, lineType=cv2.LINE_8) # cv2.LINE_8がデフォ
    return dst

