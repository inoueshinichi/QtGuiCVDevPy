# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_FFTDialog.ui'
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


class Ui_FFTDialog(object):
    def setupUi(self, FFTDialog):
        if FFTDialog.objectName():
            FFTDialog.setObjectName(u"FFTDialog")
        FFTDialog.resize(443, 180)
        self.horizontalLayout_3 = QHBoxLayout(FFTDialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pBtn_FFT = QPushButton(FFTDialog)
        self.pBtn_FFT.setObjectName(u"pBtn_FFT")

        self.verticalLayout_2.addWidget(self.pBtn_FFT)

        self.pBtn_IFFT = QPushButton(FFTDialog)
        self.pBtn_IFFT.setObjectName(u"pBtn_IFFT")

        self.verticalLayout_2.addWidget(self.pBtn_IFFT)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.grp_Frequency_Filter = QGroupBox(FFTDialog)
        self.grp_Frequency_Filter.setObjectName(u"grp_Frequency_Filter")
        self.verticalLayout = QVBoxLayout(self.grp_Frequency_Filter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pBtn_HighPassFilter = QPushButton(self.grp_Frequency_Filter)
        self.pBtn_HighPassFilter.setObjectName(u"pBtn_HighPassFilter")

        self.verticalLayout.addWidget(self.pBtn_HighPassFilter)

        self.pBtn_LowPassFilter = QPushButton(self.grp_Frequency_Filter)
        self.pBtn_LowPassFilter.setObjectName(u"pBtn_LowPassFilter")

        self.verticalLayout.addWidget(self.pBtn_LowPassFilter)

        self.pBtn_BandPassFilter = QPushButton(self.grp_Frequency_Filter)
        self.pBtn_BandPassFilter.setObjectName(u"pBtn_BandPassFilter")

        self.verticalLayout.addWidget(self.pBtn_BandPassFilter)


        self.horizontalLayout_3.addWidget(self.grp_Frequency_Filter)

        self.grp_Blending = QGroupBox(FFTDialog)
        self.grp_Blending.setObjectName(u"grp_Blending")
        self.verticalLayout_3 = QVBoxLayout(self.grp_Blending)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pBtn_HighPassCopy = QPushButton(self.grp_Blending)
        self.pBtn_HighPassCopy.setObjectName(u"pBtn_HighPassCopy")

        self.verticalLayout_3.addWidget(self.pBtn_HighPassCopy)

        self.pBtn_LowPassCopy = QPushButton(self.grp_Blending)
        self.pBtn_LowPassCopy.setObjectName(u"pBtn_LowPassCopy")

        self.verticalLayout_3.addWidget(self.pBtn_LowPassCopy)

        self.pBtn_BandPassCopy = QPushButton(self.grp_Blending)
        self.pBtn_BandPassCopy.setObjectName(u"pBtn_BandPassCopy")

        self.verticalLayout_3.addWidget(self.pBtn_BandPassCopy)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pBtn_Blending_Blend = QPushButton(self.grp_Blending)
        self.pBtn_Blending_Blend.setObjectName(u"pBtn_Blending_Blend")

        self.horizontalLayout_2.addWidget(self.pBtn_Blending_Blend)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Blending_Alpha = QLabel(self.grp_Blending)
        self.lbl_Blending_Alpha.setObjectName(u"lbl_Blending_Alpha")

        self.horizontalLayout.addWidget(self.lbl_Blending_Alpha)

        self.dsBox_Blending_Alpha = QDoubleSpinBox(self.grp_Blending)
        self.dsBox_Blending_Alpha.setObjectName(u"dsBox_Blending_Alpha")
        self.dsBox_Blending_Alpha.setMaximum(1.000000000000000)
        self.dsBox_Blending_Alpha.setSingleStep(0.100000000000000)
        self.dsBox_Blending_Alpha.setValue(0.500000000000000)

        self.horizontalLayout.addWidget(self.dsBox_Blending_Alpha)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.grp_Blending)


        self.retranslateUi(FFTDialog)

        QMetaObject.connectSlotsByName(FFTDialog)
    # setupUi

    def retranslateUi(self, FFTDialog):
        FFTDialog.setWindowTitle(QCoreApplication.translate("FFTDialog", u"FFTDialog", None))
        self.pBtn_FFT.setText(QCoreApplication.translate("FFTDialog", u"FFT", None))
        self.pBtn_IFFT.setText(QCoreApplication.translate("FFTDialog", u"IFFT", None))
        self.grp_Frequency_Filter.setTitle(QCoreApplication.translate("FFTDialog", u"Frequency Filter", None))
        self.pBtn_HighPassFilter.setText(QCoreApplication.translate("FFTDialog", u"High Pass Filter", None))
        self.pBtn_LowPassFilter.setText(QCoreApplication.translate("FFTDialog", u"Low Pass Filter", None))
        self.pBtn_BandPassFilter.setText(QCoreApplication.translate("FFTDialog", u"Band Pass Filter", None))
        self.grp_Blending.setTitle(QCoreApplication.translate("FFTDialog", u"Blending", None))
        self.pBtn_HighPassCopy.setText(QCoreApplication.translate("FFTDialog", u"High Pass Copy", None))
        self.pBtn_LowPassCopy.setText(QCoreApplication.translate("FFTDialog", u"Low Pass Copy", None))
        self.pBtn_BandPassCopy.setText(QCoreApplication.translate("FFTDialog", u"Band Pass Copy", None))
        self.pBtn_Blending_Blend.setText(QCoreApplication.translate("FFTDialog", u"Blend", None))
        self.lbl_Blending_Alpha.setText(QCoreApplication.translate("FFTDialog", u"\u03b1", None))
    # retranslateUi

