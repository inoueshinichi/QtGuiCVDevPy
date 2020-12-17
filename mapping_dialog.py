"""濃淡変換処理用ダイアログ
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

from ui.ui_MappingDialog import Ui_MappingDialog
from module import utils
from module.qt_module import qt_def
from module.imgproc import mapping


class MappingDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(MappingDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_MappingDialog()
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
        # ガンマ補正
        self.ui.pBtn_Gamma_Apply.clicked.connect(self._apply_gamma_correction)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_gamma_correction(self):
        """
        ガンマ補正
        :return:
        """
        process = "Gamma Correction"
        gamma_gain = self.ui.sBox_Gamma_Gain.value()
        def img_proc_func(src: np.ndarray) -> np.ndarray:
            dst = mapping.gamma_mapping(src, gamma=gamma_gain)
            return dst

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            qt_def.help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            qt_def.help_process_file_mode(self, img_proc_func, process)