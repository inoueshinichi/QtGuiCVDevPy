"""プロセスベースのカメラコントローラー.
デバイスI/Oの種類毎に異なるキャプチャークラスが必要.
"""

# 標準
import os
import sys
import ctypes
import time
import datetime as dt
import platform
from collections import deque
from multiprocessing import (
    Process,
    Pipe,
    Value,
    Array,
    freeze_support
)
from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Callable,
    Any,
    NoReturn,
    NewType,
    Type
)

# サードパーティ
import numpy as np
import cv2

# 自作


class ProcessCameraController:

    def __init__(self, pickle_video_capture: Any = None):

        # マルチプロセス用の共有メモリ
        self.sm_is_running: Union[Value, None] = None
        self.sm_frame: Union[Array, None] = None
        self.sm_fps: Union[Value, None] = None
        self.sm_elapsed_time: Union[Value, None] = None

        # インスタンス変数
        self.is_initialized: Union[bool, None] = None
        self.process: Union[Process, None] = None
        self.receive_frame: Union[np.ndarray, None] = None

        # キャプチャデバイス
        self.cap = pickle_video_capture

    def start_process(self):
        print("##### Enter start() #####")

        if self.is_initialized is None:
            print("No initialization of camera device. Please initialize it.")
            print("##### Exit start() #####")
            return

        if not self.is_initialized:
            print("Failed to initialize camera device. Check device_id or hardware.")
            print("##### Exit start() #####")
            return

        if self.process is not None:
            print("Process is running. Please stop_process().")
            return

        self.sm_is_running = Value(ctypes.c_bool, False)
        self.sm_frame = Array(ctypes.c_uint8, self.cap.height * self.cap.width * self.cap.channels)
        self.sm_fps = Value(ctypes.c_float, 0.0)
        self.sm_elapsed_time = Value(ctypes.c_float, 0.0)
        self.receive_frame = np.ctypeslib.as_array(self.sm_frame.get_obj())

        if platform.system() == "Windows":
            freeze_support() # 作成する子プロセスがpythonモジュールのimportを完了させることを保証する?(for Windows)

        self.process = Process(target=self._capture_loop_in_process,
                               args=(self.cap, self.sm_is_running, self.sm_frame, self.sm_fps, self.sm_elapsed_time),
                               name="Process for camera device id={0}.".format(self.cap.get_device_id),
                               daemon=True) # daemonプロセスは明示的にjoin()が必要.

        self.process.start()
        print("Sub-process start.")
        print("Running of sub-process is", self.process.is_alive())
        print("##### Exit start() #####")

    def stop_process(self):
        print("##### Enter stop() #####")
        if self.process is None:
            print("Don't call start().")
            return

        if self.process.is_alive():
            self.sm_is_running.value = False
            while self.process.is_alive():
                pass
            self.process = None
        else:
            print("Sub-process is dead.")
        print("##### Exit stop() #####")

    def _capture_loop_in_process(self,
                                 cap: Any,
                                 is_running: Value,
                                 frame: Array,
                                 fps: Value,
                                 elapsed_time: Value):
        print(">>> Enter _capture_loop().")

        # 共有メモリの定義
        interface_frame = np.ctypeslib.as_array(frame.get_obj())

        is_running.value = True

        # 所要時間のデキュー
        time_series_deq = deque(maxlen=100)

        while is_running.value:
            start = time.perf_counter()
            # print(">>> Parent process", os.getppid()) # デバッグ用
            # print(">>> Current process", os.getpid()) # デバッグ用

            status, native_frame = cap.capture()
            # print("Capture status", status) # デバッグ用
            if status:
                with frame.get_lock():
                    if (native_frame.ndim == 3) and (native_frame.shape[-1] == 3):
                        native_frame = cv2.cvtColor(native_frame, cv2.COLOR_BGR2RGB)
                    interface_frame[:] = native_frame.ravel() # 参照を返すので早い. flattenはコピーを返すので, リアルタイム処理に向かない

                cap.spin() # 指定時間だけビジーループ
            else:
                print(">>> Miss new frame!")

            end = time.perf_counter()
            elapsed_time.value = (end - start) * 1000.0
            # print(">>> Elapsed time: {0:f} [ms].".format( elapsed_time.value)) # デバッグ用

            # fpsの計算
            time_series_deq.append(elapsed_time.value)
            avg_elapsed_time = sum(time_series_deq) / len(time_series_deq)
            _fps = 1000.0 / avg_elapsed_time
            fps.value = _fps
            # print(">>> FPS {0:f} [Hz].".format(_fps)) # デバッグ用

        cap.release()
        time.sleep(0.5)
        print(">>> Exit _capture_loop().")

    def fetch_frame(self) -> Tuple[Union[np.ndarray, None], float, float, str]:
        if self.cap.channels == 1:
            frame = self.receive_frame.reshape(self.cap.height, self.cap.width)
        else:
            frame = self.receive_frame.reshape(self.cap.height, self.cap.width, self.cap.channels)

        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return frame, self.sm_fps.value, self.sm_elapsed_time.value, timestamp

    def initialize(self) -> bool:
        print("##### Enter _initialize() #####")
        status = False

        if self.cap is None:
            print("Capture device is None.")
        else:
            if self.cap.generate_device():
                print("Get first frame!")
                print("Captured image size H:{0:d} W:{1:d} C:{2:d}.".format(
                    self.cap.height, self.cap.width, self.cap.channels))
                self.is_initialized = True
                status = True
                print("Success initialization of camera device!")
            else:
                self.is_initialized = False
                print("Failed to initialize camera device id={0:d}".format(self.cap.device_id()))

        print("##### Exit _initialize() #####")
        return status

    def check_worker_running(self) -> bool:
        if self.process is None:
            return False
        else:
            return self.process.is_alive()

