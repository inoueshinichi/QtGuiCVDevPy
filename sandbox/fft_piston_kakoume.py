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
from module.imgproc import blur
from module.imgproc import binarize
from module.imgproc import morphology


def test_fft_piston():
    # filename = "NewS41U100C000L120APX-3323_0_1_200721_111351_crop.bmp"
    # filename = "NewS41U100C000L120APX-3323_0_1_200721_111351_crop-1.bmp"
    # filename = "NewS41U100C000L120APX-3323_0_1_200721_111351_crop-2.bmp"
    filename = "NewS41U100C000L120APX-3323_0_1_200721_111351_crop-3.bmp"
    target_dir = "C:\\Users\\71349012\\Desktop\\201217_二値化_報告\\FFT\\ピストン側面検査_金属部寸法測定用画像処理ロジック\\おまけ_コート部位置ずれ\\NewS41U100_コート部"
    target_name = filename.split(".")[0]
    img_src = Image.open(target_dir + "\\" + filename)
    img_src = np.asarray(img_src)
    print(f"img_src shape: {img_src.shape}")
    show_imgs = []
    show_imgs.append(np.dstack((img_src, img_src, img_src)))

    # start = time.perf_counter()

    img_fft, img_fft_mag, _ = fft.fft_2d(img_src, is_shift=True)
    print(f"img_fft shape: {img_fft.shape}")
    show_imgs.append(np.dstack((img_fft_mag, img_fft_mag, img_fft_mag)))

    # dst_dir = target_dir + "{}_fft_mag.bmp".format(target_name)
    # cv2.imwrite(dst_dir, img_fft_mag)

    fft_height, fft_width = img_fft.shape
    fft_height_half = int(fft_height/2)
    fft_width_half = int(fft_width/2)
    erase_band_x = 10
    erase_band_y = 15
    offset_x = 30
    offset_y = 0

    # img_fft[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
    #         fft_width_half - offset_x - erase_band_x : fft_width_half - offset_x + erase_band_x] = 0
    # img_fft[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
    #         fft_width_half + offset_x - erase_band_x : fft_width_half + offset_x + erase_band_x] = 0
    img_fft[fft_height_half - offset_y - erase_band_y : fft_height_half - offset_y + erase_band_y, \
            0 : fft_width_half - offset_x - erase_band_x] = 0
    img_fft[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x + erase_band_x : fft_width] = 0

    img_fft_mag_zero_band = np.copy(img_fft_mag)
    # img_fft_mag_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
    #         fft_width_half - offset_x - erase_band_x : fft_width_half - offset_x + erase_band_x] = 0
    # img_fft_mag_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
    #         fft_width_half + offset_x - erase_band_x : fft_width_half + offset_x + erase_band_x] = 0
    img_fft_mag_zero_band[fft_height_half - offset_y - erase_band_y : fft_height_half - offset_y + erase_band_y, \
            0 : fft_width_half - offset_x - erase_band_x] = 0
    img_fft_mag_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x + erase_band_x : fft_width] = 0

    show_imgs.append(np.dstack((img_fft_mag_zero_band, img_fft_mag_zero_band, img_fft_mag_zero_band)))
    # img_pil_fft_mag_zero_band = Image.fromarray(img_fft_mag_zero_band)
    # img_pil_fft_mag_zero_band.save(target_dir + "{0}_fft_mag_zero_band.bmp".format(target_name))

    img_fft_zero_band = np.copy(img_fft)
    # img_fft_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
    #         fft_width_half - offset_x - erase_band_x : fft_width_half - offset_x + erase_band_x] = 0
    # img_fft_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
    #         fft_width_half + offset_x - erase_band_x : fft_width_half + offset_x + erase_band_x] = 0
    img_fft_zero_band[fft_height_half - offset_y - erase_band_y : fft_height_half - offset_y + erase_band_y, \
            0 : fft_width_half - offset_x - erase_band_x] = 0
    img_fft_zero_band[fft_height_half + offset_y - erase_band_y : fft_height_half + offset_y + erase_band_y, \
            fft_width_half + offset_x + erase_band_x : fft_width] = 0

    # 1) バンドパス
    img_ifft = fft.ifft_2d(img_fft_zero_band, is_shift=True)

    # 2) メディアん
    median_kernel_size = 17
    img_median = blur.median_blur(img_ifft, median_kernel_size)

    # 3) バイラテラル
    bilateral_kernel_size = 31
    pos_std = 30
    lum_std = 20
    img_bilateral = blur.bilateral_blur(img_median, bilateral_kernel_size, pos_std, lum_std)

    # 4) 大津二値化
    thresholds, img_otsu_binary = binarize.otsu_binarize(img_bilateral)

    # 5) エッジ検出
    outline_kernel_size = 3
    img_outline = morphology.outline(img_otsu_binary, outline_kernel_size)
    # マゼンタ
    overray_mask = (img_outline > 0).astype(np.uint8)
    inv_overray_mask = np.logical_not(overray_mask)
    img_overray_red = np.copy(img_src) * inv_overray_mask + overray_mask * 228  # 赤
    img_overray_green = np.copy(img_src) * inv_overray_mask + overray_mask * 0  # 緑
    img_overray_blue = np.copy(img_src) * inv_overray_mask + overray_mask * 127 # 青
    img_edge_overray = np.dstack((img_overray_red, img_overray_green, img_overray_blue))


    # elapsed_time = (time.perf_counter() - start) * 1000
    # print("elapsed_time [ms]", elapsed_time)

    # バンドパスフィルタ後
    img_pil_ifft = Image.fromarray(img_ifft)
    img_pil_ifft.save(target_dir + "_result" + "\\" + "0_bandpass" + "\\" + "{0}_bandpass_offset_x={1}.bmp".format(target_name, offset_x))
    show_imgs.append(np.dstack((img_ifft, img_ifft, img_ifft)))
    # cv2.imshow("bandpass", img_ifft)
    # cv2.waitKey(0)

    # メディアンフィルタ後
    img_pil_median = Image.fromarray(img_median)
    img_pil_median.save(target_dir + "_result" + "\\" + "1_median" + "\\" + "{0}_median{1}.bmp".format(target_name, median_kernel_size))
    show_imgs.append(np.dstack((img_median, img_median, img_median)))
    # cv2.imshow("median", img_median)
    # cv2.waitKey(0)

    # バイラテラルフィルタ後
    img_pil_bilateral = Image.fromarray(img_bilateral)
    img_pil_bilateral.save(target_dir + "_result" + "\\" + "2_birateral" + "\\" + "{0}_bilateral_{1}_posstd={2}_lumstd={3}.bmp".format(target_name, bilateral_kernel_size, pos_std, lum_std))
    show_imgs.append(np.dstack((img_bilateral, img_bilateral, img_bilateral)))
    # cv2.imshow("bilateral", img_bilateral)
    # cv2.waitKey(0)

    # 大津二値化後
    img_pil_otsu_binary = Image.fromarray(img_otsu_binary)
    img_pil_otsu_binary.save(target_dir + "_result" + "\\" + "3_otsu_binary" + "\\" + "{0}_otsu_binary_thresh={1}.bmp".format(target_name, thresholds[0]))
    show_imgs.append(np.dstack((img_otsu_binary, img_otsu_binary, img_otsu_binary)))
    # cv2.imshow("otsu_binary", img_otsu_binary)
    # cv2.waitKey(0)

    # 原画像にエッジオーバーレイ後
    img_pil_edge_overray = Image.fromarray(img_edge_overray)
    img_pil_edge_overray.save(target_dir + "_result" + "\\" + "4_edge_overray" + "\\" + "{0}_edge_overray.bmp".format(target_name))
    show_imgs.append(img_edge_overray)
    # cv2.imshow("edge_overray", img_edge_overray)
    # cv2.waitKey(0)

    img_show_1 = np.concatenate(show_imgs[:4], axis=1)
    img_show_2 = np.concatenate(show_imgs[4:], axis=1)
    img_show = np.concatenate([img_show_1, img_show_2], axis=0)
    print(f"img_show shape: {img_show.shape}")
    # img_show = img_show.transpose((2, 0, 1))
    img_pil_all = Image.fromarray(img_show.astype(np.uint8))
    img_pil_all.save(target_dir + "_result" + "\\""{0}_transform.png".format(target_name), format='png')
    img_pil_all.show()






if __name__ == "__main__":
    test_fft_piston()