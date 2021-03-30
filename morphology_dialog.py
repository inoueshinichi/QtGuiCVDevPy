"""モルフォロジー処理用のダイアログ
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
    NewType,
    Generic
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
    QLabel,
    QHeaderView
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_MorphologyDialog import Ui_MorphologyDialog
from image_window import ImageWindow
from module.utils import new_serial_number_filename
from module.qt_module.qt_def import *
from module.imgproc.morphology import *


class MorphologyDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(MorphologyDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_MorphologyDialog()
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
        # Dilation(膨張)
        self.ui.pBtn_Dilation_Apply.clicked.connect(self._apply_dilation)

        # Erosion(収縮)
        self.ui.pBtn_Erosion_Apply.clicked.connect(self._apply_erosion)

        # Opening(ノイズ除去)
        self.ui.pBtn_Opening_Apply.clicked.connect(self._apply_opening)

        # Closing(穴埋め)
        self.ui.pBtn_Closing_Apply.clicked.connect(self._apply_closing)

        # 輪郭線検出
        self.ui.pBtn_Outline_Apply.clicked.connect(self._apply_outline)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_dilation(self):
        """
        膨張処理
        :return:
        """
        process = "Dilation"
        k_xy = self.ui.sBox_Dilation_k_xy.value()
        iter_num = self.ui.sBox_Dilation_iter.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = dilation(src, ksize=k_xy, iterations=iter_num)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_erosion(self):
        """
        収縮処理
        :return:
        """
        process = "Erosion"
        k_xy = self.ui.sBox_Erosion_k_xy.value()
        iter_num = self.ui.sBox_Erosion_iter.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = erosion(src, ksize=k_xy, iterations=iter_num)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_opening(self):
        """
        オープニング
        :return:
        """
        process = "Opening"
        k_xy = self.ui.sBox_Opening_k_xy.value()
        iter_num = self.ui.sBox_Opening_iter.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = opening(src, ksize=k_xy, iterations=iter_num)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_closing(self):
        """
        クロージング
        :return:
        """
        process = "Closing"
        k_xy = self.ui.sBox_Closing_k_xy.value()
        iter_num = self.ui.sBox_Closing_iter.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = closing(src, ksize=k_xy, iterations=iter_num)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_outline(self):
        """
        輪郭線抽出
        :return:
        """
        process = "Outline"
        k_xy = self.ui.sBox_Outline_k_xy.value()
        iter_num = self.ui.sBox_Outline_iter.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = outline(src, ksize=k_xy, iterations=iter_num)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

