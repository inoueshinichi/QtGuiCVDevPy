"""ユニットテスト: 解像度
"""


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

from module.imgproc.resolution import (
    down_sampler,
    up_sampler,
    gaussian_pyramid,
    laplacian_pyramid
)

def test_down_sampler():
    """
    ダウンサンプリングのテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()
    # n_octarve = 5
    # for i in range(1, n_octarve + 1):
    #     dst = down_sampler(img_src, n_octave=i)
    #     show_imgs.append(dst)
    dst_list = gaussian_pyramid(src=img_src, n_octave=5)
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs += dst_list

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()

def test_laplacian_pyramid():
    """
    ラプラシアンピラミッドのテスト
    :return:
    """
    img_src = cv2.imread("./data/dog.bmp")
    img_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    # img_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()
    dst_list = laplacian_pyramid(img_src, n_octave=10)
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    results = []
    for diff in dst_list:
        diff_max = diff.max()
        diff_min = diff.min()
        diff_norm = (diff - diff_min) / (diff_max - diff_min)
        diff_norm *= 255
        diff_norm = np.clip(a=diff_norm, a_min=0, a_max=255).astype(np.uint8)
        results.append(diff_norm)

    show_imgs += results

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()

def test_up_sampler():
    """
    アップサンプリングのテスト
    :return:
    """
    img_src = cv2.imread("./data/dog.bmp")
    img_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    # img_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)

    start = time.perf_counter()
    dst = up_sampler(img_src, n_octave=1)
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)

    img_pil = Image.fromarray(dst)
    img_pil.show()

    img_pil_ori = Image.fromarray(img_src)
    img_pil_ori.show()

if __name__ == "__main__":
    # test_resolve_lower()
    # test_laplacian_pyramid()
    test_up_sampler()