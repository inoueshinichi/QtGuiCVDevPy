"""寸法測定など
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
-- 直線の寸法
-- 曲率
-- 最小2乗法による直線検出
-- 2次曲線近似
"""
