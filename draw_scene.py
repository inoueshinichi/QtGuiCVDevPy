"""画像表示用シーン
"""

# 標準
import os
import sys
from typing import (
    Dict,
    List,
    Tuple,
    Union,
    Any,
    Callable,
    TypeVar,
    NoReturn
)

# サードパーティ
from numba import jit
import PySide2
from PySide2.QtCore import (
    Qt,
    QPointF,
    qDebug,
    QRectF,
    QLineF,
    QObject
)
from PySide2.QtGui import (
    QImage,
    QPixmap,
    QBitmap,
    QPen,
    QBrush,
    QFont,
    qGray,
    QPainterPath,
    QColor,
    QPainter
)
from PySide2.QtWidgets import (
    QGraphicsScene,
    QGraphicsPixmapItem,
    QGraphicsPathItem,
    QLabel,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QGraphicsSimpleTextItem
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from module.qt_module.qt_def import (
    status_qimage,
    qimage2ndarray,
    ndarray2qimage,
    create_mask_qimage,
    retrieve_mask_ndarray
)
from rect_graphics_item import RectGraphicsItem
from ellipse_graphics_item import EllipseGraphicsItem
from line_graphics_item import LineGraphicsItem

# QGraphicsSceneの派生クラス
class DrawScene(QGraphicsScene):

    def __init__(self, parent:QObject=None):
        super(DrawScene, self).__init__(parent)

        # 画像データ
        self.raw_dib_qimage = QImage()
        self.source_dib_qimage = QImage()
        self.off_screen_ddb_qpixmap = QPixmap()
        self.item_qpixmap = QGraphicsPixmapItem()
        self.item_qpixmap_local_pos = QPointF(0, 0)

        # マスキング
        self.mask_qimage = QImage()
        self.mask_qpixmap = QPixmap()
        self.item_mask_qpixmap = QGraphicsPixmapItem()

        # テキスト
        self.item_texts = {}

        # マウス
        self.scene_mouse_pos = QPointF(0, 0) # スクロールバーの移動量が考慮されている
        self.is_mouse_downs = {'LB': False, 'RB': False, 'MB': False}

        # Cross Line
        self.is_mouse_cross_line = False
        self.mouse_cross_path = {'x': QPainterPath(), 'y': QPainterPath()}
        self.item_mouse_cross_path = {'x': None, 'y': None}
        self.is_mouse_cross_item = {'x': False, 'y': False}

        # Profile
        self.is_draw_profile = False
        self.item_x_profile_path = {'red': None, 'green': None, 'blue': None}
        self.item_y_profile_path = {'red': None, 'green': None, 'blue': None}
        self.x_profile_path = {'red': QPainterPath(), 'green': QPainterPath(), 'blue': QPainterPath()}
        self.y_profile_path = {'red': QPainterPath(), 'green': QPainterPath(), 'blue': QPainterPath()}
        self.is_x_profile_path_item_on_scene = {'red': False, 'green': False, 'blue': False}
        self.is_y_profile_path_item_on_scene = {'red': False, 'green': False, 'blue': False}

        # ROI(矩形領域)
        self.figure_dict_roi = {
            'is_draw': False,
            'is_gen': False,
            'item': {},
            'rect': QRectF(0, 0, 0, 0),
            'anchor': QPointF(0, 0),
            'klass': RectGraphicsItem,
            'color': Qt.red
        }

        # Line(直線)
        self.figure_dict_line = {
            'is_draw': False,
            'is_gen': False,
            'item': {},
            'rect': QRectF(0, 0, 0, 0),
            'anchor': QPointF(0, 0),
            'klass': LineGraphicsItem,
            'color': Qt.yellow
        }

        # Ellipse(楕円領域)
        self.figure_dict_ellipse = {
            'is_draw': False,
            'is_gen': False,
            'item': {},
            'rect': QRectF(0, 0, 0, 0),
            'anchor': QPointF(0, 0),
            'klass': EllipseGraphicsItem,
            'color': Qt.cyan
        }

    # override
    def mouseMoveEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウス移動イベント
        :param event:
        :return:
        """
        scene_pos = event.scenePos()
        self._set_dib_qImage_to_statusbar(scene_pos)

        if self.is_mouse_downs['LB']:
            # Ctrlが押されているか
            is_ctrl = True if event.modifiers() & Qt.ControlModifier else False
            # Shiftが押されているか
            is_shift = True if event.modifiers() & Qt.ShiftModifier else False

            # roi
            if self.figure_dict_roi['is_draw']:
                self._draw_roi(scene_pos,
                               is_mouse_btn_down=True,
                               is_mouse_move=True,
                               is_center_drag=is_ctrl,
                               is_square=is_shift)

            # line
            if self.figure_dict_line['is_draw']:
                self._draw_line(scene_pos,
                                is_mouse_btn_down=True,
                                is_mouse_move=True,
                                is_center_drag=is_ctrl,
                                is_square=is_shift)

            # ellipse
            if self.figure_dict_ellipse['is_draw']:
                self._draw_ellipse(scene_pos,
                                   is_mouse_btn_down=True,
                                   is_mouse_move=True,
                                   is_center_drag=is_ctrl,
                                   is_square=is_shift)


        elif self.is_mouse_downs['RB']:
            # cross line
            self._draw_mouse_cross_line(scene_pos, show=self.is_mouse_cross_line)
            # profile
            self._draw_profiles(scene_pos, show=self.is_draw_profile)


        elif self.is_mouse_downs['MB']:
            pass

        else:
            pass

        # Sceneの描画命令
        self.update()

        super(DrawScene, self).mouseMoveEvent(event)

    # override
    def mousePressEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスプレスイベント
        :param event:
        :return:
        """
        # マウス座標
        scene_pos = event.scenePos()

        # status bar
        self._set_dib_qImage_to_statusbar(scene_pos)

        if event.button() == Qt.MouseButton().LeftButton:
            self.is_mouse_downs['LB'] = True
            # Ctrlが押されているか
            is_ctrl = True if event.modifiers() & Qt.ControlModifier else False
            # Shiftが押されているか
            is_shift = True if event.modifiers() & Qt.ShiftModifier else False

            # roi
            if self.figure_dict_roi['is_draw']:
                self._draw_roi(scene_pos,
                               is_mouse_btn_down=True,
                               is_mouse_move=False,
                               is_center_drag=is_ctrl,
                               is_square=is_shift)

            # line
            if self.figure_dict_line['is_draw']:
                self._draw_line(scene_pos,
                               is_mouse_btn_down=True,
                               is_mouse_move=False,
                               is_center_drag=is_ctrl,
                               is_square=is_shift)

            # ellipse
            if self.figure_dict_ellipse['is_draw']:
                self._draw_ellipse(scene_pos,
                                   is_mouse_btn_down=True,
                                   is_mouse_move=False,
                                   is_center_drag=is_ctrl,
                                   is_square=is_shift)


        elif event.button() == Qt.MouseButton().RightButton:
            self.is_mouse_downs['RB'] = True
            # cross line
            self._draw_mouse_cross_line(scene_pos, show=self.is_mouse_cross_line)

            # profile
            self._draw_profiles(scene_pos, show=self.is_draw_profile)

        elif event.button() == Qt.MouseButton().MiddleButton:
            self.is_mouse_downs['MB'] = True

        else:
            print("Pressed Unknown Mouse Button.")

        # Sceneの描画命令
        self.update()

        super(DrawScene, self).mousePressEvent(event)

    # override
    def mouseReleaseEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスリリースイベント
        :param event:
        :return:
        """
        # マウス座標
        scene_pos = event.scenePos()

        # status bar
        self._set_dib_qImage_to_statusbar(scene_pos)

        if event.button() == Qt.MouseButton().LeftButton:
            self.is_mouse_downs['LB'] = False
            # Ctrlが押されているか
            is_ctrl = True if event.modifiers() & Qt.ControlModifier else False
            # Shiftが押されているか
            is_shift = True if event.modifiers() & Qt.ShiftModifier else False

            # roi
            if self.figure_dict_roi['is_draw']:
                self._draw_roi(scene_pos,
                               is_mouse_btn_down=False,
                               is_mouse_move=False,
                               is_center_drag=is_ctrl,
                               is_square=is_shift)

            # line
            if self.figure_dict_line['is_draw']:
                self._draw_line(scene_pos,
                               is_mouse_btn_down=False,
                               is_mouse_move=False,
                               is_center_drag=is_ctrl,
                               is_square=is_shift)

            # ellipse
            if self.figure_dict_ellipse['is_draw']:
                self._draw_ellipse(scene_pos,
                                   is_mouse_btn_down=False,
                                   is_mouse_move=False,
                                   is_center_drag=is_ctrl,
                                   is_square=is_shift)

        elif event.button() == Qt.MouseButton().RightButton:
            self.is_mouse_downs["RB"] = False

        elif event.button() == Qt.MouseButton().MiddleButton:
            self.is_mouse_downs["MB"] = False

        else:
            print("Released Unknown Mouse Button.")

        # Sceneの描画命令
        self.update()

        super(DrawScene, self).mousePressEvent(event)

    def mouseDoubleClickEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスのダブルクリックイベント
        :param event:
        :return:
        """
        if event.button() == Qt.MouseButton().LeftButton:
            pass

        super(DrawScene, self).mouseDoubleClickEvent(event)


    def set_mask(self, mask_qimage:QImage):
        """
        マスク画像をセット
        :param qimage: QImage Format_Grayscale8
        :return:
        """
        assert mask_qimage.format() == QImage.Format_ARGB32, "Format of Qimage must be Format_ARGB32."

        if not self.source_dib_qimage.isNull():
            rect_source_dib = self.source_dib_qimage.rect()
            rect_mask = self.mask_qimage.rect()
            rect_intersect = rect_source_dib.intersected(rect_mask)
            self.mask_qimage = mask_qimage.copy(rect_intersect)

    def get_mask(self) -> QImage:
        """
        マスク画像を取得
        :return:
        """
        return self.mask_qimage

    def clear_mask(self):
        """
        マスク画像を削除
        :return:
        """
        self.mask_qimage = QImage()
        self.is_mask = False

    def reset_qimage(self):
        """
        原画像に戻す
        :return:
        """
        if not self.raw_dib_qimage.isNull():
            self.set_qimage_on_screen(self.raw_dib_qimage)
            self.update()

    def roi_rects(self) -> List[Tuple[str, QRectF]]:
        """
        ROIを取得
        :return: str:　キー文字列, QRectF: 矩形
        """
        rect_list = []
        if self.figure_dict_roi['item']:
            rect_list = [(key, value.rect()) for key, value in self.figure_dict_roi['item'].items()]
        return rect_list

    def roi_qimages(self) -> Dict[str, QImage]:
        """
        ROIの画像を取得(copy)
        :return:
        """
        roi_imgs = {}
        if self.figure_dict_roi['item']:
            for key, value in self.figure_dict_roi['item'].items():
                rect_f = value.rect() # QRectF
                roi_imgs[key] = self.source_dib_qimage.copy(rect_f.toRect())
        return roi_imgs

    def line_lines(self) -> List[Tuple[str, QLineF]]:
        """
        直線の両端座標を取得
        :return: str: キー文字列, QRectF
        """
        line_list = []
        if self.figure_dict_line['item']:
            line_list = [(key, value.line()) for key, value in self.figure_dict_line['item'].items()]
        return line_list

    def line_pixels(self) -> Dict[str, List[int]]:
        """
        直線が乗っかっている画素の画素値のリストを取得
        ※直線のラスタライズ定義によって変わるので，どうするか考える 2020/09/11 Shinichi Inoue
        :return:
        """
        pass

    def ellipse_rects(self) -> List[Tuple[str, QRectF]]:
        """
        楕円の特徴データを取得
        :return: str: キー文字列, QRectF: 楕円に接する矩形
        """
        ellipse_list = []
        if self.figure_dict_ellipse['item']:
            ellipse_list = [(key, value.rect()) for key, value in self.figure_dict_ellipse['item'].items()]
        return ellipse_list

    def ellipse_qimages(self, inner:bool=True) -> Dict[str, QImage]:
        """
        楕円の領域内/領域外の画像を取得
        :return:
        """
        ellipse_imgs = {}
        if self.figure_dict_ellipse['item']:
            for key, value in self.figure_dict_ellipse['item'].items():
                rect_f = value.rect() # QRectF
                width = rect_f.toRect().width()
                height = rect_f.toRect().height()
                img = self.source_dib_qimage.copy(rect_f.toRect())

                if inner:
                    for y in range(height):
                        for x in range(width):
                            offset_x = rect_f.x() + x # float
                            offset_y = rect_f.y() + y # float
                            if value.contains(QPointF(offset_x, offset_y)):
                                pass
                            else:
                                if img.depth() == 8:
                                    img.setPixel(x, y, 0)
                                else:
                                    img.setPixelColor(x, y, QColor(0, 0, 0))
                else:
                    for y in range(height):
                        for x in range(width):
                            offset_x = rect_f.x() + x  # float
                            offset_y = rect_f.y() + y  # float
                            if value.contains(QPointF(offset_x, offset_y)):
                                if img.depth() == 8:
                                    img.setPixel(x, y, 0)
                                else:
                                    img.setPixelColor(x, y, QColor(0, 0, 0))
                            else:
                                pass
                # 格納
                ellipse_imgs[key] = img
        return ellipse_imgs

    def dib_qimage(self) -> QImage:
        """
        source_dib_qimageを取得
        :return:
        """
        return self.source_dib_qimage

    def set_qimage_on_screen(self, qimage:QImage, is_raw:bool=False) -> bool:
        """
        SceneへQImageとQPixmapを登録する
        :param qimage:
        :param is_raw:
        :return:
        """
        if qimage.isNull():
            return False
        else:
            # QImage
            self.source_dib_qimage = qimage

            if is_raw:
                self.raw_dib_qimage = self.source_dib_qimage.copy()

            # ディスプレイに表示するQImageはARGB32(0xffRRGGBB)フォーマットで統一
            # format_rgb32_qimage = qimage.convertToFormat(QImage.Format_RGB32)

            # QPixmap for image
            self.off_screen_ddb_qpixmap = QPixmap.fromImage(self.source_dib_qimage)#(format_rgb32_qimage)

            # QGraphicsPixmapの生成or更新 for image
            if self.item_qpixmap not in self.items():
                self.item_qpixmap = QGraphicsPixmapItem(self.off_screen_ddb_qpixmap)
                self.addItem(self.item_qpixmap)
            else:
                self.item_qpixmap.setPixmap(self.off_screen_ddb_qpixmap)

        self.setSceneRect(self.off_screen_ddb_qpixmap.rect())
        scene_rect = self.sceneRect().toRect()
        x, y = scene_rect.x(), scene_rect.y()
        width, height = scene_rect.width(), scene_rect.height()
        self.parent().permanent_status.setText("SceneRect ({0:4d},{1:4d},{2:4d},{3:4d})".format(x, y, width, height))

        status = status_qimage(self.source_dib_qimage)
        self.parent().ui.lEdit_Image_Status.setText("{0}x{1} pixels; {2}-bit; {3}[bytes] {4}".format(
            status['width'], status['height'], status['bitPlaneCount'], status['dataSize'], status['format']))

        return True

    def _set_dib_qImage_to_statusbar(self, scene_pos:QPointF):
        """
        ステータスバーにマウス位置の画像情報を表示
        :param scene_pos:
        :return:
        """
        for view in self.views():
            if view.isActiveWindow():
                item = self.itemAt(scene_pos, view.transform())
                if item is not None:

                    # シーンの最下層のQGraphicsPixmapItemを取得
                    # QGraphicsPixmapItemの上位レイヤーのitemは最終的にQGraphicsPixmapItemを親とする
                    while item.parentItem() is not None:
                        item = item.parentItem()

                    # QGraphicsPixmapItem
                    if item is self.item_qpixmap:
                        view_pos = view.mapFromScene(scene_pos)
                        v_scrl = view.verticalScrollBar()
                        h_scrl = view.horizontalScrollBar()
                        x_scrl_value = h_scrl.value()
                        y_scrl_value = v_scrl.value()

                        """スクロールバーの戻り値value()がnegativeを示す場合があるので、強制的に0にする。
                            バグ? by shinichi inoue 20.03.12
                        """
                        if x_scrl_value < 0:
                            print("x_scrl_value: {0:d} < 0".format(x_scrl_value))
                            print("Force to zero the negative x_scrl_value")
                            x_scrl_value = 0
                        if y_scrl_value < 0:
                            print("y_scrl_value: {0:d} < 0".format(y_scrl_value))
                            print("Force to zero the negative y_scrl_value")
                            y_scrl_value = 0

                        # QGraphicsPixmapItemのローカル座標
                        local_qpixmap_item_pos = item.mapToItem(item, scene_pos)
                        qpixmap_rect = self.off_screen_ddb_qpixmap.rect()
                        qimage_pos = local_qpixmap_item_pos.toPoint()

                        if qpixmap_rect.contains(local_qpixmap_item_pos.toPoint()):
                            if self.source_dib_qimage.allGray():
                                """Grayscale
                                """
                                gray = qGray(self.source_dib_qimage.pixel(qimage_pos))
                                luminance = "-> Gray({0:3d},{1:3d},{2:3d})".format(gray, gray, gray)
                            else:
                                """Color(RGB)
                                """
                                pxlCol = self.source_dib_qimage.pixelColor(qimage_pos)
                                luminance = "-> RGB({0:3d},{1:3d},{2:3d})".format(int(pxlCol.red()),
                                                                               int(pxlCol.green()),
                                                                               int(pxlCol.blue()))
                            position = "pixmap({0:4.2f},{1:4.2f}) " \
                                       "scene({2:4.2f},{3:4.2f}) " \
                                       "scroll({4:4d},{5:4d}) " \
                                       "viewport({6:4d},{7:4d})".format(
                                local_qpixmap_item_pos.x(),
                                local_qpixmap_item_pos.y(),
                                scene_pos.x(),
                                scene_pos.y(),
                                x_scrl_value,
                                y_scrl_value,
                                view_pos.x(),
                                view_pos.y())
                            statusBarMsg = "".join([position, luminance])

                        else:
                            statusBarMsg = "pixmap({0:4.2f},{1:4.2f}) is out of range about self.sourceDIBImage." \
                                           " scene({2:4.2f},{3:4.2f}) scroll({4:4d},{5:4d}) " \
                                           "viewport({6:4d},{7:4d})".format(
                                local_qpixmap_item_pos.x(),
                                local_qpixmap_item_pos.y(),
                                scene_pos.x(),
                                scene_pos.y(),
                                x_scrl_value,
                                y_scrl_value,
                                view_pos.x(),
                                view_pos.y())
                    else:
                        statusBarMsg = "self.sourceDIBImage is empty."

                    # ステータスバーに画像情報を表示
                    view.parentWidget().parentWidget().ui.statusbar.showMessage(statusBarMsg)

    def toggle_cross_line(self, show:bool):
        """
        マウスのクロスラインの表示切り替え
        :param show:
        :return:
        """
        if show:
            self.is_mouse_cross_line = True
        else:
            self.is_mouse_cross_line = False
            for key in self.item_mouse_cross_path.keys():
                if self.item_mouse_cross_path[key] in self.items():
                    self.removeItem(self.item_mouse_cross_path[key])
            self.update()

    #@jit(nopython=False)
    def _draw_mouse_cross_line(self, scene_pos:QPointF, show:bool):
        """
        マウスクロスラインの表示処理
        :param scene_pos:
        :param show:
        :return:
        """
        for view in self.views():
            if view.isActiveWindow():
                item = self.itemAt(scene_pos, view.transform())
                if item is not None:
                    # シーンの最下層のQGraphicsPixmapItemを取得
                    # QGraphicsPixmapItemの上位レイヤーのitemは最終的にQGraphicsPixmapItemを親とする
                    while item.parentItem() is not None:
                        item = item.parentItem()

                    # QGraphicsPixmapItem
                    if item is self.item_qpixmap and show:
                        view_pos = view.mapFromScene(scene_pos)
                        v_scrl = view.verticalScrollBar()
                        h_scrl = view.horizontalScrollBar()
                        x_scrl_value = h_scrl.value()
                        y_scrl_value = v_scrl.value()

                        """スクロールバーの戻り値value()がnegativeを示す場合があるので、強制的に0にする。
                            バグ? by shinichi inoue 20.03.12
                        """
                        if x_scrl_value < 0:
                            print("x_scrl_value: {0:d} < 0".format(x_scrl_value))
                            print("Force to zero the negative y_scrl_value")
                            x_scrl_value = 0
                        if y_scrl_value < 0:
                            print("y_scrl_value: {0:d} < 0".format(y_scrl_value))
                            print("Force to zero the negative y_scrl_value")
                            y_scrl_value = 0

                        # QGraphicsPixmapItemのローカル座標
                        local_qpixmap_item_pos = item.mapToItem(item, scene_pos)
                        qpixmap_rect = self.off_screen_ddb_qpixmap.rect()

                        if qpixmap_rect.contains(local_qpixmap_item_pos.toPoint()):
                            for key in self.mouse_cross_path.keys():
                                # PainterPath
                                if key == 'x':
                                    self.mouse_cross_path[key].clear()
                                    # self.mouse_cross_path[key].moveTo(0 + x_scrl_value, local_qpixmap_item_pos.y())
                                    # self.mouse_cross_path[key].lineTo(view.width() + x_scrl_value, local_qpixmap_item_pos.y())
                                    self.mouse_cross_path[key].moveTo(0, local_qpixmap_item_pos.y())
                                    self.mouse_cross_path[key].lineTo(self.item_qpixmap.boundingRect().width(), local_qpixmap_item_pos.y())
                                else:
                                    self.mouse_cross_path[key].clear()
                                    # self.mouse_cross_path[key].moveTo(localItemPos.x(), 0 + yScrlValue)
                                    # self.mouse_cross_path[key].lineTo(localItemPos.x(), view.height() + yScrlValue)
                                    self.mouse_cross_path[key].moveTo(local_qpixmap_item_pos.x(), 0)
                                    self.mouse_cross_path[key].lineTo(local_qpixmap_item_pos.x(), self.item_qpixmap.boundingRect().height())

                                # PainterPathItem
                                if self.item_mouse_cross_path[key] in self.items():
                                    # self.item_mouse_cross_path[key]がSceneに登録されている場合の処理
                                    self.item_mouse_cross_path[key].setPath(self.mouse_cross_path[key])
                                else:
                                    print("self.item_mouse_cross_path[{0}] was created !".format(key))
                                    self.item_mouse_cross_path[key] = QGraphicsPathItem(self.item_qpixmap)
                                    self.item_mouse_cross_path[key].setPen(QPen(Qt.green, 1))
                                    self.item_mouse_cross_path[key].setBrush(QBrush(Qt.NoBrush))
                                    self.item_mouse_cross_path[key].setPath(self.mouse_cross_path[key])

    def toggle_profile(self, show:bool):
        """
        プロファイルの表示切り替え
        :param show:
        :return:
        """
        if show:
            self.is_draw_profile = True
        else:
            self.is_draw_profile = False
            for key in self.item_x_profile_path.keys():
                if self.item_x_profile_path[key] in self.items():
                    self.removeItem(self.item_x_profile_path[key])
                if self.item_y_profile_path[key] in self.items():
                    self.removeItem(self.item_y_profile_path[key])
            self.update()

    # @jit(nopython=False)
    def _draw_profiles(self, scene_pos:QPointF, show:bool):
        """
        プロファイルの表示
        :param scene_pos:
        :param show:
        :return:
        """
        for view in self.views():
            if view.isActiveWindow():
                item = self.itemAt(scene_pos, view.transform())
                if item is not None:
                    # シーンの最下層のQGraphicsPixmapItemを取得
                    # QGraphicsPixmapItemの上位レイヤーのitemは最終的にQGraphicsPixmapItemを親とする
                    while item.parentItem() is not None:
                        item = item.parentItem()

                    # QGraphicsPixmapItem
                    if item is self.item_qpixmap and show:
                        view_pos = view.mapFromScene(scene_pos)
                        v_scrl = view.verticalScrollBar()
                        h_scrl = view.horizontalScrollBar()
                        x_scrl_value = h_scrl.value()
                        y_scrl_value = v_scrl.value()
                        view_width = int(view.width())  # スケール対応
                        view_height = int(view.height())
                        view_hScrl_height = int(h_scrl.height())
                        view_vScrl_width = int(v_scrl.width())
                        view_x_scrl_value = int(x_scrl_value)
                        view_y_scrl_value = int(y_scrl_value)
                        viewport_width = view.viewport().width()
                        viewport_height = view.viewport().height()

                        """スクロールバーの戻り値value()がnegativeを示す場合があるので、強制的に0にする。
                            バグ? by shinichi inoue 20.03.12
                        """
                        if x_scrl_value < 0:
                            print("x_scrl_value: {0:d} < 0".format(x_scrl_value))
                            print("Force to zero the negative y_scrl_value")
                            x_scrl_value = 0
                        if y_scrl_value < 0:
                            print("y_scrl_value: {0:d} < 0".format(y_scrl_value))
                            print("Force to zero the negative y_scrl_value")
                            y_scrl_value = 0

                        # 座標・サイズ
                        local_qpixmap_item_pos = item.mapToItem(item, scene_pos)
                        qpixmap_rect = self.off_screen_ddb_qpixmap.rect()
                        img_width = self.item_qpixmap.boundingRect().width()
                        img_height = self.item_qpixmap.boundingRect().height()
                        view_anchor = view.mapFromScene(0.0, 0.0)
                        profile_y = local_qpixmap_item_pos.toPoint().y()
                        profile_x = local_qpixmap_item_pos.toPoint().x()

                        if qpixmap_rect.contains(local_qpixmap_item_pos.toPoint()):
                            # PainterPathのにデータを格納
                            if self.source_dib_qimage.allGray():
                                """Grayscale"""
                                # x-Line
                                self.x_profile_path["green"].clear()
                                for x in range(0, int(img_width) - 1):
                                    x_gray = self.source_dib_qimage.pixelColor(x, profile_y).green()
                                    x_next_gray = self.source_dib_qimage.pixelColor(x + 1, profile_y).green()
                                    self.x_profile_path['green'].moveTo(x, viewport_height - x_gray - view_anchor.y())
                                    self.x_profile_path['green'].lineTo(x + 1, viewport_height - x_next_gray - view_anchor.y())

                                # y-Line
                                self.y_profile_path['green'].clear()
                                for y in range(0, int(img_height) - 1):
                                    y_gray = self.source_dib_qimage.pixelColor(profile_x, y).green()
                                    y_next_gray = self.source_dib_qimage.pixelColor(profile_x, y + 1).green()
                                    self.y_profile_path['green'].moveTo(viewport_width - y_gray - view_anchor.x(), y)
                                    self.y_profile_path['green'].lineTo(viewport_width - y_next_gray - view_anchor.x(), y + 1)

                                # PainterPathItem
                                # X-Line
                                if self.item_x_profile_path['green'] in self.items():
                                    # self.item_x_profile_path["green"]がSceneに登録されている場合の処理
                                    self.item_x_profile_path['green'].setPath(self.x_profile_path['green'])
                                else:
                                    print("self.item_x_profile_path['green'] was created !")
                                    self.item_x_profile_path['green'] = QGraphicsPathItem(self.item_qpixmap)
                                    self.item_x_profile_path['green'].setPen(QPen(Qt.magenta, 1))
                                    self.item_x_profile_path['green'].setBrush(QBrush(Qt.NoBrush))
                                    self.item_x_profile_path['green'].setPath(self.x_profile_path['green'])

                                # y-LIne
                                if self.item_y_profile_path['green'] in self.items():
                                    # self.item_y_profile_path['green']がSceneに登録されている場合の処理
                                    self.item_y_profile_path['green'].setPath(self.y_profile_path['green'])
                                else:
                                    print("self.item_y_profile_path['green'] is craeted !")
                                    self.item_y_profile_path['green'] = QGraphicsPathItem(self.item_qpixmap)
                                    self.item_y_profile_path['green'].setPen(QPen(Qt.cyan, 1))
                                    self.item_y_profile_path['green'].setBrush(QBrush(Qt.NoBrush))
                            else:
                                """Color(RGB)"""
                                # X-Line
                                self.x_profile_path['red'].clear()
                                self.x_profile_path['green'].clear()
                                self.x_profile_path['blue'].clear()
                                for x in range(0, int(img_width) - 1):
                                    pixel = self.source_dib_qimage.pixelColor(x, profile_y)
                                    x_red, x_green, x_blue = pixel.red(), pixel.green(), pixel.blue()
                                    next_pixel = self.source_dib_qimage.pixelColor(x + 1, profile_y)
                                    x_next_red, x_next_green, x_next_blue = next_pixel.red(), next_pixel.green(), next_pixel.blue()
                                    x_lum_pairs = [(x_red, x_next_red), (x_green, x_next_green), (x_blue, x_next_blue)]
                                    for key, lum_pair in zip(self.x_profile_path.keys(), x_lum_pairs):
                                        self.x_profile_path[key].moveTo(x, viewport_height - lum_pair[0] - view_anchor.y())
                                        self.x_profile_path[key].lineTo(x + 1, viewport_height - lum_pair[1] - view_anchor.y())

                                # Y-Line
                                self.y_profile_path['red'].clear()
                                self.y_profile_path['green'].clear()
                                self.y_profile_path['blue'].clear()
                                for y in range(0, int(img_height) - 1):
                                    pixel = self.source_dib_qimage.pixelColor(profile_x, y)
                                    y_red, y_green, y_blue = pixel.red(), pixel.green(), pixel.blue()
                                    next_pixel = self.source_dib_qimage.pixelColor(profile_x, y + 1)
                                    y_next_red, y_next_green, y_next_blue = next_pixel.red(), next_pixel.green(), next_pixel.blue()
                                    y_lum_pairs = [(y_red, y_next_red), (y_green, y_next_green), (y_blue, y_next_blue)]
                                    for key, lum_pair in zip(self.y_profile_path.keys(), y_lum_pairs):
                                        self.y_profile_path[key].moveTo(viewport_width - lum_pair[0] - view_anchor.x(), y)
                                        self.y_profile_path[key].lineTo(viewport_width - lum_pair[1] - view_anchor.x(), y + 1)

                                # PainterPathItem
                                for key, color in [('red', Qt.red), ('green', Qt.green), ('blue', Qt.blue)]:
                                    # X-Line
                                    if self.item_x_profile_path[key] in self.items():
                                        # self.item_x_profile_path[key]がSceneに登録されている場合の処理
                                        self.item_x_profile_path[key].setPath(self.x_profile_path[key])
                                    else:
                                        print("self.item_x_profile_path[{0}] is created !".format(key))
                                        self.item_x_profile_path[key] = QGraphicsPathItem(self.item_qpixmap)
                                        self.item_x_profile_path[key].setPen(QPen(color, 1))
                                        self.item_x_profile_path[key].setBrush(QBrush(Qt.NoBrush))
                                        self.item_x_profile_path[key].setPath(self.x_profile_path[key])

                                    # Y-Line
                                    if self.item_y_profile_path[key] in self.items():
                                        # self.item_y_profile_path["green"]がSceneに登録されている場合の処理
                                        self.item_y_profile_path[key].setPath(self.y_profile_path[key])
                                    else:
                                        print("self.item_y_profile_path[{0}] is created !".format(key))
                                        self.item_y_profile_path[key] = QGraphicsPathItem(self.item_qpixmap)
                                        self.item_y_profile_path[key].setPen(QPen(color, 1))
                                        self.item_y_profile_path[key].setBrush(QBrush(Qt.NoBrush))
                                        self.item_x_profile_path[key].setPath(self.y_profile_path[key])


    def __draw_figure(self, figure_dict:Dict[str, Any], scene_pos:QPointF,
                      is_mouse_btn_down:bool, is_mouse_move:bool, is_center_drag:bool, is_square:bool):
        """
        図形の描画用テンプレート
        :param figure_dict:
        :param scene_pos:
        :param is_mouse_btn_down:
        :param is_mouse_move:
        :param is_show:
        :param is_center_drag:
        :param is_square:
        :return:
        """
        for view in self.views():
            if view.isActiveWindow():
                item = self.itemAt(scene_pos, view.transform())
                if item is not None:
                    # シーンの最下層のQGraphicsPixmapItemを取得
                    # QGraphicsPixmapItemの上位レイヤーのitemは最終的にQGraphicsPixmapItemを親とする
                    while item.parentItem() is not None:
                        item = item.parentItem()

                    # MouseRelease時にはitemの座標はQGraphics***Itemの上に乗っかっているので
                    # QGraphicsPixmapItemのローカル座標に変換する
                    local_item_pos = item.mapToItem(item, scene_pos)

                    # QGraphicsPixmapItem内部
                    if item is self.item_qpixmap and self.item_qpixmap.contains(local_item_pos):

                        # Sceneに登録されていないfigure_itemを削除
                        if figure_dict['item']:
                            for i in range(len(figure_dict['item'])):
                                if figure_dict['item'][str(i)] not in self.items():
                                    del figure_dict['item'][str(i)]

                        # Mouse Pressに対する処理
                        if is_mouse_btn_down and not is_mouse_move:
                            figure_dict['is_gen'] = True
                            figure_dict['rect'].setTopLeft(local_item_pos)
                            figure_dict['rect'].setBottomRight(local_item_pos)

                            # アンカーポイントの設定
                            figure_dict['anchor'] = figure_dict['rect'].center() if \
                                is_center_drag else figure_dict['rect'].topLeft()

                            figure_dict['item'][str(len(figure_dict['item']))] = \
                                figure_dict['klass'](figure_dict['rect'], self.item_qpixmap) # Graphics***Itemの生成

                            figure_key = str(len(figure_dict['item']) - 1)
                            figure_dict['item'][figure_key].setPen(QPen(figure_dict['color'], 1))
                            figure_dict['item'][figure_key].setBrush(Qt.NoBrush)
                            print("first press >>>", figure_dict['item'][figure_key].rect())
                            for key, value in figure_dict['item'].items():
                                print(f"MousePress: {str(figure_dict['klass'])} key:{key}, QRectF:{value.rect()}.")

                        # Mouse Moveに対する処理
                        elif is_mouse_btn_down and is_mouse_move:
                            if figure_dict['is_gen']:
                                if is_center_drag:
                                    dc = local_item_pos - figure_dict['anchor']
                                    dx, dy = abs(dc.x()), abs(dc.y())
                                    if is_square:
                                        dx = dx if dx < dy else dy # 小さい方と取る
                                        dy = dx

                                    anchor_x, anchor_y = figure_dict['anchor'].x(), figure_dict['anchor'].y()
                                    top_left = QPointF(anchor_x - dx, anchor_y - dy)
                                    bottom_right = QPointF(anchor_x + dx, anchor_y + dy)

                                    left, top = top_left.x(), top_left.y()
                                    if left < 0:
                                        top_left.setX(0)
                                    if top < 0:
                                        top_left.setY(0)
                                    figure_dict['rect'].setTopLeft(top_left)
                                    figure_dict['rect'].setBottomRight(bottom_right)

                                else:
                                    anchor_x, anchor_y = figure_dict['anchor'].x(), figure_dict['anchor'].y()
                                    lip_x, lip_y = local_item_pos.x(), local_item_pos.y()
                                    left, right = (anchor_x, lip_x) if anchor_x < lip_x else (lip_x, anchor_x)
                                    top, bottom = (anchor_y, lip_y) if anchor_y < lip_y else (lip_y, anchor_y)

                                    if is_square:
                                        width = right - left
                                        height = bottom - top
                                        if width < height:
                                            right = left + height
                                        else:
                                            bottom = top + width

                                    figure_dict['rect'].setTopLeft(QPointF(left, top))
                                    figure_dict['rect'].setBottomRight(QPointF(right, bottom))

                                figure_key = str(len(figure_dict['item']) - 1)
                                figure_dict['item'][figure_key].set_rect(figure_dict['rect'], local_item_pos) # 描画

                                figure_status_msg = "c({0:d},{1:d}) {2:d}x{3:d}".format(
                                    figure_dict['rect'].toRect().center().x(),
                                    figure_dict['rect'].toRect().center().y(),
                                    figure_dict['rect'].toRect().width(),
                                    figure_dict['rect'].toRect().height()
                                )
                                view.parentWidget().parentWidget().ui.statusbar.showMessage(figure_status_msg)

                        # Mouse Releaseに対する処理
                        if not is_mouse_btn_down and not is_mouse_move:
                            figure_dict['is_gen'] = False

                            # 領域内でマウスボタンが離された時
                            if item is not None and figure_dict['item']:
                                width, height = figure_dict['rect'].width(), figure_dict['rect'].height()
                                figure_key = str(len(figure_dict['item']) - 1)

                                if isinstance(figure_dict['item'][figure_key], (RectGraphicsItem, EllipseGraphicsItem)):
                                    if width > 1 and height > 1:
                                        figure_dict['item'][figure_key].set_rect(figure_dict['rect'], local_item_pos) # 描画
                                        print(figure_dict['rect'])

                                        for key, value in figure_dict['item'].items():
                                            print(f"MouseRelease:{str(figure_dict['klass'])} key:{key}, QRectF:{value.rect()}.")
                                    else:
                                        # 矩形で囲まれた領域が0の場合、RectGraphicsItem, EllipseGraphicsItem は削除
                                        if figure_dict['item']:
                                            figure_key = str(len(figure_dict['item']) - 1)
                                            self.removeItem(figure_dict['item'][figure_key])
                                            del figure_dict['item'][figure_key]
                                            print(f"MouseRelease:{str(figure_dict['klass'])} key: {figure_key} was released.")


                                elif isinstance(figure_dict['item'][figure_key], LineGraphicsItem):
                                    if width != 0 and height != 0:
                                        figure_dict['item'][figure_key].set_rect(figure_dict['rect'], local_item_pos)  # 描画
                                        print(figure_dict['rect'])
                                        for key, value in figure_dict['item'].items():
                                            print(f"MouseRelease:{str(figure_dict['klass'])} key:{key}, QRectF:{value.rect()}.")
                                    else:
                                        # 線分幅=0の場合、LineGraphicsItemは削除
                                        if figure_dict['item']:
                                            figure_key = str(len(figure_dict['item']) - 1)
                                            self.removeItem(figure_dict['item'][figure_key])
                                            del figure_dict['item'][figure_key]
                                            print(f"MouseRelease:{str(figure_dict['klass'])} key: {figure_key} was released.")






    def toggle_roi(self, is_show:bool):
        """
        ROIの表示切り替え
        :param is_show:
        :return:
        """
        if is_show:
            self.figure_dict_roi['is_draw'] = True
        else:
            self.figure_dict_roi['is_draw'] = False
            if self.figure_dict_roi['item']:
                for key in self.figure_dict_roi['item'].keys():
                    if self.figure_dict_roi['item'][key] in self.items():
                        self.removeItem(self.figure_dict_roi['item'][key])
                self.figure_dict_roi['item'].clear()
                self.update()

    def _draw_roi(self, scene_pos:QPointF, is_mouse_btn_down:bool, is_mouse_move:bool, is_center_drag:bool, is_square:bool):
        """
        ROIの描画
        :param scene_pos:
        :param is_mouse_btn_down:
        :param is_mouse_move:
        :param is_show:
        :param is_square:
        :return:
        """
        self.__draw_figure(self.figure_dict_roi, scene_pos, is_mouse_btn_down, is_mouse_move, is_center_drag, is_square)

    def toggle_line(self, is_show:bool):
        """
        直線の表示切り替え
        :param is_show:
        :return:
        """
        if is_show:
            self.figure_dict_line['is_draw'] = True
        else:
            self.figure_dict_line['is_draw'] = False
            if self.figure_dict_line['item']:
                for key in self.figure_dict_line['item'].keys():
                    if self.figure_dict_line['item'][key] in self.items():
                        self.removeItem(self.figure_dict_line['item'][key])
                self.figure_dict_line['item'].clear()
                self.update()

    def _draw_line(self, scene_pos:QPointF, is_mouse_btn_down:bool, is_mouse_move:bool, is_center_drag:bool, is_square:bool):
        """
        直線の描画
        :param scene_pos:
        :param is_mouse_btn_down:
        :param is_mouse_move:
        :param show:
        :param center_drag:
        :param square:
        :return:
        """
        self.__draw_figure(self.figure_dict_line, scene_pos, is_mouse_btn_down, is_mouse_move, is_center_drag, is_square)

    def toggle_ellipse(self, is_show:bool):
        """
        楕円の表示切り替え
        :param is_show:
        :return:
        """
        if is_show:
            self.figure_dict_ellipse['is_draw'] = True
        else:
            self.figure_dict_ellipse['is_draw'] = False
            if self.figure_dict_ellipse['item']:
                for key in self.figure_dict_ellipse['item'].keys():
                    if self.figure_dict_ellipse['item'][key] in self.items():
                        self.removeItem(self.figure_dict_ellipse['item'][key])
                self.figure_dict_ellipse['item'].clear()
                self.update()

    def _draw_ellipse(self, scene_pos:QPointF, is_mouse_btn_down:bool, is_mouse_move:bool, is_center_drag:bool, is_square:bool):
        """
        楕円領域の描画
        :param scene_pos:
        :param is_mouse_btn_down:
        :param is_mouse_move:
        :param is_show:
        :param is_center_drag:
        :param is_square:
        :return:
        """
        self.__draw_figure(self.figure_dict_ellipse, scene_pos, is_mouse_btn_down, is_mouse_move, is_center_drag, is_square)

    def toggle_mask(self, show:bool) -> bool:
        """
        マスク画像の表示切り替え
        :param show:
        :return:
        """
        # self.mask_qimage.load("data/test01_binary.bmp")
        # mask_img = qimage2ndarray(self.mask_qimage)
        # self.set_mask(create_mask_qimage(mask_img))
        # print("mask_qimage format", self.mask_qimage.format())
        # mask_array = retrieve_mask_ndarray(self.mask_qimage)

        # マスキング
        if show:
            if not self.mask_qimage.isNull():
                # QPixmap for mask
                self.mask_qpixmap = QPixmap.fromImage(self.mask_qimage)

                # QGraphicsPixmapの生成or更新 for mask
                self.item_mask_qpixmap = QGraphicsPixmapItem(self.item_qpixmap) # 親QGraphicsItemを指定
                self.item_mask_qpixmap.setPixmap(self.mask_qpixmap)
                self.addItem(self.item_mask_qpixmap)
            else:
                print("No Mask QImage.")
                return False
        else:
            if self.item_mask_qpixmap in self.items():
                self.removeItem(self.item_mask_qpixmap)

        self.update()
        return True

    def add_item_text(self, text:str, key:str, pos:QPointF, color:QColor=Qt.magenta, point_size:int=10):
        """
        指定位置にテキストを描画
        :param key:
        :param pos:
        :param text:
        :return:
        """
        if key in self.item_texts.keys():
            self.item_texts[key].setPlainText(text)
        else:
            self.item_texts[key] = QGraphicsTextItem(self.item_qpixmap)
            self.item_texts[key].setDefaultTextColor(color)
            self.item_texts[key].setFont(QFont("", pointSize=point_size))
            self.item_texts[key].setPlainText(text)
            self.item_texts[key].setPos(pos)
            self.item_texts[key].setPlainText(text)

    def remove_item_text(self, key:str):
        """
        指定したテキストを破棄
        :param key:
        :return:
        """
        keys = self.item_texts.keys()
        if key in keys:
            if self.item_texts[key] in self.items():
                self.removeItem(self.item_texts[key])
                del self.item_texts[key]
            else:
                print("self.item_texts[{0}] exists. but, is'nt in items of the scene.")

