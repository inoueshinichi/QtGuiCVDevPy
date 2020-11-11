# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_HistogramDialog.ui'
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


class Ui_HistogramDialog(object):
    def setupUi(self, HistogramDialog):
        if HistogramDialog.objectName():
            HistogramDialog.setObjectName(u"HistogramDialog")
        HistogramDialog.resize(276, 157)
        self.pBtn_Flat_Hist_Apply = QPushButton(HistogramDialog)
        self.pBtn_Flat_Hist_Apply.setObjectName(u"pBtn_Flat_Hist_Apply")
        self.pBtn_Flat_Hist_Apply.setGeometry(QRect(10, 10, 111, 26))

        self.retranslateUi(HistogramDialog)

        QMetaObject.connectSlotsByName(HistogramDialog)
    # setupUi

    def retranslateUi(self, HistogramDialog):
        HistogramDialog.setWindowTitle(QCoreApplication.translate("HistogramDialog", u"Histogram Dialog", None))
        self.pBtn_Flat_Hist_Apply.setText(QCoreApplication.translate("HistogramDialog", u" Flat Hist", None))
    # retranslateUi

