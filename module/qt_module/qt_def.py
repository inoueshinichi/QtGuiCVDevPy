"""QtGUI関連の定義
"""
# 標準
import os
import sys
import time
import datetime
import pathlib
import shutil
from typing import (
    Dict,
    List,
    Tuple,
    Union,
    Any,
    Callable,
    NewType,
    TypeVar
)

# サードパーティ
import numpy as np
import qimage2ndarray as qn
import PIL
from PIL import Image
from matplotlib import pyplot as plt
from concurrent.futures import (ThreadPoolExecutor, as_completed)
from PySide2 import (QtGui, QtCore)
from PySide2.QtCore import (Signal, Slot, Qt)
from PySide2.QtGui import QImage
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QDialog, QMessageBox)


# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

accept_text = ['txt', 'csv', 'xlsx', 'xlsm', 'pdf', 'xml', 'html', 'htm', 'json']
accept_movie = ['mov', 'mp4', 'mpg', 'mpeg', 'avi', 'vob', 'ogm', 'rm']
accept_wave = ['mp3', 'wma', 'wav', 'm4a', 'ogg', 'cda']
accept_imgs = ['bmp', 'jpeg', 'jpg', 'png']
accept_filter = "画像(*.bmp *.jpg *.jpeg *.png)"


def qimage2ndarray(qimage:QImage) -> np.ndarray:
    """
    QImageからndarrayに変換
    :param qimage:
    :return:
    """
    # view_arrayがlocalスコープしか有効でないので
    # コンバート結果(元のコピー)は，元のメモリ領域に格納しないけないのかも.
    # 2020.07.01 Inoue Shinichi
    is_grayscale = qimage.allGray() #isGrayscale()
    depth = qimage.bitPlaneCount()
    qimage = qimage.convertToFormat(QImage.Format_ARGB32)
    view_array = qn.recarray_view(qimage)
    if is_grayscale and depth == 8:
        img = np.copy(view_array['g'])
    else:
        img = np.dstack((view_array['r'], view_array['g'], view_array['b']))
    return img

def ndarray2qimage(array:np.ndarray) -> QImage:
    """
    ndarrayからQImageに変換
    :param array:
    :return:
    """
    assert array.ndim == 2 or array.ndim == 3, "ndim of array must be 2 or 3."
    qimage = qn.array2qimage(array)
    if array.ndim == 2:
        qimage = qimage.convertToFormat(QImage.Format_Grayscale8)
    else:
        qimage = qimage.convertToFormat(QImage.Format_RGB888)
    return qimage


def create_mask_qimage(mask_array:np.ndarray, mask_transparent_ratio:float=0.5) -> QImage:
    """
    numpy ndarrayからマスク用QImageの生成
    :param mask_array:
    :return:
    """
    assert mask_array.ndim == 2, "mask must be 2dims."
    height, width = mask_array.shape
    mask_color = np.zeros((height, width, 4), dtype=np.uint8)
    mask_array[mask_array > 0] = 255
    mask_color[:, :, 3] = ((255 - mask_array) * (1.0 - mask_transparent_ratio)).astype(np.uint8)
    mask_color[:, :, (0, 1, 2)] = (244, 0, 25)  # 唐紅
    mask_qimage = qn.array2qimage(mask_color)
    return mask_qimage


def retrieve_mask_ndarray(mask_qimage:QImage) -> np.ndarray:
    """
    マスク用QImageからnumpy ndarrayを生成
    :param mask_qimage:
    :return:
    """
    assert mask_qimage.format() == QImage.Format_ARGB32, "Format of mask_qimage must be Format_ARGB32."
    mask_array = qn.recarray_view(mask_qimage)
    mask_array = mask_array['a'] # alpha channel
    mask_array[mask_array > 0] = 255
    return mask_array


def format_qimage(qimage:QImage) -> (QImage.Format, str):
    """
    QImageのフォーマットを取得
    :param qImage:
    :return:
    """
    if qimage is None:
        return None
    qFmt = qimage.format()

    if qFmt == QImage.Format_Invalid:
        return (qFmt, "Format_Invalid")
    elif qFmt == QImage.Format_Mono:
        return (qFmt, "Format_Mono")  # 1bit per pixel
    elif qFmt == QImage.Format_MonoLSB:
        return (qFmt, "Format_MonoLSB")  # 1bit per pixel
    elif qFmt == QImage.Format_Indexed8:
        return (qFmt, "Format_Indexed8")  # 8bit
    elif qFmt == QImage.Format_RGB32:
        return (qFmt, "Format_RGB32")  # 0xffRRGGBB
    elif qFmt == QImage.Format_ARGB32:
        return (qFmt, "Format_ARGB32")  # 0xAARRGGBB
    elif qFmt == QImage.Format_ARGB32_Premultiplied:
        return (qFmt, "Format_ARGB32_Premultiplied")  # 0xAARRGGBB
    elif qFmt == QImage.Format_RGB16:
        return (qFmt, "Format_RGB16")
    elif qFmt == QImage.Format_ARGB8565_Premultiplied:
        return (qFmt, "Format_ARGB8565_Premultiplied")
    elif qFmt == QImage.Format_RGB666:
        return (qFmt, "Format_RGB666")
    elif qFmt == QImage.Format_ARGB6666_Premultiplied:
        return (qFmt, "Format_ARGB6666_Premultiplied")
    elif qFmt == QImage.Format_RGB555:
        return (qFmt, "Format_RGB555")
    elif qFmt == QImage.Format_ARGB8555_Premultiplied:
        return (qFmt, "Format_ARGB8555_Premultiplied")
    elif qFmt == QImage.Format_RGB888:
        return (qFmt, "Format_RGB888")
    elif qFmt == QImage.Format_RGB444:
        return (qFmt, "Format_RGB444")
    elif qFmt == QImage.Format_ARGB4444_Premultiplied:
        return (qFmt, "Format_ARGB4444_Premultiplied")
    elif qFmt == QImage.Format_RGBX8888:
        return (qFmt, "Format_RGBX8888")
    elif qFmt == QImage.Format_RGBA8888:
        return (qFmt, "Format_RGBA8888")
    elif qFmt == QImage.Format_RGBA8888_Premultiplied:
        return (qFmt, "Format_RGBA8888_Premultiplied")
    elif qFmt == QImage.Format_BGR30:
        return (qFmt, "Format_BGR30")
    elif qFmt == QImage.Format_A2BGR30_Premultiplied:
        return (qFmt, "Format_A2BGR30_Premultiplied")
    elif qFmt == QImage.Format_RGB30:
        return (qFmt, "Format_RGB30")
    elif qFmt == QImage.Format_A2RGB30_Premultiplied:
        return (qFmt, "Format_A2RGB30_Premultiplied")
    elif qFmt == QImage.Format_Alpha8:
        return (qFmt, "Format_Alpha8")
    elif qFmt == QImage.Format_Grayscale8:
        return (qFmt, "Format_Grayscale8")
    elif qFmt == QImage.Format_Grayscale16:
        return (qFmt, "Format_Grayscale16")
    elif qFmt == QImage.Format_RGBX64:
        return (qFmt, "Format_RGBX64")
    elif qFmt == QImage.Format_RGBA64:
        return (qFmt, "Format_RGBA64")
    elif qFmt == QImage.Format_RGBA64_Premultiplied:
        return (qFmt, "Format_RGBA64_Premultiplied")
    elif qFmt == QImage.Format_BGR888:
        return (qFmt, "Format_BGR888")
    elif qFmt == QImage.NImageFormats:
        return (qFmt, "NImageFormats")
    else:
        return (None, None)

def status_qimage(qimage:QImage) -> Dict[str, Any]:
    """
    QImageのステータスを表示
    :param qimage:
    :return:
    """
    if not qimage.isNull():
        # Status
        stat_dict = {}
        stat_dict['cacheKey'] = qimage.cacheKey()
        stat_dict['bitPlaneCount'] = qimage.bitPlaneCount()
        stat_dict['depth'] = qimage.depth()
        stat_dict['colorTable'] = qimage.colorTable()
        stat_dict['hasAlphaChannel'] = qimage.hasAlphaChannel()
        stat_dict['width'] = qimage.width()
        stat_dict['height'] = qimage.height()
        stat_dict['dataSize'] = qimage.sizeInBytes()
        stat_dict['textKeys'] = qimage.textKeys()
        stat_dict['logicalDpiX'] = qimage.logicalDpiX()
        stat_dict['logicalDpiY'] = qimage.logicalDpiY()
        stat_dict['physicalDpiX'] = qimage.physicalDpiX()
        stat_dict['physicalDpiY'] = qimage.physicalDpiY()
        stat_dict['devicePixelRatio'] = qimage.devicePixelRatio()

        qformat = format_qimage(qimage)
        stat_dict['format'] = qformat[-1]

        newEntryStatus = "New Entry Image Status\n\
                     CacheKey:{0:d}\n\
                     DataSize:{1:d}(bytes)\n\
                     Height:{2:d}\n\
                     Width:{3:d}\n\
                     BitPlaneCount:{4:d}\n\
                     Depth:{5:d}\n\
                     AlphaChannel: {6:d}\n\
                     DevicePixelRatio:{7:f}\n\
                     LogicalDpiX:{8:d}\n\
                     LogicalDpiY:{9:d}\n\
                     PysicalDpiX:{10:d}\n\
                     PysicalDpiY:{11:d}\n\
                     ColorTable:{12}\n\
                     TextKeys:{13}\n\
                     Format:{14}".format(
            stat_dict['cacheKey'],
            stat_dict['dataSize'],
            stat_dict['height'],
            stat_dict['width'],
            stat_dict['bitPlaneCount'],
            stat_dict['depth'],
            stat_dict['hasAlphaChannel'],
            stat_dict['devicePixelRatio'],
            stat_dict['logicalDpiX'],
            stat_dict['logicalDpiY'],
            stat_dict['physicalDpiX'],
            stat_dict['physicalDpiY'],
            stat_dict['colorTable'],
            stat_dict['textKeys'],
            stat_dict['format'])

        return stat_dict

def adjust_viewport(qimage:QImage, view:"CDrawView", widget:QWidget):
    """
    入力画像にビューポートのサイズを合わせる
    :param qimage:
    :param view:
    :return:
    """
    # 画像サイズに合わせてウィンドウサイズを変更
    [qimg_width, qimg_height] = [qimage.width(), qimage.height()]
    widget_rect = widget.geometry()
    x = widget_rect.x()
    y = widget_rect.y()
    if qimg_width < 1000 and qimg_height < 1000:
        v_scrl_width = view.verticalScrollBar().width()
        h_scrl_height = view.horizontalScrollBar().height()
        status_bar_height = widget.ui.statusbar.height()
        widget.setGeometry(x,
                           y,
                           qimg_width + 2 * v_scrl_width,
                           qimg_height + 2 * h_scrl_height + status_bar_height + 30)
    else:
        widget.setGeometry(x, y, qimg_width // 2, qimg_height // 2)


def help_process_view_mode(widget:QWidget, img_proc_func:Callable[[Any], Any], text:str):
    """
    Viewモード用のラッパー関数
    :return:
    """
    last_active_img_win = widget.main_win.last_active_img_win
    # ImageWindowをimportできないので，isinstance()条件を外した. 2020/07/15 Inoue Shinichi.
    if (last_active_img_win is not None):# and (isinstance(last_active_img_win, ImageWindow)):
        qimage = last_active_img_win.scene.dib_qimage()
        if not qimage.isNull():
            img = qimage2ndarray(qimage)
            rect_list = last_active_img_win.scene.roi_rects()
            start = time.perf_counter()

            if len(rect_list) > 0:
                for key, rect in rect_list:
                    rect = rect.toRect()
                    xmin = rect.x()
                    ymin = rect.y()
                    xmax = xmin + rect.width()
                    ymax = ymin + rect.height()
                    img[ymin:ymax, xmin:xmax], _ = img_proc_func(img[ymin:ymax, xmin:xmax])
            else:
                img, _ = img_proc_func(img)

            elapsed_time = (time.perf_counter() - start) * 1000
            qimage = ndarray2qimage(img)
            last_active_img_win.scene.set_qimage_on_screen(qimage)
            last_active_img_win.scene.update()

            widget.main_win.ui.statusBar.clearMessage()
            widget.main_win.ui.statusBar.showMessage("{0} response: {1:.3f} [ms]".format(text, elapsed_time))
        else:
            QMessageBox.warning(widget, text, "QImageがNullです.", QMessageBox.Ok)
    else:
        QMessageBox.warning(widget, "ImageWindow", "直近のアクテイブなImageWindowがNoneです.", QMessageBox.Ok)


def help_process_view_mode_2(widget:QWidget, img_proc_func:Callable[[Any], Any], text:str) \
        -> Tuple[Union[np.ndarray, None], Union[Dict[str, Any], None]]:
    """
    Viewモード用のラッパー関数2
    img_proc_func()の出力が画像以外の場合に使用する
    :param widget:
    :param img_proc_func:
    :param text:
    :return:
    """
    last_active_img_win = widget.main_win.last_active_img_win
    # ImageWindowをimportできないので，isinstance()条件を外した. 2020/07/15 Inoue Shinichi.
    if (last_active_img_win is not None):# and (isinstance(last_active_img_win, ImageWindow)):
        qimage = last_active_img_win.scene.dib_qimage()
        if not qimage.isNull():
            img = qimage2ndarray(qimage)
            rect_list = last_active_img_win.scene.roi_rects()
            start = time.perf_counter()

            result_dict = {}
            if rect_list:
                for i, (key, rect) in enumerate(rect_list):
                    rect = rect.toRect()
                    xmin = rect.x()
                    ymin = rect.y()
                    xmax = xmin + rect.width()
                    ymax = ymin + rect.height()
                    output = img_proc_func(img[ymin:ymax, xmin:xmax])
                    result_dict[str(i)] = (output, (xmin, ymin))
            else:
                output = img_proc_func(img)
                result_dict['0'] = (output, (0, 0))

            elapsed_time = (time.perf_counter() - start) * 1000
            # qimage = ndarray2qimage(img)
            # last_active_img_win.scene.set_qimage_on_screen(qimage)
            # last_active_img_win.scene.update()

            widget.main_win.ui.statusBar.clearMessage()
            widget.main_win.ui.statusBar.showMessage("{0} response: {1:.3f} [ms]".format(text, elapsed_time))
            return img, result_dict

        else:
            QMessageBox.warning(widget, text, "QImageがNullです.", QMessageBox.Ok)
    else:
        QMessageBox.warning(widget, "ImageWindow", "直近のアクテイブなImageWindowがNoneです.", QMessageBox.Ok)

    return None, None


def help_process_file_mode(widget: QWidget, img_proc_func: Callable[[Any], Any], text: str, csv_filename: str = ""):
    """
    Fileモード用のラッパー関数
    :return:
    """
    dir_input = widget.main_win.ui.lEdit_Input_Dir.text()
    dir_output = widget.main_win.ui.lEdit_Output_Dir.text()
    if os.path.isdir(dir_input):
        res = QMessageBox.information(widget,
                                      "{0} for images on input directory.".format(text),
                                      "画像ファイルに対する処理を開始してもよろしいですか？",
                                      QMessageBox.Yes | QMessageBox.No)
        if res == QMessageBox.Yes:
            start = time.perf_counter()

            # マルチスレッドプール(Executorオブジェクトを作成)
            with ThreadPoolExecutor(max_workers=None) as executor:

                def _load_save_func(img_proc_func: Callable[[np.ndarray], np.ndarray],
                                    path: str,
                                    dir_output: str,
                                    csv_filename: str):

                    qimage_load = QImage(path)
                    src = qimage2ndarray(qimage_load)
                    dst, params_list = img_proc_func(src) # 処理後の画像(np.ndarray), 処理結果パラメータ[param1, param2, ...]
                    qimage_save = ndarray2qimage(dst)
                    dir_output_obj = pathlib.Path(dir_output)
                    filename_obj = pathlib.Path(path.split(os.sep)[-1])
                    output_path_obj = dir_output_obj / filename_obj # 連結
                    qimage_save.save(str(output_path_obj))

                    # 処理結果パラメータをcsvファイルに追加
                    if csv_filename:
                        record = [str(output_path_obj)] + [str(value) for value in params_list]
                        csv_path = os.sep.join([dir_output, csv_filename])
                        with open(csv_path, mode="a", encoding='utf-8') as f:
                            f.write(",".join(record))
                            f.write("\n") # 改行
                # end: _load_save_func

                # csvファイルを作成
                if csv_filename:
                    csv_path = os.sep.join([dir_output, csv_filename])
                    # 新規作成(既存csvファイルは消える)
                    with open(csv_path, mode='w', encoding='utf-8') as f:
                        f.close()

                future_list = []
                for ext in accept_imgs:
                    file_paths = [str(path) for path in pathlib.Path(dir_input).glob("*." + ext)
                                  if not str(path).split(os.sep)[-1].startswith('.')]

                    for path in file_paths:
                        # Executorオブジェクトにタスクをsubmitし、同数だけfutureオブジェクトを得る.
                        # タスクの実行は、submit()を呼び出した瞬間から開始される.
                        future = executor.submit(fn=_load_save_func,
                                                 img_proc_func=img_proc_func,
                                                 path=path,
                                                 dir_output=dir_output,
                                                 csv_filename=csv_filename)
                        future_list.append(future)

                    # 各futureの完了を待ち、結果を取得。
                    # as_completed()は、与えられたfuturesの要素を完了順にたどるイテレータを返す。
                    # 完了したタスクが無い場合は、ひとつ完了するまでブロックされる。
                    _ = as_completed(fs=future_list)

            elapsed_time = time.perf_counter() - start
            widget.main_win.ui.statusBar.clearMessage()
            widget.main_win.ui.statusBar.showMessage("{0} response: {1:.3f} [ms]".format(text, elapsed_time))
        else:
            pass
    else:
        QMessageBox.warning(widget,
                            "Warning for input directory.",
                            "{0} は存在しません".format(dir_input),
                            QMessageBox.Ok)
