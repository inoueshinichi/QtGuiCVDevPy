"""ブラー処理用のダイアログ
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Callable,
    Any,
    TypeVar,
    Generic,
    NoReturn
)


# サードパーティ
import numpy as np
import scipy as sp
import cv2
from PIL import Image
import skimage
from matplotlib import pyplot as plt
import PySide2
from PySide2 import (
    QtGui,
    QtCore
)
from PySide2.QtCore import (
    Signal,
    Slot,
    Qt,
    QEvent,
    QTimer,
    QPointF
)
from PySide2.QtGui import QImage
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFileDialog,
    QDialog,
    QMessageBox,
    QLabel
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_BlurDialog import Ui_BlurDialog
from module import utils
from module.qt_module import qt_def
from module.imgproc import blur

class BlurDialog(QDialog):

    def __init__(self,
                 parent: QWidget = None):

        super(BlurDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_BlurDialog()
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
        # Gaussian
        self.ui.pBtn_Gaussian_Apply.clicked.connect(self._apply_gaussian_blur)

        # Median
        self.ui.pBtn_Meidan_Apply.clicked.connect(self._apply_median_blur)

        # Bilateral
        self.ui.pBtn_Bilateral_Apply.clicked.connect(self._apply_bilateral_blur)

        # Mosaic
        self.ui.pBtn_Mosaic_Apply.clicked.connect(self._apply_mosaic_blur)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_gaussian_blur(self):
        """
        ガウシアンフィルタ
        :return:
        """
        process = "Gaussian Blur"
        k_x = self.ui.sBox_Gaussian_k_x.value()
        k_y = self.ui.sBox_Gaussian_k_y.value()
        std_x = self.ui.dsBox_Gaussian_std_x.value()
        std_y = self.ui.dsBox_Gaussian_std_y.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = blur.gaussian_blur(src, kernel=(k_x, k_y), sigma=(std_x, std_y))
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            qt_def.help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            qt_def.help_process_file_mode(self, img_proc_func, process)


    @Slot()
    def _apply_median_blur(self):
        """
        メディアンフィルタ
        :return:
        """
        process = "Median Blur"
        k_xy = self.ui.sBox_Median_k_xy.value()

        def img_proc_func(src:np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = blur.median_blur(src, kernel=k_xy)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            qt_def.help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            qt_def.help_process_file_mode(self, img_proc_func, process)


    @Slot()
    def _apply_bilateral_blur(self):
        """
        バイラテラルフィルタ
        :return:
        """
        process = "Bilateral Blur"
        k_xy = self.ui.sBox_Bilateral_k_xy.value()
        sigma_space = self.ui.dsBox_Bilateral_std_space.value()
        sigma_lum = self.ui.dsBox_Bilateral_std_luminace.value()

        def img_proc_func(src:np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = blur.bilateral_blur(src, kernel=k_xy, sigma_space=sigma_space, sigma_luminance=sigma_lum)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            qt_def.help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            qt_def.help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_mosaic_blur(self):
        """
        モザイク処理
        :return:
        """
        process = "Mosaic Blur"
        blck_x = self.ui.sBox_Mosaic_block_x.value()
        blck_y = self.ui.sBox_Mosaic_block_y.value()

        def img_proc_func(src:np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = blur.mosaic_blur(src, block=(blck_x, blck_y))
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            qt_def.help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            qt_def.help_process_file_mode(self, img_proc_func, process)
