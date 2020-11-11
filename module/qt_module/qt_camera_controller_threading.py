"""QThreadベースのカメラコントローラー. 各種FrameReaderを付け替えて，様々なカメラ，I/Oに対応
"""

# 標準
import os
import sys
from typing import (List, Dict, Tuple, Union, Callable, Any, NoReturn, NewType, Type)
import datetime as dt
import time

# サードパーティ
import numpy as np
import cv2
from PySide2.QtCore import (Qt, Signal, Slot, QObject, QThread)

# 自作
from module.qt_module.qt_usb_camera_frame_reader import QtUSBCameraFrameReader


class QtCameraController(QObject):
    worker_start = Signal()
    worker_finish = Signal()
    QtUSBCameraFrameReader = NewType("QtUSBCameraFrameReader", QtUSBCameraFrameReader)

    def __init__(self, camera_frame_reader:QtUSBCameraFrameReader):
        super(QtCameraController, self).__init__()
        self.camera_frame_reader = camera_frame_reader
        self.worker_thread = QThread(self)

    def set_device_id(self, device_id:Union[int, str]) -> NoReturn:
        self.camera_frame_reader.set_device_id(device_id)

    def set_delay(self, delay:int) -> NoReturn:
        self.camera_frame_reader.set_delay(delay)

    def initialize(self) -> bool:
        return self.camera_frame_reader.initialize()

    def release(self):
        self.camera_frame_reader.release()

    def fetch_frame(self) -> Tuple[Union[np.ndarray, None], float, float, str]:
        frame, fps, elapsed_time = self.camera_frame_reader.retrieve_frame()
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return frame, fps, elapsed_time, timestamp

    def start_worker(self) -> NoReturn:
        if not self.camera_frame_reader.is_initialized:
            print("No initialization of worker thread.")
            return

        # self.camera_frame_readerをワーカースレッドに渡す
        self.camera_frame_reader.moveToThread(self.worker_thread)

        # Signal/Slot
        self.worker_start.connect(self.camera_frame_reader.start, Qt.QueuedConnection)
        self.worker_finish.connect(self.camera_frame_reader.stop, Qt.BlockingQueuedConnection)
        """[Connectionの種類]
        Qt.AutoConnection            受信側が同じスレッド上にいる場合はDirectoConnection, それ以外の場合は, QueuedConnection。
        Qt.DirectConnection          スロットの直接呼出し。シグナルを発呼したスレッドから対象のスロットを呼び出す。
        Qt.QueuedConnection　　　　　　シグナルは受信側のスレッドのキューに入れられて、受信側スレッドのイベントループによりスロットが呼び出される。
                                     シグナル発呼側は、レシーバー側のキューに入れて即時処理を再開します（スロットの実行を待たない）※非同期処理
        Qt.BlockingQueuedConnection  シグナルは受信側のスレッドのキューに入れられて、受信側スレッドのイベントループによりスロットが呼び出されます。
                                     シグナル発呼側は、受信側のスロット実行終了を待ち合わせます。※同期処理

        このシグナルとスロットの機能のため、QObjectとそのサブクラスは、いずれかのスレッドのイベントループに登録されます。
        このとき、親子関係を持つQObjectは、必ず同一のスレッドに登録される必要があります。
        つまり、移したいQObjectはその親ごとmoveToThreadしなくてはならない事に注意が必要です。
        """
        # ワーカースレッドの起動
        self.worker_thread.start()
        self.worker_start.emit()

    def stop_worker(self) -> NoReturn:
        self.camera_frame_reader.stop()
        self.worker_finish.emit()
        self.worker_start.disconnect()
        self.worker_finish.disconnect()
        self.worker_thread.quit()
        self.worker_thread.wait()

    def check_worker_running(self) -> bool:
        return self.worker_thread.isRunning()

    def worker_stack_size(self) -> int:
        return self.worker_thread.stackSize()

    def terminate_worker(self) -> NoReturn:
        self.worker_thread.terminate()




