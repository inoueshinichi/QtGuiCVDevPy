# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_EdgeDetectorDialog.ui'
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


class Ui_EdgeDetectorDialog(object):
    def setupUi(self, EdgeDetectorDialog):
        if EdgeDetectorDialog.objectName():
            EdgeDetectorDialog.setObjectName(u"EdgeDetectorDialog")
        EdgeDetectorDialog.resize(738, 300)
        self.grp_Differential = QGroupBox(EdgeDetectorDialog)
        self.grp_Differential.setObjectName(u"grp_Differential")
        self.grp_Differential.setGeometry(QRect(9, 9, 110, 82))
        self.verticalLayout = QVBoxLayout(self.grp_Differential)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Differential_Direction = QLabel(self.grp_Differential)
        self.lbl_Differential_Direction.setObjectName(u"lbl_Differential_Direction")

        self.horizontalLayout.addWidget(self.lbl_Differential_Direction)

        self.cBox_Differential_Direction = QComboBox(self.grp_Differential)
        self.cBox_Differential_Direction.addItem("")
        self.cBox_Differential_Direction.addItem("")
        self.cBox_Differential_Direction.addItem("")
        self.cBox_Differential_Direction.addItem("")
        self.cBox_Differential_Direction.setObjectName(u"cBox_Differential_Direction")

        self.horizontalLayout.addWidget(self.cBox_Differential_Direction)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pBtn_Differential_Apply = QPushButton(self.grp_Differential)
        self.pBtn_Differential_Apply.setObjectName(u"pBtn_Differential_Apply")

        self.verticalLayout.addWidget(self.pBtn_Differential_Apply)

        self.grp_Prewitt = QGroupBox(EdgeDetectorDialog)
        self.grp_Prewitt.setObjectName(u"grp_Prewitt")
        self.grp_Prewitt.setGeometry(QRect(169, 9, 110, 82))
        self.verticalLayout_2 = QVBoxLayout(self.grp_Prewitt)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Prewitt_Direction = QLabel(self.grp_Prewitt)
        self.lbl_Prewitt_Direction.setObjectName(u"lbl_Prewitt_Direction")

        self.horizontalLayout_2.addWidget(self.lbl_Prewitt_Direction)

        self.cBox_Prewitt_Direction = QComboBox(self.grp_Prewitt)
        self.cBox_Prewitt_Direction.addItem("")
        self.cBox_Prewitt_Direction.addItem("")
        self.cBox_Prewitt_Direction.addItem("")
        self.cBox_Prewitt_Direction.addItem("")
        self.cBox_Prewitt_Direction.setObjectName(u"cBox_Prewitt_Direction")

        self.horizontalLayout_2.addWidget(self.cBox_Prewitt_Direction)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pBtn_Prewitt_Apply = QPushButton(self.grp_Prewitt)
        self.pBtn_Prewitt_Apply.setObjectName(u"pBtn_Prewitt_Apply")

        self.verticalLayout_2.addWidget(self.pBtn_Prewitt_Apply)

        self.grp_Sobel = QGroupBox(EdgeDetectorDialog)
        self.grp_Sobel.setObjectName(u"grp_Sobel")
        self.grp_Sobel.setGeometry(QRect(285, 9, 109, 82))
        self.verticalLayout_3 = QVBoxLayout(self.grp_Sobel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Sobel_Direction = QLabel(self.grp_Sobel)
        self.lbl_Sobel_Direction.setObjectName(u"lbl_Sobel_Direction")

        self.horizontalLayout_3.addWidget(self.lbl_Sobel_Direction)

        self.cBox_Sobel_Direction = QComboBox(self.grp_Sobel)
        self.cBox_Sobel_Direction.addItem("")
        self.cBox_Sobel_Direction.addItem("")
        self.cBox_Sobel_Direction.addItem("")
        self.cBox_Sobel_Direction.addItem("")
        self.cBox_Sobel_Direction.setObjectName(u"cBox_Sobel_Direction")

        self.horizontalLayout_3.addWidget(self.cBox_Sobel_Direction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.pBtn_Sobel_Apply = QPushButton(self.grp_Sobel)
        self.pBtn_Sobel_Apply.setObjectName(u"pBtn_Sobel_Apply")

        self.verticalLayout_3.addWidget(self.pBtn_Sobel_Apply)

        self.grp_XDOG = QGroupBox(EdgeDetectorDialog)
        self.grp_XDOG.setObjectName(u"grp_XDOG")
        self.grp_XDOG.setGeometry(QRect(400, 9, 112, 217))
        self.verticalLayout_7 = QVBoxLayout(self.grp_XDOG)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_XDOG_kxy = QLabel(self.grp_XDOG)
        self.lbl_XDOG_kxy.setObjectName(u"lbl_XDOG_kxy")

        self.horizontalLayout_11.addWidget(self.lbl_XDOG_kxy)

        self.sBox_XDOG_kxy = QSpinBox(self.grp_XDOG)
        self.sBox_XDOG_kxy.setObjectName(u"sBox_XDOG_kxy")
        self.sBox_XDOG_kxy.setMinimum(3)
        self.sBox_XDOG_kxy.setSingleStep(2)

        self.horizontalLayout_11.addWidget(self.sBox_XDOG_kxy)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lbl_XDOG_Sigma = QLabel(self.grp_XDOG)
        self.lbl_XDOG_Sigma.setObjectName(u"lbl_XDOG_Sigma")

        self.horizontalLayout_12.addWidget(self.lbl_XDOG_Sigma)

        self.dsBox_XDOG_Sigma = QDoubleSpinBox(self.grp_XDOG)
        self.dsBox_XDOG_Sigma.setObjectName(u"dsBox_XDOG_Sigma")
        self.dsBox_XDOG_Sigma.setMinimum(0.100000000000000)
        self.dsBox_XDOG_Sigma.setMaximum(30.000000000000000)
        self.dsBox_XDOG_Sigma.setSingleStep(0.100000000000000)
        self.dsBox_XDOG_Sigma.setValue(1.300000000000000)

        self.horizontalLayout_12.addWidget(self.dsBox_XDOG_Sigma)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lbl_XDOG_k = QLabel(self.grp_XDOG)
        self.lbl_XDOG_k.setObjectName(u"lbl_XDOG_k")

        self.horizontalLayout_13.addWidget(self.lbl_XDOG_k)

        self.dsBox_XDOG_k = QDoubleSpinBox(self.grp_XDOG)
        self.dsBox_XDOG_k.setObjectName(u"dsBox_XDOG_k")
        self.dsBox_XDOG_k.setMinimum(0.100000000000000)
        self.dsBox_XDOG_k.setMaximum(5.000000000000000)
        self.dsBox_XDOG_k.setSingleStep(0.100000000000000)
        self.dsBox_XDOG_k.setValue(1.600000000000000)

        self.horizontalLayout_13.addWidget(self.dsBox_XDOG_k)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_XDOG_gamma = QLabel(self.grp_XDOG)
        self.lbl_XDOG_gamma.setObjectName(u"lbl_XDOG_gamma")

        self.horizontalLayout_14.addWidget(self.lbl_XDOG_gamma)

        self.dsBox_XDOG_p = QDoubleSpinBox(self.grp_XDOG)
        self.dsBox_XDOG_p.setObjectName(u"dsBox_XDOG_p")
        self.dsBox_XDOG_p.setMinimum(0.000000000000000)
        self.dsBox_XDOG_p.setMaximum(5.000000000000000)
        self.dsBox_XDOG_p.setSingleStep(0.100000000000000)
        self.dsBox_XDOG_p.setValue(1.000000000000000)

        self.horizontalLayout_14.addWidget(self.dsBox_XDOG_p)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_XDOG_phi = QLabel(self.grp_XDOG)
        self.lbl_XDOG_phi.setObjectName(u"lbl_XDOG_phi")

        self.horizontalLayout_15.addWidget(self.lbl_XDOG_phi)

        self.dsBox_XDOG_phi = QDoubleSpinBox(self.grp_XDOG)
        self.dsBox_XDOG_phi.setObjectName(u"dsBox_XDOG_phi")
        self.dsBox_XDOG_phi.setMinimum(0.100000000000000)
        self.dsBox_XDOG_phi.setMaximum(5.000000000000000)
        self.dsBox_XDOG_phi.setSingleStep(0.100000000000000)
        self.dsBox_XDOG_phi.setValue(1.000000000000000)

        self.horizontalLayout_15.addWidget(self.dsBox_XDOG_phi)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_XDOG_eps = QLabel(self.grp_XDOG)
        self.lbl_XDOG_eps.setObjectName(u"lbl_XDOG_eps")

        self.horizontalLayout_16.addWidget(self.lbl_XDOG_eps)

        self.dsBox_XDOG_eps = QDoubleSpinBox(self.grp_XDOG)
        self.dsBox_XDOG_eps.setObjectName(u"dsBox_XDOG_eps")
        self.dsBox_XDOG_eps.setMinimum(-50.000000000000000)
        self.dsBox_XDOG_eps.setMaximum(50.000000000000000)
        self.dsBox_XDOG_eps.setValue(10.000000000000000)

        self.horizontalLayout_16.addWidget(self.dsBox_XDOG_eps)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.pBtn_XDOG_Apply = QPushButton(self.grp_XDOG)
        self.pBtn_XDOG_Apply.setObjectName(u"pBtn_XDOG_Apply")

        self.verticalLayout_7.addWidget(self.pBtn_XDOG_Apply)

        self.grp_Laplacian = QGroupBox(EdgeDetectorDialog)
        self.grp_Laplacian.setObjectName(u"grp_Laplacian")
        self.grp_Laplacian.setGeometry(QRect(9, 97, 95, 82))
        self.verticalLayout_5 = QVBoxLayout(self.grp_Laplacian)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_Laplacian_kxy = QLabel(self.grp_Laplacian)
        self.lbl_Laplacian_kxy.setObjectName(u"lbl_Laplacian_kxy")

        self.horizontalLayout_6.addWidget(self.lbl_Laplacian_kxy)

        self.sBox_Laplacian_kxy = QSpinBox(self.grp_Laplacian)
        self.sBox_Laplacian_kxy.setObjectName(u"sBox_Laplacian_kxy")
        self.sBox_Laplacian_kxy.setMinimum(3)
        self.sBox_Laplacian_kxy.setSingleStep(2)

        self.horizontalLayout_6.addWidget(self.sBox_Laplacian_kxy)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.pBtn_Laplacian_Apply = QPushButton(self.grp_Laplacian)
        self.pBtn_Laplacian_Apply.setObjectName(u"pBtn_Laplacian_Apply")

        self.verticalLayout_5.addWidget(self.pBtn_Laplacian_Apply)

        self.grp_LOG = QGroupBox(EdgeDetectorDialog)
        self.grp_LOG.setObjectName(u"grp_LOG")
        self.grp_LOG.setGeometry(QRect(110, 97, 112, 109))
        self.verticalLayout_4 = QVBoxLayout(self.grp_LOG)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_LOG_kxy = QLabel(self.grp_LOG)
        self.lbl_LOG_kxy.setObjectName(u"lbl_LOG_kxy")

        self.horizontalLayout_5.addWidget(self.lbl_LOG_kxy)

        self.sBox_LOG_kxy = QSpinBox(self.grp_LOG)
        self.sBox_LOG_kxy.setObjectName(u"sBox_LOG_kxy")
        self.sBox_LOG_kxy.setMinimum(3)
        self.sBox_LOG_kxy.setSingleStep(2)

        self.horizontalLayout_5.addWidget(self.sBox_LOG_kxy)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_LOG_Sigma = QLabel(self.grp_LOG)
        self.lbl_LOG_Sigma.setObjectName(u"lbl_LOG_Sigma")

        self.horizontalLayout_4.addWidget(self.lbl_LOG_Sigma)

        self.dsBox_LOG_Sigma = QDoubleSpinBox(self.grp_LOG)
        self.dsBox_LOG_Sigma.setObjectName(u"dsBox_LOG_Sigma")
        self.dsBox_LOG_Sigma.setMinimum(0.100000000000000)
        self.dsBox_LOG_Sigma.setMaximum(30.000000000000000)
        self.dsBox_LOG_Sigma.setSingleStep(0.100000000000000)
        self.dsBox_LOG_Sigma.setValue(1.300000000000000)

        self.horizontalLayout_4.addWidget(self.dsBox_LOG_Sigma)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.pBtn_LOG_Apply = QPushButton(self.grp_LOG)
        self.pBtn_LOG_Apply.setObjectName(u"pBtn_LOG_Apply")

        self.verticalLayout_4.addWidget(self.pBtn_LOG_Apply)

        self.grp_DOG = QGroupBox(EdgeDetectorDialog)
        self.grp_DOG.setObjectName(u"grp_DOG")
        self.grp_DOG.setGeometry(QRect(228, 97, 112, 163))
        self.verticalLayout_6 = QVBoxLayout(self.grp_DOG)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_DOG_kxy = QLabel(self.grp_DOG)
        self.lbl_DOG_kxy.setObjectName(u"lbl_DOG_kxy")

        self.horizontalLayout_7.addWidget(self.lbl_DOG_kxy)

        self.sBox_DOG_kxy = QSpinBox(self.grp_DOG)
        self.sBox_DOG_kxy.setObjectName(u"sBox_DOG_kxy")
        self.sBox_DOG_kxy.setMinimum(3)
        self.sBox_DOG_kxy.setSingleStep(2)

        self.horizontalLayout_7.addWidget(self.sBox_DOG_kxy)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_DOG_Sigma = QLabel(self.grp_DOG)
        self.lbl_DOG_Sigma.setObjectName(u"lbl_DOG_Sigma")

        self.horizontalLayout_8.addWidget(self.lbl_DOG_Sigma)

        self.dsBox_DOG_Sigma = QDoubleSpinBox(self.grp_DOG)
        self.dsBox_DOG_Sigma.setObjectName(u"dsBox_DOG_Sigma")
        self.dsBox_DOG_Sigma.setMinimum(0.100000000000000)
        self.dsBox_DOG_Sigma.setMaximum(30.000000000000000)
        self.dsBox_DOG_Sigma.setSingleStep(0.100000000000000)
        self.dsBox_DOG_Sigma.setValue(1.300000000000000)

        self.horizontalLayout_8.addWidget(self.dsBox_DOG_Sigma)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_DOG_k = QLabel(self.grp_DOG)
        self.lbl_DOG_k.setObjectName(u"lbl_DOG_k")

        self.horizontalLayout_9.addWidget(self.lbl_DOG_k)

        self.dsBox_DOG_k = QDoubleSpinBox(self.grp_DOG)
        self.dsBox_DOG_k.setObjectName(u"dsBox_DOG_k")
        self.dsBox_DOG_k.setMinimum(0.100000000000000)
        self.dsBox_DOG_k.setMaximum(5.000000000000000)
        self.dsBox_DOG_k.setSingleStep(0.100000000000000)
        self.dsBox_DOG_k.setValue(1.600000000000000)

        self.horizontalLayout_9.addWidget(self.dsBox_DOG_k)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_DOG_gamma = QLabel(self.grp_DOG)
        self.lbl_DOG_gamma.setObjectName(u"lbl_DOG_gamma")

        self.horizontalLayout_10.addWidget(self.lbl_DOG_gamma)

        self.dsBox_DOG_gamma = QDoubleSpinBox(self.grp_DOG)
        self.dsBox_DOG_gamma.setObjectName(u"dsBox_DOG_gamma")
        self.dsBox_DOG_gamma.setMinimum(0.100000000000000)
        self.dsBox_DOG_gamma.setMaximum(5.000000000000000)
        self.dsBox_DOG_gamma.setSingleStep(0.100000000000000)
        self.dsBox_DOG_gamma.setValue(1.000000000000000)

        self.horizontalLayout_10.addWidget(self.dsBox_DOG_gamma)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.pBtn_DOG_Apply = QPushButton(self.grp_DOG)
        self.pBtn_DOG_Apply.setObjectName(u"pBtn_DOG_Apply")

        self.verticalLayout_6.addWidget(self.pBtn_DOG_Apply)

        self.grp_Canny = QGroupBox(EdgeDetectorDialog)
        self.grp_Canny.setObjectName(u"grp_Canny")
        self.grp_Canny.setGeometry(QRect(550, 10, 117, 109))
        self.verticalLayout_9 = QVBoxLayout(self.grp_Canny)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lbl_Canny_Hysterisis_Upper = QLabel(self.grp_Canny)
        self.lbl_Canny_Hysterisis_Upper.setObjectName(u"lbl_Canny_Hysterisis_Upper")

        self.horizontalLayout_19.addWidget(self.lbl_Canny_Hysterisis_Upper)

        self.sBox_Canny_Hysterisis_Upper = QSpinBox(self.grp_Canny)
        self.sBox_Canny_Hysterisis_Upper.setObjectName(u"sBox_Canny_Hysterisis_Upper")
        self.sBox_Canny_Hysterisis_Upper.setMaximum(255)
        self.sBox_Canny_Hysterisis_Upper.setValue(120)

        self.horizontalLayout_19.addWidget(self.sBox_Canny_Hysterisis_Upper)


        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lbl_Canny_Hysterisis_Lower = QLabel(self.grp_Canny)
        self.lbl_Canny_Hysterisis_Lower.setObjectName(u"lbl_Canny_Hysterisis_Lower")

        self.horizontalLayout_20.addWidget(self.lbl_Canny_Hysterisis_Lower)

        self.sBox_Canny_Hysterisis_Lower = QSpinBox(self.grp_Canny)
        self.sBox_Canny_Hysterisis_Lower.setObjectName(u"sBox_Canny_Hysterisis_Lower")
        self.sBox_Canny_Hysterisis_Lower.setMaximum(255)
        self.sBox_Canny_Hysterisis_Lower.setValue(100)

        self.horizontalLayout_20.addWidget(self.sBox_Canny_Hysterisis_Lower)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.pBtn_Canny_Apply = QPushButton(self.grp_Canny)
        self.pBtn_Canny_Apply.setObjectName(u"pBtn_Canny_Apply")

        self.verticalLayout_9.addWidget(self.pBtn_Canny_Apply)

        self.grp_Zero_Crossing = QGroupBox(EdgeDetectorDialog)
        self.grp_Zero_Crossing.setObjectName(u"grp_Zero_Crossing")
        self.grp_Zero_Crossing.setGeometry(QRect(540, 140, 151, 109))
        self.verticalLayout_8 = QVBoxLayout(self.grp_Zero_Crossing)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_Zero_Crossing_kxy = QLabel(self.grp_Zero_Crossing)
        self.lbl_Zero_Crossing_kxy.setObjectName(u"lbl_Zero_Crossing_kxy")

        self.horizontalLayout_17.addWidget(self.lbl_Zero_Crossing_kxy)

        self.sBox_Zero_Crossing_kxy = QSpinBox(self.grp_Zero_Crossing)
        self.sBox_Zero_Crossing_kxy.setObjectName(u"sBox_Zero_Crossing_kxy")
        self.sBox_Zero_Crossing_kxy.setMinimum(3)
        self.sBox_Zero_Crossing_kxy.setSingleStep(2)

        self.horizontalLayout_17.addWidget(self.sBox_Zero_Crossing_kxy)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lbl_Zero_Crossing_Sigma = QLabel(self.grp_Zero_Crossing)
        self.lbl_Zero_Crossing_Sigma.setObjectName(u"lbl_Zero_Crossing_Sigma")

        self.horizontalLayout_18.addWidget(self.lbl_Zero_Crossing_Sigma)

        self.dsBox_Zero_Crossing_Sigma = QDoubleSpinBox(self.grp_Zero_Crossing)
        self.dsBox_Zero_Crossing_Sigma.setObjectName(u"dsBox_Zero_Crossing_Sigma")
        self.dsBox_Zero_Crossing_Sigma.setMinimum(0.100000000000000)
        self.dsBox_Zero_Crossing_Sigma.setMaximum(30.000000000000000)
        self.dsBox_Zero_Crossing_Sigma.setSingleStep(0.100000000000000)
        self.dsBox_Zero_Crossing_Sigma.setValue(1.300000000000000)

        self.horizontalLayout_18.addWidget(self.dsBox_Zero_Crossing_Sigma)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.pBtn_Zero_Crossing_Apply = QPushButton(self.grp_Zero_Crossing)
        self.pBtn_Zero_Crossing_Apply.setObjectName(u"pBtn_Zero_Crossing_Apply")

        self.verticalLayout_8.addWidget(self.pBtn_Zero_Crossing_Apply)


        self.retranslateUi(EdgeDetectorDialog)

        QMetaObject.connectSlotsByName(EdgeDetectorDialog)
    # setupUi

    def retranslateUi(self, EdgeDetectorDialog):
        EdgeDetectorDialog.setWindowTitle(QCoreApplication.translate("EdgeDetectorDialog", u"EdgeDetector Dialog", None))
        self.grp_Differential.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"Differential", None))
        self.lbl_Differential_Direction.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Direction", None))
        self.cBox_Differential_Direction.setItemText(0, QCoreApplication.translate("EdgeDetectorDialog", u"h", None))
        self.cBox_Differential_Direction.setItemText(1, QCoreApplication.translate("EdgeDetectorDialog", u"v", None))
        self.cBox_Differential_Direction.setItemText(2, QCoreApplication.translate("EdgeDetectorDialog", u"ut", None))
        self.cBox_Differential_Direction.setItemText(3, QCoreApplication.translate("EdgeDetectorDialog", u"dt", None))

        self.pBtn_Differential_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_Prewitt.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"Prewitt", None))
        self.lbl_Prewitt_Direction.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Direction", None))
        self.cBox_Prewitt_Direction.setItemText(0, QCoreApplication.translate("EdgeDetectorDialog", u"h", None))
        self.cBox_Prewitt_Direction.setItemText(1, QCoreApplication.translate("EdgeDetectorDialog", u"v", None))
        self.cBox_Prewitt_Direction.setItemText(2, QCoreApplication.translate("EdgeDetectorDialog", u"ut", None))
        self.cBox_Prewitt_Direction.setItemText(3, QCoreApplication.translate("EdgeDetectorDialog", u"dt", None))

        self.pBtn_Prewitt_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_Sobel.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"Sobel", None))
        self.lbl_Sobel_Direction.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Direction", None))
        self.cBox_Sobel_Direction.setItemText(0, QCoreApplication.translate("EdgeDetectorDialog", u"h", None))
        self.cBox_Sobel_Direction.setItemText(1, QCoreApplication.translate("EdgeDetectorDialog", u"v", None))
        self.cBox_Sobel_Direction.setItemText(2, QCoreApplication.translate("EdgeDetectorDialog", u"ut", None))
        self.cBox_Sobel_Direction.setItemText(3, QCoreApplication.translate("EdgeDetectorDialog", u"dt", None))

        self.pBtn_Sobel_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_XDOG.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"XDOG", None))
        self.lbl_XDOG_kxy.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k_xy", None))
        self.lbl_XDOG_Sigma.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Sigma", None))
        self.lbl_XDOG_k.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k", None))
        self.lbl_XDOG_gamma.setText(QCoreApplication.translate("EdgeDetectorDialog", u"p", None))
        self.lbl_XDOG_phi.setText(QCoreApplication.translate("EdgeDetectorDialog", u"phi", None))
        self.lbl_XDOG_eps.setText(QCoreApplication.translate("EdgeDetectorDialog", u"eps", None))
        self.pBtn_XDOG_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_Laplacian.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"Laplacian", None))
        self.lbl_Laplacian_kxy.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k_xy", None))
        self.pBtn_Laplacian_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_LOG.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"LOG", None))
        self.lbl_LOG_kxy.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k_xy", None))
        self.lbl_LOG_Sigma.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Sigma", None))
        self.pBtn_LOG_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_DOG.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"DOG", None))
        self.lbl_DOG_kxy.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k_xy", None))
        self.lbl_DOG_Sigma.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Sigma", None))
        self.lbl_DOG_k.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k", None))
        self.lbl_DOG_gamma.setText(QCoreApplication.translate("EdgeDetectorDialog", u"gamma", None))
        self.pBtn_DOG_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_Canny.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"Canny", None))
        self.lbl_Canny_Hysterisis_Upper.setText(QCoreApplication.translate("EdgeDetectorDialog", u"hys upper", None))
        self.lbl_Canny_Hysterisis_Lower.setText(QCoreApplication.translate("EdgeDetectorDialog", u"hys lower", None))
        self.pBtn_Canny_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
        self.grp_Zero_Crossing.setTitle(QCoreApplication.translate("EdgeDetectorDialog", u"Zero Crossing with LOG", None))
        self.lbl_Zero_Crossing_kxy.setText(QCoreApplication.translate("EdgeDetectorDialog", u"k_xy", None))
        self.lbl_Zero_Crossing_Sigma.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Sigma", None))
        self.pBtn_Zero_Crossing_Apply.setText(QCoreApplication.translate("EdgeDetectorDialog", u"Apply", None))
    # retranslateUi

