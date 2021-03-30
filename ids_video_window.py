"""IDSカメラのフレームを制御及び表示するウィンドウ
"""

# 標準
import os
import sys
import time
import datetime
from typing import (
    Dict,
    List,
    Tuple,
    Union,
    Callable,
    Any,
    NewType,
    List
)

# サードパーティ
import numpy as np
import qimage2ndarray as qn
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
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFileDialog,
    QDialog,
    QMessageBox,
    QLabel
)
from PySide2.QtMultimedia import QCameraInfo

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_IDSVideoWindow import Ui_IDSVideoWindow
from image_window import ImageWindow
from module.qt_module.qt_def import *
from module.utils import new_serial_number_filename

from module.camera_frame_reader import IDSCameraFrameReader
from module.camera_controller_threading import CameraController
from module.pickle_video_capture import PickleIDSVideoCapture
from module.camera_controller_processing import ProcessCameraController


# IDSカメラのフレーム画像(動画)表示用ウィンドウ
class IDSVideoWindow(ImageWindow):

    def __init__(self, parent:QWidget=None):
        super(IDSVideoWindow, self).__init__(parent)

        # UI
        self.ui:Any = Ui_IDSVideoWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.permanent_status = QLabel(self)
        self.permanent_status.setText("SceneRect (0, 0, 0, 0)")
        self.ui.statusbar.addPermanentWidget(self.permanent_status)

        # Camera Reader/Controller
        self.camera_reader:Union[IDSCameraFrameReader, None] = None
        self.video_capture:Any = None
        self.camera_controller:Union[CameraController, None] = None

        # Timer
        self.draw_timer:QTimer = QTimer(self)

        # View
        self.ui.gView.setScene(self.scene)

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
        self.ui.toolBar.toggleViewAction().setEnabled(False) # 右クリックでツールバーを非表示にできないようにする

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
        # Start/Stop
        self.ui.pBtn_Start.clicked.connect(self._start_capture)
        self.ui.pBtn_Stop.clicked.connect(self._stop_capture)

        # Device Search
        self.ui.pBtn_Search_Device_List.clicked.connect(self._search_device_list)

        # Snapshot
        self.ui.pBtn_Snapshot.clicked.connect(self._snapshot)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @ImageWindow.overrides(ImageWindow)
    def set_filename(self, filename: str):
        """
        格納している画像ファイルの名前を与えて，ウィンドウ名を更新
        :param filename:
        :return:
        """
        self.ui.dockWidget.setWindowTitle("Inspector@" + filename)  # dockWidgetのタイトル
        self.filename = filename + ".bmp"
        self.setWindowTitle(self.filename)

    @ImageWindow.overrides(ImageWindow)
    def closeEvent(self, event: PySide2.QtGui.QCloseEvent):
        self._stop_capture()  # カメラキャプチャの停止
        super(IDSVideoWindow, self).closeEvent(event)

    @Slot()
    def _timer_handler(self):
        """
        タイマーハンドラ
        :return:
        """
        if self.camera_controller.check_worker_running() & self.draw_timer.isActive():
            frame, fps, elapsed_time, timestamp = self.camera_controller.fetch_frame()
            if frame is not None:
                qimage = ndarray2qimage(frame)
                self.scene.set_qimage_on_screen(qimage)

                # FPS
                if self.ui.cBox_FPS.isChecked():
                    fps_text = "FPS: {0:>7.3f}".format(fps)
                    self.scene.add_item_text(text=fps_text, key="fps", pos=QPointF(0, 0))
                else:
                    self.scene.remove_item_text("fps")

                # Elapsed Time
                if self.ui.cBox_Elapsed_Time.isChecked():
                    elapsed_time_text = "Elapsed time [ms]: {0:>7.3f}".format(elapsed_time)
                    self.scene.add_item_text(text=elapsed_time_text, key="elapsed_time", pos=QPointF(0, 20))
                else:
                    self.scene.remove_item_text("elapsed_time")

                # TimeStamp
                if self.ui.cBox_Timestamp.isChecked():
                    timestamp_text = "TimeStamp: {0}".format(timestamp)
                    self.scene.add_item_text(text=timestamp_text, key="timestamp", pos=QPointF(0, 40))
                else:
                    self.scene.remove_item_text("timestamp")

                self.scene.update()

    @Slot()
    def _start_capture(self):
        """
        カメラキャプチャ開始
        :return:
        """
        device_id = int(self.ui.lEdit_Device_ID.text())
        delay = int(self.ui.sBox_Read_Frame_Delay.value())

        if self.ui.rBtn_Thread.isChecked():
            self.camera_reader = IDSCameraFrameReader()
            self.camera_controller = CameraController(self.camera_reader)
            self.camera_controller.set_device_id(device_id)
            self.camera_controller.set_delay(delay)
        else:
            self.video_capture = PickleIDSVideoCapture()
            self.video_capture.set_device_id(device_id)
            self.video_capture.set_delay(delay)
            self.camera_controller = ProcessCameraController(self.video_capture)

        # フレームキャプチャのスレッドを開始する
        if self.camera_controller.initialize():
            if self.ui.rBtn_Thread.isChecked():
                self.camera_controller.start_worker()
                print("Start camera capture thread.")
            else:
                self.camera_controller.start_process()
                print("Start camera capture process.")

            while not self.camera_controller.check_worker_running():
                pass

            # 描画タイマーの設定
            interval = int(self.ui.sBox_Paint_Timer_Interval.value())
            self.draw_timer.timeout.connect(self._timer_handler)
            self.draw_timer.start(interval)
            timer_id = self.draw_timer.timerId()
            self.ui.lEdit_Timer_ID.setText(str(timer_id))
            timer_type = str(self.draw_timer.timerType()).split('.')[-1]
            self.ui.lEdit_Timer_Type.setText(str(timer_type))
            print("Start draw timer.")

            self.repaint()
        else:
            QMessageBox.warning(self, "Capture Initialization", "キャプチャデバイスの初期化に失敗しました.", QMessageBox.Ok)

    @Slot()
    def _stop_capture(self):
        """
        カメラキャプチャ停止
        :return:
        """
        if self.camera_controller is not None:
            if self.camera_controller.check_worker_running():
                if self.ui.rBtn_Thread.isChecked():
                    # スレッドの停止
                    self.camera_controller.stop_worker()
                    print("Stop camera capture thread.")
                else:
                    # プロセスの停止
                    self.camera_controller.stop_process()
                    print("Stop camera capture process.")

        if self.draw_timer.isActive():
            # 描画タイマーの停止
            self.draw_timer.stop()
            self.draw_timer.timeout.disconnect()
            print("Stop draw timer.")

    @Slot()
    def _search_device_list(self):
        """
        利用可能なデバイスIDの一覧を取得
        :return:
        """
        devices = QCameraInfo.availableCameras()
        print("##### Devices #####")
        for dev in devices:
            print("{0}. {1}.".format(dev.description(), dev.deviceName()))

    @Slot()
    def _snapshot(self):
        """
        ランニング中のカメラフレームから1枚抽出する
        :return:
        """
        if not self.draw_timer.isActive():
            QMessageBox.warning(self, "Snapshot", "キャプチャ状態ではありません.", QMessageBox.Ok)
            return

        # QImageをコピー
        qimage_snapshot = self.scene.dib_qimage().copy()
        stored_filenames = [img_win.filename for img_win in self.main_win.img_wins]
        name, ext = self.filename.split(".")
        filename = name + "_snapshot" + "." + ext
        new_filename = new_serial_number_filename(filename, stored_filenames)

        new_img_win = ImageWindow(self.main_win)
        new_img_win.set_filename(new_filename)
        self.main_win.img_wins.append(new_img_win)
        new_img_win.show()
        new_img_win.activateWindow()

        # 画像をSceneに登録
        new_img_win.scene.clear()
        new_img_win.scene.set_qimage_on_screen(qimage_snapshot, is_raw=True)
        new_img_win.scene.update()

        # 画像サイズに合わせてウィンドウサイズを変更
        adjust_viewport(qimage_snapshot, new_img_win.ui.gView, new_img_win)

