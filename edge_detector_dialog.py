"""エッジ検出用ダイアログ
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, NewType)


# サードパーティ
import numpy as np
import scipy as sp
import cv2
from PIL import Image
import skimage
from matplotlib import pyplot as plt
import PySide2
from PySide2 import (QtGui, QtCore)
from PySide2.QtCore import (Signal, Slot, Qt, QEvent, QTimer, QPointF)
from PySide2.QtGui import QImage
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QDialog, QMessageBox, QLabel)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_EdgeDetectorDialog import Ui_EdgeDetectorDialog
from image_window import ImageWindow
from module.utils import (new_serial_number_filename)
from module.qt_module.qt_def import *
from module.imgproc.edge_detector import *


class EdgeDetectorDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(EdgeDetectorDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_EdgeDetectorDialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # Closeされたときに自動でメモリ削除

        # Signal/Slot
        self._toolbar_connection()
        self._menubar_connection()
        self._ui_connection()
        self._custom_connection()

    def _toolbar_connection(self):
        """
        ToolBarに関するSignal/Slotの接続
        :return:
        """
        pass

    def _menubar_connection(self):
        """
        MenuBarに関するSignal/Slotの接続
        :return:
        """
        pass

    def _ui_connection(self):
        """
        UIに関するSignal/Slotの接続
        :return:
        """
        # 微分フィルタ
        self.ui.pBtn_Differential_Apply.clicked.connect(self._apply_differential_filter)

        # プレウィットフィルタ
        self.ui.pBtn_Prewitt_Apply.clicked.connect(self._apply_prewitt_filter)

        # ソベルフィルタ
        self.ui.pBtn_Sobel_Apply.clicked.connect(self._apply_sobel_filter)

        # ラプラシアンフィルタ
        self.ui.pBtn_Laplacian_Apply.clicked.connect(self._apply_laplacian_filter)

        # LOGフィルタ
        self.ui.pBtn_LOG_Apply.clicked.connect(self._apply_log_filter)

        # DOGフィルタ
        self.ui.pBtn_DOG_Apply.clicked.connect(self._apply_dog_filter)

        # XDOGフィルタ
        self.ui.pBtn_XDOG_Apply.clicked.connect(self._apply_xdog_filter)

        # Zero Crossing
        self.ui.pBtn_Zero_Crossing_Apply.clicked.connect(self._apply_zero_crossing)

        # Canny
        self.ui.pBtn_Canny_Apply.clicked.connect(self._apply_canny)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_differential_filter(self):
        """
        微分フィルタ
        :return:
        """
        process = "Differential Filter"
        direction = self.ui.cBox_Differential_Direction.currentText()

        def img_proc_func(src:np.ndarray) -> np.ndarray:
            dst = differential_filter(src, direction)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_prewitt_filter(self):
        """
        プレフィットフィルタ
        :return:
        """
        process = "Prewitt Filter"
        direction = self.ui.cBox_Prewitt_Direction.currentText()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = prewitt_filter(src, direction)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_sobel_filter(self):
        """
        ソベルフィルタ
        :return:
        """
        process = "Sobel Filter"
        direction = self.ui.cBox_Sobel_Direction.currentText()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = sobel_filter(src, direction)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_laplacian_filter(self):
        """
        ラプラシアン
        :return:
        """
        process = "Laplacian Filter"
        k_xy = self.ui.sBox_Laplacian_kxy.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = laplacian_filter(src, ksize=k_xy)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_log_filter(self):
        """
        LOG(Laplacian Of Gaussian)
        :return:
        """
        process = "LOG Filter"
        k_xy = self.ui.sBox_LOG_kxy.value()
        sigma = self.ui.dsBox_LOG_Sigma.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = log_filter(src, ksize=k_xy, sigma=sigma)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    def _apply_dog_filter(self):
        """
        DOG(Differential Of Gaussian)
        :return:
        """
        process = "DOG Filter"
        k_xy = self.ui.sBox_DOG_kxy.value()
        sigma = self.ui.dsBox_DOG_Sigma.value()
        k = self.ui.dsBox_DOG_k.value()
        gamma = self.ui.dsBox_DOG_gamma.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = dog_filter(src, ksize=k_xy, sigma=sigma, k=k, gamma=gamma)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_xdog_filter(self):
        """
        XDOGフィルタ
        :return:
        """
        process = "XDOG Filter"
        k_xy = self.ui.sBox_XDOG_kxy.value()
        sigma = self.ui.dsBox_XDOG_Sigma.value()
        k = self.ui.dsBox_XDOG_k.value()
        p = self.ui.dsBox_XDOG_p.value()
        phi = self.ui.dsBox_XDOG_phi.value()
        eps = self.ui.dsBox_XDOG_eps.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = xdog_filter(src, ksize=k_xy, p=p, phi=phi, eps=eps, sigma=sigma, k=k)
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_zero_crossing(self):
        """
        ROGフィルタ+ゼロ点交差処理によるエッジ検出
        :return:
        """
        process = "Zero Crossing"
        k_xy = self.ui.sBox_Zero_Crossing_kxy.value()
        sigma = self.ui.dsBox_Zero_Crossing_Sigma.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = log_filter(src, ksize=k_xy, sigma=sigma)
            dst = zero_crossing(dst) # ゼロ点交差
            lum_min = np.min(dst)
            lum_max = np.max(dst)
            dst = (dst - lum_min) / (lum_max - lum_min)
            dst *= 255
            dst = np.clip(a=dst, a_min=0, a_max=255).astype(np.uint8)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_canny(self):
        """
        キャニーエッジ検出
        :return:
        """
        process = "Canny"
        hys_upper = self.ui.sBox_Canny_Hysterisis_Upper.value()
        hys_lower = self.ui.sBox_Canny_Hysterisis_Lower.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = canny(src, hys_upper, hys_lower)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)