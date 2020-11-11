"""シェーディング"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, TypeVar, NoReturn, Generic)
from collections import namedtuple

# サードパーティ
import numpy as np
import scipy as sp
from scipy.ndimage import filters
import cv2
from PIL import Image
import skimage

# 自作


"""
OK シェーディング補正(輝度ムラを取り除く処理)
"""


def shading_correction(master:np.ndarray, base:np.ndarray, gain:float=1.0) -> np.ndarray:
    """
    シェーディング補正
    :param master: 輝度ムラがある補正対象画像(前景が写ってる)
    :param base: 補正に使用する全体的な明暗変化を表した明暗分布画像(およそ補正対象画像の背景成分が強い画像)
    :return:
    """
    assert master.ndim == 2, "master must be grayscale; 2dim."
    assert base.ndim == 2, "base must be grayscale; 2dim."
    assert master.shape == base.shape, \
        "master and base must be same shape. master:{0}, base:{1}".format(master.shape, base.shape)

    tmp_master = master.astype(np.float64)
    tmp_base = base.astype(np.float64)

    # 画素値1.0以下を1.0に制限
    tmp_master[tmp_master < 1.0] = 1.0
    tmp_base[tmp_base < 1.0] = 1.0

    # シェーディング補正
    diff_element = (tmp_master / tmp_base) * 128.0 - 128.0 # base画像に対してmaster画像の変化が大きな輝度成分だけを取り出す
    dst = 128.0 + diff_element * gain
    dst = np.clip(dst, a_min=0, a_max=255).astype(np.uint8)

    return dst





