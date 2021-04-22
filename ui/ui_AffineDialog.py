# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_AffineDialog.ui'
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


class Ui_AffineDialog(object):
    def setupUi(self, AffineDialog):
        if AffineDialog.objectName():
            AffineDialog.setObjectName(u"AffineDialog")
        AffineDialog.resize(220, 159)
        self.verticalLayout = QVBoxLayout(AffineDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Angle = QLabel(AffineDialog)
        self.lbl_Angle.setObjectName(u"lbl_Angle")

        self.horizontalLayout.addWidget(self.lbl_Angle)

        self.dsBox_Angle = QDoubleSpinBox(AffineDialog)
        self.dsBox_Angle.setObjectName(u"dsBox_Angle")
        self.dsBox_Angle.setMaximum(360.000000000000000)

        self.horizontalLayout.addWidget(self.dsBox_Angle)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_cx = QLabel(AffineDialog)
        self.lbl_cx.setObjectName(u"lbl_cx")

        self.horizontalLayout_2.addWidget(self.lbl_cx)

        self.sBox_cx = QSpinBox(AffineDialog)
        self.sBox_cx.setObjectName(u"sBox_cx")
        self.sBox_cx.setMaximum(10000)

        self.horizontalLayout_2.addWidget(self.sBox_cx)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_cy = QLabel(AffineDialog)
        self.lbl_cy.setObjectName(u"lbl_cy")

        self.horizontalLayout_3.addWidget(self.lbl_cy)

        self.sBox_cy = QSpinBox(AffineDialog)
        self.sBox_cy.setObjectName(u"sBox_cy")
        self.sBox_cy.setMaximum(10000)

        self.horizontalLayout_3.addWidget(self.sBox_cy)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_tx = QLabel(AffineDialog)
        self.lbl_tx.setObjectName(u"lbl_tx")

        self.horizontalLayout_4.addWidget(self.lbl_tx)

        self.sBox_tx = QSpinBox(AffineDialog)
        self.sBox_tx.setObjectName(u"sBox_tx")
        self.sBox_tx.setMaximum(10000)

        self.horizontalLayout_4.addWidget(self.sBox_tx)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_ty = QLabel(AffineDialog)
        self.lbl_ty.setObjectName(u"lbl_ty")

        self.horizontalLayout_5.addWidget(self.lbl_ty)

        self.sBox_ty = QSpinBox(AffineDialog)
        self.sBox_ty.setObjectName(u"sBox_ty")
        self.sBox_ty.setMaximum(10000)

        self.horizontalLayout_5.addWidget(self.sBox_ty)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_sx = QLabel(AffineDialog)
        self.lbl_sx.setObjectName(u"lbl_sx")

        self.horizontalLayout_8.addWidget(self.lbl_sx)

        self.dsBox_sx = QDoubleSpinBox(AffineDialog)
        self.dsBox_sx.setObjectName(u"dsBox_sx")
        self.dsBox_sx.setMaximum(10.000000000000000)
        self.dsBox_sx.setSingleStep(0.100000000000000)
        self.dsBox_sx.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.dsBox_sx)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_sy = QLabel(AffineDialog)
        self.lbl_sy.setObjectName(u"lbl_sy")

        self.horizontalLayout_9.addWidget(self.lbl_sy)

        self.dsBox_sy = QDoubleSpinBox(AffineDialog)
        self.dsBox_sy.setObjectName(u"dsBox_sy")
        self.dsBox_sy.setMaximum(10.000000000000000)
        self.dsBox_sy.setSingleStep(0.100000000000000)
        self.dsBox_sy.setValue(1.000000000000000)

        self.horizontalLayout_9.addWidget(self.dsBox_sy)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.pBtn_Affine_Apply = QPushButton(AffineDialog)
        self.pBtn_Affine_Apply.setObjectName(u"pBtn_Affine_Apply")

        self.verticalLayout.addWidget(self.pBtn_Affine_Apply)


        self.retranslateUi(AffineDialog)

        QMetaObject.connectSlotsByName(AffineDialog)
    # setupUi

    def retranslateUi(self, AffineDialog):
        AffineDialog.setWindowTitle(QCoreApplication.translate("AffineDialog", u"AffineDialog", None))
        self.lbl_Angle.setText(QCoreApplication.translate("AffineDialog", u"Angle(deg)", None))
        self.lbl_cx.setText(QCoreApplication.translate("AffineDialog", u"cx", None))
        self.lbl_cy.setText(QCoreApplication.translate("AffineDialog", u"cy", None))
        self.lbl_tx.setText(QCoreApplication.translate("AffineDialog", u"tx", None))
        self.lbl_ty.setText(QCoreApplication.translate("AffineDialog", u"ty", None))
        self.lbl_sx.setText(QCoreApplication.translate("AffineDialog", u"sx", None))
        self.lbl_sy.setText(QCoreApplication.translate("AffineDialog", u"sx", None))
        self.pBtn_Affine_Apply.setText(QCoreApplication.translate("AffineDialog", u"Apply", None))
    # retranslateUi

