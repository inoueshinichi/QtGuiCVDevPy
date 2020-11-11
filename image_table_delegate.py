"""ImageTableDelegate"""

# 標準
from typing import (Union, Dict, List, Tuple, NoReturn, Any, Callable, TypeVar, Generic)

# サードパーティ
import PySide2
from PySide2.QtCore import (Qt, QObject, QModelIndex, QSortFilterProxyModel)
from PySide2.QtGui import (QStandardItem, QStandardItemModel, QBrush, QImage, QPixmap, QIcon)
from PySide2.QtWidgets import (QStyledItemDelegate)

# 自作


class ImageTableDelegate(QStyledItemDelegate):

    def __init__(self, parent:QObject):
        super(ImageTableDelegate, self).__init__(parent)


    def paint(self, painter:PySide2.QtGui.QPainter,
              option:PySide2.QtWidgets.QStyleOptionViewItem,
              index:PySide2.QtCore.QModelIndex):
        """
        Modelに格納したデータ(item)をViewに描画
        画像やアイコン、文字列など型によって描画処理を分ける
        :param painter:
        :param option:
        :param index:
        :return:
        """
        model = index.model()
        if isinstance(model, QSortFilterProxyModel):
            index = model.mapToSource(index)
            src_model = model.sourceModel()
            item = src_model.itemFromIndex(index)
        else:
            item = model.itemFromIndex(index)

        row = index.row()
        column = index.column()

        if column == 1:
            # QStandardItemに格納されているQPixmapを描画する

            # QPixmap
            qimage = item.data(role=Qt.DecorationRole) # QPixmap
            qpixmap = QPixmap.fromImage(qimage)
            qpixmap_width = qpixmap.width()
            qpixmap_height = qpixmap.height()

            # Cell
            cell_width = option.rect.width()
            cell_height = option.rect.height()
            cell_left = option.rect.x()
            cell_top = option.rect.y()

            # Aspect
            cell_aspect_ratio = cell_width / cell_height
            qpixmap_aspect_ratio = qpixmap_width / qpixmap_height
            if cell_aspect_ratio < qpixmap_aspect_ratio:
                qpixmap_scaled = qpixmap.scaledToWidth(cell_width)
            else:
                qpixmap_scaled = qpixmap.scaledToHeight(cell_height)

            # Paint
            painter.drawPixmap(cell_left, cell_top, qpixmap_scaled.width(), qpixmap_scaled.height(), qpixmap_scaled)
        else:
            # QImage以外の処理
            super(ImageTableDelegate, self).paint(painter, option, index)


"""
enum Qt::ItemDataRoleについて
ItemDataRoleはModelに格納されているデータに付随するもので、
Viewに表示するときのインジケーターとしての役割がある。

General Purpose Role
0   Qt::DisplayRole     The key data to be rendered in the form of text.(QString)
1   Qt::DecorationRole  The data to be rendered as a decoration in the from of an icon.(QColor, QIcon or QPixmap)
2   Qt::EditRole        The data in a form suitable for editing an editor.(QString)
3   Qt::ToolTipRole     The data displayed in the item's tooltip.(QString)
4   Qt::StatusTipRole   The data displayed in the status bar.(QString)
5   Qt::WhatsThisRole   The data displayed for the item in "What's This?" mode.(QString)
13  Qt::SizeHintRole    The size hint for the item that will be supllied to views.(QSize)

Appearance Role
6   Qt::FontRole        The font used for items rendered with the default delegate.(QFont)
7   Qt::TextAlignmentRole   The alignment of the text for items rendered with the default delegate.(Qt::Alignment)
8   Qt::BackgroundRole  The background brush used for items rendered with the default delegate.(Qt::Alignment)
9   Qt::ForegroundRole  The foreground brush (text color, typically) used for items rendered with the default delegate.(QBrush)
10  Qt::CheckStateRole  This role is used to obtain the checked state of an item.(Qt::CheckState)
14  Qt::InitialSortOrderRole    This role is used to obtain the initial sort order of a header view section.(Qt::SortOrder).

Accessibility Role
11  Qt::AccessibleTextRole  The text to be used by accessibility extensions and plugins, such as screen readers.(QString)
12  Qt::AccessibleDescriptionRole   A description of the item for accessiblity purposes.(QString)

"""