"""DrawScene用のLineアイテム"""

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
    Generic,
    NoReturn
)

# サードパーティ
from numba import jit
import numpy as np
import PySide2
from PySide2.QtCore import (
    Qt,
    QPointF,
    qDebug,
    QRectF,
    QObject,
)
from PySide2.QtGui import (
    QImage,
    QPixmap,
    QPen,
    QBrush,
    QFont,
    qGray,
    QPainterPath
)
from PySide2.QtWidgets import (
    QGraphicsScene,
    QGraphicsPixmapItem,
    QGraphicsPathItem,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QGraphicsLineItem,
    QGraphicsItem
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

# QGraphicsLineItemの派生クラス
class LineGraphicsItem(QGraphicsLineItem):

    def __init__(self, rect:QRectF, parent:QObject):
        super(LineGraphicsItem, self).__init__(rect.left(), rect.top(), rect.right(), rect.bottom(), parent)

        # アンカーポイント
        self.__anchor: QPointF = rect.topLeft()
        # 矩形領域
        self.__rect: QRectF = rect
        # ブラシの色
        self.__brush = None

        # タッチイベントを有効化
        self.setAcceptTouchEvents(True)

        # Drag&Dropイベントを有効化
        self.setAcceptDrops(True)

        # 親領域内にクリッピングする
        self.setFlag(QGraphicsItem.ItemClipsChildrenToShape, True)

    def rect(self) -> PySide2.QtCore.QRectF:
        """
        矩形領域の取得
        :return:
        """
        return self.__rect

    # 自作関数
    def set_rect(self, rect: PySide2.QtCore.QRectF, mouse_pos: PySide2.QtCore.QPointF):
        """
        矩形領域の設定
        :param rect:
        :return:
        """
        left, top = rect.left(), rect.top()
        right, bottom = rect.right(), rect.bottom()
        mouse_x, mouse_y = mouse_pos.x(), mouse_pos.y()
        if self.__anchor.x() < mouse_x:
            x1, x2 = left, right
        else:
            x1, x2 = right, left

        if self.__anchor.y() < mouse_y:
            y1, y2 = top, bottom
        else:
            y1, y2 = bottom, top

        self.__rect = rect

        # setLine()を呼んで，lineをセット.
        # 実質，ここでSceneに描画される.
        self.setLine(x1, y1, x2, y2)

    def setBrush(self, brush:PySide2.QtGui.QBrush):
        """
        ブラシ色の設定
        :param brush:
        :return:
        """
        self.__brush = brush

    # override
    def contextMenuEvent(self, event: PySide2.QtWidgets.QGraphicsSceneContextMenuEvent):
        """
        コンテキストメニューイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).contextMenuEvent(event)

    # override
    def mousePressEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスクリックイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).mousePressEvent(event)

    # override
    def mouseReleaseEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスリリースイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).mouseReleaseEvent(event)

    # override
    def mouseDoubleClickEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスダブルクリックイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).mouseDoubleClickEvent(event)

    # override
    def mouseMoveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスムーブイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).mouseMoveEvent(event)

    # override
    def dropEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドロップイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).dropEvent(event)

    # override
    def dragEnterEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドラッグエンターイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).dragEnterEvent(event)

    # override
    def dragLeaveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドラッグリーブイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).dragLeaveEvent(event)

    # override
    def dragMoveEvent(self, event: PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドラッグムーブイベント
        :param event:
        :return:
        """
        super(LineGraphicsItem, self).dragMoveEvent(event)

    # override
    def itemChange(self, change: PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value: Any) -> Any:
        """
        何かしらこのアイテムの状態が変更されたときに呼ばれるメソッド
        ここで，様々なリアクションを取れる.
        :param change:
        :param value:
        :return:
        """
        return super(LineGraphicsItem, self).itemChange(change, value)
