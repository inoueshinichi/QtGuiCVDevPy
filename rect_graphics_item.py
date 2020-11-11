"""DrawScene用のROIアイテム
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
    QObject
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
    QGraphicsItem
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

# QGraphicsRectItemの派生クラス
class RectGraphicsItem(QGraphicsRectItem):

    def __init__(self, rect:QRectF, parent:QObject):
        super(RectGraphicsItem, self).__init__(rect, parent)

        # アンカーポイント
        self.__anchor: QPointF = rect.topLeft()
        # 矩形領域
        self.__rect: QRectF = rect
        # 矩形領域の特徴
        self.features = {
            'center': [0.0, 0.0],
            'mean': 0.0,
            'var': 0.0,
            'std': 0.0,
            'max': 0.0,
            'min': 0.0,
            'contrast': 0.0,
        }

        # タッチイベントを有効化
        self.setAcceptTouchEvents(True)

        # Drag&Dropイベントを有効化
        self.setAcceptDrops(True)

        # 親領域内にクリッピングする
        self.setFlag(QGraphicsItem.ItemClipsChildrenToShape, True)

    def set_rect(self, rect:PySide2.QtCore.QRectF, mouse_pos: PySide2.QtCore.QPointF):
        """
        矩形領域の指定
        オーバーライド
        :param rect:
        :param mouse_pos:
        :return:
        """
        self.__rect = rect

        super(RectGraphicsItem, self).setRect(rect)


    # override
    def contextMenuEvent(self, event:PySide2.QtWidgets.QGraphicsSceneContextMenuEvent):
        """
        コンテキストメニューイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).contextMenuEvent(event)

    # override
    def mousePressEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスクリックイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).mousePressEvent(event)

    # override
    def mouseReleaseEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスリリースイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).mouseReleaseEvent(event)

    # override
    def mouseDoubleClickEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスダブルクリックイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).mouseDoubleClickEvent(event)

    # override
    def mouseMoveEvent(self, event:PySide2.QtWidgets.QGraphicsSceneMouseEvent):
        """
        マウスムーブイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).mouseMoveEvent(event)

    # override
    def dropEvent(self, event:PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドロップイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).dropEvent(event)

    # override
    def dragEnterEvent(self, event:PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドラッグエンターイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).dragEnterEvent(event)

    # override
    def dragLeaveEvent(self, event:PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドラッグリーブイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).dragLeaveEvent(event)

    # override
    def dragMoveEvent(self, event:PySide2.QtWidgets.QGraphicsSceneDragDropEvent):
        """
        ドラッグムーブイベント
        :param event:
        :return:
        """
        super(RectGraphicsItem, self).dragMoveEvent(event)

    # override
    def itemChange(self, change:PySide2.QtWidgets.QGraphicsItem.GraphicsItemChange, value:Any) -> Any:
        """
        何かしらこのアイテムの状態が変更されたときに呼ばれるメソッド
        ここで，様々なリアクションを取れる.
        :param change:
        :param value:
        :return:
        """
        return super(RectGraphicsItem, self).itemChange(change, value)
