"""ユニットテスト: 幾何学変換
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

from module.imgproc.geometry import (
    flip,
    resize,
    affine2d,
    translate,
    rotate
)


def test_flip():
    """
    フリップのテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()
    flip_img = flip(img_src, flip_pattern='b')
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(flip_img)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


def test_resize():
    """
    拡大・縮小のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    start = time.perf_counter()
    r_w = int(img_src.shape[1]/2)
    r_h = int(img_src.shape[0]/2)
    dst = resize(img_src, (r_w, r_h), interpo=1)
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    img_pil = Image.fromarray(dst)
    img_pil.show()


def test_affine2d():
    """
    アフィン変換のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)


    start = time.perf_counter()
    cy, cx = img_src.shape[:2]
    cx, cy = int(cx/2), int(cy/2)
    dst = affine2d(src=img_src, deg=-20, tran=(0, 0), scale=0.75, center=(cx, cy)) # 回転 -> 平行移動
    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


def test_translate():
    """
    平行移動のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)
    start = time.perf_counter()

    dst = translate(img_src, (0, 0))

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


def test_rotate():
    """
    回転のテスト
    :return:
    """
    img_src = cv2.imread("./data/test04.bmp")
    show_imgs = []
    show_imgs.append(img_src)
    start = time.perf_counter()

    height, width = img_src.shape[:2]
    cx = int(width/2)
    cy = int(height/2)
    dst = rotate(src=img_src, deg=-35, center=(cx,cy))

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


if __name__ == "__main__":
    # test_flip()
    # test_resize()
    # test_affine2d()
    # test_translate()
    test_rotate()
