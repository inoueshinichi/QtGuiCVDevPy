"""ラベリング用のダイアログ
"""

# 標準
import os
import shutil
import sys
import pathlib
import math
import time
from typing import (List, Dict, Tuple, Union, Callable, Any, NewType)

# サードパーティ
import numpy as np
import scipy as sp
import cv2
from PIL import Image
import skimage
from matplotlib import pyplot as plt
import PySide2
from PySide2 import (QtGui, QtCore)
from PySide2.QtCore import (Signal, Slot, Qt, QEvent, QTimer, QPointF)
from PySide2.QtGui import QImage
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFileDialog,
    QDialog,
    QMessageBox,
    QLabel,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_LabelingDialog import Ui_LabelingDialog
from image_window import ImageWindow
from module.utils import (new_serial_number_filename)
from module.imgproc.figure import *
from module.qt_module.qt_def import *
from module.imgproc.analyze_structure import *


class LabelingDialog(QDialog):

    def __init__(self, parent:QWidget=None):
        super(LabelingDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_LabelingDialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # Closeされたときに自動でメモリ削除

        # tableWidget_Labeling
        self.ui.tableWidget_Labeling.setColumnCount(9)
        header_labels = ['Label', 'Center(cx,cy)', 'LeftTop(x,y)', 'Size(w,h)',
                         'Area(pixel)', 'Angle[deg]', 'Aspect Ratio', 'Perimeter', 'Circularity']
        self.ui.tableWidget_Labeling.setHorizontalHeaderLabels(header_labels)
        self.ui.tableWidget_Labeling.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableWidget_Labeling.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_Labeling.setEditTriggers(QTableWidget.NoEditTriggers)

        # 主軸角度を持つ直線の２点
        self.principal_axes_lines = {}

        # ラベリングしたImageWindow
        self.target_image_window = None

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
        pass

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
        # ラベリング
        self.ui.pBtn_Labeling_Apply.clicked.connect(self._apply_labeling)

        # 主軸角度を持つ直線を描画
        self.ui.pBtn_Principal_Axes_Line_Apply.clicked.connect(self._apply_draw_principal_axes_lines)

        # バウンディングボックスの描画
        self.ui.pBtn_BBox_Apply.clicked.connect(self._apply_draw_bounding_box)

        # Clear
        self.ui.pBtn_Clear_Apply.clicked.connect(self._apply_clear_table_view)

        # Save
        self.ui.pBtn_Save_Features.clicked.connect(self._apply_save_features)

    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _apply_labeling(self):
        """
        ラベリング
        :return:
        """
        process = "Labeling"

        if self.main_win.ui.rBtn_View_Mode.isChecked():
            """View Mode"""

            # Grayscaleチェック
            last_active_img_win = self.main_win.last_active_img_win
            if (last_active_img_win is not None):
                qimage = last_active_img_win.scene.dib_qimage()
                if not qimage.isNull():
                    img = qimage2ndarray(qimage)
                    if img.ndim != 2:
                        QMessageBox.warning(self, "入力画像", "入力画像はGrayscaleでなければなりません.", QMessageBox.Ok)
                        return

            def img_proc_func(src: np.ndarray) -> Tuple[int, np.ndarray, List[NamedTuple]]:
                label_count, label_images, features = labeling(src)
                return label_count, label_images, features

            img_array, result_dict = help_process_view_mode_2(self, img_proc_func, process)

            if img_array is None or result_dict is None:
                return

            # テーブルの初期化
            self.ui.tableWidget_Labeling.clearContents()
            row_count = 0
            for value in result_dict.values():
                result, _ = value
                row_count += result[0]  # label_count
            self.ui.tableWidget_Labeling.setRowCount(row_count)

            # 主軸角度をもつ直線の初期化
            self.principal_axes_lines.clear()

            row = 0
            for j, (key, value) in enumerate(result_dict.items(), 1):
                result, offset_pos = value
                label_count, label_images, features = result
                for i in range(label_count):
                    feat = features[i]
                    label = feat.label
                    x = feat.x
                    y = feat.y
                    w = feat.w
                    h = feat.h
                    area = feat.area
                    cx = feat.center[0]
                    cy = feat.center[1]
                    print("{0}_{1}: x:{2}, y:{3}, w:{4}, h:{5}, area:{6}, cx:{7}, cy:{8}".format(
                        key, label, x, y, w, h, area, cx, cy))

                    # アスペクト比(縦/横)
                    aspect_ratio = h / w

                    # 主軸角度
                    angle_deg, line_points = principal_axes_angle(label_images, i + 1)
                    line_points = np.array(line_points) + np.array(offset_pos)
                    self.principal_axes_lines['{0}_{1}'.format(key, label)] = line_points

                    # オフセット補正
                    x += offset_pos[0]
                    y += offset_pos[1]
                    cx += offset_pos[0]
                    cy += offset_pos[1]

                    # label
                    item_label = QTableWidgetItem("{0}_{1}".format(key, label))
                    item_center = QTableWidgetItem("({0},{1})".format(int(cx), int(cy)))
                    item_xy = QTableWidgetItem("({0},{1})".format(x, y))
                    item_size = QTableWidgetItem("({0},{1})".format(w, h))
                    item_area = QTableWidgetItem(str(area))
                    item_angle = QTableWidgetItem(str(angle_deg))
                    item_aspect_ratio = QTableWidgetItem(str(aspect_ratio))

                    self.ui.tableWidget_Labeling.setItem(row, 0, item_label)
                    self.ui.tableWidget_Labeling.setItem(row, 1, item_center)
                    self.ui.tableWidget_Labeling.setItem(row, 2, item_xy)
                    self.ui.tableWidget_Labeling.setItem(row, 3, item_size)
                    self.ui.tableWidget_Labeling.setItem(row, 4, item_area)
                    self.ui.tableWidget_Labeling.setItem(row, 5, item_angle)
                    self.ui.tableWidget_Labeling.setItem(row, 6, item_aspect_ratio)

                    row += 1

            # ラベリングしたImageWindowの参照を確保
            self.target_image_window = self.main_win.last_active_img_win


        else:
            """File Mode"""
            pass

    @Slot()
    def _apply_draw_principal_axes_lines(self):
        """
        主軸角度を持つ直線を描画
        :return:
        """
        if self.principal_axes_lines:
            if self.main_win.last_active_img_win is self.target_image_window:
                qimage = self.target_image_window.scene.dib_qimage()
                if not qimage.isNull():
                    img = qimage2ndarray(qimage)
                    if img.ndim == 2:
                        img = np.dstack([img, img, img]) # Grayscale -> RGB
                    start = time.perf_counter()

                    for value in self.principal_axes_lines.values():
                        color = tuple([int(x) for x in np.random.randint(0, 255, size=3)])
                        pt1, pt2 = value
                        img = line(img, tuple(pt1), tuple(pt2), color=color, thickness=1)

                    elapsed_time = (time.perf_counter() - start) * 1000
                    qimage = ndarray2qimage(img)
                    self.target_image_window.scene.set_qimage_on_screen(qimage)
                    self.target_image_window.scene.update()

                    self.main_win.ui.statusBar.clearMessage()
                    self.main_win.ui.statusBar.showMessage("{0} response: {1:.3f} [ms]".format("Draw Lines", elapsed_time))
                else:
                    QMessageBox.warning(self, "Principal Axes Lines", "QImageがNullです.", QMessageBox.Ok)

    @Slot()
    def _apply_draw_bounding_box(self):
        """
        バウンディングボックス(BBox)を描画する
        :return:
        """
        pass

    @Slot()
    def _apply_clear_table_view(self):
        """
        TableViewをクリア
        :return:
        """
        # Clear View model
        self.ui.tableWidget_Labeling.clearContents()
        rows = self.ui.tableWidget_Labeling.rowCount()
        self.ui.tableWidget_Labeling.model().removeRows(0, rows)

        # Clear Principal Axes
        self.principal_axes_lines.clear()

    @Slot()
    def _apply_save_features(self):
        """
        TableViewの特徴量をcsvに保存
        :return:
        """
        pass