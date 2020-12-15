"""メインウィンドウ
"""

# 標準
import os
import sys
import re
import time
import datetime
import pathlib
from copy import deepcopy
from typing import (Dict, List, Tuple, Union, Any, Callable, TypeVar, NoReturn)


# サードパーティ
import numpy as np
from scipy import (
    ndimage
)
import qimage2ndarray as qn
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import cv2
import openpyxl
import PySide2
from PySide2 import (QtGui, QtCore)
from PySide2.QtCore import (
    Signal,
    Slot,
    Qt,
    QBuffer,
    QIODevice,
    QSortFilterProxyModel,
    QRegExp
)
from PySide2.QtGui import (
    QImage,
    QPixmap,
    QDrag,
    QStandardItem
)
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QMessageBox,
    QLineEdit,
    QFileDialog,
    QDialog,
    QInputDialog,
    QColorDialog,
    QTableView
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_MainWindow import Ui_MainWindow
from image_window import ImageWindow
from edit_border_dialog import EditBorderDialog
from blur_dialog import BlurDialog
from shading_dialog import ShadingDialog
from unsharp_masking_dialog import UnsharpMaskingDialog
from edge_detector_dialog import EdgeDetectorDialog
from binarize_dialog import BinarizeDialog
from morphology_dialog import MorphologyDialog
from noise_denoise_dialog import NoiseDenoiseDialog
from histogram_dialog import HistogramDialog
from labeling_dialog import LabelingDialog
from fft_dialog import FFTDialog # 編集中
from dataset_dialog import DatasetDialog
from dl_image_recognition_dialog import DLImageRecognitionDialog

from usb_video_window import USBVideoWindow # 編集中
from ids_video_window import IDSVideoWindow # 編集中
from omron_video_window import OMRONVideoWindow # 編集中
from image_table_model import ImageTableModel
from image_table_delegate import ImageTableDelegate
from module.utils import new_serial_number_filename
from module.qt_module.qt_def import *
from module.imgproc.color import *
from module.imgproc.histgram import *


# メインのウィンドウ
class MainWindow(QMainWindow):

    signal_remove_mpl_figures = Signal(str)

    def __init__(self, parent:QWidget=None):
        super(MainWindow, self).__init__(parent)

        # UI
        self.ui:Any = Ui_MainWindow()
        self.ui.setupUi(self)

        # Image Window
        self.img_wins:List[Union[ImageWindow, None]] = []
        self.last_active_img_win:Union[ImageWindow, None] = None
        self.is_last_active = False

        # Copy/Paste
        self.qimage_copy:Union[QImage, None] = None

        # File Mode
        self.current_dir:str = os.getcwd()

        # Matplotlib figure
        self.mpl_figures = {}

        # QTableView/ImageTableModel
        self.image_table_model = ImageTableModel(0, 4, self)
        self.image_table_model.setHeaderData(0, Qt.Horizontal, "Check/Name")
        self.image_table_model.setHeaderData(1, Qt.Horizontal, 'Image')
        self.image_table_model.setHeaderData(2, Qt.Horizontal, "Size")
        self.image_table_model.setHeaderData(3, Qt.Horizontal, "Path")
        # dir_path = pathlib.Path("./data/coils")
        # file_paths = [str(path) for path in dir_path.glob("*.bmp") if not str(path).startswith('.')]
        # for i, path in enumerate(file_paths):
        #     item_for_checker = QStandardItem()
        #     item_for_checker.setCheckState(Qt.Checked)
        #     item_for_checker.setText(path.split(os.sep)[-1].split('.')[0])
        #
        #     qimage = QImage(path)
        #     item_for_image = QStandardItem()
        #     item_for_image.setData(qimage, role=Qt.DecorationRole)
        #
        #     item_for_size = QStandardItem()
        #     item_for_size.setText("{0}x{1}".format(qimage.width(), qimage.height()))
        #
        #     item_for_path = QStandardItem()
        #     item_for_path.setText(path)
        #
        #     # self.image_table_model.setItem(i, 0, item_for_checker)
        #     # self.image_table_model.setItem(i, 1, item_for_image)
        #     # self.image_table_model.setItem(i, 2, item_for_size)
        #     # self.image_table_model.setItem(i, 3, item_for_filename)
        #     self.image_table_model.appendRow([item_for_checker, item_for_image, item_for_size, item_for_path])

        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setDynamicSortFilter(True)
        self.proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setSourceModel(self.image_table_model)
        self.ui.tView_ImageTable.setSortingEnabled(True)
        self.ui.tView_ImageTable.setModel(self.proxy_model)
        self.image_table_delegate = ImageTableDelegate(self)
        self.ui.tView_ImageTable.setItemDelegate(self.image_table_delegate)
        self.ui.lEdit_ImageTable_Target_Count.setText(str(self.proxy_model.rowCount()))

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

        # 原画像
        self.ui.actionReset_Image.triggered.connect(self._act_toolbar_reset_image)

        # インジケータ
        self.ui.actionIndicator.triggered.connect(self._act_toolbar_indicator)

        # マスク
        self.ui.actionMask.toggled.connect(self._act_toolbar_mask)

        # クロスライン
        self.ui.actionCross_Line.toggled.connect(self._act_toolbar_show_cross_line)

        # プロファイル
        self.ui.actionProfile.toggled.connect(self._act_toolbar_show_profile)

        # ROI
        self.ui.actionROI.toggled.connect(self._act_toolbar_roi)

        # 直線
        self.ui.actionLine.toggled.connect(self._act_toolbar_line)

        # Ellipse
        self.ui.actionEllipse.toggled.connect(self._act_toolbar_ellipse)

        # 寸法
        self.ui.actionLine_Measure.toggled.connect(self._act_toolbar_line_measure)

        # 角度
        self.ui.actionAngle_Measure.toggled.connect(self._act_toolbar_angle_measure)


    def _menubar_connection(self):
        """
        MenuBarに関するSignal/Slotの接続
        :return:
        """
        """File"""
        # New
        self.ui.actionNew.triggered.connect(self._act_menubar_file_new)

        # Open
        self.ui.actionOpen.triggered.connect(self._act_menubar_file_open)

        # Close
        self.ui.actionClose.triggered.connect(self._act_menubar_file_close)

        # Close All
        self.ui.actionClose_All.triggered.connect(self._act_menubar_file_close_all)

        # Save
        self.ui.actionSave.triggered.connect(self._act_menubar_file_save)

        # Save As
        self.ui.actionBMP.triggered.connect(self._act_menubar_file_save_as)
        self.ui.actionJPG.triggered.connect(self._act_menubar_file_save_as)
        self.ui.actionJPEG.triggered.connect(self._act_menubar_file_save_as)
        self.ui.actionPNG.triggered.connect(self._act_menubar_file_save_as)
        self.ui.actionCSV.triggered.connect(self._act_menubar_file_save_as)
        self.ui.actionXLSX.triggered.connect(self._act_menubar_file_save_as)

        # Print
        self.ui.actionPrint.triggered.connect(self._act_menubar_file_print)

        # Quit
        self.ui.actionQuit.triggered.connect(self._act_menubar_file_quit)


        """Edit"""
        # Undo
        # self.ui.actionUndo.triggered.connect(self._act_menubar_edit_undo)

        # Cut
        self.ui.actionCut.triggered.connect(self._act_menubar_edit_cut)

        # Copy
        self.ui.actionCopy.triggered.connect(self._act_menubar_edit_copy)

        # Paste
        self.ui.actionPaste.triggered.connect(self._act_menubar_edit_paste)

        # Clear
        self.ui.actionClear.triggered.connect(self._act_menubar_edit_clear)

        # Clear Outside
        self.ui.actionClear_Outside.triggered.connect(self._act_menubar_clear_edit_outside)

        # Fill
        self.ui.actionFill.triggered.connect(self._act_menubar_edit_fill)

        # Invert
        self.ui.actionInvert.triggered.connect(self._act_menubar_edit_invert)


        """Image"""
        # Type
        self.ui.action8_bit.triggered.connect(self._act_menubar_image_type)
        self.ui.action24_bit.triggered.connect(self._act_menubar_image_type)
        self.ui.actionRGB_Color.triggered.connect(self._act_menubar_image_type)

        # Show Info
        self.ui.actionShow_Info.triggered.connect(self._act_menubar_image_show_info)

        # Color
        self.ui.actionRGB2Gray.triggered.connect(self._act_menubar_image_color)
        self.ui.actionGray2RGB.triggered.connect(self._act_menubar_image_color)
        self.ui.actionRGB2HSV.triggered.connect(self._act_menubar_image_color)
        self.ui.actionHSV2RGB.triggered.connect(self._act_menubar_image_color)
        # self.ui.actionSplit_Channels.triggered.connect(self._act_menubar_image_split_channels)
        # self.ui.actionMerge_Channels.triggered.connect(self._act_menubar_image_marge_channels)

        # Boarder
        self.ui.actionBoarder.triggered.connect(self._act_menubar_image_boarder)

        # Crop
        self.ui.actionCrop.triggered.connect(self._act_menubar_image_crop)

        # Duplicate
        self.ui.actionDuplicate.triggered.connect(self._act_menubar_image_duplicate)

        # Rename
        self.ui.actionRename.triggered.connect(self._act_menubar_image_rename)

        # Scale
        # self.ui.actionScale.triggered.connect(self._act_menubar_image_scale)

        # Transform
        self.ui.actionVertical_Flip.triggered.connect(self._act_menubar_image_transform)
        self.ui.actionHorizontal_Flip.triggered.connect(self._act_menubar_image_transform)
        self.ui.actionRotate_90_Degree_Left.triggered.connect(self._act_menubar_image_transform)
        self.ui.actionRotate_90_Degree_Right.triggered.connect(self._act_menubar_image_transform)
        self.ui.actionRotate.triggered.connect(self._act_menubar_image_transform)
        self.ui.actionTranslate.triggered.connect(self._act_menubar_image_transform)
        self.ui.actionBin.triggered.connect(self._act_menubar_image_transform)

        # Zoom
        # self.ui.actionZoomIn.triggered.connect(self._act_menubar_zoom)
        # self.ui.actionZoomOut.triggered.connect(self._act_menubar_zoom)
        # self.ui.actionOriginal_Scale.triggered.connect(self._act_menubar_zoom)
        # self.ui.actionFit_View.triggered.connect(self._act_menubar_zoom)

        """Camera"""
        self.ui.actionUSB_Camera.triggered.connect(self._act_menubar_camera)
        self.ui.actionIP_Address_Camera.triggered.connect(self._act_menubar_camera)
        self.ui.actionIDS_Camera.triggered.connect(self._act_menubar_camera)
        self.ui.actionBASLER_Camera.triggered.connect(self._act_menubar_camera)
        self.ui.actionOMRON_Camera.triggered.connect(self._act_menubar_camera)
        self.ui.actionCOGNEX_Camera.triggered.connect(self._act_menubar_camera)

        """Video"""
        pass

        """Process"""
        # Blur
        self.ui.actionBlur.triggered.connect(self._act_menubar_blur)

        # Shading
        self.ui.actionShading.triggered.connect(self._act_menubar_shading)

        # UnsharpMasking
        self.ui.actionUnsharp_Masking.triggered.connect(self._act_menubar_unsharp_masking)

        # Edge Detector
        self.ui.actionEdge_Detector.triggered.connect(self._act_menubar_edge_detector)

        # Mapping
        self.ui.actionMapping.triggered.connect(self._act_menubar_mapping)

        # Binary
        self.ui.actionBinarize.triggered.connect(self._act_menubar_binarize)

        # Morphology
        self.ui.actionMorphology.triggered.connect(self._act_menubar_morphology)

        # Noize/Denoise
        self.ui.actionNoise_Denoise.triggered.connect(self._act_menubar_noise_denoise)

        # Histgram
        self.ui.actionHistogram.triggered.connect(self._act_menubar_histogram)


        """Analyze"""
        # Labeling
        self.ui.actionLabeling.triggered.connect(self._act_menubar_labeling)

        # Show Histgram
        self.ui.actionShow_Histogram.triggered.connect(self._act_menubar_show_histogram)

        # Surface Plot
        self.ui.actionSurface_Plot.triggered.connect(self._act_menubar_surface_plot)

        # FFT
        self.ui.actionFFT.triggered.connect(self._act_menubar_fft)

        # Wavelet
        # self.ui.actionWavelet.triggered.connect(self._act_menubar_wavelet)

        """Local Feature"""
        # # KeyPoint: KLT Corner
        # self.ui.actionKLT_Corner.triggered.connect(self._act_menubar_keypoint)
        #
        # # KeyPoint: Harris Corner
        # self.ui.actionHarris_Corner.triggered.connect(self._act_menubar_keypoint)
        #
        # # KeyPoint: FAST Corner
        # self.ui.actionFAST_Corner.triggered.connect(self._act_menubar_keypoint)
        #
        # # KeyPoint: AGAST Corner
        # self.ui.actionAGAST_Corner.triggered.connect(self._act_menubar_keypoint)
        #
        # # KeyPoint: MSER Resion
        # self.ui.actionMSER_Resion.triggered.connect(self._act_menubar_keypoint)
        #
        # # KeyPoint: Star Corner
        # self.ui.actionStar_Detector.triggered.connect(self._act_menubar_keypoint)
        #
        # # KeyPoint: MSD Corner
        # self.ui.actionMSD_Detector.triggered.connect(self._act_menubar_keypoint)

        """Descriptor"""
        # # Descriptor: BRIEF
        # self.ui.actionBRIEF_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: FREAK
        # self.ui.actionFREAK_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: LATCH
        # self.ui.actionLATCH_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: LUCID
        # self.ui.actionLUCID_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: DAISY
        # self.ui.actionDAISY_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: HOG
        # self.ui.actionHOG_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: Harr-Like
        # self.ui.actionHarrLile_Descriptor.triggered.connect(self._act_menubar_descriptor)
        #
        # # Descriptor: LBP
        # self.ui.actionLBP_Descriptor.triggered.connect(self._act_menubar_descriptor)

        """KeyPoint-Descriptor"""
        # # Binary-Base: ORB
        # self.ui.actionORB.triggered.connect(self._act_menubar_keypoint_and_descriptor)
        #
        # # Binary-Base: BRISK
        # self.ui.actionBRISK.triggered.connect(self._act_menubar_keypoint_and_descriptor)
        #
        # # Binary-Base: KAZE
        # self.ui.actionKAZE.triggered.connect(self._act_menubar_keypoint_and_descriptor)
        #
        # # Binary-Base: Accelerated-KAZE
        # self.ui.actionAKAZE.triggered.connect(self._act_menubar_keypoint_and_descriptor)
        #
        # # Real-Base: SIFT
        # self.ui.actionSIFT.triggered.connect(self._act_menubar_keypoint_and_descriptor)
        #
        # # Real-Base: SURF
        # self.ui.actionSURF.triggered.connect(self._act_menubar_keypoint_and_descriptor)

        """Detector"""
        pass


        """Motion Tracking"""
        pass


        """ML/dl"""
        # Annotation: Simple-Annotation
        self.ui.actionSimple_Annotation.triggered.connect(self._act_menubar_annotation)

        # dataset
        self.ui.actionDataset.triggered.connect(self._act_menubar_dataset)

        # dl -> Classification -> Image
        self.ui.actionImage.triggered.connect(self._act_menubar_dl_classification_image)




    def _ui_connection(self):
        """
        UIに関するSignal/Slotの接続
        :return:
        """
        # File/View Mode
        self.ui.rBtn_View_Mode.clicked.connect(self._enable_view_mode)
        self.ui.rBtn_File_Mode.clicked.connect(self._enable_file_mode)

        # Input/Output Directory
        self.ui.tBtn_Input_Dir.clicked.connect(self._select_input_dir)
        self.ui.tBtn_Output_Dir.clicked.connect(self._select_output_dir)

        # Review ImageTable
        self.ui.pBtn_ImageTable_Review.clicked.connect(self._review_image_table)

        # All Check/UnCheck ImageTable
        self.ui.pBtn_ImageTable_All_Check.clicked.connect(self._all_check_image_table)
        self.ui.pBtn_ImageTable_All_Uncheck.clicked.connect(self._all_uncheck_image_table)

        # Search recode in ImageTable
        self.ui.lEdit_ImageTable_Search_Recode.textChanged.connect(self._search_recode_image_table)


    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        # self.mpl_figuresに格納したMatplotlibのfigureオブジェクトを削除
        self.signal_remove_mpl_figures.connect(self._remove_mpl_figures)


    # override
    def dropEvent(self, event:PySide2.QtGui.QDropEvent):
        """
        ドロップイベント
        :param event:
        :return:
        """
        urls = event.mimeData().urls()
        if len(urls) == 0:
            return

        """画像を取得してImageWindowで表示"""
        dt_now = datetime.datetime.now()
        for url in urls:
            # ファイルパスの取得
            file_path = str(url.toLocalFile())
            root, extension = os.path.splitext(file_path)

            # 受け入れ可能な拡張子のワイルドカードを作成 r"^\.(png|jpg|jpeg|bmp|)$"
            match_ext = r"^\.(" + "|".join(accept_imgs) + r")$"

            # マッチングすれば，SceneのQImageに画像ファイルを格納
            if re.match(match_ext, extension, re.IGNORECASE):
                if os.path.isfile(file_path):

                    # 最新連番でファイル名を作成
                    filename = file_path.split('/')[-1]
                    stored_filenames = [img_win.filename for img_win in self.img_wins]
                    filename = new_serial_number_filename(filename, stored_filenames)

                    # QImage
                    droped_qimage = QImage(file_path)
                    depth = droped_qimage.bitPlaneCount()
                    is_grayscale = droped_qimage.allGray()
                    if is_grayscale and depth == 8:
                        droped_qimage = droped_qimage.convertToFormat(QImage.Format_Grayscale8)
                    else:
                        droped_qimage = droped_qimage.convertToFormat(QImage.Format_RGB888)

                    # ImageWindow
                    new_img_win = ImageWindow(self)
                    new_img_win.set_filename(filename)

                    new_img_win.show()

                    # 画像サイズに合わせてウィンドウサイズを変更
                    adjust_viewport(droped_qimage, new_img_win.ui.gView, new_img_win)

                    new_img_win.activateWindow()
                    self.img_wins.append(new_img_win)

                    # 画像をSceneに登録
                    new_img_win.scene.clear()
                    new_img_win.scene.set_qimage_on_screen(droped_qimage, is_raw=True)
                    new_img_win.scene.update()



            else:
                # ファイル拡張子が不適切な場合
                valid_ext = ",".join(accept_imgs)
                valid_ext.strip(',')
                QMessageBox.warning(self,
                                    "Invalid Image",
                                    "画像ファイルの拡張子が不適切です。\n有効拡張子: {0}".format(valid_ext),
                                    QMessageBox.Ok)

        super(MainWindow, self).dropEvent(event)

    # override
    def dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent):
        """
        ドラッグエンターイベント
        :param event:
        :return:
        """

        """
        よく使用するMIMEタイプ
        Tester      Getter      Setter         MIME Types
        -----------------------------------------------------
        hasText()   text()      setText()      text/plain
        hasHtml()   html()      setHtml()      text/html
        hasUrls()   urls()      setUrls()      text/uri-text
        hasImages() imageData() setImageData() image/*
        hasColor()  colorData() setColorData() application/x-color

        image/*で受け付けるファイル拡張子
        bmp, fif, gif, ifm, ief, jpe, jpg, jpeg, png, svg, tif, tiff,
        mcf, rp, wbmp, ras, fh, fh4, fh5, fh7, fhc, ico, jps, pnm, pbm,
        ppm, rgb, xbm, xpm, swx, xwd

        QImageで受け付けるファイル拡張子
        bmp(R/W), gif(R), jpg(R/W), jpeg(R/W), png(R/W), pbm(R), pgm(R),
        ppm(R/W), xbm(R/W), xpm(R/W) 
        """
        # QMimeDataにファイル名、URL(HTTPパスやFTPパスなど)が格納されている場合
        if event.mimeData().hasUrls():
            event.accept()
            event.acceptProposedAction()

        super(MainWindow, self).dragEnterEvent(event)

    # override
    def dragMoveEvent(self, event: PySide2.QtGui.QDragMoveEvent):
        """
        ドラッグムーブイベント
        :param event:
        :return:
        """
        super(MainWindow, self).dragMoveEvent(event)

    # override
    def dragLeaveEvent(self, event: PySide2.QtGui.QDragLeaveEvent):
        """
        ドラッグリーブイベント
        :param event:
        :return:
        """
        super(MainWindow, self).dragLeaveEvent(event)

    # override
    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent):
        """
        マウスムーブイベント
        :param event:
        :return:
        """
        win_pos = event.pos()

        # ドラッグ開始を検出
        if event.button() == Qt.LeftButton:
            distance = (win_pos - self.pressMousePos).manhattanLength()  # マンハッタン距離

            # Qtアプリの推奨距離(4pxl)以上であればドラッグ開始時の処理を起動
            if distance >= QApplication.startDragDistance():
                self._startDrag(Qt.MoveAction, event)

        super(MainWindow, self).mouseMoveEvent(event)

    def _startDrag(self, action:Qt.DropActions, event:PySide2.QtGui.QMouseEvent):
        """
        ドラッグ開始時の処理
        :return:
        """
        # ドラッグした画像をマウスカーソル付近に表示
        for url in event.mimeData().urls():
            file_path = str(url.toLocalFile)
            root, extension = os.path.splitext(file_path)

            # 受け入れ可能な拡張子のワイルドカードを作成 r"^\.(png|jpg|jpeg|bmp|)$"
            match_ext = r"^\.(" + "|".join(accept_imgs) + r")$"

            # マッチングすれば、QImageに画像ファイルのデータを格納してDragIconを表示
            if re.match(match_ext, extension, re.IGNORECASE):
                if os.path.isfile(file_path):
                    drag = QDrag(self)
                    drag.setPixmap(QPixmap(file_path))
                    if drag.exec_(supportedActions=action) == Qt.MoveAction:
                        pass  # dragのイベントループ終了時の処理


    def _help_apply_qimage(self, img_proc_func: object) -> bool:
        """
        直前のアクティブなImageWindowがもつQImageに対して
        処理を行うラッパー
        :param img_proc_func:
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                img_src = qimage2ndarray(qimage)
                img_dst = img_proc_func(img_src)
                qimg_dst = ndarray2qimage(img_dst)
                self.last_active_img_win.scene.set_qimage_on_screen(qimg_dst)
                self.last_active_img_win.scene.update()
                return True
        return False

    @Slot(str)
    def _remove_mpl_figures(self, figure_key:str):
        """
        self.mpl_figuresに格納したMatplotlibのfigureオブジェクトを削除する
        :param figure_key:
        :return:
        """
        if figure_key in self.mpl_figures.keys():
            del self.mpl_figures[figure_key]
            print("Removed self.mpl_figures[{0}].".format(figure_key))
            print("self.mpl_figures type: ")
            for fig in self.mpl_figures:
                print("object: {0} id: {1}".format(fig, id(fig)))
        else:
            print("No object with ", figure_key)

    @Slot()
    def _enable_view_mode(self):
        """
        ビューモードに切り替え
        :return:
        """
        self.ui.lEdit_Input_Dir.setEnabled(False)
        self.ui.lEdit_Output_Dir.setEnabled(False)
        self.ui.tBtn_Input_Dir.setEnabled(False)
        self.ui.tBtn_Output_Dir.setEnabled(False)
        self.repaint()

    @Slot()
    def _enable_file_mode(self):
        """
        ファイルモードに切り替え
        :return:
        """
        self.ui.lEdit_Input_Dir.setEnabled(True)
        self.ui.lEdit_Output_Dir.setEnabled(True)
        self.ui.tBtn_Input_Dir.setEnabled(True)
        self.ui.tBtn_Output_Dir.setEnabled(True)
        self.repaint()

    @Slot()
    def _select_input_dir(self):
        """
        ファイルモードで使う入力ディレクトリを選択
        :return:
        """
        dir = QFileDialog.getExistingDirectory(self, "入力ディレクトリを開く", self.current_dir)
        if dir != "":
            self.current_dir = dir
            self.ui.lEdit_Input_Dir.setText(self.current_dir)
            self.repaint()

    @Slot()
    def _select_output_dir(self):
        """
        ファイルモードで使う出力ディレクトリを選択
        :return:
        """
        dir = QFileDialog.getExistingDirectory(self, "出力ディレクトリを開く", self.current_dir)
        if dir != "":
            self.current_dir = dir
            self.ui.lEdit_Output_Dir.setText(self.current_dir)
            self.repaint()

    @Slot()
    def _review_image_table(self):
        """
        ImageTableViewの表示を初期状態に戻す
        :return:
        """
        self.ui.tView_ImageTable.review()

    @Slot()
    def _all_check_image_table(self):
        """
        ImageTableViewの全チェックボックスをONにする
        :return:
        """
        self.ui.tView_ImageTable.all_check()

    @Slot()
    def _all_uncheck_image_table(self):
        """
        ImageTableViewの全チェックボックスをOFFにする
        :return:
        """
        self.ui.tView_ImageTable.all_uncheck()

    @Slot()
    def _search_recode_image_table(self):
        """
        ImageTableViewの検索フィルタを変更
        :return:
        """
        reg_exp = QRegExp(self.ui.lEdit_ImageTable_Search_Recode.text(),
                          Qt.CaseSensitive,
                          QRegExp.Wildcard)
        self.ui.tView_ImageTable.update_search_filter(reg_exp)
        recode_count = self.ui.tView_ImageTable.model().rowCount()
        self.ui.lEdit_ImageTable_Target_Count.setText(str(recode_count))
        print("recode_count", recode_count)

    @Slot()
    def _act_toolbar_reset_image(self):
        """
        原画像の表示
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            self.last_active_img_win.scene.reset_qimage()


    @Slot(bool)
    def _act_toolbar_indicator(self):
        """
        インジケータの表示切り替え
        :return:
        """
        for img_win in self.img_wins:
            pass

    @Slot(bool)
    def _act_toolbar_mask(self, checked: bool):
        """
        マスク画像の表示切り替え
        :param checked:
        :return:
        """
        for img_win in self.img_wins:
            img_win.toggle_scene_mask(show=checked)

    @Slot(bool)
    def _act_toolbar_show_cross_line(self, checked:bool):
        """
        マウスクロスラインの表示切替
        :return:
        """
        for img_win in self.img_wins:
            img_win.toggle_scene_cross_line(show=checked)


    @Slot(bool)
    def _act_toolbar_show_profile(self, checked:bool):
        """
        プロファイルの表示切替
        :return:
        """
        for img_win in self.img_wins:
            img_win.toggle_scene_profile(show=checked)


    @Slot(bool)
    def _act_toolbar_roi(self, checked:bool):
        """
        ROIの表示切替
        :return:
        """
        for img_win in self.img_wins:
            img_win.toggle_scene_roi(show=checked)

    @Slot(bool)
    def _act_toolbar_line(self, checked:bool):
        """
        直線の表示切り替え
        :param checked:
        :return:
        """
        for img_win in self.img_wins:
            img_win.toggle_scene_line(show=checked)

    @Slot(bool)
    def _act_toolbar_ellipse(self, checked:bool):
        """
        楕円の表示切り替え
        :param checked:
        :return:
        """
        for img_win in self.img_wins:
            img_win.toggle_scene_ellipse(show=checked)



    @Slot(bool)
    def _act_toolbar_line_measure(self, checked:bool):
        """
        寸法の表示切り替え
        :param checked:
        :return:
        """
        if checked:
            QMessageBox.information(self, "Line Measure", "checked True", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Line Measure", "checked False", QMessageBox.Ok)

    @Slot(bool)
    def _act_toolbar_angle_measure(self, checked:bool):
        """
        角度の表示切り替え
        :param checked:
        :return:
        """
        if checked:
            QMessageBox.information(self, "Angle Measure", "checked True", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Angle Measure", "checked False", QMessageBox.Ok)

    @Slot()
    def _act_menubar_file_new(self):
        """
        新規の画像を生成
        :return:
        """
        new_img_win = ImageWindow(self)
        new_img_win.set_filename("Empty")
        self.img_wins.append(new_img_win)
        new_img_win.show()
        new_img_win.activateWindow()

    @Slot()
    def _act_menubar_file_open(self):
        """
        画像を読み込む
        :return:
        """
        file_path_list, _ = QFileDialog.getOpenFileNames(self, "画像ファイルを開く", os.getcwd(), accept_filter)

        for file_path in file_path_list:
            if file_path != "":
                qimage = QImage(file_path)
                depth = qimage.bitPlaneCount()
                is_grayscale = qimage.isGrayscale()
                if is_grayscale and depth == 8:
                    qimage = qimage.convertToFormat(QImage.Format_Grayscale8)
                else:
                    qimage = qimage.convertToFormat(QImage.Format_RGB888)

                filename = file_path.split('/')[-1]
                stored_filenames = [img_win.filename for img_win in self.img_wins]
                filename = new_serial_number_filename(filename, stored_filenames)

                new_img_win = ImageWindow(self)
                new_img_win.filename = filename
                new_img_win.set_filename(filename)
                new_img_win.ui.lbl_Image_Scale.setText('100%')
                self.img_wins.append(new_img_win)
                new_img_win.show()
                new_img_win.activateWindow()

                # 画像をSceneに登録
                new_img_win.scene.clear()
                new_img_win.scene.set_qimage_on_screen(qimage, is_raw=True)
                new_img_win.scene.setSceneRect(QPixmap(qimage).rect())
                print("Scene Rect", new_img_win.scene.sceneRect())
                new_img_win.scene.update()

                # 画像サイズに合わせてウィンドウサイズを変更
                adjust_viewport(qimage, new_img_win.ui.gView, new_img_win)


    @Slot()
    def _act_menubar_file_close(self):
        """
        アクティブな画像ウィンドウを閉じる
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            if self.last_active_img_win in self.img_wins:
                self.last_active_img_win.close()
                self.last_active_img_win = None
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_file_close_all(self):
        """
        現在開いている画像ウィンドウを閉じる
        :return:
        """
        wins = self.img_wins[:-1]
        last_win = self.img_wins[-1]
        for img_win in wins:
            img_win.close()
        last_win.close()
        self.img_wins.clear()
        self.last_active_img_win = None

    @Slot()
    def _act_menubar_file_save(self):
        """
        アクティブな画像ウィンドウの画像を保存
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                filename = self.last_active_img_win.filename
                ext_filter = "画像(*.bmp *.jpeg *.jpg *.png)"
                tmp_file_path = "/".join([os.getcwd(), filename])
                file_path, _ = QFileDialog.getSaveFileName(self, "画像を保存", tmp_file_path, ext_filter)

                if file_path != "":
                    try:
                        ret = qimage.save(file_path)
                        if not ret:
                            raise Exception("QImage Saveが失敗しました.\n拡張子かディレクトリが不適切です.")

                    except Exception as e:
                        msg = e.args[0]
                        QMessageBox.warning(self, "Save Error", msg, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Save Error", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    # @Slot()
    def _act_menubar_file_save_as(self):
        """
        アクティブな画像ウィンドウを指定した形式で保存
        :return:
        """
        sender = self.sender()
        if sender == self.ui.actionBMP:
            as_type = 'bmp'
        elif sender == self.ui.actionJPEG:
            as_type = 'jpeg'
        elif sender == self.ui.actionJPG:
            as_type = 'jpg'
        elif sender == self.ui.actionPNG:
            as_type = 'png'
        elif sender == self.ui.actionCSV:
            as_type = 'csv'
        elif sender == self.ui.actionXLSX:
            as_type = 'xlsx'
        else:
            as_type = 'unknown'

        if as_type == 'unknown':
            QMessageBox.warning(self, "Save As Error", "拡張子が不明です. unknown", QMessageBox.Ok)
            return

        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                filename = self.last_active_img_win.filename
                name, ext = filename.split('.')
                filename = name + "." + as_type
                ext_filter = "画像(*.bmp *.jpeg *.jpg *.png);;Text(*.csv *.xlsx)"
                tmp_file_path = "/".join([os.getcwd(), filename])
                file_path, _ = QFileDialog.getSaveFileName(self, "指定した拡張子で保存", tmp_file_path, ext_filter)

                if file_path != "":
                    try:
                        if as_type == 'bmp' or as_type == 'jpeg' or as_type == 'jpg' or as_type == 'png':
                            ret = qimage.save(file_path)
                            if not ret:
                                raise Exception("QImage Saveが失敗しました.\n拡張子かディレクトリが不適切です.")
                        else:
                            # QImage -> Numpy
                            colors = []
                            img = None
                            if qimage.allGray():
                                view_array = qimage2ndarray(qimage)
                                h, w = view_array.shape
                                img = view_array.reshape((1, h, w)) # (1, H, W)
                                colors = ['gray']
                            else:
                                view_array = qimage2ndarray(qimage) # (3, H, W)
                                h, w, c = view_array.shape
                                img = view_array.reshape((c, h, w))
                                colors = ['r', 'g', 'b']

                            if as_type == 'csv':
                                tokens = file_path.split('/')[:-1]
                                dir = ""
                                for token in tokens:
                                    dir += token + "/"

                                file_list = []
                                for c, color in enumerate(colors):
                                    fpath = dir + name + "-" + color + "." + as_type
                                    np.savetxt(fpath, img[c], delimiter=',', fmt='%d', encoding='utf-8', header=as_type)
                                    file_list.append(fpath)

                                with open(file_path, mode='w') as f:
                                    f.writelines(file_list)

                            else:
                                # .xlsx
                                with pd.ExcelWriter(file_path) as writer:
                                    for c, color in enumerate(colors):
                                        df = pd.DataFrame(img[c])
                                        df.to_excel(writer, sheet_name=color, index=False, header=False)

                    except Exception as e:
                        msg = e.args[0]
                        QMessageBox.warning(self, "Save As Error", msg, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Save Error", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_file_print(self):
        """
        アクティブな画像ウィンドウの画像を印刷
        :return:
        """
        QMessageBox.information(self, "Print", "工事中", QMessageBox.Ok)

    @Slot()
    def _act_menubar_file_quit(self):
        """
        アプリケーションを閉じる
        :return:
        """
        QApplication.closeAllWindows()

    @Slot()
    def _act_menubar_undo(self):
        """
        直前の状態に戻す
        :return:
        """
        QMessageBox.information(self, "Undo", "工事中", QMessageBox.Ok)

    @Slot()
    def _act_menubar_edit_cut(self):
        """
        指定したROI領域をカットする
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                if len(rect_list) > 0:
                    process = "Cut"
                    start = time.perf_counter()

                    rect = rect_list[-1][-1].toRect()
                    self.qimage_copy = qimage.copy(rect) # copy
                    xmin, ymin = rect.x(), rect.y()
                    xmax, ymax = xmin + rect.width(), ymin + rect.height()
                    img = qimage2ndarray(qimage)
                    img[ymin:ymax, xmin:xmax] = 0 # cut
                    qimage = ndarray2qimage(img)
                    self.last_active_img_win.scene.set_qimage_on_screen(qimage)

                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
                else:
                    QMessageBox.warning(self, "Copy", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Copy", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    @Slot()
    def _act_menubar_edit_copy(self):
        """
        指定したROI領域をコピーする
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                if len(rect_list) > 0:
                    process = "Copy"

                    start = time.perf_counter()
                    rect = rect_list[-1][-1].toRect()
                    self.qimage_copy = qimage.copy(rect)
                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
                else:
                    QMessageBox.warning(self, "Copy", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Copy", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_edit_paste(self):
        """
        指定ポイントをコピー画像の左上として貼り付け
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                if len(rect_list) > 0:
                    process = "Paste"

                    def paste(src:np.ndarray) -> np.ndarray:
                        rect = rect_list[-1][-1].toRect()
                        xmin, ymin = rect.x(), rect.y()
                        xmax, ymax = xmin + self.qimage_copy.width(), ymin + self.qimage_copy.height()
                        if xmax > qimage.width():
                            xmax = qimage.width()
                        if ymax > qimage.height():
                            ymax = qimage.height()

                        dst = np.copy(src)
                        img_copy = qimage2ndarray(self.qimage_copy)
                        if dst.ndim == 3:
                            if dst.shape[-1] == 3:
                                # dst is color
                                if img_copy.ndim == 2 or (img_copy.ndim == 3 and img_copy.shape[-1] == 1):
                                    img_copy_2d = img_copy.reshape(img_copy.shape[0], img_copy.shape[1]) # gray
                                    img_copy = np.dstack([img_copy_2d, img_copy_2d, img_copy_2d]) # all gray
                            else:
                                # dst is grayscale
                                if img_copy.ndim == 2 or (img_copy.ndim == 3 and img_copy.shape[-1] == 1):
                                    img_copy = img_copy.reshape(img_copy.shape[0], img_copy.shape[1])
                                else:
                                    img_copy = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY) # RGB -> Grayscale
                        else:
                            # dst is grayscale
                            if img_copy.ndim == 2 or (img_copy.ndim == 3 and img_copy.shape[-1] == 1):
                                img_copy = img_copy.reshape(img_copy.shape[0], img_copy.shape[1])
                            else:
                                img_copy = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY)  # RGB -> Grayscale

                        dst[ymin:ymax, xmin:xmax] = img_copy[0:ymax - ymin, 0:xmax - xmin]
                        return dst

                    img_proc_func = paste
                    start = time.perf_counter()
                    self._help_apply_qimage(img_proc_func)
                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
                else:
                    QMessageBox.warning(self, "Paste", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Paste", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    @Slot()
    def _act_menubar_edit_clear(self):
        """
        指定したROI領域の画素値を0にする
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                if len(rect_list) > 0:
                    process = "Clear"

                    def clear_roi(src:np.ndarray) -> np.ndarray:
                        for key, rect in rect_list:
                            rect = rect.toRect()
                            xmin = rect.x()
                            ymin = rect.y()
                            xmax = xmin + rect.width()
                            ymax = ymin + rect.height()
                            dst = np.copy(src)
                            dst[ymin:ymax, xmin:xmax] = 0
                        return dst

                    img_proc_func = clear_roi
                    start = time.perf_counter()
                    self._help_apply_qimage(img_proc_func)
                    elapsed_time = (time.perf_counter() - start) * 1000

                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))

                else:
                    QMessageBox.warning(self, "Clear", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Clear", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    @Slot()
    def _act_menubar_clear_edit_outside(self):
        """
        指定したROI領域以外の画素値を0にする
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                if len(rect_list) > 0:
                    process = "Clear outside"

                    def clear_outside_roi(src:np.ndarray) -> np.ndarray:
                        dst = np.zeros_like(src)
                        for key, rect in rect_list:
                            rect = rect.toRect()
                            xmin = rect.x()
                            ymin = rect.y()
                            xmax = xmin + rect.width()
                            ymax = ymin + rect.height()
                            dst[ymin:ymax, xmin:xmax] = src[ymin:ymax, xmin:xmax]
                        return dst

                    img_proc_func = clear_outside_roi
                    start = time.perf_counter()
                    self._help_apply_qimage(img_proc_func)
                    elapsed_time = (time.perf_counter() - start) * 1000

                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
                else:
                    QMessageBox.warning(self, "Clear outside", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Clear outside", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    @Slot()
    def _act_menubar_edit_fill(self):
        """
        指定したROI領域の画素値を255にする
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                if len(rect_list) > 0:
                    process = "Fill"
                    color = QColorDialog.getColor()

                    def fill(src:np.ndarray) -> np.ndarray:
                        dst = np.copy(src)
                        if src.ndim == 3 and src.shape[-1] == 3:
                            if color.isValid():
                                r = color.red()
                                g = color.green()
                                b = color.blue()
                                for key, rect in rect_list:
                                    rect = rect.toRect()
                                    xmin = rect.x()
                                    ymin = rect.y()
                                    xmax = xmin + rect.width()
                                    ymax = ymin + rect.height()
                                    dst[ymin:ymax, xmin:xmax] = (r, g, b)
                        else:
                            if color.isValid():
                                luminance = color.value()
                                for key, rect in rect_list:
                                    rect = rect.toRect()
                                    xmin = rect.x()
                                    ymin = rect.y()
                                    xmax = xmin + rect.width()
                                    ymax = ymin + rect.height()
                                    dst[ymin:ymax, xmin:xmax] = luminance
                        return dst

                    img_proc_func = fill
                    start = time.perf_counter()
                    self._help_apply_qimage(img_proc_func)
                    elapsed_time = (time.perf_counter() - start) * 1000

                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
                else:
                    QMessageBox.warning(self, "Fill", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Fill", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    @Slot()
    def _act_menubar_edit_invert(self):
        """
        指定したROI領域の画素値を反転させる
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                rect_list = self.last_active_img_win.scene.roi_rects()
                process = "Invert"

                if len(rect_list) > 0:
                    def invert(src: np.ndarray) -> np.ndarray:
                        dst = np.copy(src)
                        for key, rect in rect_list:
                            rect = rect.toRect()
                            xmin = rect.x()
                            ymin = rect.y()
                            xmax = xmin + rect.width()
                            ymax = ymin + rect.height()
                            dst[ymin:ymax, xmin:xmax] = 255 - src[ymin:ymax, xmin:xmax]
                        return dst
                else:
                    def invert(src: np.ndarray) -> np.ndarray:
                        dst = 255 - src
                        return dst

                img_proc_func = invert
                start = time.perf_counter()
                self._help_apply_qimage(img_proc_func)
                elapsed_time = (time.perf_counter() - start) * 1000

                self.ui.statusBar.clearMessage()
                self.ui.statusBar.showMessage(
                    "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
            else:
                QMessageBox.warning(self, "Invert", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    # @Slot(bool)
    def _act_menubar_image_type(self):
        """
        画像のビット深度を切り替える
        :param clicked:
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                self.ui.action8_bit.setChecked(False)
                self.ui.action24_bit.setChecked(False)
                self.ui.actionRGB_Color.setChecked(False)

                sender = self.sender()
                _format = None
                if sender == self.ui.action8_bit:
                    self.ui.action8_bit.setChecked(True)
                    _format = QImage.Format_Grayscale8

                elif sender == self.ui.action24_bit:
                    self.ui.action24_bit.setChecked(True)
                    qimage = qimage.convertToFormat(QImage.Format_Grayscale8)
                    _format = QImage.Format_RGB888

                elif sender == self.ui.actionRGB_Color:
                    self.ui.actionRGB_Color.setChecked(True)
                    _format = QImage.Format_RGB32

                else:
                    print(f"Error: sender is unknown; {sender}")
                    return

                start = time.perf_counter()
                qimage_cvt = qimage.convertToFormat(_format)
                self.last_active_img_win.scene.set_qimage_on_screen(qimage_cvt)
                elapsed_time = (time.perf_counter() - start) * 1000

                process = "Type"
                self.ui.statusBar.clearMessage()
                self.ui.statusBar.showMessage(
                    "{0} response: {1:.3f} [ms]".format(process, elapsed_time))


            else:
                QMessageBox.warning(self, "Type", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_image_show_info(self):
        """
        画像情報を表示する
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):

            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                # Status
                cache_key = qimage.cacheKey()
                _format = qimage.format()
                depth = qimage.depth()
                bit_plane_count = qimage.bitPlaneCount()
                color_table = qimage.colorTable()
                color_count = qimage.colorCount()
                has_alpha_channel = qimage.hasAlphaChannel()
                is_all_gray = qimage.allGray()
                is_grayscale = qimage.isGrayscale()
                width = qimage.width()
                height = qimage.height()
                bytes_per_line = qimage.bytesPerLine()
                data_size = qimage.sizeInBytes()
                logical_dpi_x = qimage.logicalDpiX()
                logical_dpi_y = qimage.logicalDpiY()
                physical_dpi_x = qimage.physicalDpiX()
                physical_dpi_y = qimage.physicalDpiY()
                dots_per_meter_x = qimage.dotsPerMeterX()
                dots_per_meter_y = qimage.dotsPerMeterY()
                device_pixel_ratio = qimage.devicePixelRatio()
                text_keys = qimage.textKeys()
                text = qimage.text()

                status = (
                    "Cache Key: {0}".format(cache_key),
                    "Format: {0}".format(_format),
                    "Depth: {0}".format(depth),
                    "Bit plane count: {0}".format(bit_plane_count),
                    "Color table: {0}".format(color_table),
                    "Color count: {0}".format(color_count),
                    "Has alpha channel: {0}".format(has_alpha_channel),
                    "Is all gray: {0}".format(is_all_gray),
                    "Is grayscale: {0}".format(is_grayscale),
                    "Width: {0}".format(width),
                    "Height: {0}".format(height),
                    "Bytes per line: {0}".format(bytes_per_line),
                    "Data size: {0}".format(data_size),
                    "Logical dpi x: {0}".format(logical_dpi_x),
                    "Logical dpi y: {0}".format(logical_dpi_y),
                    "Physical dpi x: {0}".format(physical_dpi_x),
                    "Physical dpi y: {0}".format(physical_dpi_y),
                    "Dots per meter x: {0}".format(dots_per_meter_x),
                    "Dots per meter y: {0}".format(dots_per_meter_y),
                    "Device pixel ratio: {0}".format(device_pixel_ratio),
                    "Text keys: {0}".format(text_keys),
                    "Text: {0}".format(text)
                )
                text = ""
                for msg in status:
                    text += msg + "\n"

                QInputDialog.getMultiLineText(self, "Show Information of Image", "画像情報", text)

            else:
                QMessageBox.warning(self, "Show Info", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    # @Slot()
    def _act_menubar_image_color(self):
        """
        画像のカラー情報に関する操作
        1) HSV化
        2) GrayScale化
        3) RGB化
        4) Split Channels
        5) Merge Channels
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                process = 'Color '

                sender = self.sender()
                if sender == self.ui.actionRGB2Gray:
                    process += 'RGB->Gray'
                    start = time.perf_counter()
                    self._help_apply_qimage(rgb2gray)
                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))

                elif sender == self.ui.actionGray2RGB:
                    process += 'Gray->RGB'
                    start = time.perf_counter()
                    self._help_apply_qimage(gray2rgb)
                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))

                elif sender == self.ui.actionRGB2HSV:
                    process += 'RGB->HSV'
                    start = time.perf_counter()
                    self._help_apply_qimage(rgb2hsv)
                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))

                elif sender == self.ui.actionHSV2RGB:
                    process += 'HSV->RGB'
                    start = time.perf_counter()
                    self._help_apply_qimage(hsv2rgb)
                    elapsed_time = (time.perf_counter() - start) * 1000
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage(
                        "{0} response: {1:.3f} [ms]".format(process, elapsed_time))

                else:
                    process += 'Unknown'
                    self.ui.statusBar.clearMessage()
                    self.ui.statusBar.showMessage("{0} response".format(process))
            else:
                QMessageBox.warning(self, "Color", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_image_boarder(self):
        """
        画像の縁に新たにピクセルを追加する
        :return:
        """
        edit_border = EditBorderDialog(self)
        edit_border.show()
        edit_border.activateWindow()

    @Slot()
    def _act_menubar_image_crop(self):
        """
        画像をクロップして新たにImageWindowを生成
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                roi_rects = self.last_active_img_win.scene.roi_rects()
                if roi_rects:
                    filename = self.last_active_img_win.filename
                    for key, rect_f in roi_rects:
                        cropped_img = qimage.copy(rect_f.toRect())

                        new_img_win = ImageWindow(self)
                        stored_filenames = [img_win.filename for img_win in self.img_wins]

                        if filename.rfind("_crop") == -1:
                            name, ext = filename.split('.')
                            filename = name + "_crop" + "." + ext

                        new_filename = new_serial_number_filename(filename, stored_filenames)
                        new_img_win.set_filename(new_filename)
                        self.img_wins.append(new_img_win)
                        new_img_win.show()
                        new_img_win.activateWindow()

                        # 画像をSceneに登録
                        new_img_win.scene.clear()
                        new_img_win.scene.set_qimage_on_screen(cropped_img, is_raw=True)
                        new_img_win.scene.update()

                        # 画像サイズに合わせてウィンドウサイズを変更
                        adjust_viewport(cropped_img, new_img_win.ui.gView, new_img_win)

                else:
                    QMessageBox.warning(self, "Crop", "ROIが設定されていません.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Crop", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_image_duplicate(self):
        """
        画像を複製して新たにImageWindowを生成
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                qimage_deplicate = qimage.copy()

                filename = self.last_active_img_win.filename
                stored_filenames = [img_win.filename for img_win in self.img_wins]
                new_filename = new_serial_number_filename(filename, stored_filenames)

                new_img_win = ImageWindow(self)
                new_img_win.set_filename(new_filename)
                self.img_wins.append(new_img_win)
                new_img_win.show()
                new_img_win.activateWindow()

                # 画像をSceneに登録
                new_img_win.scene.clear()
                new_img_win.scene.set_qimage_on_screen(qimage_deplicate, is_raw=True)
                new_img_win.scene.update()

                # 画像サイズに合わせてウィンドウサイズを変更
                adjust_viewport(qimage_deplicate, new_img_win.ui.gView, new_img_win)
            else:
                QMessageBox.warning(self, "Duplicate", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_image_rename(self):
        """
        直近のアクティブなImageWindowに属する画像ファイル名を変更する
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                if self.last_active_img_win.filename != "":
                    filename = self.last_active_img_win.filename
                else:
                    filename = "Empty"

                new_filename, ret = QInputDialog.getText(self, "画像ファイル名の変更", "新しいファイル名", QLineEdit.Normal, filename)
                if ret: # bool
                    root, extension = os.path.splitext(new_filename)

                    # 受け入れ可能な拡張子のワイルドカードを作成 r"^\.(png|jpg|jpeg|bmp|)$"
                    match_ext = r"^\.(" + "|".join(accept_imgs) + r")$"

                    # マッチングすれば，SceneのQImageに画像ファイルを格納
                    m = re.match(match_ext, extension, re.IGNORECASE)
                    if m:
                        self.last_active_img_win.set_filename(new_filename)
                    else:
                        QMessageBox.warning(self, "画像ファイル名の変更", "拡張子が無いか無効です.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Rename", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクテイブなImageWindowがNoneです.", QMessageBox.Ok)

    # @Slot()
    def _act_menubar_image_transform(self):
        """
        画像に簡単な幾何学的変換を行う
        ・水平フリップ
        ・垂直フリップ
        ・90度右回転
        ・90度左回転
        ・並進
        ・縮める処理 e.g x方向7ピクセルを1ピクセルにまとめる(この時，average, median, max, min, sumなどを行う)
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                sender = self.sender()
                if sender == self.ui.actionVertical_Flip:
                    process = "Vertical Flip"
                    def v_flip(src:np.ndarray) -> np.ndarray:
                        dst = np.copy(src[::-1]) # Vertical Flip
                        return dst
                    img_proc_func = v_flip

                elif sender == self.ui.actionHorizontal_Flip:
                    process = "Horizontal Flip"
                    def h_flip(src:np.ndarray) -> np.ndarray:
                        dst = src[:, ::-1]  # Horizontal Flip
                        return dst
                    img_proc_func = h_flip

                elif sender == self.ui.actionRotate_90_Degree_Left:
                    process = "Rotate_90_Degree_Left"
                    def rot_90deg_left(src:np.ndarray) -> np.ndarray:
                        dst = ndimage.rotate(src, angle=90, mode='reflect')
                        return dst
                    img_proc_func = rot_90deg_left

                elif sender == self.ui.actionRotate_90_Degree_Right:
                    process = "Rotate_90_Degree_Right"
                    def rot_90deg_right(src:np.ndarray) -> np.ndarray:
                        dst = ndimage.rotate(src, angle=-90, mode='reflect')
                        return dst
                    img_proc_func = rot_90deg_right

                elif sender == self.ui.actionRotate:
                    process = "Rotate"
                    pass
                elif sender == self.ui.actionTranslate:
                    process = "Translate"
                    pass
                elif sender == self.ui.actionBin:
                    process = "Bin"
                    pass

                start = time.perf_counter()
                self._help_apply_qimage(img_proc_func)
                elapsed_time = (time.perf_counter() - start) * 1000

                self.ui.statusBar.clearMessage()
                self.ui.statusBar.showMessage(
                    "{0} response: {1:.3f} [ms]".format(process, elapsed_time))
            else:
                QMessageBox.warning(self, "Transform", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクテイブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_zoom(self):
        """
        ズーム処理
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                pass
                QMessageBox.information(self, "Zoom", "工事中", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Zoom", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクテイブなImageWindowがNoneです.", QMessageBox.Ok)

    # @Slot()
    def _act_menubar_camera(self):
        """
        カメラ専用のVideoWindowを表示する
        :return:
        """
        video_window = None
        sender = self.sender()

        if sender == self.ui.actionUSB_Camera:
            video_window = USBVideoWindow(self)

        elif sender == self.ui.actionIP_Address_Camera:
            pass

        elif sender == self.ui.actionIDS_Camera:
            video_window = IDSVideoWindow(self)

        elif sender == self.ui.actionBASLER_Camera:
            pass

        elif sender == self.ui.actionOMRON_Camera:
            video_window = OMRONVideoWindow(self)

        elif sender == self.ui.actionCOGNEX_Camera:
            pass

        else:
            pass

        if video_window is not None:
            title = video_window.windowTitle()
            win_titles = [win.windowTitle() for win in self.img_wins]
            new_title = new_serial_number_filename(title, win_titles)
            video_window.set_filename(new_title)
            self.img_wins.append(video_window)  # self.img_winsで一括管理
            video_window.show()
            video_window.activateWindow()


    @Slot()
    def _act_menubar_blur(self):
        """
        ブラー処理用のダイアログを開く
        :return: 
        """
        blur_dialog = BlurDialog(self)
        blur_dialog.show()
        blur_dialog.activateWindow()

    @Slot()
    def _act_menubar_shading(self):
        """
        シェーディング補正用のダイアログを開く
        :return:
        """
        shading_dialog = ShadingDialog(self)
        shading_dialog.show()
        shading_dialog.activateWindow()

    @Slot()
    def _act_menubar_unsharp_masking(self):
        """
        先鋭化処理のダイアログを開く
        :return:
        """
        unsharp_masking = UnsharpMaskingDialog(self)
        unsharp_masking.show()
        unsharp_masking.activateWindow()

    @Slot()
    def _act_menubar_edge_detector(self):
        """
        エッジ検出用のダイアログを開く
        :return:
        """
        edge_detector_dialog = EdgeDetectorDialog(self)
        edge_detector_dialog.show()
        edge_detector_dialog.activateWindow()

    @Slot()
    def _act_menubar_mapping(self):
        """
        濃淡変換用のダイアログを開く
        :return:
        """
        # mapping_dialog = MappingDialog(self)
        # mapping_dialog.show()
        # mapping_dialog.activateWindow()
        pass

    @Slot()
    def _act_menubar_binarize(self):
        """
        2値化用のダイアログを開く
        :return:
        """
        binarize_dialog = BinarizeDialog(self)
        binarize_dialog.show()
        binarize_dialog.activateWindow()

    @Slot()
    def _act_menubar_morphology(self):
        """
        モルフォロジー処理を行うダイアログを開く
        :return:
        """
        morphology_dialog = MorphologyDialog(self)
        morphology_dialog.show()
        morphology_dialog.activateWindow()

    @Slot()
    def _act_menubar_noise_denoise(self):
        """
        ノイズ付加/ノイズ除去を行うダイアログを開く
        :return:
        """
        noise_denoise_dialog = NoiseDenoiseDialog(self)
        noise_denoise_dialog.show()
        noise_denoise_dialog.activateWindow()

    @Slot()
    def _act_menubar_histogram(self):
        """
        ヒストグラム処理用のダイアログを開く
        :return:
        """
        histogram_dialog = HistogramDialog(self)
        histogram_dialog.show()
        histogram_dialog.activateWindow()

    @Slot()
    def _act_menubar_labeling(self):
        """
        ラベリング処理用のダイアログを開く
        :return:
        """
        labeling_dialog = LabelingDialog(self)
        labeling_dialog.show()
        labeling_dialog.activateWindow()

    @Slot()
    def _act_menubar_show_histogram(self):
        """
        ヒストグラムの表示
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                roi_rects = self.last_active_img_win.scene.roi_rects()
                if roi_rects:
                    roi_imgs = [qimage2ndarray(qimage.copy(rect_f.toRect())) for _, rect_f in roi_rects]
                    roi_keys = [key for key, _ in roi_rects]
                else:
                    roi_imgs = [qimage2ndarray(qimage)]
                    roi_keys = ['0']

                # ヒストグラムの取得
                hist_features = gen_histogram(roi_imgs)

                # ファイル名の取得
                filename = self.last_active_img_win.get_filename()

                # ヒストグラムと累積ヒストグラムの可視化
                plt.ion() # インタラクティブモードON
                for key, hist_feat_colors in zip(roi_keys, hist_features):
                    if len(hist_feat_colors) > 1:
                        fig = plt.figure(figsize=(12, 4))
                        key_name = f"{filename}_Hist{key}_RGB"
                    else:
                        fig = plt.figure()
                        key_name = f"{filename}_Hist{key}_Gray"

                    self.mpl_figures[key_name] = fig
                    print("self.mpl_figures", self.mpl_figures)

                    # print("self.mpl_figures type: ")
                    # for fig in self.mpl_figures:
                    #     tmp_fig = deepcopy(fig)-
                    #     print("object: {0}".format(str(tmp_fig)))

                    # color
                    colors = ['grey'] if len(hist_feat_colors) == 1 else ['r', 'g', 'b']
                    for c, feature in enumerate(hist_feat_colors):
                        hist = feature.hist
                        bin = feature.bin
                        cdf = feature.cdf
                        normalized_cdf = feature.normalized_cdf

                        # ヒストグラムのx値を求める
                        x_bins = [ (bin[i-1] + bin[i])/2 for i in range(1, len(bin))]

                        # RGB対応
                        if len(hist_feat_colors) > 1:
                            plt.subplot(1, len(hist_feat_colors), c+1)

                        # 描画
                        plt.plot(normalized_cdf, color='k')
                        plt.bar(x_bins, hist, width=1, color=colors[c])
                        plt.xlim([0, 256])
                        plt.legend(("cdf", "hist"), loc="upper left")
                        plt.title("Hist and CDF about {0}".format(colors[c]))
                        plt.draw()

                    # シグナル
                    self.signal_remove_mpl_figures.emit(key_name)

                plt.ioff() # インタラクティブモードOFF

            else:
                QMessageBox.warning(self, "Show Histogram", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)


    @Slot()
    def _act_menubar_surface_plot(self):
        """
        画像の3D描画
        :return:
        """
        if (self.last_active_img_win is not None) and (isinstance(self.last_active_img_win, ImageWindow)):
            qimage = self.last_active_img_win.scene.dib_qimage()
            if not qimage.isNull():
                roi_rects = self.last_active_img_win.scene.roi_rects()
                if roi_rects:
                    roi_imgs = [qimage2ndarray(qimage.copy(rect_f.toRect())) for _, rect_f in roi_rects]
                    roi_keys = [key for key, _ in roi_rects]
                else:
                    roi_imgs = [qimage2ndarray(qimage)]
                    roi_keys = ['0']

                # ファイル名の取得
                filename = self.last_active_img_win.get_filename()

                # 3D表示
                plt.ion()  # インタラクティブモードON
                for key, roi_img in zip(roi_keys, roi_imgs):
                    if roi_img.ndim == 2:
                        fig = plt.figure()
                        key_name = f"{filename}_3DPlot{key}_Gray"
                    else:
                        fig = plt.figure(figsize=(12, 4))
                        key_name = f"{filename}_3DPlot{key}_RGB"

                    self.mpl_figures[key_name] = fig
                    print("self.mpl_figures", self.mpl_figures)

                    # print("self.mpl_figures type: ")
                    # for fig in self.mpl_figures:
                    #     tmp_fig = deepcopy(fig)
                    #     print("object: {0}".format(str(tmp_fig)))

                    # 3Dプロット
                    colors = ['grey'] if roi_img.ndim == 2 else ['r', 'g', 'b']
                    channels = len(colors)
                    if roi_img.ndim == 2:
                        roi_img = roi_img[:, :, np.newaxis]
                    roi_img = np.transpose(roi_img, (2, 0, 1))

                    for c in range(channels):
                        h, w = roi_img[c].shape

                        x = np.arange(0, w)
                        y = -np.arange(0, h)
                        X, Y = np.meshgrid(x, y)

                        # 描画
                        location_num = 100 + channels * 10 + (c+1)
                        ax = fig.add_subplot(location_num, projection="3d")
                        surf = ax.plot_surface(X, Y, roi_img[c], cmap='jet', linewidth=1, zsort='min')
                        plt.colorbar(surf)
                        plt.tight_layout()
                        ax.set_title(f"{key_name}_{colors[c]}")
                        ax.set_zlim([0, 255])
                        plt.draw()

                    # シグナル
                    self.signal_remove_mpl_figures.emit(key_name)

                plt.ioff()  # インタラクティブモードOFF

            else:
                QMessageBox.warning(self, "Surface Plot", "QImageがNullです.", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "ImageWindow", "直近のアクティブなImageWindowがNoneです.", QMessageBox.Ok)

    @Slot()
    def _act_menubar_fft(self):
        """
        FFTダイアログを開く
        :return:
        """
        fft_dialog = FFTDialog(self)
        fft_dialog.show()
        fft_dialog.activateWindow()



    @Slot()
    def _act_menubar_annotation(self):
        """
        アノテーションダイアログを開く
        :return:
        """
        pass


    @Slot()
    def _act_menubar_dataset(self):
        """
        データセットの操作(All-> PureTrain, Validation, test)
        :return:
        """
        dataset_dialog = DatasetDialog(self)
        dataset_dialog.show()
        dataset_dialog.activateWindow()

    @Slot()
    def _act_menubar_dl_classification_image(self):
        """
        dl -> Classification -> Image
        ディープラーニング用ダイアログを開く
        :return:
        """
        dl_classification_image_dialog = DLImageRecognitionDialog(self)
        dl_classification_image_dialog.show()
        dl_classification_image_dialog.activateWindow()