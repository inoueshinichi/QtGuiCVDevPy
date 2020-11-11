"""threadingベースのカメラコントローラー.
各種FrameReaderを付け替えて，様々なカメラ, I/Oに対応
"""

# 標準
import os
import sys
from typing import (List, Dict, Tuple, Union, Callable, Any, NoReturn, NewType, Type)
import datetime as dt
import time
import threading
from threading import Thread

# サードパーティ
import numpy as np
import cv2

# 自作
from module.camera_frame_reader import CameraFrameReader


class CameraController:
    CameraFrameReader = NewType('CameraFrameReader', CameraFrameReader)

    def __init__(self, camera_frame_reader:CameraFrameReader):
        self.camera_frame_reader:Union[CameraFrameReader, None] = camera_frame_reader
        self.worker_thread:Union[Thread, None] = None

    def set_device_id(self, device_id:Union[int, str]) -> NoReturn:
        self.camera_frame_reader.set_device_id(device_id)

    def get_device_id(self) -> Union[int, None]:
        return self.camera_frame_reader.get_device_id()

    def set_delay(self, delay:int) -> NoReturn:
        self.camera_frame_reader.set_delay(delay)

    def get_delay(self) -> Union[int, None]:
        return self.camera_frame_reader.get_delay()

    def initialize(self) -> bool:
        return self.camera_frame_reader.initialize()

    def release(self):
        self.camera_frame_reader.release()

    def fetch_frame(self) -> Tuple[Union[np.ndarray, None], float, float, str]:
        frame, fps, elapsed_time = self.camera_frame_reader.retrieve_frame()
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return frame, fps, elapsed_time, timestamp

    def start_worker(self) -> NoReturn:
        print("##### Enter start_worker() #####")

        if self.camera_frame_reader.is_initialized is None:
            print("No initialization of camera device. Please initialize it.")
            print("##### Exit start() #####")
            return

        if not self.camera_frame_reader.is_initialized:
            print("Failed to initialize camera device. Check device_id or hardware.")
            print("##### Exit start() #####")
            return

        if self.worker_thread is not None:
            print("Worker-thread is running. Please stop_worker().")
            return

        # daemonスレッド: 残っているスレッドがデーモンスレッドだけになった時に Python プログラム全体を終了させる
        self.worker_thread = Thread(target=self.camera_frame_reader.capture_loop,
                                    args=(),
                                    name="Thread for camera device id={0}.".format(self.camera_frame_reader.get_device_id()),
                                    daemon=True)

        self.worker_thread.start()
        print("Worker-thread start.")
        print("Running of worker-thread is", self.worker_thread.is_alive())
        print("##### Exit start_worker() #####")

    def stop_worker(self) -> NoReturn:
        print("##### Enter stop_worker() #####")
        if self.worker_thread is None:
            print("Don't call start_worker().")
            return

        if self.worker_thread.is_alive():
            self.camera_frame_reader.stop()
            self.worker_thread.join() # worker_thread終了までメインスレッドを待機させる
            self.worker_thread = None
        else:
            print("Worker-thread is dead.")
        print("##### Exit stop_worker() #####")

    def check_worker_running(self) -> bool:
        if self.worker_thread is None:
            return False
        else:
            return self.worker_thread.is_alive()







