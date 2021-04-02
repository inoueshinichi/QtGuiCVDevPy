"""
ダイアログプログラムのひな形
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

from image_window import ImageWindow
from module.utils import new_serial_number_filename
from module.qt_module.qt_def import *
from module.imgproc.binarize import *

# from ui.ui_template_dialog import Ui_TemplateDialog


class TemplateDialog(QDialog):

    def __init__(self, parent: QWidget = None):
        super(TemplateDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        # self.ui = Ui_TemplateDialog() # 作成するダイアログの装飾クラスをここに書く.
        # Qt Designerで設計して, pyside2-uic.exeでコンパイルしたもの.
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose) # Closeされたときに自動でメモリ削除

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
        pass

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    """
    Slot用関数は以下に任意で作成する
    """
