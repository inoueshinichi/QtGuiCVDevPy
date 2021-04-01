# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MappingDialog.ui'
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


class Ui_MappingDialog(object):
    def setupUi(self, MappingDialog):
        if MappingDialog.objectName():
            MappingDialog.setObjectName(u"MappingDialog")
        MappingDialog.resize(400, 300)
        self.pBtn_Gamma_Apply = QPushButton(MappingDialog)
        self.pBtn_Gamma_Apply.setObjectName(u"pBtn_Gamma_Apply")
        self.pBtn_Gamma_Apply.setGeometry(QRect(60, 140, 75, 23))

        self.retranslateUi(MappingDialog)

        QMetaObject.connectSlotsByName(MappingDialog)
    # setupUi

    def retranslateUi(self, MappingDialog):
        MappingDialog.setWindowTitle(QCoreApplication.translate("MappingDialog", u"Dialog", None))
        self.pBtn_Gamma_Apply.setText(QCoreApplication.translate("MappingDialog", u"Gamma", None))
    # retranslateUi

