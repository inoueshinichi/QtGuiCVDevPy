"""ユニットテスト：濃淡変換"""

# 標準
import os
import sys
import shutil
import pathlib
import math
import time

# サードパーティ
import numpy as np
import cv2
from PIL import Image

# 自作
cwd = os.getcwd()
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from module.imgproc.mapping import (
    gamma_mapping,
    linear_mapping,
    clip_mapping
)

def test_gamma_mapping():
    """
    ガンマ補正のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()

    dst = gamma_mapping(img_src, gamma=50)

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


def test_linear_mapping():
    """
    線形濃淡変換のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()

    dst = linear_mapping(img_src, alpha=0.8, beta=0)

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


def test_clip_mapping():
    """
    clip_mappingのテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()


    dst = clip_mapping(img_src, lum_low=50, lum_high=200, is_contrast_up=False)

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()

if __name__ == "__main__":
    # test_gamma_mapping()
    # test_linear_mapping()
    test_clip_mapping()
