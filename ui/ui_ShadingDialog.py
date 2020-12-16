# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_ShadingDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ShadingDialog(object):
    def setupUi(self, ShadingDialog):
        if not ShadingDialog.objectName():
            ShadingDialog.setObjectName(u"ShadingDialog")
        ShadingDialog.resize(352, 280)
        self.verticalLayout_3 = QVBoxLayout(ShadingDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.grp_Shading_Generate_Base_Image = QGroupBox(ShadingDialog)
        self.grp_Shading_Generate_Base_Image.setObjectName(u"grp_Shading_Generate_Base_Image")
        self.horizontalLayout_2 = QHBoxLayout(self.grp_Shading_Generate_Base_Image)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rBtn_Shading_Gaussian_Blur = QRadioButton(self.grp_Shading_Generate_Base_Image)
        self.rBtn_Shading_Gaussian_Blur.setObjectName(u"rBtn_Shading_Gaussian_Blur")
        self.rBtn_Shading_Gaussian_Blur.setChecked(True)

        self.verticalLayout.addWidget(self.rBtn_Shading_Gaussian_Blur)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_Shading_Gaussian_k_x = QLabel(self.grp_Shading_Generate_Base_Image)
        self.lbl_Shading_Gaussian_k_x.setObjectName(u"lbl_Shading_Gaussian_k_x")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_Shading_Gaussian_k_x)

        self.sBox_Shading_Gaussian_k_x = QSpinBox(self.grp_Shading_Generate_Base_Image)
        self.sBox_Shading_Gaussian_k_x.setObjectName(u"sBox_Shading_Gaussian_k_x")
        self.sBox_Shading_Gaussian_k_x.setMinimum(3)
        self.sBox_Shading_Gaussian_k_x.setSingleStep(2)
        self.sBox_Shading_Gaussian_k_x.setValue(3)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.sBox_Shading_Gaussian_k_x)

        self.lbl_Shading_Gaussian_k_y = QLabel(self.grp_Shading_Generate_Base_Image)
        self.lbl_Shading_Gaussian_k_y.setObjectName(u"lbl_Shading_Gaussian_k_y")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_Shading_Gaussian_k_y)

        self.sBox_Shading_Gaussian_k_y = QSpinBox(self.grp_Shading_Generate_Base_Image)
        self.sBox_Shading_Gaussian_k_y.setObjectName(u"sBox_Shading_Gaussian_k_y")
        self.sBox_Shading_Gaussian_k_y.setMinimum(3)
        self.sBox_Shading_Gaussian_k_y.setSingleStep(2)
        self.sBox_Shading_Gaussian_k_y.setValue(3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.sBox_Shading_Gaussian_k_y)

        self.lbl_Shading_Gaussian_std_x = QLabel(self.grp_Shading_Generate_Base_Image)
        self.lbl_Shading_Gaussian_std_x.setObjectName(u"lbl_Shading_Gaussian_std_x")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_Shading_Gaussian_std_x)

        self.dsBox_Shading_Gaussian_std_x = QDoubleSpinBox(self.grp_Shading_Generate_Base_Image)
        self.dsBox_Shading_Gaussian_std_x.setObjectName(u"dsBox_Shading_Gaussian_std_x")
        self.dsBox_Shading_Gaussian_std_x.setMinimum(0.100000000000000)
        self.dsBox_Shading_Gaussian_std_x.setMaximum(5.000000000000000)
        self.dsBox_Shading_Gaussian_std_x.setSingleStep(0.100000000000000)
        self.dsBox_Shading_Gaussian_std_x.setValue(1.300000000000000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.dsBox_Shading_Gaussian_std_x)

        self.lbl_Shading_Gaussian_std_y = QLabel(self.grp_Shading_Generate_Base_Image)
        self.lbl_Shading_Gaussian_std_y.setObjectName(u"lbl_Shading_Gaussian_std_y")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lbl_Shading_Gaussian_std_y)

        self.dsBox_Shading_Gaussian_std_y = QDoubleSpinBox(self.grp_Shading_Generate_Base_Image)
        self.dsBox_Shading_Gaussian_std_y.setObjectName(u"dsBox_Shading_Gaussian_std_y")
        self.dsBox_Shading_Gaussian_std_y.setMinimum(0.100000000000000)
        self.dsBox_Shading_Gaussian_std_y.setMaximum(5.000000000000000)
        self.dsBox_Shading_Gaussian_std_y.setSingleStep(0.100000000000000)
        self.dsBox_Shading_Gaussian_std_y.setValue(1.300000000000000)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.dsBox_Shading_Gaussian_std_y)

        self.pBtn_Shading_Gaussian_Check = QPushButton(self.grp_Shading_Generate_Base_Image)
        self.pBtn_Shading_Gaussian_Check.setObjectName(u"pBtn_Shading_Gaussian_Check")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.pBtn_Shading_Gaussian_Check)


        self.verticalLayout.addLayout(self.formLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rBtn_Shading_Median_Blur = QRadioButton(self.grp_Shading_Generate_Base_Image)
        self.rBtn_Shading_Median_Blur.setObjectName(u"rBtn_Shading_Median_Blur")

        self.verticalLayout_2.addWidget(self.rBtn_Shading_Median_Blur)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lbl_Shading_Median_k_xy = QLabel(self.grp_Shading_Generate_Base_Image)
        self.lbl_Shading_Median_k_xy.setObjectName(u"lbl_Shading_Median_k_xy")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lbl_Shading_Median_k_xy)

        self.sBox_Shadng_Median_k_xy = QSpinBox(self.grp_Shading_Generate_Base_Image)
        self.sBox_Shadng_Median_k_xy.setObjectName(u"sBox_Shadng_Median_k_xy")
        self.sBox_Shadng_Median_k_xy.setMinimum(3)
        self.sBox_Shadng_Median_k_xy.setSingleStep(2)
        self.sBox_Shadng_Median_k_xy.setValue(3)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.sBox_Shadng_Median_k_xy)

        self.pBtn_Shading_Meidan_Check = QPushButton(self.grp_Shading_Generate_Base_Image)
        self.pBtn_Shading_Meidan_Check.setObjectName(u"pBtn_Shading_Meidan_Check")

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.pBtn_Shading_Meidan_Check)


        self.verticalLayout_2.addLayout(self.formLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.grp_Shading_Generate_Base_Image)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Shading_Gain = QLabel(ShadingDialog)
        self.lbl_Shading_Gain.setObjectName(u"lbl_Shading_Gain")

        self.horizontalLayout.addWidget(self.lbl_Shading_Gain)

        self.dsBox_Shading_Gain = QDoubleSpinBox(ShadingDialog)
        self.dsBox_Shading_Gain.setObjectName(u"dsBox_Shading_Gain")
        self.dsBox_Shading_Gain.setMaximum(5.000000000000000)
        self.dsBox_Shading_Gain.setSingleStep(0.100000000000000)
        self.dsBox_Shading_Gain.setValue(3.500000000000000)

        self.horizontalLayout.addWidget(self.dsBox_Shading_Gain)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.pBtn_Shading_Correction_Apply = QPushButton(ShadingDialog)
        self.pBtn_Shading_Correction_Apply.setObjectName(u"pBtn_Shading_Correction_Apply")

        self.horizontalLayout_3.addWidget(self.pBtn_Shading_Correction_Apply)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(ShadingDialog)

        QMetaObject.connectSlotsByName(ShadingDialog)
    # setupUi

    def retranslateUi(self, ShadingDialog):
        ShadingDialog.setWindowTitle(QCoreApplication.translate("ShadingDialog", u"ShadingDialog", None))
        self.grp_Shading_Generate_Base_Image.setTitle(QCoreApplication.translate("ShadingDialog", u"Generate Base Image", None))
        self.rBtn_Shading_Gaussian_Blur.setText(QCoreApplication.translate("ShadingDialog", u"Gaussian Blur", None))
        self.lbl_Shading_Gaussian_k_x.setText(QCoreApplication.translate("ShadingDialog", u"k_x", None))
        self.lbl_Shading_Gaussian_k_y.setText(QCoreApplication.translate("ShadingDialog", u"k_y", None))
        self.lbl_Shading_Gaussian_std_x.setText(QCoreApplication.translate("ShadingDialog", u"std_x", None))
        self.lbl_Shading_Gaussian_std_y.setText(QCoreApplication.translate("ShadingDialog", u"std_y", None))
        self.pBtn_Shading_Gaussian_Check.setText(QCoreApplication.translate("ShadingDialog", u"Check", None))
        self.rBtn_Shading_Median_Blur.setText(QCoreApplication.translate("ShadingDialog", u"Median Blur", None))
        self.lbl_Shading_Median_k_xy.setText(QCoreApplication.translate("ShadingDialog", u"k xy", None))
        self.pBtn_Shading_Meidan_Check.setText(QCoreApplication.translate("ShadingDialog", u"Check", None))
        self.lbl_Shading_Gain.setText(QCoreApplication.translate("ShadingDialog", u"Gain", None))
        self.pBtn_Shading_Correction_Apply.setText(QCoreApplication.translate("ShadingDialog", u"Apply", None))
    # retranslateUi

