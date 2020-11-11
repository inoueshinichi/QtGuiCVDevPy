"""画像の縁処理
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
OK 縁の追加
-- 縁の削除
"""

def make_border(src:np.ndarray, extended_pixels:List[int], constant_colors:List[int], border_type:str) -> np.ndarray:
    """
    画像の縁の追加
    :param src:
    :param extended_pixels: 追加するピクセル数 (left, top, right, bottom)
    :param constant_colors: 固定色時の色 (gray, red, green, blue)
    :param border_type: ボーダーパターン
    Reflect  [gfedcb|abcdefgh|gfedcba]
    Replicate  [aaaaaa|abcdefgh|hhhhhhh]
    Warp  [cdefgh|abcdefgh|abcdefg]
    # Transparent  [uvwxyz|absdefgh|ijklmno] ※除外
    Constant  [iiiiii|abcdefgh|iiiiiii]
    :return:
    """

    if border_type == "Reflect":
        border_type = cv2.BORDER_REFLECT
    elif border_type == "Replicate":
        border_type = cv2.BORDER_REPLICATE
    elif border_type == "Warp":
        border_type = cv2.BORDER_WRAP
    elif border_type == "Constant":
        border_type = cv2.BORDER_CONSTANT
    else:
        assert False, "Invalid Border Type."
    """
    # BORDER_TYPE
    # BORDER_DEFAULT:      BORDER_REFLECT_101
    # BORDER_CONSTANT:     iiiiii|abcdefgh|iiiiiii with i
    # BORDER_REFLECT:      fedcba|abcdefgh|hgfedcb
    # BORDER_REFLECT_101:  gfedcb|abcdefgh|gfedcba
    # BORDER_REFLECT101:   BORDER_REFLECT_101
    # BORDER_WRAP:         cdefgh|abcdefgh|abcdefg
    # BORDER_TRANSPARENT:  uvwxyz|absdefgh|ijklmno
    # BORDER_REPLICATE:    aaaaaa|abcdefgh|hhhhhhh
    # BORDER_ISOLATE:      do not look outside of ROI (パディングなし)
    """

    left, top, right, bottom = extended_pixels
    gray, red, green, blue = constant_colors
    constant_value = (red, green, blue) if src.ndim == 3 else gray
    dst = cv2.copyMakeBorder(src,
                             top=top, left=left,
                             bottom=bottom, right=right,
                             value=constant_value, borderType=border_type)

    return dst


def erase_border(src:np.ndarray, erase_pixels:List[int]) -> np.ndarray:
    """
    画像の縁の削除
    :param src:
    :param erase_pixels:
    :return:
    """
    if src.ndim == 2:
        height, width = src.shape
    else:
        height, width, _ = src.shape

    left, top, right, bottom = erase_pixels
    right = width - right
    bottom = height - bottom

    dst = src[top:bottom, left:right]
    return dst
