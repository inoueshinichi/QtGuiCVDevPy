"""
ProcessedCameraControllerへのインターフェースとなる
Pickle化可能なI/Oキャプチャクラス
"""

# 標準
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, NoReturn, TypeVar, Generic)
import abc
import functools
import inspect

# サードパーティ
import numpy as np
import cv2
from pyueye import ueye

# 自作


class PickleVideoCapture(metaclass=abc.ABCMeta):

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

    def __init__(self, device_id:Union[int, None]=None, delay:Union[int, None]=None):
        self.device_id:Union[int, None] = device_id
        self.delay:Union[int, None] = delay
        self.height: Union[int, None] = None
        self.width: Union[int, None] = None
        self.channels: Union[int, None] = None

    def __getstate__(self) -> Tuple[int, int]:
        """
        親プロセス側でPickle化されるオブジェクトを指定する
        :return:
        """
        # 一つのデバイスオブジェクトを親プロセスと子プロセスで共有できないため
        # 子プロセスにPickleかしたPickleUSBVideoCaptureを引き渡すときに，親プロセス側でrelease()する.
        self.release()
        return self.device_id, self.delay

    def __setstate__(self, state) -> NoReturn:
        """
        子プロセス側でPickleデータからメモリオブジェクトに解凍
        :param state: Pickleデータ
        :return:
        """
        # Pickle化されたdevice_idとdelayをオブジェクトに戻す
        self.device_id, self.delay = state

        # デバイスの生成
        self.generate_device()

    @abc.abstractmethod
    def generate_device(self) -> bool:
        return False

    @abc.abstractmethod
    def release(self) -> NoReturn:
        return

    @abc.abstractmethod
    def capture(self) -> Tuple[bool, Union[np.ndarray, None]]:
        return (False, None)

    def spin(self) -> NoReturn:
        if self.delay != 0:
            # ビジーループを実行
            until = time.perf_counter() + self.delay / 1000.0
            while time.perf_counter() < until:
                pass

    def get_device_id(self) -> Union[int, None]:
        return self.device_id

    def get_delay(self) -> Union[int, None]:
        return self.delay

    def set_device_id(self, device_id:int) -> NoReturn:
        self.device_id = device_id

    def set_delay(self, delay:int) -> NoReturn:
        self.delay = delay


# USBカメラ専用のキャプチャデバイスクラス
class PickleUSBVideoCapture(PickleVideoCapture):

    def __init__(self, device_id:Union[int, None]=None, delay:Union[int, None]=None):
        super(PickleUSBVideoCapture, self).__init__(device_id, delay)

        # デバイス(OpencvのVideoCaputure)
        self.cap:Union[cv2.VideoCapture, None] = None

        if (device_id is not None) and (delay is not None):
            self.generate_device()

    @PickleVideoCapture.overrides(PickleVideoCapture)
    def release(self):
        self.cap.release()

    @PickleVideoCapture.overrides(PickleVideoCapture)
    def capture(self) -> Tuple[bool, Union[np.ndarray, None]]:
        status, frame = self.cap.read()
        return status, frame

    @PickleVideoCapture.overrides(PickleVideoCapture)
    def generate_device(self) -> bool:
        # デバイスの生成
        self.cap = cv2.VideoCapture(self.device_id)
        # 次のフレームがあるか否かをチェック
        assert self.cap.grab()

        if self.cap.isOpened():
            status, first_frame = self.capture()
            if status:
                if first_frame.ndim == 2:
                    first_frame = first_frame[:, :, np.newaxis]
                self.height, self.width, self.channels = first_frame.shape
                return True
        else:
            return False



# IDSカメラ専用のキャプチャデバイスクラス
class PickleIDSVideoCapture(PickleVideoCapture):

    def __init__(self, device_id:Union[int, None]=None, delay:Union[int, None]=None, ):
        super(PickleIDSVideoCapture, self).__init__(device_id, delay)

        # IDS-UIカメラのパラメータ
        self.handler_camera: Union[int, None] = None  # 0: first available camera;  1-254: The camera with the specified camera ID
        self.sensor_info: Union[str, None] = None
        self.camera_info: Union[str, None] = None
        self.pc_image_memory: Union[int, None] = None
        self.memory_id: Union[int, None] = None
        self.rect_aoi:Any = None  # ROI
        self.pitch: Union[int, None] = None
        self.nbits_per_pixel: Union[int, None] = None  # 24: bits per pixel for color mode; take 8 bits per pixel for monochrome
        self.channels: Union[int, None] = None  # 3: channels for color mode(RGB); take 1 channel for monochrome
        self.ncolor_mode: Union[str, None] = None  # Y8/RGB16/RGB24/REG32
        self.bytes_per_pixel: Union[int, None] = None

        if (device_id is not None) and (delay is not None):
            self.generate_device()

    @PickleVideoCapture.overrides(PickleVideoCapture)
    def release(self):
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


    @PickleVideoCapture.overrides(PickleVideoCapture)
    def capture(self) -> Tuple[bool, Union[np.ndarray, None]]:
        """
        IDSカメラのフレーム取り込み処理
        :return:
        """
        array = ueye.get_data(self.pc_image_memory, self.width, self.height,
                              self.nbits_per_pixel, self.pitch, copy=False)
        if array is None:
            return (False, None)

        if self.channels == 1:
            frame = array.reshape((self.height, self.width))
        else:
            frame = array.reshape((self.height, self.width, self.channels))

        return (True, frame)


    @PickleVideoCapture.overrides(PickleVideoCapture)
    def generate_device(self) -> bool:
        """
        IDSカメラデバイスの設定とチェック
        :param device_id:
        :return:
        """
        print("START IDS-initialization.")

        if self.device_id < 0 or self.device_id >= 255:
            print("ERROR Invalid device ID. Must be 0 <= device_id < 255.")
            print("END IDS-initialization.")
            return False

        # IDSカメラのパラメータ初期化
        self.camera_handler = ueye.HIDS(self.device_id)
        self.sensor_info = ueye.SENSORINFO()
        self.camera_info = ueye.CAMINFO()
        self.pc_image_memory = ueye.c_mem_p()  # ポインタ?
        self.memory_id = ueye.INT()
        self.rect_aoi = ueye.IS_RECT()
        self.pitch = ueye.INT()
        self.ncolor_mode = ueye.INT()
        self.nbits_per_pixel = ueye.INT(0)
        self.bytes_per_pixel = int(self.nbits_per_pixel / 8)  # 8:1byte, 24:3bytes

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




