# """シェーディング補正用のダイアログ
# """
#
# # 標準
# import os
# import shutil
# import sys
# import pathlib
# import math
# import time
# from typing import (
#     List,
#     Dict,
#     Tuple,
#     Union,
#     Callable,
#     Any,
#     TypeVar,
#     Generic,
#     NoReturn
# )
#
#
# # サードパーティ
# import numpy as np
# import scipy as sp
# import cv2
# from PIL import Image
# import skimage
# from matplotlib import pyplot as plt
# import PySide2
# from PySide2 import (QtGui, QtCore)
# from PySide2.QtCore import (Signal, Slot, Qt, QEvent, QTimer, QPointF)
# from PySide2.QtGui import QImage
# from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QFileDialog, QDialog, QMessageBox, QLabel)
#
# # 自作
# cwd = os.getcwd()
# ui_dir = "/".join([cwd, "ui"])
# sys.path.append(ui_dir)
# module_dir = "/".join([cwd, "module"])
# sys.path.append(module_dir)
#
# from ui.ui_ShadingDialog import Ui_ShadingDialog
# from module.qt_module import qt_def
# from module.imgproc import shading
# from module.imgproc import blur
#
# class ShadingDialog(QDialog):
#
#     def __init__(self, parent:QWidget=None):
#         super(ShadingDialog, self).__init__(parent)
#
#         # 親
#         self.main_win = parent
#
#         # UI
#         self.ui = Ui_ShadingDialog()
#         self.ui.setupUi(self)
#         self.setAttribute(Qt.WA_DeleteOnClose)  # Closeされたときに自動でメモリ削除
#
#         # Signal/Slot
#         self._toolbar_connection()
#         self._menubar_connection()
#         self._ui_connection()
#         self._custom_connection()
#
#     def _toolbar_connection(self):
#         """
#         ToolBarに関するSignal/Slotの接続
#         :return:
#         """
#         pass
#
#     def _menubar_connection(self):
#         """
#         MenuBarに関するSignal/Slotの接続
#         :return:
#         """
#         pass
#
#     def _ui_connection(self):
#         """
#         UIに関するSignal/Slotの接続
#         :return:
#         """
#         # Check Gaussian Blur for Base Image
#         self.ui.pBtn_Shading_Gaussian_Check.clicked.connect(self._check_baseimg)
#
#         # Check Median Blur for Base Image
#         self.ui.pBtn_Shading_Meidan_Check.clicked.connect(self._check_baseimg)
#
#         # Apply Shading Correction
#         self.ui.pBtn_Shading_Correction_Apply.clicked.connect(self._apply_shading_correction)
#
#     def _custom_connection(self):
#         """
#         ユーザー定義のカスタムSignal/Slotの接続
#         :return:
#         """
#         pass
#
#
#     # @Slot()
#     def _check_baseimg(self):
#         """
#         BaseImageの確認
#         :return:
#         """
#         sender = self.sender()
#         process = "Gaussian Blur" if sender == self.ui.pBtn_Shading_Gaussian_Check else "Median Blur"
#
#         processing_func = None
#         if process == "Gaussian Blur":
#             k_x = self.ui.sBox_Shading_Gaussian_k_x.value()
#             k_y = self.ui.sBox_Shading_Gaussian_k_y.value()
#             std_x = self.ui.dsBox_Shading_Gaussian_std_x.value()
#             std_y = self.ui.dsBox_Shading_Gaussian_std_y.value()
#             def img_proc_func(src:np.ndarray) -> np.ndarray:
#                 dst = blur.gaussian_blur(src, (k_x, k_y), (std_x, std_y))
#                 return dst
#             processing_func = img_proc_func
#
#         else: # Median Blur
#             k_xy = self.ui.sBox_Shadng_Median_k_xy.value()
#             def img_proc_func(src:np.ndarray) -> np.ndarray:
#                 dst = blur.median_blur(src, k_xy)
#                 return dst
#             processing_func = img_proc_func
#
#
#         img_win = self.main_win.last_active_img_win
#         if img_win:
#             qimage = img_win.scene.dib_qimage()
#             if not qimage.isNull():
#                 img_copy = qt_def.qimage2ndarray(qimage).copy() # copyed ndarray image
#                 rect_list = img_win.scene.roi_rects()
#                 elapsed_time_list = []
#
#                 if len(rect_list) > 0:
#                     for key, rect in rect_list:
#                         start = time.perf_counter()
#                         rect = rect.toRect()
#                         xmin = rect.x()
#                         ymin = rect.y()
#                         xmax = xmin + rect.width()
#                         ymax = ymin + rect.height()
#                         img_roi = img_copy[ymin:ymax, xmin:xmax]
#                         img_dst = processing_func(img_roi)
#                         elapsed_time = (time.perf_counter() - start) * 1000
#                         elapsed_time_list.append(elapsed_time)
#                         img_pil = Image.fromarray(img_dst)
#                         img_pil.show()
#                 else:
#                     start = time.perf_counter()
#                     elapsed_time = (time.perf_counter() - start) * 1000
#                     img_dst = processing_func(img_copy)
#                     elapsed_time_list.append(elapsed_time)
#                     img_pil = Image.fromarray(img_dst)
#                     img_pil.show()
#
#                 avg_elapsed_time = np.array(elapsed_time_list, dtype=np.float32).mean(axis=0)
#                 self.main_win.ui.statusBar.clearMessage()
#                 self.main_win.ui.statusBar.showMessage("{0} response: {1:.3f} [ms]".format(process, avg_elapsed_time))
#             else:
#                 QMessageBox.warning(self, process, "QImageがNullです.", QMessageBox.Ok)
#         else:
#             QMessageBox.warning(self, "ImageWindow", "直近のアクテイブなImageWindowがNoneです.", QMessageBox.Ok)
#
#
#     @Slot()
#     def _apply_shading_correction(self):
#         """
#         シェーディング補正
#         :return:
#         """
#         process = "Shading Correction"
#         process_type = "Gaussian Blur" if self.ui.rBtn_Shading_Gaussian_Blur.isChecked() else "Median Blur"
#         process = process + " with " + process_type
#
#         processing_func = None
#         if process_type == "Gaussian Blur":
#             k_x = self.ui.sBox_Shading_Gaussian_k_x.value()
#             k_y = self.ui.sBox_Shading_Gaussian_k_y.value()
#             std_x = self.ui.dsBox_Shading_Gaussian_std_x.value()
#             std_y = self.ui.dsBox_Shading_Gaussian_std_y.value()
#
#             def img_proc_func(src: np.ndarray) -> np.ndarray:
#                 dst = blur.gaussian_blur(src, (k_x, k_y), (std_x, std_y))
#                 return dst
#
#             processing_func = img_proc_func
#
#         else:  # Median Blur
#             k_xy = self.ui.sBox_Shadng_Median_k_xy.value()
#
#             def img_proc_func(src: np.ndarray) -> np.ndarray:
#                 dst = blur.median_blur(src, k_xy)
#                 return dst
#
#             processing_func = img_proc_func
#
#         # Shading Correction
#         gain = self.ui.dsBox_Shading_Gain.value()
#         def img_proc_func(src:np.ndarray) -> np.ndarray:
#             base = processing_func(src.copy())
#             master = src
#             dst = shading.shading_correction(master, base, gain)
#             return dst
#
#         if self.main_win.ui.rBtn_View_Mode.isChecked():
#             """View Mode"""
#             qt_def.help_process_view_mode(self, img_proc_func, process)
#         else:
#             """File Mode"""
#             qt_def.help_process_file_mode(self, img_proc_func, process)
#
