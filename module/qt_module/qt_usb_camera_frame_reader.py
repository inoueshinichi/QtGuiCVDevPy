"""USBカメラ専用のカメラフレーム読み取りスレッド
"""

# 標準
import time
from collections import deque # スレッドセーフなデキュー
from typing import (List, Dict, Tuple, Union, Callable, Any, NoReturn)

# サードパーティ
import numpy as np
import cv2
from PySide2.QtCore import (Signal, Slot, QObject, QThread, QMutexLocker, QCoreApplication)

# 自作


class QtUSBCameraFrameReader(QObject):
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

    def __init__(self, device_id:Union[int, None]=None, delay:Union[int, None]=None, deque_size:int=1):
        super(QtUSBCameraFrameReader, self).__init__()
        self.width:Union[int, None] = None
        self.height:Union[int, None] = None
        self.channels:Union[int, None] = None
        self.is_initialized:Union[bool, None] = None
        self.is_running:bool = False
        self.is_network:bool = True if isinstance(device_id, str) else False
        self.frame_pool:deque = deque(maxlen=deque_size)
        self.device_id:Union[int, str, None] = device_id
        self.delay:Union[int, None] = delay
        self.capture:Any = None

    def set_device_id(self, device_id:Union[int, str]) -> NoReturn:
        self.is_network = True if isinstance(device_id, str) else False
        self.device_id = device_id

    def get_device_id(self) -> Union[int, str, None]:
        return self.device_id

    def set_delay(self, delay:int) -> NoReturn:
        self.delay = delay

    def get_delay(self) -> Union[int, None]:
        return self.delay

    def _check_stream(self, device_id:Union[int, str]) -> bool:
        cap = cv2.VideoCapture(device_id)
        if not cap.isOpened():
            return False
        cap.release()
        return True

    def initialize(self) -> bool:
        self.is_initialized = False

        if self.device_id is None:
            print("device_id is None. Please set valid device_id.")
            return False

        if self.delay is None:
            print("delay is None. Please set valid delay.")
            return False

        print("##### Enter initialize section of device_id:{0} camera. #####".format(self.device_id))
        if self._check_stream(self.device_id):
            self.capture = cv2.VideoCapture(self.device_id)
            status, frame = self.capture.read()
            if status:
                if frame.ndim == 2:
                    self.height, self.width = frame.shape
                    self.channels = 1
                else:
                    self.height, self.width, self.channels = frame.shape
                # 成功
                print("Success to initialize camera device.")
                print("Retrieved frame: H:{0} W:{1} C:{2}.".format(self.height, self.width, self.channels))
                self.is_initialized = True
            else:
                print("Failed to attempt to read frame first.")
        else:
            print("Invalid device_id. Please check hardware or connection config.")
        print("##### Exit initialize section of device_id:{0} camera. #####".format(self.device_id))
        return self.is_initialized

    def release(self) -> NoReturn:
        print("##### Enter release section of device_id:{0} camera. #####".format(self.device_id))
        if self.capture is not None:
            self.capture.release()
            print("Success to release.")
        print("##### Exit release section of device_id:{0} camera. #####".format(self.device_id))

    def _spin(self, delay:int=0):
        # QThread(サブスレッド)のイベントキューに溜まったシグナルを処理する
        QCoreApplication.processEvents()
        if delay != 0:
            # ビジーループを実行
            until = time.perf_counter() + delay / 1000.0
            while time.perf_counter() < until:
                QCoreApplication.processEvents()

    @Slot()
    def start(self) -> NoReturn:
        # QThreadのexec_()イベントループからディスパッチされる
        print(">>> Enter capture loop.")

        self.is_running = True
        elapsed_time_deq = deque(maxlen=100)

        # サブスレッドのイベントループであるexec_()処理シーケンスの中でstart()->while文が呼ばれるため、
        # このwhile文でループに突入して移行、workerThread(QThread)のイベントループexec_()が使えなくなるので、
        # QCoreApplication.processEvent()でイベントキューに溜まったイベント(signal)を処理する
        while self.is_running:
            print(">>> Current thread", QThread.currentThread())
            # print(">>> Priority is", QThread.currentThread().priority())
            start = time.perf_counter()
            try:
                status, frame = self.capture.read()
                if status:
                    if frame.ndim == 3:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # RGB
                    print(">>> Get new frame.")
                else:
                    print(">>> Miss new frame!")

                self._spin(self.delay) # workerThread(QThread)のイベントキューに溜まったイベント(signal)を処理する

                # 1周期の所要時間を計算
                end = time.perf_counter()
                elapsed_time = (end - start) * 1000 # [ms]
                print(">>> Elapsed Time: {0:f} [ms]".format(elapsed_time))

                # フレームレートの計算
                elapsed_time_deq.append(elapsed_time)
                avg_elapsed_time = sum(elapsed_time_deq) / len(elapsed_time_deq)
                fps = 1000.0 / avg_elapsed_time
                print(">>> fps", fps)

                # スレッドセーフなデキューにプッシュ
                self.frame_pool.append((frame, fps, elapsed_time))

            except AttributeError:
                pass

        self.capture.release()
        print(">>> Exit capture loop.")

    @Slot()
    def stop(self) -> NoReturn:
        self.is_running = False # スレッドを使っているのでメモリは元々共有しているが，Qtの枠組みに沿ってSignal/Slotで制御
        return

    def retrieve_frame(self) -> Tuple[Union[np.ndarray, None], float, float]:
        if len(self.frame_pool) > 0:
            frame, fps, elapsed_time = self.frame_pool[-1]
            return frame, fps, elapsed_time
        else:
            return None, 0.0, 0.0

