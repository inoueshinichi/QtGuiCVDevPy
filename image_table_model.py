"""ImageTableModel"""

# 標準
from typing import (Union, Dict, List, Tuple, NoReturn, Any, Callable, TypeVar, Generic)

# サードパーティ
import PySide2
from PySide2.QtCore import (Qt, QObject, QModelIndex)
from PySide2.QtGui import (QStandardItem, QStandardItemModel, QBrush)

# 自作


class ImageTableModel(QStandardItemModel):

    def __init__(self, rows:int, columns:int, parent:QObject):
        super(ImageTableModel, self).__init__(rows, columns, parent)

    # override
    def flags(self, index:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags:
        """
        インデックスの条件によってアイテムの状態を制御する
        :param index:
        :return:
        """
        row = index.row()
        column = index.column()
        item = index.model().itemFromIndex(index)
        item.setCheckable(False)

        # アイテム制御フラグ
        item_flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable
        if column == 0:
            item.setCheckable(True)
            # item_flags |= Qt.ItemIsUserCheckable
        elif column == 1:
            item_flags |= (Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        return item_flags





