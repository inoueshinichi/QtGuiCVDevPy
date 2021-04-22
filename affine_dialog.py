"""
画像回転用ダイアログ
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
from module.qt_module import qt_def
from module.imgproc.geometry import affine2d
from ui.ui_AffineDialog import Ui_AffineDialog


class AffineDialog(QDialog):

    def __init__(self, parent: QWidget = None, cx: int = 0, cy: int = 0):
        super(AffineDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_AffineDialog() # 作成するダイアログの装飾クラスをここに書く.
        # Qt Designerで設計して, pyside2-uic.exeでコンパイルしたもの.
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose) # Closeされたときに自動でメモリ削除

        # 回転中心
        self.ui.sBox_cx.setValue(cx)
        self.ui.sBox_cy.setValue(cy)

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
        # Affine
        self.ui.pBtn_Affine_Apply.clicked.connect(self._apply_affine)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    """
    Slot用関数は以下に任意で作成する
    """
    @Slot()
    def _apply_affine(self):
        """
        アフィン変換
        :return:
        """
        process = "Affine2d"
        angle = self.ui.dsBox_Angle.value()
        cx = self.ui.sBox_cx.value()
        cy = self.ui.sBox_cy.value()
        sx = self.ui.dsBox_sx.value()
        sy = self.ui.dsBox_sy.value()
        tx = self.ui.sBox_tx.value()
        ty = self.ui.sBox_ty.value()

        def img_proc_func(src: np.ndarray) -> Union[np.ndarray, List[Any]]:
            dst = affine2d(src, angle, tran=(tx, ty), scale=(sx, sy), center=(cx, cy))
            return dst, list()

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""
            qt_def.help_process_view_mode(self, img_proc_func, process)
        else:
            """File Mode"""
            qt_def.help_process_file_mode(self, img_proc_func, process)