# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_UnsharpMaskingDialog.ui'
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


class Ui_UnsharpMaskingDialog(object):
    def setupUi(self, UnsharpMaskingDialog):
        if UnsharpMaskingDialog.objectName():
            UnsharpMaskingDialog.setObjectName(u"UnsharpMaskingDialog")
        UnsharpMaskingDialog.resize(372, 179)
        self.grp_Sharpen = QGroupBox(UnsharpMaskingDialog)
        self.grp_Sharpen.setObjectName(u"grp_Sharpen")
        self.grp_Sharpen.setGeometry(QRect(10, 10, 141, 157))
        self.verticalLayout = QVBoxLayout(self.grp_Sharpen)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Sharpen_k_xy = QLabel(self.grp_Sharpen)
        self.lbl_Sharpen_k_xy.setObjectName(u"lbl_Sharpen_k_xy")

        self.horizontalLayout_3.addWidget(self.lbl_Sharpen_k_xy)

        self.sBox_Sharpen_k_xy = QSpinBox(self.grp_Sharpen)
        self.sBox_Sharpen_k_xy.setObjectName(u"sBox_Sharpen_k_xy")
        self.sBox_Sharpen_k_xy.setMinimum(3)
        self.sBox_Sharpen_k_xy.setMaximum(50)
        self.sBox_Sharpen_k_xy.setSingleStep(2)

        self.horizontalLayout_3.addWidget(self.sBox_Sharpen_k_xy)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Sharpen_Sigma = QLabel(self.grp_Sharpen)
        self.lbl_Sharpen_Sigma.setObjectName(u"lbl_Sharpen_Sigma")

        self.horizontalLayout_2.addWidget(self.lbl_Sharpen_Sigma)

        self.dsBox_Sharpen_Sigma = QDoubleSpinBox(self.grp_Sharpen)
        self.dsBox_Sharpen_Sigma.setObjectName(u"dsBox_Sharpen_Sigma")
        self.dsBox_Sharpen_Sigma.setMinimum(0.100000000000000)
        self.dsBox_Sharpen_Sigma.setMaximum(5.000000000000000)
        self.dsBox_Sharpen_Sigma.setSingleStep(0.100000000000000)
        self.dsBox_Sharpen_Sigma.setValue(1.300000000000000)

        self.horizontalLayout_2.addWidget(self.dsBox_Sharpen_Sigma)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Sharpen_Strong = QLabel(self.grp_Sharpen)
        self.lbl_Sharpen_Strong.setObjectName(u"lbl_Sharpen_Strong")

        self.horizontalLayout.addWidget(self.lbl_Sharpen_Strong)

        self.dsBox_Sharpen_Strong = QDoubleSpinBox(self.grp_Sharpen)
        self.dsBox_Sharpen_Strong.setObjectName(u"dsBox_Sharpen_Strong")
        self.dsBox_Sharpen_Strong.setMinimum(0.100000000000000)
        self.dsBox_Sharpen_Strong.setMaximum(20.000000000000000)
        self.dsBox_Sharpen_Strong.setSingleStep(1.000000000000000)
        self.dsBox_Sharpen_Strong.setValue(5.000000000000000)

        self.horizontalLayout.addWidget(self.dsBox_Sharpen_Strong)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pBtn_Sharpen_Apply = QPushButton(self.grp_Sharpen)
        self.pBtn_Sharpen_Apply.setObjectName(u"pBtn_Sharpen_Apply")

        self.verticalLayout.addWidget(self.pBtn_Sharpen_Apply)


        self.retranslateUi(UnsharpMaskingDialog)

        QMetaObject.connectSlotsByName(UnsharpMaskingDialog)
    # setupUi

    def retranslateUi(self, UnsharpMaskingDialog):
        UnsharpMaskingDialog.setWindowTitle(QCoreApplication.translate("UnsharpMaskingDialog", u"UnsharpMasking Dialog", None))
        self.grp_Sharpen.setTitle(QCoreApplication.translate("UnsharpMaskingDialog", u"Sharpen", None))
        self.lbl_Sharpen_k_xy.setText(QCoreApplication.translate("UnsharpMaskingDialog", u"k_xy", None))
        self.lbl_Sharpen_Sigma.setText(QCoreApplication.translate("UnsharpMaskingDialog", u"Sigma", None))
        self.lbl_Sharpen_Strong.setText(QCoreApplication.translate("UnsharpMaskingDialog", u"Strong", None))
        self.pBtn_Sharpen_Apply.setText(QCoreApplication.translate("UnsharpMaskingDialog", u"Apply", None))
    # retranslateUi

