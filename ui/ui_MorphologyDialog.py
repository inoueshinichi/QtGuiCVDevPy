# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MorphologyDialog.ui'
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


class Ui_MorphologyDialog(object):
    def setupUi(self, MorphologyDialog):
        if MorphologyDialog.objectName():
            MorphologyDialog.setObjectName(u"MorphologyDialog")
        MorphologyDialog.resize(565, 146)
        self.gridLayout = QGridLayout(MorphologyDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.grp_Dilation = QGroupBox(MorphologyDialog)
        self.grp_Dilation.setObjectName(u"grp_Dilation")
        self.verticalLayout = QVBoxLayout(self.grp_Dilation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Dilation_k_xy = QLabel(self.grp_Dilation)
        self.lbl_Dilation_k_xy.setObjectName(u"lbl_Dilation_k_xy")

        self.horizontalLayout.addWidget(self.lbl_Dilation_k_xy)

        self.sBox_Dilation_k_xy = QSpinBox(self.grp_Dilation)
        self.sBox_Dilation_k_xy.setObjectName(u"sBox_Dilation_k_xy")
        self.sBox_Dilation_k_xy.setMinimum(3)
        self.sBox_Dilation_k_xy.setSingleStep(2)

        self.horizontalLayout.addWidget(self.sBox_Dilation_k_xy)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Dilation_iter = QLabel(self.grp_Dilation)
        self.lbl_Dilation_iter.setObjectName(u"lbl_Dilation_iter")

        self.horizontalLayout_2.addWidget(self.lbl_Dilation_iter)

        self.sBox_Dilation_iter = QSpinBox(self.grp_Dilation)
        self.sBox_Dilation_iter.setObjectName(u"sBox_Dilation_iter")
        self.sBox_Dilation_iter.setMinimum(1)
        self.sBox_Dilation_iter.setSingleStep(1)
        self.sBox_Dilation_iter.setValue(1)

        self.horizontalLayout_2.addWidget(self.sBox_Dilation_iter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pBtn_Dilation_Apply = QPushButton(self.grp_Dilation)
        self.pBtn_Dilation_Apply.setObjectName(u"pBtn_Dilation_Apply")

        self.verticalLayout.addWidget(self.pBtn_Dilation_Apply)


        self.horizontalLayout_12.addWidget(self.grp_Dilation)

        self.grp_Erosion = QGroupBox(MorphologyDialog)
        self.grp_Erosion.setObjectName(u"grp_Erosion")
        self.verticalLayout_2 = QVBoxLayout(self.grp_Erosion)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Erosion_k_xy = QLabel(self.grp_Erosion)
        self.lbl_Erosion_k_xy.setObjectName(u"lbl_Erosion_k_xy")

        self.horizontalLayout_3.addWidget(self.lbl_Erosion_k_xy)

        self.sBox_Erosion_k_xy = QSpinBox(self.grp_Erosion)
        self.sBox_Erosion_k_xy.setObjectName(u"sBox_Erosion_k_xy")
        self.sBox_Erosion_k_xy.setMinimum(3)
        self.sBox_Erosion_k_xy.setSingleStep(2)

        self.horizontalLayout_3.addWidget(self.sBox_Erosion_k_xy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_Erosion_iter = QLabel(self.grp_Erosion)
        self.lbl_Erosion_iter.setObjectName(u"lbl_Erosion_iter")

        self.horizontalLayout_4.addWidget(self.lbl_Erosion_iter)

        self.sBox_Erosion_iter = QSpinBox(self.grp_Erosion)
        self.sBox_Erosion_iter.setObjectName(u"sBox_Erosion_iter")
        self.sBox_Erosion_iter.setMinimum(1)
        self.sBox_Erosion_iter.setSingleStep(1)
        self.sBox_Erosion_iter.setValue(1)

        self.horizontalLayout_4.addWidget(self.sBox_Erosion_iter)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.pBtn_Erosion_Apply = QPushButton(self.grp_Erosion)
        self.pBtn_Erosion_Apply.setObjectName(u"pBtn_Erosion_Apply")

        self.verticalLayout_2.addWidget(self.pBtn_Erosion_Apply)


        self.horizontalLayout_12.addWidget(self.grp_Erosion)

        self.grp_Opening = QGroupBox(MorphologyDialog)
        self.grp_Opening.setObjectName(u"grp_Opening")
        self.verticalLayout_3 = QVBoxLayout(self.grp_Opening)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_Opening_k_xy = QLabel(self.grp_Opening)
        self.lbl_Opening_k_xy.setObjectName(u"lbl_Opening_k_xy")

        self.horizontalLayout_5.addWidget(self.lbl_Opening_k_xy)

        self.sBox_Opening_k_xy = QSpinBox(self.grp_Opening)
        self.sBox_Opening_k_xy.setObjectName(u"sBox_Opening_k_xy")
        self.sBox_Opening_k_xy.setMinimum(3)
        self.sBox_Opening_k_xy.setSingleStep(2)

        self.horizontalLayout_5.addWidget(self.sBox_Opening_k_xy)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_Opening_iter = QLabel(self.grp_Opening)
        self.lbl_Opening_iter.setObjectName(u"lbl_Opening_iter")

        self.horizontalLayout_6.addWidget(self.lbl_Opening_iter)

        self.sBox_Opening_iter = QSpinBox(self.grp_Opening)
        self.sBox_Opening_iter.setObjectName(u"sBox_Opening_iter")
        self.sBox_Opening_iter.setMinimum(1)
        self.sBox_Opening_iter.setSingleStep(1)
        self.sBox_Opening_iter.setValue(1)

        self.horizontalLayout_6.addWidget(self.sBox_Opening_iter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.pBtn_Opening_Apply = QPushButton(self.grp_Opening)
        self.pBtn_Opening_Apply.setObjectName(u"pBtn_Opening_Apply")

        self.verticalLayout_3.addWidget(self.pBtn_Opening_Apply)


        self.horizontalLayout_12.addWidget(self.grp_Opening)

        self.grp_Closing = QGroupBox(MorphologyDialog)
        self.grp_Closing.setObjectName(u"grp_Closing")
        self.verticalLayout_4 = QVBoxLayout(self.grp_Closing)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_Closing_k_xy = QLabel(self.grp_Closing)
        self.lbl_Closing_k_xy.setObjectName(u"lbl_Closing_k_xy")

        self.horizontalLayout_7.addWidget(self.lbl_Closing_k_xy)

        self.sBox_Closing_k_xy = QSpinBox(self.grp_Closing)
        self.sBox_Closing_k_xy.setObjectName(u"sBox_Closing_k_xy")
        self.sBox_Closing_k_xy.setMinimum(3)
        self.sBox_Closing_k_xy.setSingleStep(2)

        self.horizontalLayout_7.addWidget(self.sBox_Closing_k_xy)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_Closing_iter = QLabel(self.grp_Closing)
        self.lbl_Closing_iter.setObjectName(u"lbl_Closing_iter")

        self.horizontalLayout_8.addWidget(self.lbl_Closing_iter)

        self.sBox_Closing_iter = QSpinBox(self.grp_Closing)
        self.sBox_Closing_iter.setObjectName(u"sBox_Closing_iter")
        self.sBox_Closing_iter.setMinimum(1)
        self.sBox_Closing_iter.setSingleStep(1)
        self.sBox_Closing_iter.setValue(1)

        self.horizontalLayout_8.addWidget(self.sBox_Closing_iter)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.pBtn_Closing_Apply = QPushButton(self.grp_Closing)
        self.pBtn_Closing_Apply.setObjectName(u"pBtn_Closing_Apply")

        self.verticalLayout_4.addWidget(self.pBtn_Closing_Apply)


        self.horizontalLayout_12.addWidget(self.grp_Closing)

        self.grp_Outline = QGroupBox(MorphologyDialog)
        self.grp_Outline.setObjectName(u"grp_Outline")
        self.verticalLayout_5 = QVBoxLayout(self.grp_Outline)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_Outline_k_xy = QLabel(self.grp_Outline)
        self.lbl_Outline_k_xy.setObjectName(u"lbl_Outline_k_xy")

        self.horizontalLayout_9.addWidget(self.lbl_Outline_k_xy)

        self.sBox_Outline_k_xy = QSpinBox(self.grp_Outline)
        self.sBox_Outline_k_xy.setObjectName(u"sBox_Outline_k_xy")
        self.sBox_Outline_k_xy.setMinimum(3)
        self.sBox_Outline_k_xy.setSingleStep(2)

        self.horizontalLayout_9.addWidget(self.sBox_Outline_k_xy)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_Outline_iter = QLabel(self.grp_Outline)
        self.lbl_Outline_iter.setObjectName(u"lbl_Outline_iter")

        self.horizontalLayout_10.addWidget(self.lbl_Outline_iter)

        self.sBox_Outline_iter = QSpinBox(self.grp_Outline)
        self.sBox_Outline_iter.setObjectName(u"sBox_Outline_iter")
        self.sBox_Outline_iter.setMinimum(1)
        self.sBox_Outline_iter.setSingleStep(1)
        self.sBox_Outline_iter.setValue(1)

        self.horizontalLayout_10.addWidget(self.sBox_Outline_iter)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.pBtn_Outline_Apply = QPushButton(self.grp_Outline)
        self.pBtn_Outline_Apply.setObjectName(u"pBtn_Outline_Apply")

        self.verticalLayout_5.addWidget(self.pBtn_Outline_Apply)


        self.horizontalLayout_12.addWidget(self.grp_Outline)


        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(MorphologyDialog)

        QMetaObject.connectSlotsByName(MorphologyDialog)
    # setupUi

    def retranslateUi(self, MorphologyDialog):
        MorphologyDialog.setWindowTitle(QCoreApplication.translate("MorphologyDialog", u"MorphologyDialog", None))
        self.grp_Dilation.setTitle(QCoreApplication.translate("MorphologyDialog", u"Dilation", None))
        self.lbl_Dilation_k_xy.setText(QCoreApplication.translate("MorphologyDialog", u"k_xy", None))
        self.lbl_Dilation_iter.setText(QCoreApplication.translate("MorphologyDialog", u"iter", None))
        self.pBtn_Dilation_Apply.setText(QCoreApplication.translate("MorphologyDialog", u"Apply", None))
        self.grp_Erosion.setTitle(QCoreApplication.translate("MorphologyDialog", u"Erosion", None))
        self.lbl_Erosion_k_xy.setText(QCoreApplication.translate("MorphologyDialog", u"k_xy", None))
        self.lbl_Erosion_iter.setText(QCoreApplication.translate("MorphologyDialog", u"iter", None))
        self.pBtn_Erosion_Apply.setText(QCoreApplication.translate("MorphologyDialog", u"Apply", None))
        self.grp_Opening.setTitle(QCoreApplication.translate("MorphologyDialog", u"Opening", None))
        self.lbl_Opening_k_xy.setText(QCoreApplication.translate("MorphologyDialog", u"k_xy", None))
        self.lbl_Opening_iter.setText(QCoreApplication.translate("MorphologyDialog", u"iter", None))
        self.pBtn_Opening_Apply.setText(QCoreApplication.translate("MorphologyDialog", u"Apply", None))
        self.grp_Closing.setTitle(QCoreApplication.translate("MorphologyDialog", u"Closing", None))
        self.lbl_Closing_k_xy.setText(QCoreApplication.translate("MorphologyDialog", u"k_xy", None))
        self.lbl_Closing_iter.setText(QCoreApplication.translate("MorphologyDialog", u"iter", None))
        self.pBtn_Closing_Apply.setText(QCoreApplication.translate("MorphologyDialog", u"Apply", None))
        self.grp_Outline.setTitle(QCoreApplication.translate("MorphologyDialog", u"Outline", None))
        self.lbl_Outline_k_xy.setText(QCoreApplication.translate("MorphologyDialog", u"k_xy", None))
        self.lbl_Outline_iter.setText(QCoreApplication.translate("MorphologyDialog", u"iter", None))
        self.pBtn_Outline_Apply.setText(QCoreApplication.translate("MorphologyDialog", u"Apply", None))
    # retranslateUi

