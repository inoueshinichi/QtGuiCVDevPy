"""ピストン画像加工目のFFT
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

from module.imgproc import fft


def test_fft_piston():
    filename = "NewS43U100C000L120APX-3323_0_1_200721_111454_crop.bmp"
    # filename = "NewS43U100C000L120APX-3323_0_1_200721_111454_crop_2.bmp"
    # filename = "NewS42U100C000L120APX-3323_0_1_200721_111425_crop.bmp"
    # filename = "0545_18rpmU120C000L120_JustFocus_201202_104831_crop.bmp"
    filename = "0545_18rpmU120C000L120_JustFocus_201202_104831_crop_sideall.bmp"
    target_dir = "C:\\Users\\71349012\\Desktop\\2値化_報告書_r1\\test\\"
    target_name = filename.split(".")[0]
    img_src = Image.open(target_dir + filename)
    img_src = np.asarray(img_src)
    print(f"img_src shape: {img_src.shape}")
    show_imgs = []
    show_imgs.append(img_src)

    start = time.perf_counter()

    img_fft, img_fft_mag, _ = fft.fft_2d(img_src, is_shift=True)
    print(f"img_fft shape: {img_fft.shape}")
    show_imgs.append(img_fft_mag)

    # dst_dir = target_dir + "{}_fft_mag.bmp".format(target_name)
    # cv2.imwrite(dst_dir, img_fft_mag)

    fft_height, fft_width = img_fft.shape
    fft_height_half = int(fft_height/2)
    fft_width_half = int(fft_width/2)
    erase_band_x = 10
    erase_band_y = 15
    offset_x = 30
    offset_y = 0

    img_fft[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half - offset_x - erase_band_x : fft_width_half - offset_x + erase_band_x] = 0
    img_fft[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x - erase_band_x : fft_width_half + offset_x + erase_band_x] = 0
    img_fft[fft_height_half - offset_y - erase_band_y : fft_height_half - offset_y + erase_band_y, \
            0 : fft_width_half - offset_x - erase_band_x] = 0
    img_fft[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x + erase_band_x : fft_width] = 0

    img_fft_mag_zero_band = np.copy(img_fft_mag)
    img_fft_mag_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half - offset_x - erase_band_x : fft_width_half - offset_x + erase_band_x] = 0
    img_fft_mag_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x - erase_band_x : fft_width_half + offset_x + erase_band_x] = 0
    img_fft_mag_zero_band[fft_height_half - offset_y - erase_band_y : fft_height_half - offset_y + erase_band_y, \
            0 : fft_width_half - offset_x - erase_band_x] = 0
    img_fft_mag_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x + erase_band_x : fft_width] = 0

    show_imgs.append(img_fft_mag_zero_band)
    # img_pil_fft_mag_zero_band = Image.fromarray(img_fft_mag_zero_band)
    # img_pil_fft_mag_zero_band.save(target_dir + "{0}_fft_mag_zero_band.bmp".format(target_name))

    img_fft_zero_band = np.copy(img_fft)
    img_fft_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half - offset_x - erase_band_x : fft_width_half - offset_x + erase_band_x] = 0
    img_fft_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x - erase_band_x : fft_width_half + offset_x + erase_band_x] = 0
    img_fft_zero_band[fft_height_half - offset_y - erase_band_y : fft_height_half - offset_y + erase_band_y, \
            0 : fft_width_half - offset_x - erase_band_x] = 0
    img_fft_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x + erase_band_x : fft_width] = 0

    img_ifft = fft.ifft_2d(img_fft_zero_band, is_shift=True)

    elapsed_time = (time.perf_counter() - start) * 1000
    print("elapsed_time [ms]", elapsed_time)

    img_pil_ifft = Image.fromarray(img_ifft)
    img_pil_ifft.save(target_dir + "{0}_ffted.bmp".format(target_name))
    show_imgs.append(img_ifft)

    img_show = np.concatenate(show_imgs, axis=1)
    img_pil_all = Image.fromarray(img_show)
    # img_pil_all.save(target_dir + "{0}_transform.png".format(target_name), format='png')
    img_pil_all.show()





if __name__ == "__main__":
    test_fft_piston()