"""ImageTableView"""

# 標準
import os
import sys
from typing import (Union, Dict, List, Tuple, NoReturn, Any, Callable, TypeVar, Generic)

# サードパーティ
import PySide2
from PySide2.QtCore import (Qt, QObject, QModelIndex, Signal, Slot, QSortFilterProxyModel, QRegExp)
from PySide2.QtGui import (QStandardItem, QStandardItemModel, QBrush, QImage, QPixmap, QIcon)
from PySide2.QtWidgets import (QStyledItemDelegate, QTableView, QWidget)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)



class ImageTableView(QTableView):

    def __init__(self, parent:QWidget):
        super(ImageTableView, self).__init__(parent)

        # Setting
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QTableView.ExtendedSelection)
        self.horizontalHeader().setStretchLastSection(True)


        # Signal/Slot
        self.clicked.connect(self._clicked_item)

    # override
    def sizeHintForRow(self, row:int) -> int:
        """
        resizeRowsToContents()が呼び出されたときに設定する行の高さを指定
        :param row:
        :return:
        """
        model = self.model()
        index = model.index(row, 0)
        if isinstance(model, QSortFilterProxyModel):
            index = model.mapToSource(index)
            src_model = model.sourceModel()
            item = src_model.itemFromIndex(index)
        else:
            item = model.itemFromIndex(index)

        size = item.sizeHint()
        height = size.height()
        return height

    def review(self):
        """
        ImageTableViewの体裁を整える
        :return:
        """
        # self.reset()
        self.clearFocus()
        self.clearSpans()
        self.clearMask()
        self.clearSelection()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def all_check(self):
        """
        ImageTableViewの全チェックボックスをONにする
        :return:
        """
        model = self.model()
        for row in range(model.rowCount()):
            index = model.index(row, 0)

            if isinstance(model, QSortFilterProxyModel):
                index = model.mapToSource(index)
                src_model = model.sourceModel()
                item = src_model.itemFromIndex(index)
            else:
                item = model.itemFromIndex(index)

            item.setCheckState(Qt.Checked)

    def all_uncheck(self):
        """
            ImageTableViewの全チェックボックスをOFFにする
            :return:
            """
        model = self.model()
        for row in range(model.rowCount()):
            index = model.index(row, 0)

            if isinstance(model, QSortFilterProxyModel):
                index = model.mapToSource(index)
                src_model = model.sourceModel()
                item = src_model.itemFromIndex(index)
            else:
                item = model.itemFromIndex(index)

            item.setCheckState(Qt.Unchecked)

    def update_search_filter(self, reg_exp:QRegExp) -> NoReturn:
        """
        ImageTableViewの検索フィルタの更新
        :param reg_exp:
        :return:
        """
        model = self.model()
        if isinstance(model, QSortFilterProxyModel):
            model.setFilterKeyColumn(0) # 0列目を対象
            model.setFilterRegExp(reg_exp)


    @Slot(QModelIndex)
    def _clicked_item(self, index:QModelIndex) -> NoReturn:
        """
        クリックされたアイテムに対しての制御
        :param index:
        :return:
        """
        if not index.isValid():
            return

        model = index.model()
        if isinstance(model, QSortFilterProxyModel):
            index = model.mapToSource(index)
            src_model = model.sourceModel()
            item = src_model.itemFromIndex(index)
        else:
            item = model.itemFromIndex(index)

        row = index.row()
        column = index.column()

        if column == 0:
            check_state = item.checkState()
            if check_state == Qt.Checked:
                item.setCheckState(Qt.Unchecked)
            elif check_state == Qt.Unchecked:
                item.setCheckState(Qt.Checked)