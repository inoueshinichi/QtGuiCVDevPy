# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_BlurDialog.ui'
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


class Ui_BlurDialog(object):
    def setupUi(self, BlurDialog):
        if BlurDialog.objectName():
            BlurDialog.setObjectName(u"BlurDialog")
        BlurDialog.resize(348, 219)
        BlurDialog.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(BlurDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(BlurDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.Gaussian_tab = QWidget()
        self.Gaussian_tab.setObjectName(u"Gaussian_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.Gaussian_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.grp_Gaussian_Normal = QGroupBox(self.Gaussian_tab)
        self.grp_Gaussian_Normal.setObjectName(u"grp_Gaussian_Normal")
        self.horizontalLayout_2 = QHBoxLayout(self.grp_Gaussian_Normal)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_Gaussian_k_x = QLabel(self.grp_Gaussian_Normal)
        self.lbl_Gaussian_k_x.setObjectName(u"lbl_Gaussian_k_x")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_Gaussian_k_x)

        self.sBox_Gaussian_k_x = QSpinBox(self.grp_Gaussian_Normal)
        self.sBox_Gaussian_k_x.setObjectName(u"sBox_Gaussian_k_x")
        self.sBox_Gaussian_k_x.setMinimum(3)
        self.sBox_Gaussian_k_x.setSingleStep(2)
        self.sBox_Gaussian_k_x.setValue(3)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.sBox_Gaussian_k_x)

        self.lbl_Gaussian_k_y = QLabel(self.grp_Gaussian_Normal)
        self.lbl_Gaussian_k_y.setObjectName(u"lbl_Gaussian_k_y")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_Gaussian_k_y)

        self.sBox_Gaussian_k_y = QSpinBox(self.grp_Gaussian_Normal)
        self.sBox_Gaussian_k_y.setObjectName(u"sBox_Gaussian_k_y")
        self.sBox_Gaussian_k_y.setMinimum(3)
        self.sBox_Gaussian_k_y.setSingleStep(2)
        self.sBox_Gaussian_k_y.setValue(3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.sBox_Gaussian_k_y)

        self.lbl_Gaussian_std_x = QLabel(self.grp_Gaussian_Normal)
        self.lbl_Gaussian_std_x.setObjectName(u"lbl_Gaussian_std_x")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_Gaussian_std_x)

        self.dsBox_Gaussian_std_x = QDoubleSpinBox(self.grp_Gaussian_Normal)
        self.dsBox_Gaussian_std_x.setObjectName(u"dsBox_Gaussian_std_x")
        self.dsBox_Gaussian_std_x.setMinimum(0.100000000000000)
        self.dsBox_Gaussian_std_x.setMaximum(5.000000000000000)
        self.dsBox_Gaussian_std_x.setSingleStep(0.100000000000000)
        self.dsBox_Gaussian_std_x.setValue(1.300000000000000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.dsBox_Gaussian_std_x)

        self.lbl_Gaussian_std_y = QLabel(self.grp_Gaussian_Normal)
        self.lbl_Gaussian_std_y.setObjectName(u"lbl_Gaussian_std_y")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lbl_Gaussian_std_y)

        self.dsBox_Gaussian_std_y = QDoubleSpinBox(self.grp_Gaussian_Normal)
        self.dsBox_Gaussian_std_y.setObjectName(u"dsBox_Gaussian_std_y")
        self.dsBox_Gaussian_std_y.setMinimum(0.100000000000000)
        self.dsBox_Gaussian_std_y.setMaximum(5.000000000000000)
        self.dsBox_Gaussian_std_y.setSingleStep(0.100000000000000)
        self.dsBox_Gaussian_std_y.setValue(1.300000000000000)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.dsBox_Gaussian_std_y)

        self.pBtn_Gaussian_Apply = QPushButton(self.grp_Gaussian_Normal)
        self.pBtn_Gaussian_Apply.setObjectName(u"pBtn_Gaussian_Apply")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.pBtn_Gaussian_Apply)


        self.horizontalLayout_2.addLayout(self.formLayout_3)


        self.horizontalLayout_4.addWidget(self.grp_Gaussian_Normal)

        self.grp_Gaussian_Expart = QGroupBox(self.Gaussian_tab)
        self.grp_Gaussian_Expart.setObjectName(u"grp_Gaussian_Expart")
        self.horizontalLayout_3 = QHBoxLayout(self.grp_Gaussian_Expart)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addWidget(self.grp_Gaussian_Expart)

        self.tabWidget.addTab(self.Gaussian_tab, "")
        self.Median_tab = QWidget()
        self.Median_tab.setObjectName(u"Median_tab")
        self.horizontalLayout_7 = QHBoxLayout(self.Median_tab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.grp_Median_Normal = QGroupBox(self.Median_tab)
        self.grp_Median_Normal.setObjectName(u"grp_Median_Normal")
        self.horizontalLayout_5 = QHBoxLayout(self.grp_Median_Normal)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lbl_Median_k_xy = QLabel(self.grp_Median_Normal)
        self.lbl_Median_k_xy.setObjectName(u"lbl_Median_k_xy")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lbl_Median_k_xy)

        self.sBox_Median_k_xy = QSpinBox(self.grp_Median_Normal)
        self.sBox_Median_k_xy.setObjectName(u"sBox_Median_k_xy")
        self.sBox_Median_k_xy.setMinimum(3)
        self.sBox_Median_k_xy.setSingleStep(2)
        self.sBox_Median_k_xy.setValue(3)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.sBox_Median_k_xy)

        self.pBtn_Meidan_Apply = QPushButton(self.grp_Median_Normal)
        self.pBtn_Meidan_Apply.setObjectName(u"pBtn_Meidan_Apply")

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.pBtn_Meidan_Apply)


        self.horizontalLayout_5.addLayout(self.formLayout_4)


        self.horizontalLayout_7.addWidget(self.grp_Median_Normal)

        self.grp_Median_Expart = QGroupBox(self.Median_tab)
        self.grp_Median_Expart.setObjectName(u"grp_Median_Expart")
        self.horizontalLayout_6 = QHBoxLayout(self.grp_Median_Expart)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_7.addWidget(self.grp_Median_Expart)

        self.tabWidget.addTab(self.Median_tab, "")
        self.Other_tab = QWidget()
        self.Other_tab.setObjectName(u"Other_tab")
        self.horizontalLayout_10 = QHBoxLayout(self.Other_tab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.grp_Bilateral = QGroupBox(self.Other_tab)
        self.grp_Bilateral.setObjectName(u"grp_Bilateral")
        self.horizontalLayout_8 = QHBoxLayout(self.grp_Bilateral)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.lbl_Bilateral_k_xy = QLabel(self.grp_Bilateral)
        self.lbl_Bilateral_k_xy.setObjectName(u"lbl_Bilateral_k_xy")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.lbl_Bilateral_k_xy)

        self.sBox_Bilateral_k_xy = QSpinBox(self.grp_Bilateral)
        self.sBox_Bilateral_k_xy.setObjectName(u"sBox_Bilateral_k_xy")
        self.sBox_Bilateral_k_xy.setMinimum(3)
        self.sBox_Bilateral_k_xy.setSingleStep(2)
        self.sBox_Bilateral_k_xy.setValue(3)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.sBox_Bilateral_k_xy)

        self.lbl_Bilateral_std_space = QLabel(self.grp_Bilateral)
        self.lbl_Bilateral_std_space.setObjectName(u"lbl_Bilateral_std_space")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.lbl_Bilateral_std_space)

        self.dsBox_Bilateral_std_space = QDoubleSpinBox(self.grp_Bilateral)
        self.dsBox_Bilateral_std_space.setObjectName(u"dsBox_Bilateral_std_space")
        self.dsBox_Bilateral_std_space.setMinimum(10.000000000000000)
        self.dsBox_Bilateral_std_space.setMaximum(300.000000000000000)
        self.dsBox_Bilateral_std_space.setSingleStep(1.000000000000000)
        self.dsBox_Bilateral_std_space.setValue(20.000000000000000)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.dsBox_Bilateral_std_space)

        self.lbl_Bilateral_std_luminance = QLabel(self.grp_Bilateral)
        self.lbl_Bilateral_std_luminance.setObjectName(u"lbl_Bilateral_std_luminance")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.lbl_Bilateral_std_luminance)

        self.dsBox_Bilateral_std_luminace = QDoubleSpinBox(self.grp_Bilateral)
        self.dsBox_Bilateral_std_luminace.setObjectName(u"dsBox_Bilateral_std_luminace")
        self.dsBox_Bilateral_std_luminace.setMinimum(10.000000000000000)
        self.dsBox_Bilateral_std_luminace.setMaximum(200.000000000000000)
        self.dsBox_Bilateral_std_luminace.setSingleStep(1.000000000000000)
        self.dsBox_Bilateral_std_luminace.setValue(10.000000000000000)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.dsBox_Bilateral_std_luminace)

        self.pBtn_Bilateral_Apply = QPushButton(self.grp_Bilateral)
        self.pBtn_Bilateral_Apply.setObjectName(u"pBtn_Bilateral_Apply")

        self.formLayout_5.setWidget(3, QFormLayout.SpanningRole, self.pBtn_Bilateral_Apply)


        self.horizontalLayout_8.addLayout(self.formLayout_5)


        self.horizontalLayout_10.addWidget(self.grp_Bilateral)

        self.grp_Mosaic = QGroupBox(self.Other_tab)
        self.grp_Mosaic.setObjectName(u"grp_Mosaic")
        self.formLayout_6 = QFormLayout(self.grp_Mosaic)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lbl_Mosaic_block_x = QLabel(self.grp_Mosaic)
        self.lbl_Mosaic_block_x.setObjectName(u"lbl_Mosaic_block_x")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.lbl_Mosaic_block_x)

        self.sBox_Mosaic_block_x = QSpinBox(self.grp_Mosaic)
        self.sBox_Mosaic_block_x.setObjectName(u"sBox_Mosaic_block_x")
        self.sBox_Mosaic_block_x.setMinimum(3)
        self.sBox_Mosaic_block_x.setSingleStep(1)
        self.sBox_Mosaic_block_x.setValue(5)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.sBox_Mosaic_block_x)

        self.lbl_Mosaic_block_y = QLabel(self.grp_Mosaic)
        self.lbl_Mosaic_block_y.setObjectName(u"lbl_Mosaic_block_y")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.lbl_Mosaic_block_y)

        self.sBox_Mosaic_block_y = QSpinBox(self.grp_Mosaic)
        self.sBox_Mosaic_block_y.setObjectName(u"sBox_Mosaic_block_y")
        self.sBox_Mosaic_block_y.setMinimum(3)
        self.sBox_Mosaic_block_y.setSingleStep(1)
        self.sBox_Mosaic_block_y.setValue(5)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.sBox_Mosaic_block_y)

        self.pBtn_Mosaic_Apply = QPushButton(self.grp_Mosaic)
        self.pBtn_Mosaic_Apply.setObjectName(u"pBtn_Mosaic_Apply")

        self.formLayout_6.setWidget(2, QFormLayout.SpanningRole, self.pBtn_Mosaic_Apply)


        self.horizontalLayout_10.addWidget(self.grp_Mosaic)

        self.tabWidget.addTab(self.Other_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(BlurDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BlurDialog)
    # setupUi

    def retranslateUi(self, BlurDialog):
        BlurDialog.setWindowTitle(QCoreApplication.translate("BlurDialog", u"BlurDialog", None))
        self.grp_Gaussian_Normal.setTitle(QCoreApplication.translate("BlurDialog", u"Normal", None))
        self.lbl_Gaussian_k_x.setText(QCoreApplication.translate("BlurDialog", u"k_x", None))
        self.lbl_Gaussian_k_y.setText(QCoreApplication.translate("BlurDialog", u"k_y", None))
        self.lbl_Gaussian_std_x.setText(QCoreApplication.translate("BlurDialog", u"std_x", None))
        self.lbl_Gaussian_std_y.setText(QCoreApplication.translate("BlurDialog", u"std_y", None))
        self.pBtn_Gaussian_Apply.setText(QCoreApplication.translate("BlurDialog", u"Apply", None))
        self.grp_Gaussian_Expart.setTitle(QCoreApplication.translate("BlurDialog", u"Expart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gaussian_tab), QCoreApplication.translate("BlurDialog", u"Gaussian", None))
        self.grp_Median_Normal.setTitle(QCoreApplication.translate("BlurDialog", u"Normal", None))
        self.lbl_Median_k_xy.setText(QCoreApplication.translate("BlurDialog", u"k xy", None))
        self.pBtn_Meidan_Apply.setText(QCoreApplication.translate("BlurDialog", u"Apply", None))
        self.grp_Median_Expart.setTitle(QCoreApplication.translate("BlurDialog", u"Expart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Median_tab), QCoreApplication.translate("BlurDialog", u"Median", None))
        self.grp_Bilateral.setTitle(QCoreApplication.translate("BlurDialog", u"Bilateral", None))
        self.lbl_Bilateral_k_xy.setText(QCoreApplication.translate("BlurDialog", u"k xy", None))
        self.lbl_Bilateral_std_space.setText(QCoreApplication.translate("BlurDialog", u"space std", None))
        self.lbl_Bilateral_std_luminance.setText(QCoreApplication.translate("BlurDialog", u"luminance std", None))
        self.pBtn_Bilateral_Apply.setText(QCoreApplication.translate("BlurDialog", u"Apply", None))
        self.grp_Mosaic.setTitle(QCoreApplication.translate("BlurDialog", u"Mosaic", None))
        self.lbl_Mosaic_block_x.setText(QCoreApplication.translate("BlurDialog", u"block_x", None))
        self.lbl_Mosaic_block_y.setText(QCoreApplication.translate("BlurDialog", u"block_y", None))
        self.pBtn_Mosaic_Apply.setText(QCoreApplication.translate("BlurDialog", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Other_tab), QCoreApplication.translate("BlurDialog", u"Other", None))
    # retranslateUi

