# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_RotateDialog.ui'
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


class Ui_RotateDialog(object):
    def setupUi(self, RotateDialog):
        if RotateDialog.objectName():
            RotateDialog.setObjectName(u"RotateDialog")
        RotateDialog.resize(302, 183)
        self.layoutWidget = QWidget(RotateDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 120, 54, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_cy = QLabel(self.layoutWidget)
        self.lbl_cy.setObjectName(u"lbl_cy")

        self.horizontalLayout_3.addWidget(self.lbl_cy)

        self.sBox_cy = QSpinBox(self.layoutWidget)
        self.sBox_cy.setObjectName(u"sBox_cy")

        self.horizontalLayout_3.addWidget(self.sBox_cy)

        self.widget = QWidget(RotateDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 109, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_Angle = QLabel(self.widget)
        self.lbl_Angle.setObjectName(u"lbl_Angle")

        self.horizontalLayout.addWidget(self.lbl_Angle)

        self.dsBox_Angle = QDoubleSpinBox(self.widget)
        self.dsBox_Angle.setObjectName(u"dsBox_Angle")

        self.horizontalLayout.addWidget(self.dsBox_Angle)

        self.widget1 = QWidget(RotateDialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 80, 54, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_cx = QLabel(self.widget1)
        self.lbl_cx.setObjectName(u"lbl_cx")

        self.horizontalLayout_2.addWidget(self.lbl_cx)

        self.sBox_cx = QSpinBox(self.widget1)
        self.sBox_cx.setObjectName(u"sBox_cx")

        self.horizontalLayout_2.addWidget(self.sBox_cx)


        self.retranslateUi(RotateDialog)

        QMetaObject.connectSlotsByName(RotateDialog)
    # setupUi

    def retranslateUi(self, RotateDialog):
        RotateDialog.setWindowTitle(QCoreApplication.translate("RotateDialog", u"RotateDialog", None))
        self.lbl_cy.setText(QCoreApplication.translate("RotateDialog", u"c", None))
        self.lbl_Angle.setText(QCoreApplication.translate("RotateDialog", u"Angle(deg)", None))
        self.lbl_cx.setText(QCoreApplication.translate("RotateDialog", u"cx", None))
    # retranslateUi

