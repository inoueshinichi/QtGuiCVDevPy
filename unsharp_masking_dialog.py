"""先鋭化処理のダイアログ
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

from ui.ui_UnsharpMaskingDialog import Ui_UnsharpMaskingDialog
from image_window import ImageWindow
from module.utils import new_serial_number_filename
from module.qt_module.qt_def import *
from module.imgproc.unsharp_masking import *


class UnsharpMaskingDialog(QDialog):

    def __init__(self, parent: QWidget = None):
        super(UnsharpMaskingDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_UnsharpMaskingDialog()
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
        # Sharpen
        self.ui.pBtn_Sharpen_Apply.clicked.connect(self._apply_sharpen)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_sharpen(self):
        """
        先鋭化フィルタ
        :return:
        """
        process = "Sharpen Filter"
        k_xy = self.ui.sBox_Sharpen_k_xy.value()
        sigma = self.ui.dsBox_Sharpen_Sigma.value()
        strong = self.ui.dsBox_Sharpen_Strong.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = sharpen_filter(src, ksize=k_xy, sigma=sigma, strong=strong)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)