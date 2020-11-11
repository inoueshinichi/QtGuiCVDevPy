"""画像表示用のビュー
"""

# 標準
import os
import sys
import re
import math
import time
import datetime
from typing import Dict, List, Tuple, Union, Any

# サードパーティ
import PySide2
from PySide2.QtCore import (Qt, QRectF, QRect)
from PySide2.QtGui import (QImage, QPainter, QColor, QDrag, QPixmap)
from PySide2.QtWidgets import (QGraphicsView, QWidget, QMessageBox, QApplication)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from module.qt_module.qt_def import *
from module.utils import new_serial_number_filename

# QGraphicsViewの派生クラス
class DrawView(QGraphicsView):
    zoom_level = [1 / 72., 1 / 48., 1 / 32., 1 / 24., 1 / 16., 1 / 12.,
                  1 / 8., 1 / 6., 1 / 4., 1 / 3., 1 / 2., 0.75, 1.,
                  1.5, 2., 3., 4., 6., 8., 12., 16., 24., 32.]


    def __init__(self, parent:QWidget=None):
        super(DrawView, self).__init__(parent)

        # centralWidgetを間に挟んでいるために，二階層上のQWidgetがCImageWindow
        self.img_win = self.parentWidget().parentWidget()

        # ドロップ処理を有効化
        self.setAcceptDrops(True)  # ドロップイベントは親から子へ伝播する。無効化するとMainWindowでドロップ処理をしなければならない。
        self.accept_drag_and_drop = False

        # Setting View
        # self.setAlignment(Qt.AlignLeft | Qt.AlignTop) # 原点を左上にする
        self.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate)  # FullViewportUpdate, SmartViewportUpdate, BoundingRectViewportUpdate
        self.setRenderHint(QPainter.Antialiasing, enabled=False)  # Sceneの画像，図形のアンチエイリアスをOFFにする
        self.setRenderHint(QPainter.TextAntialiasing, enabled=True) # Sceneの文字のアンチエイリアスをONにする
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse) # アフィン変換の原点をマウス直下にする
        self.setBackgroundBrush(QColor(64, 64, 64, 255)) # 背景を灰色にする

        # Transformation between QGraphicsVeiw and QGraphicsScene
        """行優先型Affine変換行列
            [m11, m12, m13],
            [m21, m22, m23],
            [m31, m32, m33]
            並進要素 X方向m31(x), Y方向:m32(y)
            回転・スケール・スキューの合成要素 m11,m12,m21,m22
            m33:1
        """
        # QGraphicsViewクラスが持つ内部変数を使うこと
        # self.transform()

        # Zoom
        self.zoom_level_index = self.zoom_level.index(1.0)
        self.scale_factor = 1.0

    def fit_view(self):
        """
        アスペクト比を保ったまま
        PixmapをViewのビューポートに合わせる
        :return:
        """
        self.fitInView(self.scene().sceneRect(), Qt.KeepAspectRatio)
        self.scale_factor = self.transform().mapRect(QRectF(0, 0, 1, 1)).width()

    def zoom_in(self):
        """
        ズームイン
        :return:
        """
        self._scale_view(zoom_level_shift=1)

    def zoom_out(self):
        """
        ズームアウト
        :return:
        """
        self._scale_view(zoom_level_shift=-1)

    def reset_zoom(self):
        """
        ズームリセット
        :return:
        """
        self.resetMatrix()
        self.zoom_level_index = self.zoom_level.index(1.0)

    def _scale_view(self, zoom_level_shift:int):
        """
        Pixmapの拡大・縮小
        :param zoom_level_shift 拡大+1, 縮小-1
        :return:
        """
        assert zoom_level_shift == 1 or zoom_level_shift == -1, "zoom_level_shift must be +1 or -1."
        new_zoom_level_index = self.zoom_level_index + zoom_level_shift

        if (new_zoom_level_index < 0) or (new_zoom_level_index >= len(self.zoom_level)):
            # Zoom Levelの範囲外の拡大・縮小は禁止
            return

        self.scale_factor = self.zoom_level[new_zoom_level_index]
        self.zoom_level_index = new_zoom_level_index
        self.resetMatrix()
        self.scale(self.scale_factor, self.scale_factor)

        self.img_win.ui.lbl_Image_Scale.setText(str(100 * self.zoom_level[self.zoom_level_index]) + "%")

    # override
    def wheelEvent(self, event: PySide2.QtGui.QWheelEvent):
        """
        マウスホイールイベント
        :param event:
        :return:
        """
        degree = event.angleDelta().y() / 8  # マウスホイールは15度進む度に120単位で進むので，実際の角度は8で割った値

        if event.modifiers() == Qt.ControlModifier:
            # ズーム処理

            # ズーム中心をマウス位置に指定
            self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)

            sign = degree > 0
            if sign:
                self._scale_view(zoom_level_shift=1)
            else:
                self._scale_view(zoom_level_shift=-1)

        elif event.modifiers() == Qt.ShiftModifier:
            # 水平方向にスクロールバーを動かす
            h_scrl = self.horizontalScrollBar()
            h_scrl_value = h_scrl.value()
            if h_scrl_value < h_scrl.minimum() or h_scrl_value > h_scrl.maximum():
                return
            else:
                h_scrl.setValue(h_scrl_value - degree)
        else:
            # 垂直方向にスクロールバーを動かす
            v_scrl = self.verticalScrollBar()
            v_scrl_value = v_scrl.value()
            if v_scrl_value < v_scrl.minimum() or v_scrl_value > v_scrl.maximum():
                return
            else:
                v_scrl.setValue(v_scrl_value - degree)



    # override
    def dropEvent(self, event: PySide2.QtGui.QDropEvent):
        """
        ドロップイベント
        :param event:
        :return:
        """
        urls = event.mimeData().urls()
        if len(urls) == 0:
            return

        """画像を取得する"""
        if len(urls) == 1:
            url = urls[-1]

            # ファイルパスの取得
            file_path = str(url.toLocalFile())
            root, extention = os.path.splitext(file_path)

            # 受け入れ可能な拡張子のワイルドカードを作成 r"^\.(png|jpg|jpeg|bmp|)$"
            match_ext = r"^\.(" + "|".join(accept_imgs) + r")$"

            # マッチングすれば，SceneのQImageに画像ファイルを格納
            if re.match(match_ext, extention, re.IGNORECASE):
                if os.path.isfile(file_path):
                    filename = file_path.split('/')[-1]

                    # ファイル名の更新または新規作成
                    new_filename = filename
                    if self.img_win.filename is not None:
                        name, ext = filename.split('.')
                        pattern = r"^({0}|{0}-[0-9]+)\.{1}$".format(name, ext)
                        m = re.match(pattern, self.img_win.filename)
                        if m:
                            pass # 名前を変えない
                        else:
                            stored_filenames = [img_win.filename for img_win in self.img_win.parentWidget().img_wins]
                            new_filename = new_serial_number_filename(filename, stored_filenames)
                    else:
                        new_filename = filename

                    self.img_win.set_filename(new_filename)

                    # QImage
                    droped_qimage = QImage(file_path)
                    depth = droped_qimage.bitPlaneCount()
                    is_grayscale = droped_qimage.allGray()
                    if is_grayscale and depth == 8:
                        droped_qimage = droped_qimage.convertToFormat(QImage.Format_Grayscale8)
                    else:
                        droped_qimage = droped_qimage.convertToFormat(QImage.Format_RGB888)

                    # 画像をSceneに登録
                    self.scene().clear()
                    self.scene().set_qimage_on_screen(droped_qimage, is_raw=True)
                    self.scene().update()

                    # 画像サイズに合わせてウィンドウサイズを変更
                    adjust_viewport(droped_qimage, self, self.img_win)

            else:
                # ファイル拡張子が不適切な場合
                valid_ext = ",".join(accept_imgs)
                valid_ext.strip(',')
                QMessageBox.warning(self,
                                    "Invalid Image",
                                    "画像ファイルの拡張子が不適切です。\n有効拡張子: {0}".format(valid_ext),
                                    QMessageBox.Ok)

        # ビューのDrag&Dropの受け入れモードを解除
        self.accept_drag_and_drop = False

        super(DrawView, self).dropEvent(event) # SceneにDropイベントを伝播させるために必要

    # override
    def dragEnterEvent(self, event:PySide2.QtGui.QDragEnterEvent):
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
            self.accept_drag_and_drop = True

        super(DrawView, self).dragEnterEvent(event) # SceneにDragEnterイベントを伝搬するために必要

    # override
    def dragMoveEvent(self, event:PySide2.QtGui.QDragMoveEvent):
        """
               ドラッグムーブイベント
               :param event:
               :return:
               """
        """
        QGraphicsView が QGraphicsScene を含む場合は、dragMoveEvent()でacceptが上書きされるので、
        基底のdragMoveEvent()を呼び出した後に、再度acceptを行う
        """
        super(DrawView, self).dragMoveEvent(event)  # SceneにDragMoveイベントを伝搬するために必要

        if self.accept_drag_and_drop:
            event.accept()

    # override
    def dragLeaveEvent(self, event: PySide2.QtGui.QDragLeaveEvent):
        """
        ドラッグリーブイベント
        :param event:
        :return:
        """

        """
        QGraphicsView が QGraphicsScene を含む場合は、dragLeaveEvent()でacceptが上書きされるので、
        基底のdragLeaveEvent()を呼び出した後に、再度acceptを行う"""
        super(DrawView, self).dragLeaveEvent(event)  # SceneにDragLeaveイベントを伝搬するために必要

        if self.accept_drag_and_drop:
            event.accept()

    # override
    def mouseMoveEvent(self, event:PySide2.QtGui.QMouseEvent):
        """
        マウスムーブイベント
        :param event:
        :return:
        """
        view_pos = event.pos()

        # ドラッグ開始を検出
        if event.button() == Qt.LeftButton:
            distance = (view_pos - self.pressMousePos).manhattanLength()  # マンハッタン距離

            # Qtアプリの推奨距離(4pxl)以上であればドラッグ開始時の処理を起動
            if distance >= QApplication.startDragDistance():
                self._startDrag(Qt.MoveAction, event)

        self.parentWidget().parentWidget().ui.statusbar.showMessage("viewport ({0:4d},{1:4d})".format(view_pos.x(), view_pos.y()))

        super(DrawView, self).mouseMoveEvent(event)  # SceneにMouseMoveイベントを伝搬させるために必要

    def _startDrag(self, action:Qt.DropActions, event:PySide2.QtGui.QMouseEvent):
        """
        ドラッグ開始時の処理
        :return:
        """
        # ドラッグした画像をマウスカーソル付近に表示
        for url in event.mimeData().urls():
            file_path = str(url.toLocalFile)
            root, extention = os.path.splitext(file_path)

            # 受け入れ可能な拡張子のワイルドカードを作成 r"^\.(png|jpg|jpeg|bmp|)$"
            match_ext = r"^\.(" + "|".join(accept_imgs) + r")$"

            # マッチングすれば、QImageに画像ファイルのデータを格納してDragIconを表示
            if re.match(match_ext, extention, re.IGNORECASE):
                if os.path.isfile(file_path):
                    drag = QDrag(self)
                    drag.setPixmap(QPixmap(file_path))
                    if drag.exec_(supportedActions=action) == Qt.MoveAction:
                        pass  # dragのイベントループ終了時の処理

    # override
    def mousePressEvent(self, event:PySide2.QtGui.QMouseEvent):
        """
        マウスプレスイベント
        :param event:
        :return:
        """
        view_pos = event.pos()
        self.parentWidget().parentWidget().ui.statusbar.showMessage(str(view_pos))

        super(DrawView, self).mousePressEvent(event)