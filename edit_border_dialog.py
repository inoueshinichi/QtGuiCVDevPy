"""画像縁を編集するダイアログ
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

from ui.ui_EditBorderDialog import Ui_EditBorderDialog
from image_window import ImageWindow
from module.utils import new_serial_number_filename
from module.qt_module.qt_def import *
from module.imgproc.border import *


class EditBorderDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(EditBorderDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_EditBorderDialog()
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
        # Make Boarder
        self.ui.pBtn_Make_Border_Apply.clicked.connect(self._apply_make_border)

        # Erase Boarder
        self.ui.pBtn_Erase_Border_Apply.clicked.connect(self._apply_erase_border)

        # Clear Prams
        self.ui.pBtn_Make_Border_Clear_Location.clicked.connect(self._apply_clear_make_location)
        self.ui.pBtn_Make_Border_Clear_Color.clicked.connect(self._apply_clear_make_color)
        self.ui.pBtn_Erase_Border_Clear_Location.clicked.connect(self._apply_clear_erase_location)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_make_border(self):
        """
        領域の縁を作る処理
        :return:
        """
        process = "Make Boarder"

        # Boarder
        border_type = self.ui.cBox_Border_Type.currentText()
        border_type = border_type.split(' ')[0]

        # Position
        left = self.ui.sBox_Border_Left.value()
        top = self.ui.sBox_Border_Top.value()
        right = self.ui.sBox_Border_Right.value()
        bottom = self.ui.sBox_Border_Bottom.value()

        # Constant Color
        gray = self.ui.sBox_Border_Constant_Gray.value()
        red = self.ui.sBox_Border_Constant_Red.value()
        green = self.ui.sBox_Border_Constant_Green.value()
        blue = self.ui.sBox_Border_Constant_Blue.value()

        def img_proc_func(src:np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = make_border(src,
                              extended_pixels=[left, top, right, bottom],
                              constant_colors=[gray, red, green, blue],
                              border_type=border_type)
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_erase_border(self):
        """
        画像の縁を削除
        :return:
        """
        process = "Erase Border"

        left = self.ui.sBox_Erase_Border_Left.value()
        top = self.ui.sBox_Erase_Border_Top.value()
        right = self.ui.sBox_Erase_Border_Right.value()
        bottom = self.ui.sBox_Erase_Border_Bottom.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = erase_border(src, erase_pixels=[left, top, right, bottom])
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            help_process_file_mode(self, img_proc_func, process)

    @Slot()
    def _apply_clear_make_location(self):
        """
        追加するピクセル数の初期化
        :return:
        """
        self.ui.sBox_Border_Left.setValue(0)
        self.ui.sBox_Border_Top.setValue(0)
        self.ui.sBox_Border_Right.setValue(0)
        self.ui.sBox_Border_Bottom.setValue(0)

    @Slot()
    def _apply_clear_make_color(self):
        """
        指定色の初期化
        :return:
        """
        self.ui.sBox_Border_Constant_Gray.setValue(0)
        self.ui.sBox_Border_Constant_Red.setValue(0)
        self.ui.sBox_Border_Constant_Green.setValue(0)
        self.ui.sBox_Border_Constant_Blue.setValue(0)

    @Slot()
    def _apply_clear_erase_location(self):
        """
        削除するピクセル数の初期化
        :return:
        """
        self.ui.sBox_Erase_Border_Left.setValue(0)
        self.ui.sBox_Erase_Border_Top.setValue(0)
        self.ui.sBox_Erase_Border_Right.setValue(0)
        self.ui.sBox_Erase_Border_Bottom.setValue(0)


