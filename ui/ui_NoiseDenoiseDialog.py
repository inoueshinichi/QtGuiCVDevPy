# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NoiseDenoiseDialog.ui'
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


class Ui_NoiseDenoiseDialog(object):
    def setupUi(self, NoiseDenoiseDialog):
        if NoiseDenoiseDialog.objectName():
            NoiseDenoiseDialog.setObjectName(u"NoiseDenoiseDialog")
        NoiseDenoiseDialog.resize(420, 172)
        self.horizontalLayout_8 = QHBoxLayout(NoiseDenoiseDialog)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.grp_Uniform = QGroupBox(NoiseDenoiseDialog)
        self.grp_Uniform.setObjectName(u"grp_Uniform")
        self.verticalLayout_2 = QVBoxLayout(self.grp_Uniform)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Uniform_Lower = QLabel(self.grp_Uniform)
        self.lbl_Uniform_Lower.setObjectName(u"lbl_Uniform_Lower")

        self.horizontalLayout.addWidget(self.lbl_Uniform_Lower)

        self.sBox_Uniform_Lower = QSpinBox(self.grp_Uniform)
        self.sBox_Uniform_Lower.setObjectName(u"sBox_Uniform_Lower")
        self.sBox_Uniform_Lower.setMinimum(-255)
        self.sBox_Uniform_Lower.setMaximum(255)
        self.sBox_Uniform_Lower.setValue(-10)

        self.horizontalLayout.addWidget(self.sBox_Uniform_Lower)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Uniform_Upper = QLabel(self.grp_Uniform)
        self.lbl_Uniform_Upper.setObjectName(u"lbl_Uniform_Upper")

        self.horizontalLayout_2.addWidget(self.lbl_Uniform_Upper)

        self.sBox_Uniform_Upper = QSpinBox(self.grp_Uniform)
        self.sBox_Uniform_Upper.setObjectName(u"sBox_Uniform_Upper")
        self.sBox_Uniform_Upper.setMinimum(-254)
        self.sBox_Uniform_Upper.setMaximum(256)
        self.sBox_Uniform_Upper.setValue(10)
        self.sBox_Uniform_Upper.setDisplayIntegerBase(10)

        self.horizontalLayout_2.addWidget(self.sBox_Uniform_Upper)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pBtn_Uniform_Apply = QPushButton(self.grp_Uniform)
        self.pBtn_Uniform_Apply.setObjectName(u"pBtn_Uniform_Apply")

        self.verticalLayout_2.addWidget(self.pBtn_Uniform_Apply)


        self.horizontalLayout_8.addWidget(self.grp_Uniform)

        self.grp_Standard = QGroupBox(NoiseDenoiseDialog)
        self.grp_Standard.setObjectName(u"grp_Standard")
        self.verticalLayout_3 = QVBoxLayout(self.grp_Standard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Standard_Mean = QLabel(self.grp_Standard)
        self.lbl_Standard_Mean.setObjectName(u"lbl_Standard_Mean")

        self.horizontalLayout_3.addWidget(self.lbl_Standard_Mean)

        self.dsBox_Standard_Mean = QDoubleSpinBox(self.grp_Standard)
        self.dsBox_Standard_Mean.setObjectName(u"dsBox_Standard_Mean")
        self.dsBox_Standard_Mean.setMaximum(255.000000000000000)

        self.horizontalLayout_3.addWidget(self.dsBox_Standard_Mean)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_Standard_Sigma = QLabel(self.grp_Standard)
        self.lbl_Standard_Sigma.setObjectName(u"lbl_Standard_Sigma")

        self.horizontalLayout_4.addWidget(self.lbl_Standard_Sigma)

        self.dsBox_Standard_Sigma = QDoubleSpinBox(self.grp_Standard)
        self.dsBox_Standard_Sigma.setObjectName(u"dsBox_Standard_Sigma")
        self.dsBox_Standard_Sigma.setMaximum(100.000000000000000)
        self.dsBox_Standard_Sigma.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.dsBox_Standard_Sigma)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.pBtn_Standard_Apply = QPushButton(self.grp_Standard)
        self.pBtn_Standard_Apply.setObjectName(u"pBtn_Standard_Apply")

        self.verticalLayout_3.addWidget(self.pBtn_Standard_Apply)


        self.horizontalLayout_8.addWidget(self.grp_Standard)

        self.groupBox = QGroupBox(NoiseDenoiseDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_ROF = QLabel(self.groupBox)
        self.lbl_ROF.setObjectName(u"lbl_ROF")

        self.verticalLayout_4.addWidget(self.lbl_ROF)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_ROF_Tolerance = QLabel(self.groupBox)
        self.lbl_ROF_Tolerance.setObjectName(u"lbl_ROF_Tolerance")

        self.horizontalLayout_5.addWidget(self.lbl_ROF_Tolerance)

        self.dsBox_ROF_Tolerance = QDoubleSpinBox(self.groupBox)
        self.dsBox_ROF_Tolerance.setObjectName(u"dsBox_ROF_Tolerance")
        self.dsBox_ROF_Tolerance.setMaximum(1.000000000000000)
        self.dsBox_ROF_Tolerance.setSingleStep(0.100000000000000)
        self.dsBox_ROF_Tolerance.setValue(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.dsBox_ROF_Tolerance)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_ROF_Step = QLabel(self.groupBox)
        self.lbl_ROF_Step.setObjectName(u"lbl_ROF_Step")

        self.horizontalLayout_6.addWidget(self.lbl_ROF_Step)

        self.dsBox_ROF_Step = QDoubleSpinBox(self.groupBox)
        self.dsBox_ROF_Step.setObjectName(u"dsBox_ROF_Step")
        self.dsBox_ROF_Step.setDecimals(3)
        self.dsBox_ROF_Step.setMaximum(1.000000000000000)
        self.dsBox_ROF_Step.setSingleStep(0.001000000000000)
        self.dsBox_ROF_Step.setValue(0.125000000000000)

        self.horizontalLayout_6.addWidget(self.dsBox_ROF_Step)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_ROF_Norm_Weight = QLabel(self.groupBox)
        self.lbl_ROF_Norm_Weight.setObjectName(u"lbl_ROF_Norm_Weight")

        self.horizontalLayout_7.addWidget(self.lbl_ROF_Norm_Weight)

        self.sBox_ROF_Norm_Weight = QSpinBox(self.groupBox)
        self.sBox_ROF_Norm_Weight.setObjectName(u"sBox_ROF_Norm_Weight")
        self.sBox_ROF_Norm_Weight.setMaximum(255)
        self.sBox_ROF_Norm_Weight.setValue(100)

        self.horizontalLayout_7.addWidget(self.sBox_ROF_Norm_Weight)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.pBtn_ROF_Apply = QPushButton(self.groupBox)
        self.pBtn_ROF_Apply.setObjectName(u"pBtn_ROF_Apply")

        self.verticalLayout_4.addWidget(self.pBtn_ROF_Apply)


        self.horizontalLayout_8.addWidget(self.groupBox)


        self.retranslateUi(NoiseDenoiseDialog)

        QMetaObject.connectSlotsByName(NoiseDenoiseDialog)
    # setupUi

    def retranslateUi(self, NoiseDenoiseDialog):
        NoiseDenoiseDialog.setWindowTitle(QCoreApplication.translate("NoiseDenoiseDialog", u"NoiseDenoiseDialog", None))
        self.grp_Uniform.setTitle(QCoreApplication.translate("NoiseDenoiseDialog", u"Uniform_Noise", None))
        self.lbl_Uniform_Lower.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Lower", None))
        self.lbl_Uniform_Upper.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Upper", None))
        self.pBtn_Uniform_Apply.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Apply", None))
        self.grp_Standard.setTitle(QCoreApplication.translate("NoiseDenoiseDialog", u"Standard_Noise", None))
        self.lbl_Standard_Mean.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Mean", None))
        self.lbl_Standard_Sigma.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Sigma", None))
        self.pBtn_Standard_Apply.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Apply", None))
        self.groupBox.setTitle(QCoreApplication.translate("NoiseDenoiseDialog", u"ROF Denoise", None))
        self.lbl_ROF.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Rudin-Osher-Fatemi", None))
        self.lbl_ROF_Tolerance.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Tolerance", None))
        self.lbl_ROF_Step.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Step", None))
        self.lbl_ROF_Norm_Weight.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Norm Weight", None))
        self.pBtn_ROF_Apply.setText(QCoreApplication.translate("NoiseDenoiseDialog", u"Apply", None))
    # retranslateUi

