"""ユニットテスト: シェーディング補正
"""
# 標準
import os
import sys
import shutil
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, NewType)

# サードパーティ
import numpy as np
import cv2

# 自作
cwd = os.getcwd()
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from module.imgproc.shading import shading_correction
from module.imgproc.blur import median_blur, gaussian_blur

def test_shading_correction():
    """
    シェーディング補正のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []

    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    img_master = img_gray
    show_imgs.append(img_master)
    cv2.imwrite("img_master.bmp", img_master)

    # img_base = median_blur(img_gray, kernel=5)
    img_base = gaussian_blur(img_gray, kernel=(7, 7), sigma=(1.3, 1.3))
    show_imgs.append(img_base)

    start = time.perf_counter()
    img_shading = shading_correction(master=img_master, base=img_base, gain=3.5)
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    cv2.imwrite("img_shading.bmp", img_shading)
    show_imgs.append(img_shading)

    img_show = np.concatenate(show_imgs, axis=1)
    cv2.imshow("img_show", img_show)
    cv2.waitKey(0)

if __name__ == "__main__":
    test_shading_correction()
