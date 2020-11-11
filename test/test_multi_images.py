"""ユニットテスト：複数画像を用いた演算
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

from module.imgproc.multi_images import (
    add_two_imgs,
    sub_two_imgs,
    mul_two_imgs,
    div_two_imgs,
    add_img,
    sub_img,
    mul_img,
    div_img,
    average_of_imgs,
    blend_two_imgs,
    chromakey
)

def test_multi_calc():
    """
    ２枚の画像を用いた四則演算のテスト
    :return:
    """
    show_imgs = []
    img_src1 = cv2.imread("./data/test02.bmp")
    show_imgs.append(img_src1)
    img_src2 = cv2.imread("./data/test04.bmp")
    show_imgs.append(img_src2)



    # dst = add_two_imgs(img_src1, img_src2, is_clip=True)
    # dst = sub_two_imgs(img_src1, img_src2, is_clip=True)
    # dst = mul_two_imgs(img_src1, img_src2, is_clip=True)
    # dst = sub_two_imgs(img_src1, img_src2, is_clip=True)
    dst = add_img(img_src1, add=50, is_clip=True)
    show_imgs.append(dst)
    dst = sub_img(img_src1, sub=50, is_clip=True)
    show_imgs.append(dst)
    dst = mul_img(img_src1, mul=1.5, is_clip=True)
    show_imgs.append(dst)
    dst = div_img(img_src1, div=1.5, is_clip=True)
    show_imgs.append(dst)


    dst = average_of_imgs(show_imgs, is_clip=True)
    show_imgs.append(dst)

    start = time.perf_counter()
    dst = blend_two_imgs(img_src1, img_src2, ratio=0.1, bias=-10, is_clip=True)

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


def test_chromakey():
    """
    クロマキー合成のテスト
    :return:
    """
    show_imgs = []
    img_src1 = cv2.imread("./data/test04.bmp")
    show_imgs.append(img_src1)
    img_src2 = cv2.imread("./data/dog.bmp")
    tmp_src2 = np.zeros_like(img_src1)
    tmp_src2[:img_src2.shape[0], :img_src2.shape[1]] = img_src2
    show_imgs.append(tmp_src2)

    start = time.perf_counter()

    dst = chromakey(img_src1, img_src2, pos=(150, 100))

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)
    show_imgs.append(dst)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil = Image.fromarray(img_show)
    img_pil.show()


if __name__ == "__main__":
    # test_multi_calc()
    test_chromakey()