"""２値化用ダイアログ
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
    NewType
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
from PySide2.QtGui import (
    QImage
)
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

from ui.ui_BinarizeDialog import Ui_BinarizeDialog
from image_window import ImageWindow
from module.utils import new_serial_number_filename
from module.qt_module.qt_def import *
from module.imgproc.binarize import *


class BinarizeDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(BinarizeDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_BinarizeDialog()
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
        # Simple
        self.ui.pBtn_Simple_Apply.clicked.connect(self._apply_simple_binarize)

        # Otsu
        self.ui.pBtn_Otsu_Apply.clicked.connect(self._apply_otsu_binarize)

        # Adaptive
        self.ui.pBtn_Adaptive_Apply.clicked.connect(self._apply_adaptive_binarize)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass


    @Slot()
    def _apply_simple_binarize(self):
        """
        単純２値化
        :return:
        """
        process = "Simple Binarize"
        threshold = self.ui.sBox_Simple_Threshold.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = binarize(src, thresh=threshold)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_otsu_binarize(self):
        """
        大津の２値化(判別分析法)
        :return:
        """
        process = "Otsu Binarize"

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            thresholds, dst = otsu_binarize(src)
            self.ui.lEdit_Otsu_Threshold.setText(str(thresholds))
            return dst, [*thresholds] # リストのアンパック

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process, "otsu_threshold.csv")


    @Slot()
    def _apply_adaptive_binarize(self):
        """
        適用的２値化
        :return:
        """
        process = "Adaptive Binarize"
        patch_size = self.ui.sBox_Adaptive_Patchsize.value()
        sub_thresh_bias = self.ui.sBox_Adaptive_SubThreshBias.value()

        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = adaptive_binarize(src, patch_size=patch_size, sub_thresh_bias=sub_thresh_bias)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)