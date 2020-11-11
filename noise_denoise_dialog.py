"""ノイズ付加/ノイズ除去のダイアログ
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, TypeVar, NoReturn, Generic)

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

from ui.ui_NoiseDenoiseDialog import Ui_NoiseDenoiseDialog
from image_window import ImageWindow
from module.utils import (new_serial_number_filename)
from module.qt_module.qt_def import *
from module.imgproc.noise_denoise import *

class NoiseDenoiseDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(NoiseDenoiseDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_NoiseDenoiseDialog()
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
        # Uniform Noise
        self.ui.pBtn_Uniform_Apply.clicked.connect(self._apply_uniform_noise)

        # Standard Noise
        self.ui.pBtn_Standard_Apply.clicked.connect(self._apply_standard_noise)

        # ROF Denoise
        self.ui.pBtn_ROF_Apply.clicked.connect(self._apply_denoise_rof)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_uniform_noise(self):
        """
        一様分布に基づくノイズを付加する処理
        :return:
        """
        process = "Uniform Noise"
        lower = self.ui.sBox_Uniform_Lower.value()
        upper = self.ui.sBox_Uniform_Upper.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            random_state = np.random.RandomState(None)
            dst = noise_uniform(src, lower, upper, random_state)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)


    @Slot()
    def _apply_standard_noise(self):
        """
        正規分布(平均，標準偏差は指定)に基づくノイズを付加する処理
        :return:
        """
        process = "Standard Noise"
        mean = self.ui.dsBox_Standard_Mean.value()
        sigma = self.ui.dsBox_Standard_Sigma.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            random_state = np.random.RandomState(None)
            dst = noise_standard(src, mean, sigma, random_state)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_denoise_rof(self):
        """
        ROF Denoise処理
        :return:
        """
        process = "Rudin-Osher-Fatemi(ROF) Denoise"
        tolerance = self.ui.dsBox_ROF_Tolerance.value()
        step_tau = self.ui.dsBox_ROF_Step.value()
        tv_weight = self.ui.sBox_ROF_Norm_Weight.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst, _ = denoise_rof(src, src, tolerance=tolerance, step=step_tau, tv_weight=tv_weight)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)