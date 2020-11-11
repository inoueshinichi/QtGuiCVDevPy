# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ImageWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from draw_view import DrawView


class Ui_ImageWindow(object):
    def setupUi(self, ImageWindow):
        if ImageWindow.objectName():
            ImageWindow.setObjectName(u"ImageWindow")
        ImageWindow.resize(509, 328)
        self.centralwidget = QWidget(ImageWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gView = DrawView(self.centralwidget)
        self.gView.setObjectName(u"gView")
        self.gView.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.gView.setMouseTracking(True)
        self.gView.setAutoFillBackground(True)
        brush = QBrush(QColor(64, 64, 64, 255))
        brush.setStyle(Qt.SolidPattern)
        self.gView.setBackgroundBrush(brush)
        self.gView.setDragMode(QGraphicsView.NoDrag)

        self.gridLayout.addWidget(self.gView, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.lEdit_Image_Status = QLineEdit(self.centralwidget)
        self.lEdit_Image_Status.setObjectName(u"lEdit_Image_Status")
        self.lEdit_Image_Status.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lEdit_Image_Status)

        self.lbl_Image_Scale = QLabel(self.centralwidget)
        self.lbl_Image_Scale.setObjectName(u"lbl_Image_Scale")
        self.lbl_Image_Scale.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbl_Image_Scale)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        ImageWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImageWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageWindow)

        QMetaObject.connectSlotsByName(ImageWindow)
    # setupUi

    def retranslateUi(self, ImageWindow):
        ImageWindow.setWindowTitle(QCoreApplication.translate("ImageWindow", u"MainWindow", None))
        self.lEdit_Image_Status.setPlaceholderText(QCoreApplication.translate("ImageWindow", u"Image Status", None))
        self.lbl_Image_Scale.setText(QCoreApplication.translate("ImageWindow", u"100%", None))
    # retranslateUi

