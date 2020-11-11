# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_BinarizeDialog.ui'
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


class Ui_BinarizeDialog(object):
    def setupUi(self, BinarizeDialog):
        if BinarizeDialog.objectName():
            BinarizeDialog.setObjectName(u"BinarizeDialog")
        BinarizeDialog.resize(558, 144)
        self.gridLayout = QGridLayout(BinarizeDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grp_Adaptive = QGroupBox(BinarizeDialog)
        self.grp_Adaptive.setObjectName(u"grp_Adaptive")
        self.verticalLayout_3 = QVBoxLayout(self.grp_Adaptive)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Adaptive_Patchsize = QLabel(self.grp_Adaptive)
        self.lbl_Adaptive_Patchsize.setObjectName(u"lbl_Adaptive_Patchsize")

        self.horizontalLayout_2.addWidget(self.lbl_Adaptive_Patchsize)

        self.sBox_Adaptive_Patchsize = QSpinBox(self.grp_Adaptive)
        self.sBox_Adaptive_Patchsize.setObjectName(u"sBox_Adaptive_Patchsize")
        self.sBox_Adaptive_Patchsize.setMinimum(3)
        self.sBox_Adaptive_Patchsize.setMaximum(50)
        self.sBox_Adaptive_Patchsize.setSingleStep(2)
        self.sBox_Adaptive_Patchsize.setValue(3)

        self.horizontalLayout_2.addWidget(self.sBox_Adaptive_Patchsize)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Adaptive_SubThreshBias = QLabel(self.grp_Adaptive)
        self.lbl_Adaptive_SubThreshBias.setObjectName(u"lbl_Adaptive_SubThreshBias")

        self.horizontalLayout_3.addWidget(self.lbl_Adaptive_SubThreshBias)

        self.sBox_Adaptive_SubThreshBias = QSpinBox(self.grp_Adaptive)
        self.sBox_Adaptive_SubThreshBias.setObjectName(u"sBox_Adaptive_SubThreshBias")
        self.sBox_Adaptive_SubThreshBias.setMinimum(0)
        self.sBox_Adaptive_SubThreshBias.setMaximum(255)
        self.sBox_Adaptive_SubThreshBias.setValue(0)

        self.horizontalLayout_3.addWidget(self.sBox_Adaptive_SubThreshBias)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.pBtn_Adaptive_Apply = QPushButton(self.grp_Adaptive)
        self.pBtn_Adaptive_Apply.setObjectName(u"pBtn_Adaptive_Apply")

        self.verticalLayout_3.addWidget(self.pBtn_Adaptive_Apply)


        self.gridLayout.addWidget(self.grp_Adaptive, 0, 2, 1, 1)

        self.grp_Simple = QGroupBox(BinarizeDialog)
        self.grp_Simple.setObjectName(u"grp_Simple")
        self.verticalLayout = QVBoxLayout(self.grp_Simple)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Simple_Threshold = QLabel(self.grp_Simple)
        self.lbl_Simple_Threshold.setObjectName(u"lbl_Simple_Threshold")

        self.horizontalLayout.addWidget(self.lbl_Simple_Threshold)

        self.sBox_Simple_Threshold = QSpinBox(self.grp_Simple)
        self.sBox_Simple_Threshold.setObjectName(u"sBox_Simple_Threshold")
        self.sBox_Simple_Threshold.setMaximum(255)
        self.sBox_Simple_Threshold.setValue(80)

        self.horizontalLayout.addWidget(self.sBox_Simple_Threshold)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pBtn_Simple_Apply = QPushButton(self.grp_Simple)
        self.pBtn_Simple_Apply.setObjectName(u"pBtn_Simple_Apply")

        self.verticalLayout.addWidget(self.pBtn_Simple_Apply)


        self.gridLayout.addWidget(self.grp_Simple, 0, 0, 1, 1)

        self.groupBox = QGroupBox(BinarizeDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lEdit_Otsu_Threshold = QLineEdit(self.groupBox)
        self.lEdit_Otsu_Threshold.setObjectName(u"lEdit_Otsu_Threshold")
        self.lEdit_Otsu_Threshold.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lEdit_Otsu_Threshold)

        self.pBtn_Otsu_Apply = QPushButton(self.groupBox)
        self.pBtn_Otsu_Apply.setObjectName(u"pBtn_Otsu_Apply")

        self.verticalLayout_2.addWidget(self.pBtn_Otsu_Apply)


        self.gridLayout.addWidget(self.groupBox, 0, 3, 1, 1)


        self.retranslateUi(BinarizeDialog)

        QMetaObject.connectSlotsByName(BinarizeDialog)
    # setupUi

    def retranslateUi(self, BinarizeDialog):
        BinarizeDialog.setWindowTitle(QCoreApplication.translate("BinarizeDialog", u"BinarizeDialog", None))
        self.grp_Adaptive.setTitle(QCoreApplication.translate("BinarizeDialog", u"Adaptive", None))
        self.lbl_Adaptive_Patchsize.setText(QCoreApplication.translate("BinarizeDialog", u"Patch size", None))
        self.lbl_Adaptive_SubThreshBias.setText(QCoreApplication.translate("BinarizeDialog", u"Sub thresh bias", None))
        self.pBtn_Adaptive_Apply.setText(QCoreApplication.translate("BinarizeDialog", u"Apply", None))
        self.grp_Simple.setTitle(QCoreApplication.translate("BinarizeDialog", u"Simple", None))
        self.lbl_Simple_Threshold.setText(QCoreApplication.translate("BinarizeDialog", u"Threshold", None))
        self.pBtn_Simple_Apply.setText(QCoreApplication.translate("BinarizeDialog", u"Apply", None))
        self.groupBox.setTitle(QCoreApplication.translate("BinarizeDialog", u"Otsu", None))
        self.lEdit_Otsu_Threshold.setPlaceholderText(QCoreApplication.translate("BinarizeDialog", u"Threshold", None))
        self.pBtn_Otsu_Apply.setText(QCoreApplication.translate("BinarizeDialog", u"Apply", None))
    # retranslateUi

