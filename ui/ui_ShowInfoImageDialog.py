# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ShowInfoImageDialog.ui'
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


class Ui_ShowInfoImageDialog(object):
    def setupUi(self, ShowInfoImageDialog):
        if ShowInfoImageDialog.objectName():
            ShowInfoImageDialog.setObjectName(u"ShowInfoImageDialog")
        ShowInfoImageDialog.resize(333, 363)
        ShowInfoImageDialog.setSizeGripEnabled(True)
        ShowInfoImageDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(ShowInfoImageDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(ShowInfoImageDialog)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(ShowInfoImageDialog)

        QMetaObject.connectSlotsByName(ShowInfoImageDialog)
    # setupUi

    def retranslateUi(self, ShowInfoImageDialog):
        ShowInfoImageDialog.setWindowTitle(QCoreApplication.translate("ShowInfoImageDialog", u"Information of Image", None))
    # retranslateUi

