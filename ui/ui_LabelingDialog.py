# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_LabelingDialog.ui'
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


class Ui_LabelingDialog(object):
    def setupUi(self, LabelingDialog):
        if LabelingDialog.objectName():
            LabelingDialog.setObjectName(u"LabelingDialog")
        LabelingDialog.resize(764, 300)
        self.verticalLayout = QVBoxLayout(LabelingDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grp_Labeling = QGroupBox(LabelingDialog)
        self.grp_Labeling.setObjectName(u"grp_Labeling")
        self.horizontalLayout_11 = QHBoxLayout(self.grp_Labeling)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pBtn_Principal_Axes_Line_Apply = QPushButton(self.grp_Labeling)
        self.pBtn_Principal_Axes_Line_Apply.setObjectName(u"pBtn_Principal_Axes_Line_Apply")

        self.gridLayout.addWidget(self.pBtn_Principal_Axes_Line_Apply, 1, 0, 1, 1)

        self.pBtn_BBox_Apply = QPushButton(self.grp_Labeling)
        self.pBtn_BBox_Apply.setObjectName(u"pBtn_BBox_Apply")

        self.gridLayout.addWidget(self.pBtn_BBox_Apply, 2, 0, 1, 1)

        self.pBtn_Clear_Apply = QPushButton(self.grp_Labeling)
        self.pBtn_Clear_Apply.setObjectName(u"pBtn_Clear_Apply")

        self.gridLayout.addWidget(self.pBtn_Clear_Apply, 3, 0, 1, 1)

        self.pBtn_Labeling_Apply = QPushButton(self.grp_Labeling)
        self.pBtn_Labeling_Apply.setObjectName(u"pBtn_Labeling_Apply")

        self.gridLayout.addWidget(self.pBtn_Labeling_Apply, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.pBtn_Save_Features = QPushButton(self.grp_Labeling)
        self.pBtn_Save_Features.setObjectName(u"pBtn_Save_Features")

        self.gridLayout.addWidget(self.pBtn_Save_Features, 4, 0, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout)

        self.tableWidget_Labeling = QTableWidget(self.grp_Labeling)
        self.tableWidget_Labeling.setObjectName(u"tableWidget_Labeling")

        self.horizontalLayout_11.addWidget(self.tableWidget_Labeling)


        self.verticalLayout.addWidget(self.grp_Labeling)


        self.retranslateUi(LabelingDialog)

        QMetaObject.connectSlotsByName(LabelingDialog)
    # setupUi

    def retranslateUi(self, LabelingDialog):
        LabelingDialog.setWindowTitle(QCoreApplication.translate("LabelingDialog", u"LabelingDialog", None))
        self.grp_Labeling.setTitle(QCoreApplication.translate("LabelingDialog", u"Labeling", None))
        self.pBtn_Principal_Axes_Line_Apply.setText(QCoreApplication.translate("LabelingDialog", u"Lines", None))
        self.pBtn_BBox_Apply.setText(QCoreApplication.translate("LabelingDialog", u"BBox", None))
        self.pBtn_Clear_Apply.setText(QCoreApplication.translate("LabelingDialog", u"Clear", None))
        self.pBtn_Labeling_Apply.setText(QCoreApplication.translate("LabelingDialog", u"Apply", None))
        self.pBtn_Save_Features.setText(QCoreApplication.translate("LabelingDialog", u"Save", None))
    # retranslateUi

