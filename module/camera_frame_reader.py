"""各種カメラ専用のフレーム読み取りスレッドの基底クラス
"""

# 標準
import time
from collections import deque # スレッドセーフなデキュー
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
import abc

import cv2
# サードパーティ
import numpy as np
from pyueye import ueye # IDS
import stapipy as st

# 自作


# カメラフレーム読み取りの基底クラス
class CameraFrameReader(metaclass=abc.ABCMeta):

    # 派生クラスにインターフェース(関数API)を強制させるために必要なおまじない.
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

    def __init__(self,
                 device_id: Union[int, None] = None,
                 delay: Union[int, None] = None,
                 deque_size: int = 1):

        self.width: Union[int, None] = None
        self.height: Union[int, None] = None
        self.channels: Union[int, None] = None
        self.is_initialized: Union[bool, None] = None
        self.is_running: bool = False
        self.frame_pool: deque = deque(maxlen=deque_size)
        self.device_id: Union[int, str, None] = device_id
        self.delay: Union[int, None] = delay

    def set_device_id(self, device_id: Union[int, str]) -> NoReturn:
        self.device_id = device_id

    def get_device_id(self) -> Union[int, str, None]:
        return self.device_id

    def set_delay(self, delay:int) -> NoReturn:
        self.delay = delay

    def get_delay(self) -> Union[int, None]:
        return self.delay

    @abc.abstractmethod
    def _check_stream(self, device_id: Union[int, str]) -> bool:
        return False

    @abc.abstractmethod
    def initialize(self) -> bool:
        return False

    @abc.abstractmethod
    def release(self) -> NoReturn:
        return

    @abc.abstractmethod
    def _capture(self) -> Tuple[bool, Union[np.ndarray, None]]:
        return (False, None)

    def _spin(self, delay:int=0):
        if delay != 0:
            # ビジーループを実行
            until = time.perf_counter() + delay / 1000.0
            while time.perf_counter() < until:
                pass

    def capture_loop(self) -> NoReturn:
        print(">>> Enter capture loop.")

        self.is_running = True
        elapsed_time_deq = deque(maxlen=100)

        while self.is_running:
            # print(">>> Current thread", threading.current_thread()) # デバッグ用
            start = time.perf_counter()
            try:
                status, frame = self._capture()
                if status:
                    if frame.ndim == 3:
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # RGB
                    # print(">>> Get new frame.") # デバッグ用
                else:
                    print(">>> Miss new frame!")

                self._spin(self.delay) # delay

                # 1周期の所要時間を計算
                end = time.perf_counter()
                elapsed_time = (end - start) * 1000  # [ms]
                # print(">>> Elapsed Time: {0:f} [ms]".format(elapsed_time)) # デバッグ用

                # フレームレートの計算
                elapsed_time_deq.append(elapsed_time)
                avg_elapsed_time = sum(elapsed_time_deq) / len(elapsed_time_deq)
                fps = 1000.0 / avg_elapsed_time
                # print(">>> fps", fps) # デバッグ用

                # スレッドセーフなデキューにプッシュ
                self.frame_pool.append((frame, fps, elapsed_time))

            except AttributeError:
                pass

        self.release()
        print(">>> Exit capture loop.")

    def stop(self) -> NoReturn:
        self.is_running = False
        return

    def retrieve_frame(self) -> Tuple[Union[np.ndarray, None], float, float]:
        if len(self.frame_pool) > 0:
            frame, fps, elapsed_time = self.frame_pool[-1]
            return frame, fps, elapsed_time
        else:
            return (None, 0.0, 0.0)


# USBカメラ専用フレーム読み取りクラス
class USBCameraFrameReader(CameraFrameReader):

    def __init__(self,
                 device_id: Union[int, None] = None,
                 delay: Union[int, None] = None,
                 deque_size: int = 1):

        super(USBCameraFrameReader, self).__init__(device_id, delay, deque_size)

        # USB(opencv VideoCapture)
        self.capture: Any = None

    @CameraFrameReader.overrides(CameraFrameReader)
    def _check_stream(self, device_id: Union[int, str]) -> bool:
        cap = cv2.VideoCapture(device_id)
        if not cap.isOpened():
            return False
        cap.release()
        return True

    @CameraFrameReader.overrides(CameraFrameReader)
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
            status, frame = self._capture()
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
            print("Fail to initialize device. Please check hardware or connection config.")
        print("##### Exit initialize section of device_id:{0} camera. #####".format(self.device_id))
        return self.is_initialized

    @CameraFrameReader.overrides(CameraFrameReader)
    def release(self) -> NoReturn:
        print("##### Enter release section of device_id:{0} camera. #####".format(self.device_id))
        if self.capture is not None:
            self.capture.release()
            print("Success to release.")
        print("##### Exit release section of device_id:{0} camera. #####".format(self.device_id))

    @CameraFrameReader.overrides(CameraFrameReader)
    def _capture(self) -> Tuple[bool, Union[np.ndarray, None]]:
        return self.capture.read()


# IDSカメラ専用フレーム読み取りクラス
class IDSCameraFrameReader(CameraFrameReader):
    """
    スレッドによる画像取り込みを行うと，delay=0[ms]でCPU使用率100%に達してしまう...
    理由がわからない。サブプロセスによる画像取り込みはdelay=0[ms]でCPU使用率60%ぐらい。
    """

    def __init__(self,
                 device_id: Union[int, None] = None,
                 delay: Union[int, None] = None,
                 deque_size:int = 1):

        super(IDSCameraFrameReader, self).__init__(device_id, delay, deque_size)

        # IDS-UIカメラのパラメータ
        self.handler_camera: Union[int, None] = None   # 0: first available camera;  1-254: The camera with the specified camera ID
        self.sensor_info: Union[str, None] = None
        self.camera_info: Union[str, None] = None
        self.pc_image_memory: Union[int, None] = None
        self.memory_id: Union[int, None] = None
        self.rect_aoi: Any = None # ROI
        self.pitch: Union[int, None] = None
        self.nbits_per_pixel: Union[int, None] = None  # 24: bits per pixel for color mode; take 8 bits per pixel for monochrome
        self.channels: Union[int, None] = None         # 3: channels for color mode(RGB); take 1 channel for monochrome
        self.ncolor_mode: Union[str, None] = None      # Y8/RGB16/RGB24/REG32
        self.bytes_per_pixel: Union[int, None] = None

    @CameraFrameReader.overrides(CameraFrameReader)
    def _check_stream(self, device_id: Union[int, str]) -> bool:
        """
        IDSカメラデバイスの設定とチェック
        :param device_id:
        :return:
        """
        print("START IDS-initialization.")

        if device_id < 0 or device_id >= 255:
            print("ERROR Invalid device ID. Must be 0 <= device_id < 255.")
            print("END IDS-initialization.")
            return False

        # IDSカメラのパラメータ初期化
        self.camera_handler = ueye.HIDS(self.device_id)
        self.sensor_info = ueye.SENSORINFO()
        self.camera_info = ueye.CAMINFO()
        self.pc_image_memory = ueye.c_mem_p() # ポインタ?
        self.memory_id = ueye.INT()
        self.rect_aoi = ueye.IS_RECT()
        self.pitch = ueye.INT()
        self.ncolor_mode = ueye.INT()
        self.nbits_per_pixel = ueye.INT(0)
        self.bytes_per_pixel = int(self.nbits_per_pixel / 8) # 8:1byte, 24:3bytes

        # デバイスドライバ起動 & カメラへの接続を確立
        status = ueye.is_InitCamera(self.camera_handler, None)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_InitCamera().")
            print("END IDS-initialization.")
            return False

        # 排他的でないカメラハードウェアのカメラ情報を読取る
        status = ueye.is_GetCameraInfo(self.camera_handler, self.camera_info)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_GetCameraInfo().")
            print("END IDS-initialization.")
            return False

        # カメラで使用されているセンサータイプに付いて追加の情報を要求
        status = ueye.is_GetSensorInfo(self.camera_handler, self.sensor_info)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_GetSensorInfo().")
            print("END IDS-initialization.")
            return False

        # カメラハンドラをデフォルトに設定?
        status = ueye.is_ResetToDefault(self.camera_handler)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_ResetToDefault().")
            print("END IDS-initialization.")
            return False

        # ディスプレイモードをDIBに設定
        status = ueye.is_SetDisplayMode(self.camera_handler, ueye.IS_SET_DM_DIB)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_SetDisplayMode().")
            print("END IDS-initialization.")
            return False

        # カラーモードを設定
        status = ueye.is_GetColorDepth(self.camera_handler, self.nbits_per_pixel, self.ncolor_mode)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_GetColorDepth().")
            print("END IDS-initialization.")
            return False
        else:
            if int.from_bytes(self.sensor_info.nColorMode.value, byteorder='big') == ueye.IS_COLORMODE_BAYER:
                # setup the color depth to the current windows setting
                self.bytes_per_pixel = int(self.nbits_per_pixel / 8)
                self.channels = 3
                print(">>> IS_COLORMODE_BAYER:")
                print(">>> ncolor_mode:\t", self.ncolor_mode)
                print(">>> nbits_per_pixel:\t", self.nbits_per_pixel)
                print(">>> bytes_per_pixel:\t", self.bytes_per_pixel)
                print()
            elif int.from_bytes(self.sensor_info.nColorMode.value, byteorder='big') == ueye.IS_COLORMODE_CBYCRY:
                # for color camera models use RGB32 mode
                self.ncolor_mode = ueye.IS_CM_RGBA8_PACKED
                self.nbits_per_pixel = ueye.INT(32)
                self.bytes_per_pixel = int(self.nbits_per_pixel / 8)
                self.channels = 3
                print(">>> IS_COLORMODE_CBYCRY:")
                print(">>> ncolor_mode:\t", self.ncolor_mode)
                print(">>> nbits_per_pixel:\t", self.nbits_per_pixel)
                print(">>> bytes_per_pixel:\t", self.bytes_per_pixel)
                print()
            elif int.from_bytes(self.sensor_info.nColorMode.value, byteorder='big') == ueye.IS_COLORMODE_MONOCHROME:
                # for color camera models use RGB32 mode
                self.ncolor_mode = ueye.IS_CM_MONO8
                self.nbits_per_pixel = ueye.INT(8)
                self.bytes_per_pixel = int(self.nbits_per_pixel / 8)
                self.channels = 1
                print(">>> IS_COLORMODE_MONOCHROME:")
                print(">>> ncolor_mode:\t", self.ncolor_mode)
                print(">>> nbits_per_pixel:\t", self.nbits_per_pixel)
                print(">>> bytes_per_pixel:\t", self.bytes_per_pixel)
                print()
            else:
                # for monochrome camera models use Y8 mode
                self.ncolor_mode = ueye.IS_CM_MONO8
                self.nbits_per_pixel = ueye.INT(8)
                self.bytes_per_pixel = int(self.nbits_per_pixel / 8)
                self.channels = 1
                print(">>> IS_CM_MONO8:")
                print(">>> ncolor_mode:\t", self.ncolor_mode)
                print(">>> nbits_per_pixel:\t", self.nbits_per_pixel)
                print(">>> bytes_per_pixel:\t", self.bytes_per_pixel)
                print()

        # 画像内でAOI(area of intreset)のサイズと位置を設定
        status = ueye.is_AOI(self.camera_handler, ueye.IS_AOI_IMAGE_GET_AOI, self.rect_aoi, ueye.sizeof(self.rect_aoi))
        if status != ueye.IS_SUCCESS:
            print("ERROR is_AOI().")
            print("END IDS-initialization.")
            return False

        # ソフト側で受け取る画像サイズ
        width = self.rect_aoi.s32Width
        height = self.rect_aoi.s32Height
        self.width = width.value
        self.height = height.value

        # カメラとセンサーについてのいくつかの情報を出力
        print(">>> Camera model:\t", self.sensor_info.strSensorName.decode('utf-8'))
        print(">>> Camera serial no.:\t", self.camera_info.SerNo.decode('utf-8'))
        print(">>> Maximum image width:\t", width)
        print(">>> Maximum image height:\t", height)
        print(">>> Channels:\t", self.channels)
        print()

        # 画像情報(nbits_per_pixel, width, height)をもつ画像メモリを確保
        status = ueye.is_AllocImageMem(self.camera_handler, width, height,
                                       self.nbits_per_pixel, self.pc_image_memory, self.memory_id)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_AllocImageMem().")
            print("END IDS-initialization.")
            return False
        else:
            # Makes the specified image memory the active memory
            status = ueye.is_SetImageMem(self.camera_handler, self.pc_image_memory, self.memory_id)
            if status != ueye.IS_SUCCESS:
                print("ERROR is_SetImageMem().")
                print("END IDS-initialization.")
                return False
            else:
                # 望ましいカラーモードを設定
                status = ueye.is_SetColorMode(self.camera_handler, self.ncolor_mode)
                if status != ueye.IS_SUCCESS:
                    print("ERROR is_SetColorMode().")
                    print("END IDS-initialization.")
                    return False

        # カメラのライブビデオモード（フリーランモード）の有効化
        status = ueye.is_CaptureVideo(self.camera_handler, ueye.IS_DONT_WAIT)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_CaptureVideo().")
            print("END IDS-initialization.")
            return False

        # 画像メモリのシーケンスを作るためにキューモードを確立
        status = ueye.is_InquireImageMem(self.camera_handler, self.pc_image_memory, self.memory_id,
                                         width, height, self.nbits_per_pixel, self.pitch)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_InquireImageMem().")
            print("END IDS-initialization.")
            return False

        return True

    @CameraFrameReader.overrides(CameraFrameReader)
    def _capture(self) -> Tuple[bool, Union[np.ndarray, None]]:
        """
        IDSカメラのフレーム取り込み処理
        :return:
        """
        array = ueye.get_data(self.pc_image_memory,
                              self.width, self.height,
                              self.nbits_per_pixel, self.pitch, copy=False)

        if array is None:
            return (False, None)

        frame = array.reshape((self.height, self.width, self.channels))
        return True, frame

    @CameraFrameReader.overrides(CameraFrameReader)
    def initialize(self) -> bool:
        """
        IDS(UIシリーズ)カメラの初期化処理
        :return:
        """
        self.is_initialized = False

        if self.device_id is None:
            print("device_id is None. Please set valid device_id.")
            return False

        if self.delay is None:
            print("delay is None. Please set valid delay.")
            return False

        print("##### Enter initialize section of device_id:{0} camera. #####".format(self.device_id))

        if self._check_stream(self.device_id):
            status, frame = self._capture()
            if status:
                # 成功
                print("Success to initialize camera device.")
                print("Retrieved frame: H:{0} W:{1} C:{2}.".format(self.height, self.width, self.channels))
                self.is_initialized = True
            else:
                print("Failed to attempt to read frame first.")
        else:
            print("Fail to initialize device. Please check hardware or connection config.")

        print("##### Exit initialize section of device_id:{0} camera. #####".format(self.device_id))
        return self.is_initialized

    @CameraFrameReader.overrides(CameraFrameReader)
    def release(self) -> NoReturn:
        """
        IDS(UIシリーズ)のカメラドライバの終了処理
        :return:
        """
        print("##### Enter release section of IDS-Camera device ID={0}. #####".format(self.device_id))

        # is_AllocImageMem()で確保した画像メモリを解放し、ドライバーマネジメントから画像メモリを取り除く
        status = ueye.is_FreeImageMem(self.camera_handler, self.pc_image_memory, self.memory_id)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_FreeImageMem().")
            return

        # カメラハンドルを無効にし、uEye cameraによって確保されていたデータ構造とメモリ領域を解放
        status = ueye.is_ExitCamera(self.camera_handler)
        if status != ueye.IS_SUCCESS:
            print("ERROR is_ExitCamera().")
            return

        print("Success to release.")
        print("##### Exit release section of IDS-Camera device ID={0}. #####".format(self.device_id))



# OMRON-Sentechカメラ専用フレーム読み取りクラス
class OMRONCameraFrameReader(CameraFrameReader):

    def __init__(self,
                 device_id: Union[int, None] = None,
                 delay: Union[int, None] = None,
                 deque_size: int = 1):

        super(OMRONCameraFrameReader, self).__init__(device_id, delay, deque_size)

        """OMRON-Sentechカメラのパラメータ"""
        # Transport Layer
        # System
        self.st_system: Union[st.PyStSystem, None] = None
        self.st_system_info: Union[st.PyStSystemInfo, None] = None
        # Interface
        self.st_interface: Union[st.PyStInterface, None] = None
        self.st_interface_info: Union[st.PyStInterfaceInfo, None] = None
        # Device
        self.st_device: Union[st.PyStDevice, None] = None
        self.st_device_info: Union[st.PyStDeviceInfo, None] = None
        # DataStream
        self.st_data_stream: Union[st.PyStDataStream, None] = None
        self.st_data_stream_info: Union[st.PyDataStreamInfo, None] = None
        # DataStreamBuffer
        self.st_data_stream_buffer: Union[st.PyDataStreamBuffer, None] = None
        self.st_data_stream_buffer_info: Union[st.PyDataStreamBufferInfo, None] = None

        # Port
        self.st_port: Union[st.PyStPort, None] = None
        self.st_port_info: Union[st.PyStPortInfo, None] = None
        self.st_port_url_info: Union[st.PyStPortURLInfo, None] = None





