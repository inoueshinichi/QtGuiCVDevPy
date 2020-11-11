# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_EditBorderDialog.ui'
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


class Ui_EditBorderDialog(object):
    def setupUi(self, EditBorderDialog):
        if EditBorderDialog.objectName():
            EditBorderDialog.setObjectName(u"EditBorderDialog")
        EditBorderDialog.resize(451, 236)
        EditBorderDialog.setMaximumSize(QSize(451, 236))
        self.horizontalLayout_2 = QHBoxLayout(EditBorderDialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.grp_Make_Border = QGroupBox(EditBorderDialog)
        self.grp_Make_Border.setObjectName(u"grp_Make_Border")
        self.verticalLayout = QVBoxLayout(self.grp_Make_Border)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Boarder_Type = QLabel(self.grp_Make_Border)
        self.lbl_Boarder_Type.setObjectName(u"lbl_Boarder_Type")

        self.horizontalLayout.addWidget(self.lbl_Boarder_Type)

        self.cBox_Border_Type = QComboBox(self.grp_Make_Border)
        self.cBox_Border_Type.addItem("")
        self.cBox_Border_Type.addItem("")
        self.cBox_Border_Type.addItem("")
        self.cBox_Border_Type.addItem("")
        self.cBox_Border_Type.setObjectName(u"cBox_Border_Type")

        self.horizontalLayout.addWidget(self.cBox_Border_Type)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.grp_Location = QGroupBox(self.grp_Make_Border)
        self.grp_Location.setObjectName(u"grp_Location")
        self.formLayout = QFormLayout(self.grp_Location)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_Left = QLabel(self.grp_Location)
        self.lbl_Left.setObjectName(u"lbl_Left")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_Left)

        self.sBox_Border_Left = QSpinBox(self.grp_Location)
        self.sBox_Border_Left.setObjectName(u"sBox_Border_Left")
        self.sBox_Border_Left.setMaximum(5000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sBox_Border_Left)

        self.lbl_Top = QLabel(self.grp_Location)
        self.lbl_Top.setObjectName(u"lbl_Top")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_Top)

        self.sBox_Border_Top = QSpinBox(self.grp_Location)
        self.sBox_Border_Top.setObjectName(u"sBox_Border_Top")
        self.sBox_Border_Top.setMaximum(5000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sBox_Border_Top)

        self.lbl_Right = QLabel(self.grp_Location)
        self.lbl_Right.setObjectName(u"lbl_Right")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_Right)

        self.sBox_Border_Right = QSpinBox(self.grp_Location)
        self.sBox_Border_Right.setObjectName(u"sBox_Border_Right")
        self.sBox_Border_Right.setMaximum(5000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sBox_Border_Right)

        self.lbl_Bottom = QLabel(self.grp_Location)
        self.lbl_Bottom.setObjectName(u"lbl_Bottom")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_Bottom)

        self.sBox_Border_Bottom = QSpinBox(self.grp_Location)
        self.sBox_Border_Bottom.setObjectName(u"sBox_Border_Bottom")
        self.sBox_Border_Bottom.setMaximum(5000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sBox_Border_Bottom)


        self.horizontalLayout_3.addWidget(self.grp_Location)

        self.grp_Constant_Color = QGroupBox(self.grp_Make_Border)
        self.grp_Constant_Color.setObjectName(u"grp_Constant_Color")
        self.formLayout_2 = QFormLayout(self.grp_Constant_Color)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_Constant_Gray = QLabel(self.grp_Constant_Color)
        self.lbl_Constant_Gray.setObjectName(u"lbl_Constant_Gray")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_Constant_Gray)

        self.sBox_Border_Constant_Gray = QSpinBox(self.grp_Constant_Color)
        self.sBox_Border_Constant_Gray.setObjectName(u"sBox_Border_Constant_Gray")
        self.sBox_Border_Constant_Gray.setMaximum(255)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sBox_Border_Constant_Gray)

        self.lbl_Constant_Red = QLabel(self.grp_Constant_Color)
        self.lbl_Constant_Red.setObjectName(u"lbl_Constant_Red")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_Constant_Red)

        self.sBox_Border_Constant_Red = QSpinBox(self.grp_Constant_Color)
        self.sBox_Border_Constant_Red.setObjectName(u"sBox_Border_Constant_Red")
        self.sBox_Border_Constant_Red.setMaximum(255)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sBox_Border_Constant_Red)

        self.lbl_Constant_Green = QLabel(self.grp_Constant_Color)
        self.lbl_Constant_Green.setObjectName(u"lbl_Constant_Green")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_Constant_Green)

        self.sBox_Border_Constant_Green = QSpinBox(self.grp_Constant_Color)
        self.sBox_Border_Constant_Green.setObjectName(u"sBox_Border_Constant_Green")
        self.sBox_Border_Constant_Green.setMaximum(255)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.sBox_Border_Constant_Green)

        self.lbl_Constant_B = QLabel(self.grp_Constant_Color)
        self.lbl_Constant_B.setObjectName(u"lbl_Constant_B")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_Constant_B)

        self.sBox_Border_Constant_Blue = QSpinBox(self.grp_Constant_Color)
        self.sBox_Border_Constant_Blue.setObjectName(u"sBox_Border_Constant_Blue")
        self.sBox_Border_Constant_Blue.setMaximum(255)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.sBox_Border_Constant_Blue)


        self.horizontalLayout_3.addWidget(self.grp_Constant_Color)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pBtn_Make_Border_Clear_Location = QPushButton(self.grp_Make_Border)
        self.pBtn_Make_Border_Clear_Location.setObjectName(u"pBtn_Make_Border_Clear_Location")

        self.horizontalLayout_4.addWidget(self.pBtn_Make_Border_Clear_Location)

        self.pBtn_Make_Border_Clear_Color = QPushButton(self.grp_Make_Border)
        self.pBtn_Make_Border_Clear_Color.setObjectName(u"pBtn_Make_Border_Clear_Color")

        self.horizontalLayout_4.addWidget(self.pBtn_Make_Border_Clear_Color)

        self.pBtn_Make_Border_Apply = QPushButton(self.grp_Make_Border)
        self.pBtn_Make_Border_Apply.setObjectName(u"pBtn_Make_Border_Apply")

        self.horizontalLayout_4.addWidget(self.pBtn_Make_Border_Apply)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.grp_Make_Border)

        self.grp_Erase_Border = QGroupBox(EditBorderDialog)
        self.grp_Erase_Border.setObjectName(u"grp_Erase_Border")
        self.formLayout_3 = QFormLayout(self.grp_Erase_Border)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_Erase_Border_Left = QLabel(self.grp_Erase_Border)
        self.lbl_Erase_Border_Left.setObjectName(u"lbl_Erase_Border_Left")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_Erase_Border_Left)

        self.sBox_Erase_Border_Left = QSpinBox(self.grp_Erase_Border)
        self.sBox_Erase_Border_Left.setObjectName(u"sBox_Erase_Border_Left")
        self.sBox_Erase_Border_Left.setMaximum(5000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.sBox_Erase_Border_Left)

        self.lbl_Erase_Border_Top = QLabel(self.grp_Erase_Border)
        self.lbl_Erase_Border_Top.setObjectName(u"lbl_Erase_Border_Top")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_Erase_Border_Top)

        self.sBox_Erase_Border_Top = QSpinBox(self.grp_Erase_Border)
        self.sBox_Erase_Border_Top.setObjectName(u"sBox_Erase_Border_Top")
        self.sBox_Erase_Border_Top.setMaximum(5000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.sBox_Erase_Border_Top)

        self.lbl_Erase_Border_Right = QLabel(self.grp_Erase_Border)
        self.lbl_Erase_Border_Right.setObjectName(u"lbl_Erase_Border_Right")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lbl_Erase_Border_Right)

        self.sBox_Erase_Border_Right = QSpinBox(self.grp_Erase_Border)
        self.sBox_Erase_Border_Right.setObjectName(u"sBox_Erase_Border_Right")
        self.sBox_Erase_Border_Right.setMaximum(5000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.sBox_Erase_Border_Right)

        self.lbl_Erase_Border_Bottom = QLabel(self.grp_Erase_Border)
        self.lbl_Erase_Border_Bottom.setObjectName(u"lbl_Erase_Border_Bottom")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lbl_Erase_Border_Bottom)

        self.sBox_Erase_Border_Bottom = QSpinBox(self.grp_Erase_Border)
        self.sBox_Erase_Border_Bottom.setObjectName(u"sBox_Erase_Border_Bottom")
        self.sBox_Erase_Border_Bottom.setMaximum(5000)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.sBox_Erase_Border_Bottom)

        self.pBtn_Erase_Border_Apply = QPushButton(self.grp_Erase_Border)
        self.pBtn_Erase_Border_Apply.setObjectName(u"pBtn_Erase_Border_Apply")

        self.formLayout_3.setWidget(5, QFormLayout.SpanningRole, self.pBtn_Erase_Border_Apply)

        self.pBtn_Erase_Border_Clear_Location = QPushButton(self.grp_Erase_Border)
        self.pBtn_Erase_Border_Clear_Location.setObjectName(u"pBtn_Erase_Border_Clear_Location")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.pBtn_Erase_Border_Clear_Location)


        self.horizontalLayout_2.addWidget(self.grp_Erase_Border)


        self.retranslateUi(EditBorderDialog)

        QMetaObject.connectSlotsByName(EditBorderDialog)
    # setupUi

    def retranslateUi(self, EditBorderDialog):
        EditBorderDialog.setWindowTitle(QCoreApplication.translate("EditBorderDialog", u"EditBorderDialog", None))
        self.grp_Make_Border.setTitle(QCoreApplication.translate("EditBorderDialog", u"Make Border", None))
        self.lbl_Boarder_Type.setText(QCoreApplication.translate("EditBorderDialog", u"Border Type", None))
        self.cBox_Border_Type.setItemText(0, QCoreApplication.translate("EditBorderDialog", u"Reflect  [gfedcb|abcdefgh|gfedcba]", None))
        self.cBox_Border_Type.setItemText(1, QCoreApplication.translate("EditBorderDialog", u"Replicate  [aaaaaa|abcdefgh|hhhhhhh]", None))
        self.cBox_Border_Type.setItemText(2, QCoreApplication.translate("EditBorderDialog", u"Warp  [cdefgh|abcdefgh|abcdefg]", None))
        self.cBox_Border_Type.setItemText(3, QCoreApplication.translate("EditBorderDialog", u"Constant  [iiiiii|abcdefgh|iiiiiii]", None))

        self.grp_Location.setTitle(QCoreApplication.translate("EditBorderDialog", u"Location", None))
        self.lbl_Left.setText(QCoreApplication.translate("EditBorderDialog", u"Left", None))
        self.lbl_Top.setText(QCoreApplication.translate("EditBorderDialog", u"Top", None))
        self.lbl_Right.setText(QCoreApplication.translate("EditBorderDialog", u"Right", None))
        self.lbl_Bottom.setText(QCoreApplication.translate("EditBorderDialog", u"Bottom", None))
        self.grp_Constant_Color.setTitle(QCoreApplication.translate("EditBorderDialog", u"Constant Color", None))
        self.lbl_Constant_Gray.setText(QCoreApplication.translate("EditBorderDialog", u"Gray", None))
        self.lbl_Constant_Red.setText(QCoreApplication.translate("EditBorderDialog", u"Red", None))
        self.lbl_Constant_Green.setText(QCoreApplication.translate("EditBorderDialog", u"Green", None))
        self.lbl_Constant_B.setText(QCoreApplication.translate("EditBorderDialog", u"Blue", None))
        self.pBtn_Make_Border_Clear_Location.setText(QCoreApplication.translate("EditBorderDialog", u"Clear Loc", None))
        self.pBtn_Make_Border_Clear_Color.setText(QCoreApplication.translate("EditBorderDialog", u"Clear Color", None))
        self.pBtn_Make_Border_Apply.setText(QCoreApplication.translate("EditBorderDialog", u"Make", None))
        self.grp_Erase_Border.setTitle(QCoreApplication.translate("EditBorderDialog", u"Erase Border", None))
        self.lbl_Erase_Border_Left.setText(QCoreApplication.translate("EditBorderDialog", u"Left", None))
        self.lbl_Erase_Border_Top.setText(QCoreApplication.translate("EditBorderDialog", u"Top", None))
        self.lbl_Erase_Border_Right.setText(QCoreApplication.translate("EditBorderDialog", u"Right", None))
        self.lbl_Erase_Border_Bottom.setText(QCoreApplication.translate("EditBorderDialog", u"Bottom", None))
        self.pBtn_Erase_Border_Apply.setText(QCoreApplication.translate("EditBorderDialog", u"Erase", None))
        self.pBtn_Erase_Border_Clear_Location.setText(QCoreApplication.translate("EditBorderDialog", u"Clear Loc", None))
    # retranslateUi

