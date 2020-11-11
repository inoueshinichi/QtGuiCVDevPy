"""画像表示用のウィンドウ
"""

# 標準
import os
import sys
import time
import datetime
from typing import (Dict, List, Tuple, Union, Any, NewType)

# サードパーティ
import numpy as np
import qimage2ndarray as qn
from matplotlib import pyplot as plt
import PySide2
from PySide2 import (QtGui, QtCore)
from PySide2.QtCore import (Signal, Slot, Qt, QEvent)
from PySide2.QtGui import QImage
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QDialog, QMessageBox, QLabel)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_ImageWindow import Ui_ImageWindow
from draw_scene import DrawScene

# 画像表示用のウィンドウ
class ImageWindow(QMainWindow):

    @staticmethod
    def overrides(klass):
        def check_super(method) -> Any:
            method_name = method.__name__
            msg = f"`{method_name}()` is not defined in `{klass.__name__}`."
            assert method_name in dir(klass), msg

        def wrapper(method) -> Any:
            check_super(method)
            return method

        return wrapper


    def __init__(self, parent:QWidget=None):
        # PythonによるQtオブジェクトのガーベッジコレクションの対象になるのは，
        # 自身のオブジェクトが削除され，更に親オブジェクトを設定している場合，
        # 親オブジェクトの破棄も行われてた場合に限る。Pythonの参照オブジェクトを
        # 破棄しても，内部でオブジェクトが保持されているため，Python上で
        # QObject系列のオブジェクトの生成と破棄を繰り返すと，莫大なメモリを消費してしまう。
        # self.setAttribute(Qt.WA_DeleteOnClose)を設定すると，QWidget系は
        # closeEvent()実行後に自動でメモリ破棄される。しかし，Python参照オブジェクトは
        # 破棄されておらず，Python参照オブジェクトから内部的に空になったメモリオブジェクトを
        # 参照できてしまう。この対策を思案中. 2020/07/10
        super(ImageWindow, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_ImageWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.permanent_status = QLabel(self)
        self.permanent_status.setText("SceneRect (0, 0, 0, 0)")
        self.ui.statusbar.addPermanentWidget(self.permanent_status)

        self.filename = ""

        # View & Scene
        self.scene = DrawScene(self)
        self.ui.gView.setScene(self.scene)

    # virtual
    def set_filename(self, filename:str):
        """
        格納している画像ファイルの名前を与えて，ウィンドウ名を更新
        :param filename:
        :return:
        """
        self.filename = filename
        dt_now = datetime.datetime.now()
        self.setWindowTitle(dt_now.strftime("%Y-%m-%d %H:%M") + " " + filename)

    # virtual
    def get_filename(self):
        """
        格納している画像ファイル名を取得
        :return:
        """
        return self.filename

    # override
    def event(self, event:PySide2.QtCore.QEvent) -> bool:
        """
        イベント処理の基底
        :param event:
        :return:
        """

        if event.type() == QEvent.WindowActivate:
            self.main_win.last_active_img_win = self
            self.main_win.is_last_active = True

            # メニュー->Image->Type 画像のビット深度を更新
            if not self.scene.dib_qimage().isNull():
                depth = self.scene.dib_qimage().bitPlaneCount()
                self.main_win.ui.action8_bit.setChecked(False)
                self.main_win.ui.action24_bit.setChecked(False)
                self.main_win.ui.actionRGB_Color.setChecked(False)

                if depth == 8:
                    self.main_win.ui.action8_bit.setChecked(True)
                elif depth == 16:
                    self.main_win.ui.action16_bit.setChecked(True)
                elif depth == 24:
                    if self.scene.source_dib_qimage.allGray():
                        self.main_win.ui.action24_bit.setChecked(True)
                    else:
                        self.main_win.ui.actionRGB_Color.setChecked(True)
                else:
                    fmt = self.scene.format()
                    QMessageBox.warning(self,
                                        "Image Type",
                                        "Unknow Type. depth:{0}, format:{1}".format(depth, fmt[-1]),
                                        QMessageBox.Ok)

                # Toolbar->Cross LineのOn/Off状態を取得
                checked = self.main_win.ui.actionCross_Line.isChecked()
                self.toggle_scene_cross_line(checked)

                # Toolbar->ProfileのOn/Off状態を取得
                checked = self.main_win.ui.actionProfile.isChecked()
                self.toggle_scene_profile(checked)

                # Toolbar->ROIのOn/Off状態を取得
                checked = self.main_win.ui.actionROI.isChecked()
                self.toggle_scene_roi(checked)

                # Toolbar->LineのOn/Off状態を取得
                checked = self.main_win.ui.actionLine.isChecked()
                self.toggle_scene_line(checked)

                # Toolbar->EllipseのOn/Off状態を取得
                checked = self.main_win.ui.actionEllipse.isChecked()
                self.toggle_scene_ellipse(checked)

                # Toolbar->MaskのOn/Off状態を取得
                checked = self.main_win.ui.actionMask.isChecked()
                self.toggle_scene_mask(checked)

        return super(ImageWindow, self).event(event)

    # override
    def closeEvent(self, event:PySide2.QtGui.QCloseEvent):
        """
        ウィンドウのクローズイベント
        :param event:
        :return:
        """

        self.main_win.img_wins.remove(self)
        # if len(self.main_win.img_wins) == 0:
        #     self.main_win.last_active_img_win = None
        #     print("closeEvent")

        self.main_win.last_active_img_win = None
        self.main_win.is_last_active = False
        print("CImageWindow closeEvent")
        super(ImageWindow, self).closeEvent(event)

    def toggle_scene_cross_line(self, show:bool):
        """
        マウスのクロスラインの表示切り替え
        :param show:
        :return:
        """
        self.scene.toggle_cross_line(show)

    def toggle_scene_profile(self, show:bool):
        """
        プロファイルの表示切り替え
        :param show:
        :return:
        """
        self.scene.toggle_profile(show)

    def toggle_scene_roi(self, show:bool):
        """
        ROIの表示切り替え
        :param show:
        :return:
        """
        if show:
            self.ui.gView.setDragMode(self.ui.gView.RubberBandDrag)
        else:
            self.ui.gView.setDragMode(self.ui.gView.NoDrag)
        self.scene.toggle_roi(show)

    def toggle_scene_line(self, show:bool):
        """
        Lineの表示切り替え
        :param show:
        :return:
        """
        if show:
            self.ui.gView.setDragMode(self.ui.gView.RubberBandDrag)
        else:
            self.ui.gView.setDragMode(self.ui.gView.NoDrag)
        self.scene.toggle_line(show)

    def toggle_scene_ellipse(self, show:bool):
        """
        楕円の表示切り替え
        :param show:
        :return:
        """
        if show:
            self.ui.gView.setDragMode(self.ui.gView.RubberBandDrag)
        else:
            self.ui.gView.setDragMode(self.ui.gView.NoDrag)
        self.scene.toggle_ellipse(show)

    def toggle_scene_mask(self, show:bool):
        """
        マスクの表示切り替え
        :param show:
        :return:
        """
        if self.scene.toggle_mask(show):
            pass
        else:
            self.ui.statusbar.clearMessage()
            self.ui.statusbar.showMessage("No Mask QImage.")

