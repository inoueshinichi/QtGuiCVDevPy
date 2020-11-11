# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_DatasetDialog.ui'
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


class Ui_DatasetDialog(object):
    def setupUi(self, DatasetDialog):
        if DatasetDialog.objectName():
            DatasetDialog.setObjectName(u"DatasetDialog")
        DatasetDialog.resize(731, 418)
        self.verticalLayout_2 = QVBoxLayout(DatasetDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.grp_Numerical_Labeling = QGroupBox(DatasetDialog)
        self.grp_Numerical_Labeling.setObjectName(u"grp_Numerical_Labeling")
        self.horizontalLayout_4 = QHBoxLayout(self.grp_Numerical_Labeling)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Raw_Data_Dir = QLabel(self.grp_Numerical_Labeling)
        self.lbl_Raw_Data_Dir.setObjectName(u"lbl_Raw_Data_Dir")

        self.horizontalLayout_2.addWidget(self.lbl_Raw_Data_Dir)

        self.lEdit_Raw_Data_Dir = QLineEdit(self.grp_Numerical_Labeling)
        self.lEdit_Raw_Data_Dir.setObjectName(u"lEdit_Raw_Data_Dir")

        self.horizontalLayout_2.addWidget(self.lEdit_Raw_Data_Dir)

        self.tBtn_Raw_Data_Dir = QToolButton(self.grp_Numerical_Labeling)
        self.tBtn_Raw_Data_Dir.setObjectName(u"tBtn_Raw_Data_Dir")

        self.horizontalLayout_2.addWidget(self.tBtn_Raw_Data_Dir)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Csv_Data_Dir = QLabel(self.grp_Numerical_Labeling)
        self.lbl_Csv_Data_Dir.setObjectName(u"lbl_Csv_Data_Dir")

        self.horizontalLayout_3.addWidget(self.lbl_Csv_Data_Dir)

        self.lEdit_Csv_Data_Dir = QLineEdit(self.grp_Numerical_Labeling)
        self.lEdit_Csv_Data_Dir.setObjectName(u"lEdit_Csv_Data_Dir")

        self.horizontalLayout_3.addWidget(self.lEdit_Csv_Data_Dir)

        self.tBtn_Csv_Data_Dir = QToolButton(self.grp_Numerical_Labeling)
        self.tBtn_Csv_Data_Dir.setObjectName(u"tBtn_Csv_Data_Dir")

        self.horizontalLayout_3.addWidget(self.tBtn_Csv_Data_Dir)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableWidget_Raw_Data_Dir = QTableWidget(self.grp_Numerical_Labeling)
        self.tableWidget_Raw_Data_Dir.setObjectName(u"tableWidget_Raw_Data_Dir")
        self.tableWidget_Raw_Data_Dir.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.tableWidget_Raw_Data_Dir)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Raw_Data_Count = QLabel(self.grp_Numerical_Labeling)
        self.lbl_Raw_Data_Count.setObjectName(u"lbl_Raw_Data_Count")

        self.horizontalLayout.addWidget(self.lbl_Raw_Data_Count)

        self.lEdit_Raw_Data_Count = QLineEdit(self.grp_Numerical_Labeling)
        self.lEdit_Raw_Data_Count.setObjectName(u"lEdit_Raw_Data_Count")
        self.lEdit_Raw_Data_Count.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lEdit_Raw_Data_Count)

        self.lbl_Raw_Data_Label = QLabel(self.grp_Numerical_Labeling)
        self.lbl_Raw_Data_Label.setObjectName(u"lbl_Raw_Data_Label")

        self.horizontalLayout.addWidget(self.lbl_Raw_Data_Label)

        self.lEdit_Raw_Data_Label = QLineEdit(self.grp_Numerical_Labeling)
        self.lEdit_Raw_Data_Label.setObjectName(u"lEdit_Raw_Data_Label")

        self.horizontalLayout.addWidget(self.lEdit_Raw_Data_Label)

        self.pBtn_Labeling = QPushButton(self.grp_Numerical_Labeling)
        self.pBtn_Labeling.setObjectName(u"pBtn_Labeling")

        self.horizontalLayout.addWidget(self.pBtn_Labeling)

        self.lEdit_Valid_Raw_Data_Count = QLineEdit(self.grp_Numerical_Labeling)
        self.lEdit_Valid_Raw_Data_Count.setObjectName(u"lEdit_Valid_Raw_Data_Count")
        self.lEdit_Valid_Raw_Data_Count.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lEdit_Valid_Raw_Data_Count)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout_15.addWidget(self.grp_Numerical_Labeling)

        self.grp_Split_Train = QGroupBox(DatasetDialog)
        self.grp_Split_Train.setObjectName(u"grp_Split_Train")
        self.verticalLayout_5 = QVBoxLayout(self.grp_Split_Train)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_Target_Directory_Path = QLabel(self.grp_Split_Train)
        self.lbl_Target_Directory_Path.setObjectName(u"lbl_Target_Directory_Path")

        self.gridLayout_3.addWidget(self.lbl_Target_Directory_Path, 0, 0, 1, 1)

        self.lEdit_Target_Directory_Path = QLineEdit(self.grp_Split_Train)
        self.lEdit_Target_Directory_Path.setObjectName(u"lEdit_Target_Directory_Path")
        self.lEdit_Target_Directory_Path.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lEdit_Target_Directory_Path, 0, 1, 1, 1)

        self.tBtn_Target_Directory_Path = QToolButton(self.grp_Split_Train)
        self.tBtn_Target_Directory_Path.setObjectName(u"tBtn_Target_Directory_Path")

        self.gridLayout_3.addWidget(self.tBtn_Target_Directory_Path, 0, 2, 1, 1)

        self.lbl_A_Directory_Path = QLabel(self.grp_Split_Train)
        self.lbl_A_Directory_Path.setObjectName(u"lbl_A_Directory_Path")

        self.gridLayout_3.addWidget(self.lbl_A_Directory_Path, 1, 0, 1, 1)

        self.lEdit_A_Directory_Path = QLineEdit(self.grp_Split_Train)
        self.lEdit_A_Directory_Path.setObjectName(u"lEdit_A_Directory_Path")
        self.lEdit_A_Directory_Path.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lEdit_A_Directory_Path, 1, 1, 1, 1)

        self.tBtn_A_Directory_Path = QToolButton(self.grp_Split_Train)
        self.tBtn_A_Directory_Path.setObjectName(u"tBtn_A_Directory_Path")

        self.gridLayout_3.addWidget(self.tBtn_A_Directory_Path, 1, 2, 1, 1)

        self.lbl_B_Directory_Path = QLabel(self.grp_Split_Train)
        self.lbl_B_Directory_Path.setObjectName(u"lbl_B_Directory_Path")

        self.gridLayout_3.addWidget(self.lbl_B_Directory_Path, 2, 0, 1, 1)

        self.lEdit_B_Directory_Path = QLineEdit(self.grp_Split_Train)
        self.lEdit_B_Directory_Path.setObjectName(u"lEdit_B_Directory_Path")
        self.lEdit_B_Directory_Path.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lEdit_B_Directory_Path, 2, 1, 1, 1)

        self.tBtn_B_Directory_Path = QToolButton(self.grp_Split_Train)
        self.tBtn_B_Directory_Path.setObjectName(u"tBtn_B_Directory_Path")

        self.gridLayout_3.addWidget(self.tBtn_B_Directory_Path, 2, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lbl_B_Percentage = QLabel(self.grp_Split_Train)
        self.lbl_B_Percentage.setObjectName(u"lbl_B_Percentage")

        self.horizontalLayout_12.addWidget(self.lbl_B_Percentage)

        self.cBox_B_Percentage = QComboBox(self.grp_Split_Train)
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.addItem("")
        self.cBox_B_Percentage.setObjectName(u"cBox_B_Percentage")

        self.horizontalLayout_12.addWidget(self.cBox_B_Percentage)

        self.chBox_Manual_Shuffle = QCheckBox(self.grp_Split_Train)
        self.chBox_Manual_Shuffle.setObjectName(u"chBox_Manual_Shuffle")
        self.chBox_Manual_Shuffle.setChecked(True)

        self.horizontalLayout_12.addWidget(self.chBox_Manual_Shuffle)

        self.pBtn_Split_Target_To_A_B = QPushButton(self.grp_Split_Train)
        self.pBtn_Split_Target_To_A_B.setObjectName(u"pBtn_Split_Target_To_A_B")

        self.horizontalLayout_12.addWidget(self.pBtn_Split_Target_To_A_B)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_Target_Num = QLabel(self.grp_Split_Train)
        self.lbl_Target_Num.setObjectName(u"lbl_Target_Num")

        self.horizontalLayout_11.addWidget(self.lbl_Target_Num)

        self.lEdit_Target_Num = QLineEdit(self.grp_Split_Train)
        self.lEdit_Target_Num.setObjectName(u"lEdit_Target_Num")

        self.horizontalLayout_11.addWidget(self.lEdit_Target_Num)

        self.lbl_A_Num = QLabel(self.grp_Split_Train)
        self.lbl_A_Num.setObjectName(u"lbl_A_Num")

        self.horizontalLayout_11.addWidget(self.lbl_A_Num)

        self.lEdit_A_Num = QLineEdit(self.grp_Split_Train)
        self.lEdit_A_Num.setObjectName(u"lEdit_A_Num")
        self.lEdit_A_Num.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lEdit_A_Num)

        self.lbl_B_Num = QLabel(self.grp_Split_Train)
        self.lbl_B_Num.setObjectName(u"lbl_B_Num")

        self.horizontalLayout_11.addWidget(self.lbl_B_Num)

        self.lEdit_B_Num = QLineEdit(self.grp_Split_Train)
        self.lEdit_B_Num.setObjectName(u"lEdit_B_Num")
        self.lEdit_B_Num.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lEdit_B_Num)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_15.addWidget(self.grp_Split_Train)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.grp_Split_All = QGroupBox(DatasetDialog)
        self.grp_Split_All.setObjectName(u"grp_Split_All")
        self.horizontalLayout_13 = QHBoxLayout(self.grp_Split_All)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_All_Directory = QLabel(self.grp_Split_All)
        self.lbl_All_Directory.setObjectName(u"lbl_All_Directory")

        self.horizontalLayout_9.addWidget(self.lbl_All_Directory)

        self.tBtn_All_Directory = QToolButton(self.grp_Split_All)
        self.tBtn_All_Directory.setObjectName(u"tBtn_All_Directory")

        self.horizontalLayout_9.addWidget(self.tBtn_All_Directory)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.tableWidget_All_Directory = QTableWidget(self.grp_Split_All)
        self.tableWidget_All_Directory.setObjectName(u"tableWidget_All_Directory")
        self.tableWidget_All_Directory.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.tableWidget_All_Directory)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_Output_Directory = QLabel(self.grp_Split_All)
        self.lbl_Output_Directory.setObjectName(u"lbl_Output_Directory")

        self.horizontalLayout_5.addWidget(self.lbl_Output_Directory)

        self.lEdit_Output_Directory_Path = QLineEdit(self.grp_Split_All)
        self.lEdit_Output_Directory_Path.setObjectName(u"lEdit_Output_Directory_Path")

        self.horizontalLayout_5.addWidget(self.lEdit_Output_Directory_Path)

        self.tBtn_Output_Directory = QToolButton(self.grp_Split_All)
        self.tBtn_Output_Directory.setObjectName(u"tBtn_Output_Directory")

        self.horizontalLayout_5.addWidget(self.tBtn_Output_Directory)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_13.addLayout(self.verticalLayout_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_Test_Percentage = QLabel(self.grp_Split_All)
        self.lbl_Test_Percentage.setObjectName(u"lbl_Test_Percentage")

        self.horizontalLayout_10.addWidget(self.lbl_Test_Percentage)

        self.cBox_Test_Percentage = QComboBox(self.grp_Split_All)
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.addItem("")
        self.cBox_Test_Percentage.setObjectName(u"cBox_Test_Percentage")

        self.horizontalLayout_10.addWidget(self.cBox_Test_Percentage)

        self.lbl_Validation_Percentage = QLabel(self.grp_Split_All)
        self.lbl_Validation_Percentage.setObjectName(u"lbl_Validation_Percentage")

        self.horizontalLayout_10.addWidget(self.lbl_Validation_Percentage)

        self.cBox_Validation_Percentage = QComboBox(self.grp_Split_All)
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.addItem("")
        self.cBox_Validation_Percentage.setObjectName(u"cBox_Validation_Percentage")

        self.horizontalLayout_10.addWidget(self.cBox_Validation_Percentage)

        self.chBox_Auto_Shuffle = QCheckBox(self.grp_Split_All)
        self.chBox_Auto_Shuffle.setObjectName(u"chBox_Auto_Shuffle")
        self.chBox_Auto_Shuffle.setChecked(True)

        self.horizontalLayout_10.addWidget(self.chBox_Auto_Shuffle)

        self.pBtn_Split_All_To_Train_Validation_Test = QPushButton(self.grp_Split_All)
        self.pBtn_Split_All_To_Train_Validation_Test.setObjectName(u"pBtn_Split_All_To_Train_Validation_Test")

        self.horizontalLayout_10.addWidget(self.pBtn_Split_All_To_Train_Validation_Test)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.tableWidget_Train_Validation_Test = QTableWidget(self.grp_Split_All)
        self.tableWidget_Train_Validation_Test.setObjectName(u"tableWidget_Train_Validation_Test")
        self.tableWidget_Train_Validation_Test.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_9.addWidget(self.tableWidget_Train_Validation_Test)

        self.splitter = QSplitter(self.grp_Split_All)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.cBox_Dataset_Type = QComboBox(self.splitter)
        self.cBox_Dataset_Type.addItem("")
        self.cBox_Dataset_Type.addItem("")
        self.cBox_Dataset_Type.addItem("")
        self.cBox_Dataset_Type.setObjectName(u"cBox_Dataset_Type")
        self.splitter.addWidget(self.cBox_Dataset_Type)
        self.pBtn_Make_Meta_CSV = QPushButton(self.splitter)
        self.pBtn_Make_Meta_CSV.setObjectName(u"pBtn_Make_Meta_CSV")
        self.splitter.addWidget(self.pBtn_Make_Meta_CSV)

        self.verticalLayout_9.addWidget(self.splitter)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.verticalLayout_2.addWidget(self.grp_Split_All)


        self.retranslateUi(DatasetDialog)

        self.cBox_B_Percentage.setCurrentIndex(4)
        self.cBox_Test_Percentage.setCurrentIndex(4)
        self.cBox_Validation_Percentage.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(DatasetDialog)
    # setupUi

    def retranslateUi(self, DatasetDialog):
        DatasetDialog.setWindowTitle(QCoreApplication.translate("DatasetDialog", u"DatasetDialog", None))
        self.grp_Numerical_Labeling.setTitle(QCoreApplication.translate("DatasetDialog", u"\u30a2\u30ce\u30c6\u30fc\u30b7\u30e7\u30f3\u3092CSV\u30d5\u30a1\u30a4\u30eb\u3068\u3057\u3066\u4fdd\u5b58\u3059\u308b", None))
        self.lbl_Raw_Data_Dir.setText(QCoreApplication.translate("DatasetDialog", u"Raw Data Dir", None))
        self.lEdit_Raw_Data_Dir.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Raw Directory Path", None))
        self.tBtn_Raw_Data_Dir.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_Csv_Data_Dir.setText(QCoreApplication.translate("DatasetDialog", u"Csv Data Dir", None))
        self.lEdit_Csv_Data_Dir.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Csv Directory Path", None))
        self.tBtn_Csv_Data_Dir.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_Raw_Data_Count.setText(QCoreApplication.translate("DatasetDialog", u"Count", None))
        self.lEdit_Raw_Data_Count.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Count", None))
        self.lbl_Raw_Data_Label.setText(QCoreApplication.translate("DatasetDialog", u"Label", None))
        self.lEdit_Raw_Data_Label.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Label", None))
        self.pBtn_Labeling.setText(QCoreApplication.translate("DatasetDialog", u"Labeling", None))
        self.lEdit_Valid_Raw_Data_Count.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Valid Count", None))
        self.grp_Split_Train.setTitle(QCoreApplication.translate("DatasetDialog", u"\u624b\u52d5\u5206\u5272(Target -> A B)", None))
        self.lbl_Target_Directory_Path.setText(QCoreApplication.translate("DatasetDialog", u"Target", None))
        self.lEdit_Target_Directory_Path.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Target Directory Path", None))
        self.tBtn_Target_Directory_Path.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_A_Directory_Path.setText(QCoreApplication.translate("DatasetDialog", u"A", None))
        self.lEdit_A_Directory_Path.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"A Directory Path", None))
        self.tBtn_A_Directory_Path.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_B_Directory_Path.setText(QCoreApplication.translate("DatasetDialog", u"B", None))
        self.lEdit_B_Directory_Path.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"B Directory Path", None))
        self.tBtn_B_Directory_Path.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_B_Percentage.setText(QCoreApplication.translate("DatasetDialog", u"B %", None))
        self.cBox_B_Percentage.setItemText(0, QCoreApplication.translate("DatasetDialog", u"90%", None))
        self.cBox_B_Percentage.setItemText(1, QCoreApplication.translate("DatasetDialog", u"80%", None))
        self.cBox_B_Percentage.setItemText(2, QCoreApplication.translate("DatasetDialog", u"70%", None))
        self.cBox_B_Percentage.setItemText(3, QCoreApplication.translate("DatasetDialog", u"60%", None))
        self.cBox_B_Percentage.setItemText(4, QCoreApplication.translate("DatasetDialog", u"50%", None))
        self.cBox_B_Percentage.setItemText(5, QCoreApplication.translate("DatasetDialog", u"40%", None))
        self.cBox_B_Percentage.setItemText(6, QCoreApplication.translate("DatasetDialog", u"30%", None))
        self.cBox_B_Percentage.setItemText(7, QCoreApplication.translate("DatasetDialog", u"20%", None))
        self.cBox_B_Percentage.setItemText(8, QCoreApplication.translate("DatasetDialog", u"10%", None))

        self.chBox_Manual_Shuffle.setText(QCoreApplication.translate("DatasetDialog", u"Shuffle", None))
        self.pBtn_Split_Target_To_A_B.setText(QCoreApplication.translate("DatasetDialog", u"Split", None))
        self.lbl_Target_Num.setText(QCoreApplication.translate("DatasetDialog", u"Target", None))
        self.lEdit_Target_Num.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Count", None))
        self.lbl_A_Num.setText(QCoreApplication.translate("DatasetDialog", u"A", None))
        self.lEdit_A_Num.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Count", None))
        self.lbl_B_Num.setText(QCoreApplication.translate("DatasetDialog", u"B", None))
        self.lEdit_B_Num.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Count", None))
        self.grp_Split_All.setTitle(QCoreApplication.translate("DatasetDialog", u"\u81ea\u52d5\u5206\u5272(All -> Train Validation test)", None))
        self.lbl_All_Directory.setText(QCoreApplication.translate("DatasetDialog", u"Select All Directories which are split to Train, Validation, test", None))
        self.tBtn_All_Directory.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_Output_Directory.setText(QCoreApplication.translate("DatasetDialog", u"Output", None))
        self.lEdit_Output_Directory_Path.setPlaceholderText(QCoreApplication.translate("DatasetDialog", u"Output Directory Path", None))
        self.tBtn_Output_Directory.setText(QCoreApplication.translate("DatasetDialog", u"...", None))
        self.lbl_Test_Percentage.setText(QCoreApplication.translate("DatasetDialog", u"test %", None))
        self.cBox_Test_Percentage.setItemText(0, QCoreApplication.translate("DatasetDialog", u"90%", None))
        self.cBox_Test_Percentage.setItemText(1, QCoreApplication.translate("DatasetDialog", u"80%", None))
        self.cBox_Test_Percentage.setItemText(2, QCoreApplication.translate("DatasetDialog", u"70%", None))
        self.cBox_Test_Percentage.setItemText(3, QCoreApplication.translate("DatasetDialog", u"60%", None))
        self.cBox_Test_Percentage.setItemText(4, QCoreApplication.translate("DatasetDialog", u"50%", None))
        self.cBox_Test_Percentage.setItemText(5, QCoreApplication.translate("DatasetDialog", u"40%", None))
        self.cBox_Test_Percentage.setItemText(6, QCoreApplication.translate("DatasetDialog", u"30%", None))
        self.cBox_Test_Percentage.setItemText(7, QCoreApplication.translate("DatasetDialog", u"20%", None))
        self.cBox_Test_Percentage.setItemText(8, QCoreApplication.translate("DatasetDialog", u"10%", None))

        self.lbl_Validation_Percentage.setText(QCoreApplication.translate("DatasetDialog", u"Validation %", None))
        self.cBox_Validation_Percentage.setItemText(0, QCoreApplication.translate("DatasetDialog", u"90%", None))
        self.cBox_Validation_Percentage.setItemText(1, QCoreApplication.translate("DatasetDialog", u"80%", None))
        self.cBox_Validation_Percentage.setItemText(2, QCoreApplication.translate("DatasetDialog", u"70%", None))
        self.cBox_Validation_Percentage.setItemText(3, QCoreApplication.translate("DatasetDialog", u"60%", None))
        self.cBox_Validation_Percentage.setItemText(4, QCoreApplication.translate("DatasetDialog", u"50%", None))
        self.cBox_Validation_Percentage.setItemText(5, QCoreApplication.translate("DatasetDialog", u"40%", None))
        self.cBox_Validation_Percentage.setItemText(6, QCoreApplication.translate("DatasetDialog", u"30%", None))
        self.cBox_Validation_Percentage.setItemText(7, QCoreApplication.translate("DatasetDialog", u"20%", None))
        self.cBox_Validation_Percentage.setItemText(8, QCoreApplication.translate("DatasetDialog", u"10%", None))

        self.chBox_Auto_Shuffle.setText(QCoreApplication.translate("DatasetDialog", u"Shuffle", None))
        self.pBtn_Split_All_To_Train_Validation_Test.setText(QCoreApplication.translate("DatasetDialog", u"Split", None))
        self.cBox_Dataset_Type.setItemText(0, QCoreApplication.translate("DatasetDialog", u"Train", None))
        self.cBox_Dataset_Type.setItemText(1, QCoreApplication.translate("DatasetDialog", u"Validation", None))
        self.cBox_Dataset_Type.setItemText(2, QCoreApplication.translate("DatasetDialog", u"test", None))

        self.pBtn_Make_Meta_CSV.setText(QCoreApplication.translate("DatasetDialog", u"Make Meta CSV", None))
    # retranslateUi

