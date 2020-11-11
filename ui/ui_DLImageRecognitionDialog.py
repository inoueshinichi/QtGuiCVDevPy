# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_DLImageRecognitionDialog.ui'
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


class Ui_DLImageRecognitionDialog(object):
    def setupUi(self, DLImageRecognitionDialog):
        if DLImageRecognitionDialog.objectName():
            DLImageRecognitionDialog.setObjectName(u"DLImageRecognitionDialog")
        DLImageRecognitionDialog.resize(1362, 666)
        self.verticalLayout_7 = QVBoxLayout(DLImageRecognitionDialog)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grp_Dataset_Meta_CSV = QGroupBox(DLImageRecognitionDialog)
        self.grp_Dataset_Meta_CSV.setObjectName(u"grp_Dataset_Meta_CSV")
        self.verticalLayout_5 = QVBoxLayout(self.grp_Dataset_Meta_CSV)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lbl_Meta_CSV_Test = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Meta_CSV_Test.setObjectName(u"lbl_Meta_CSV_Test")

        self.gridLayout_9.addWidget(self.lbl_Meta_CSV_Test, 4, 0, 1, 1)

        self.lEdit_Meta_CSV_Train_File_Path = QLineEdit(self.grp_Dataset_Meta_CSV)
        self.lEdit_Meta_CSV_Train_File_Path.setObjectName(u"lEdit_Meta_CSV_Train_File_Path")

        self.gridLayout_9.addWidget(self.lEdit_Meta_CSV_Train_File_Path, 2, 1, 1, 1)

        self.tBtn_Meta_CSV_Test_File_Path = QToolButton(self.grp_Dataset_Meta_CSV)
        self.tBtn_Meta_CSV_Test_File_Path.setObjectName(u"tBtn_Meta_CSV_Test_File_Path")

        self.gridLayout_9.addWidget(self.tBtn_Meta_CSV_Test_File_Path, 4, 2, 1, 1)

        self.tBtn_Meta_CSV_Train_File_Path = QToolButton(self.grp_Dataset_Meta_CSV)
        self.tBtn_Meta_CSV_Train_File_Path.setObjectName(u"tBtn_Meta_CSV_Train_File_Path")

        self.gridLayout_9.addWidget(self.tBtn_Meta_CSV_Train_File_Path, 2, 2, 1, 1)

        self.lbl_Encode_Type = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Encode_Type.setObjectName(u"lbl_Encode_Type")

        self.gridLayout_9.addWidget(self.lbl_Encode_Type, 0, 0, 1, 1)

        self.tBtn_Meta_CSV_Validation_File_Path = QToolButton(self.grp_Dataset_Meta_CSV)
        self.tBtn_Meta_CSV_Validation_File_Path.setObjectName(u"tBtn_Meta_CSV_Validation_File_Path")

        self.gridLayout_9.addWidget(self.tBtn_Meta_CSV_Validation_File_Path, 3, 2, 1, 1)

        self.cBox_Encode_Type = QComboBox(self.grp_Dataset_Meta_CSV)
        self.cBox_Encode_Type.addItem("")
        self.cBox_Encode_Type.addItem("")
        self.cBox_Encode_Type.setObjectName(u"cBox_Encode_Type")

        self.gridLayout_9.addWidget(self.cBox_Encode_Type, 0, 1, 1, 2)

        self.lEdit_Meta_CSV_Validation_File_Path = QLineEdit(self.grp_Dataset_Meta_CSV)
        self.lEdit_Meta_CSV_Validation_File_Path.setObjectName(u"lEdit_Meta_CSV_Validation_File_Path")

        self.gridLayout_9.addWidget(self.lEdit_Meta_CSV_Validation_File_Path, 3, 1, 1, 1)

        self.lbl_Meta_CSV_Train_Dir = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Meta_CSV_Train_Dir.setObjectName(u"lbl_Meta_CSV_Train_Dir")

        self.gridLayout_9.addWidget(self.lbl_Meta_CSV_Train_Dir, 2, 0, 1, 1)

        self.lbl_Meta_CSV_Validation_Dir = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Meta_CSV_Validation_Dir.setObjectName(u"lbl_Meta_CSV_Validation_Dir")

        self.gridLayout_9.addWidget(self.lbl_Meta_CSV_Validation_Dir, 3, 0, 1, 1)

        self.lEdit_Meta_CSV_Test_File_Path = QLineEdit(self.grp_Dataset_Meta_CSV)
        self.lEdit_Meta_CSV_Test_File_Path.setObjectName(u"lEdit_Meta_CSV_Test_File_Path")

        self.gridLayout_9.addWidget(self.lEdit_Meta_CSV_Test_File_Path, 4, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_Header_Meta_CSV = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Header_Meta_CSV.setObjectName(u"lbl_Header_Meta_CSV")

        self.horizontalLayout_16.addWidget(self.lbl_Header_Meta_CSV)

        self.rBtn_Header_ON = QRadioButton(self.grp_Dataset_Meta_CSV)
        self.rBtn_Header_ON.setObjectName(u"rBtn_Header_ON")
        self.rBtn_Header_ON.setChecked(True)

        self.horizontalLayout_16.addWidget(self.rBtn_Header_ON)

        self.rBtn_Header_OFF = QRadioButton(self.grp_Dataset_Meta_CSV)
        self.rBtn_Header_OFF.setObjectName(u"rBtn_Header_OFF")

        self.horizontalLayout_16.addWidget(self.rBtn_Header_OFF)


        self.gridLayout_9.addLayout(self.horizontalLayout_16, 1, 0, 1, 3)


        self.verticalLayout_5.addLayout(self.gridLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_Train_Count = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Train_Count.setObjectName(u"lbl_Train_Count")

        self.horizontalLayout.addWidget(self.lbl_Train_Count)

        self.lEdit_Train_Count = QLineEdit(self.grp_Dataset_Meta_CSV)
        self.lEdit_Train_Count.setObjectName(u"lEdit_Train_Count")
        self.lEdit_Train_Count.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lEdit_Train_Count)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Validation_Count = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Validation_Count.setObjectName(u"lbl_Validation_Count")

        self.horizontalLayout_2.addWidget(self.lbl_Validation_Count)

        self.lEdit_Validation_Count = QLineEdit(self.grp_Dataset_Meta_CSV)
        self.lEdit_Validation_Count.setObjectName(u"lEdit_Validation_Count")
        self.lEdit_Validation_Count.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lEdit_Validation_Count)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Test_Count = QLabel(self.grp_Dataset_Meta_CSV)
        self.lbl_Test_Count.setObjectName(u"lbl_Test_Count")

        self.horizontalLayout_3.addWidget(self.lbl_Test_Count)

        self.lEdit_Test_Count = QLineEdit(self.grp_Dataset_Meta_CSV)
        self.lEdit_Test_Count.setObjectName(u"lEdit_Test_Count")
        self.lEdit_Test_Count.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lEdit_Test_Count)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.grp_Dataset_Meta_CSV)

        self.grp_Operation = QGroupBox(DLImageRecognitionDialog)
        self.grp_Operation.setObjectName(u"grp_Operation")
        self.gridLayout_3 = QGridLayout(self.grp_Operation)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pBtn_Data_Augmentation = QPushButton(self.grp_Operation)
        self.pBtn_Data_Augmentation.setObjectName(u"pBtn_Data_Augmentation")

        self.gridLayout_3.addWidget(self.pBtn_Data_Augmentation, 0, 0, 1, 1)

        self.pBtn_Training_Init = QPushButton(self.grp_Operation)
        self.pBtn_Training_Init.setObjectName(u"pBtn_Training_Init")

        self.gridLayout_3.addWidget(self.pBtn_Training_Init, 0, 1, 1, 1)

        self.pBtn_Training = QPushButton(self.grp_Operation)
        self.pBtn_Training.setObjectName(u"pBtn_Training")

        self.gridLayout_3.addWidget(self.pBtn_Training, 1, 0, 1, 1)

        self.pBtn_Training_Stop = QPushButton(self.grp_Operation)
        self.pBtn_Training_Stop.setObjectName(u"pBtn_Training_Stop")

        self.gridLayout_3.addWidget(self.pBtn_Training_Stop, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.grp_Operation)

        self.grp_Metrics = QGroupBox(DLImageRecognitionDialog)
        self.grp_Metrics.setObjectName(u"grp_Metrics")
        self.verticalLayout_3 = QVBoxLayout(self.grp_Metrics)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_Inference_Time = QLabel(self.grp_Metrics)
        self.lbl_Inference_Time.setObjectName(u"lbl_Inference_Time")

        self.horizontalLayout_15.addWidget(self.lbl_Inference_Time)

        self.lEdit_Inference_Time = QLineEdit(self.grp_Metrics)
        self.lEdit_Inference_Time.setObjectName(u"lEdit_Inference_Time")

        self.horizontalLayout_15.addWidget(self.lEdit_Inference_Time)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pBtn_ROC_Curve = QPushButton(self.grp_Metrics)
        self.pBtn_ROC_Curve.setObjectName(u"pBtn_ROC_Curve")

        self.horizontalLayout_9.addWidget(self.pBtn_ROC_Curve)

        self.pBtn_Confusion_Matrix = QPushButton(self.grp_Metrics)
        self.pBtn_Confusion_Matrix.setObjectName(u"pBtn_Confusion_Matrix")

        self.horizontalLayout_9.addWidget(self.pBtn_Confusion_Matrix)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pBtn_Score = QPushButton(self.grp_Metrics)
        self.pBtn_Score.setObjectName(u"pBtn_Score")

        self.horizontalLayout_10.addWidget(self.pBtn_Score)

        self.pBtn_Loss = QPushButton(self.grp_Metrics)
        self.pBtn_Loss.setObjectName(u"pBtn_Loss")

        self.horizontalLayout_10.addWidget(self.pBtn_Loss)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 31, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.grp_Metrics)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)

        self.grp_PreTraining_Model = QGroupBox(DLImageRecognitionDialog)
        self.grp_PreTraining_Model.setObjectName(u"grp_PreTraining_Model")
        self.gridLayout = QGridLayout(self.grp_PreTraining_Model)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_Final_Layer_Neuron = QLabel(self.grp_PreTraining_Model)
        self.lbl_Final_Layer_Neuron.setObjectName(u"lbl_Final_Layer_Neuron")

        self.horizontalLayout_5.addWidget(self.lbl_Final_Layer_Neuron)

        self.sBox_Final_Layer_Neuron = QSpinBox(self.grp_PreTraining_Model)
        self.sBox_Final_Layer_Neuron.setObjectName(u"sBox_Final_Layer_Neuron")
        self.sBox_Final_Layer_Neuron.setMinimum(2)
        self.sBox_Final_Layer_Neuron.setMaximum(10000)

        self.horizontalLayout_5.addWidget(self.sBox_Final_Layer_Neuron)

        self.pBtn_Model_Architecture = QPushButton(self.grp_PreTraining_Model)
        self.pBtn_Model_Architecture.setObjectName(u"pBtn_Model_Architecture")

        self.horizontalLayout_5.addWidget(self.pBtn_Model_Architecture)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.cBox_PreTraining_Model = QComboBox(self.grp_PreTraining_Model)
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.addItem("")
        self.cBox_PreTraining_Model.setObjectName(u"cBox_PreTraining_Model")

        self.gridLayout.addWidget(self.cBox_PreTraining_Model, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lbl_Leaerning_Type = QLabel(self.grp_PreTraining_Model)
        self.lbl_Leaerning_Type.setObjectName(u"lbl_Leaerning_Type")

        self.horizontalLayout_14.addWidget(self.lbl_Leaerning_Type)

        self.cBox_Learning_Type = QComboBox(self.grp_PreTraining_Model)
        self.cBox_Learning_Type.addItem("")
        self.cBox_Learning_Type.addItem("")
        self.cBox_Learning_Type.addItem("")
        self.cBox_Learning_Type.setObjectName(u"cBox_Learning_Type")

        self.horizontalLayout_14.addWidget(self.cBox_Learning_Type)


        self.gridLayout.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        self.tEdit_ModelStructure = QTextEdit(self.grp_PreTraining_Model)
        self.tEdit_ModelStructure.setObjectName(u"tEdit_ModelStructure")

        self.gridLayout.addWidget(self.tEdit_ModelStructure, 3, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.grp_PreTraining_Model)

        self.grp_Training_Parameters = QGroupBox(DLImageRecognitionDialog)
        self.grp_Training_Parameters.setObjectName(u"grp_Training_Parameters")
        self.horizontalLayout_73 = QHBoxLayout(self.grp_Training_Parameters)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_Batch_Size = QLabel(self.grp_Training_Parameters)
        self.lbl_Batch_Size.setObjectName(u"lbl_Batch_Size")

        self.horizontalLayout_6.addWidget(self.lbl_Batch_Size)

        self.sBox_Batch_Size = QSpinBox(self.grp_Training_Parameters)
        self.sBox_Batch_Size.setObjectName(u"sBox_Batch_Size")
        self.sBox_Batch_Size.setMinimum(1)
        self.sBox_Batch_Size.setMaximum(100)
        self.sBox_Batch_Size.setValue(5)

        self.horizontalLayout_6.addWidget(self.sBox_Batch_Size)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.lbl_Epochs = QLabel(self.grp_Training_Parameters)
        self.lbl_Epochs.setObjectName(u"lbl_Epochs")

        self.horizontalLayout_74.addWidget(self.lbl_Epochs)

        self.sBox_Epochs = QSpinBox(self.grp_Training_Parameters)
        self.sBox_Epochs.setObjectName(u"sBox_Epochs")
        self.sBox_Epochs.setMinimum(10)
        self.sBox_Epochs.setMaximum(1000)
        self.sBox_Epochs.setValue(100)

        self.horizontalLayout_74.addWidget(self.sBox_Epochs)


        self.verticalLayout_2.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_Update_Interval = QLabel(self.grp_Training_Parameters)
        self.lbl_Update_Interval.setObjectName(u"lbl_Update_Interval")

        self.horizontalLayout_17.addWidget(self.lbl_Update_Interval)

        self.sBox_Update_Interval = QSpinBox(self.grp_Training_Parameters)
        self.sBox_Update_Interval.setObjectName(u"sBox_Update_Interval")
        self.sBox_Update_Interval.setMinimum(1)
        self.sBox_Update_Interval.setMaximum(100)

        self.horizontalLayout_17.addWidget(self.sBox_Update_Interval)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.lbl_Weight_Decay = QLabel(self.grp_Training_Parameters)
        self.lbl_Weight_Decay.setObjectName(u"lbl_Weight_Decay")

        self.horizontalLayout_75.addWidget(self.lbl_Weight_Decay)

        self.dsBox_Weight_Decay = QDoubleSpinBox(self.grp_Training_Parameters)
        self.dsBox_Weight_Decay.setObjectName(u"dsBox_Weight_Decay")
        self.dsBox_Weight_Decay.setMaximum(10.000000000000000)
        self.dsBox_Weight_Decay.setSingleStep(0.010000000000000)

        self.horizontalLayout_75.addWidget(self.dsBox_Weight_Decay)


        self.verticalLayout_2.addLayout(self.horizontalLayout_75)

        self.cBox_Optimizer = QComboBox(self.grp_Training_Parameters)
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.addItem("")
        self.cBox_Optimizer.setObjectName(u"cBox_Optimizer")

        self.verticalLayout_2.addWidget(self.cBox_Optimizer)

        self.stackedWidget_Optimizer = QStackedWidget(self.grp_Training_Parameters)
        self.stackedWidget_Optimizer.setObjectName(u"stackedWidget_Optimizer")
        self.page_Optimizer_SGD = QWidget()
        self.page_Optimizer_SGD.setObjectName(u"page_Optimizer_SGD")
        self.verticalLayout_10 = QVBoxLayout(self.page_Optimizer_SGD)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.grp_SGD = QGroupBox(self.page_Optimizer_SGD)
        self.grp_SGD.setObjectName(u"grp_SGD")
        self.verticalLayout_13 = QVBoxLayout(self.grp_SGD)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lbl_SGD_Learning_Rate = QLabel(self.grp_SGD)
        self.lbl_SGD_Learning_Rate.setObjectName(u"lbl_SGD_Learning_Rate")

        self.horizontalLayout_19.addWidget(self.lbl_SGD_Learning_Rate)

        self.dsBox_SGD_Learning_Rate = QDoubleSpinBox(self.grp_SGD)
        self.dsBox_SGD_Learning_Rate.setObjectName(u"dsBox_SGD_Learning_Rate")
        self.dsBox_SGD_Learning_Rate.setDecimals(3)
        self.dsBox_SGD_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_SGD_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_SGD_Learning_Rate.setValue(0.010000000000000)

        self.horizontalLayout_19.addWidget(self.dsBox_SGD_Learning_Rate)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)


        self.verticalLayout_13.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.pBtn_SGD_Reset = QPushButton(self.grp_SGD)
        self.pBtn_SGD_Reset.setObjectName(u"pBtn_SGD_Reset")

        self.verticalLayout_13.addWidget(self.pBtn_SGD_Reset)


        self.verticalLayout_10.addWidget(self.grp_SGD)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_SGD)
        self.page_Optimizer_Momentum = QWidget()
        self.page_Optimizer_Momentum.setObjectName(u"page_Optimizer_Momentum")
        self.verticalLayout_12 = QVBoxLayout(self.page_Optimizer_Momentum)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.grp_Momentum = QGroupBox(self.page_Optimizer_Momentum)
        self.grp_Momentum.setObjectName(u"grp_Momentum")
        self.verticalLayout_11 = QVBoxLayout(self.grp_Momentum)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lbl_Momentum_Learning_Rate = QLabel(self.grp_Momentum)
        self.lbl_Momentum_Learning_Rate.setObjectName(u"lbl_Momentum_Learning_Rate")

        self.horizontalLayout_22.addWidget(self.lbl_Momentum_Learning_Rate)

        self.dsBox_Momentum_Learning_Rate = QDoubleSpinBox(self.grp_Momentum)
        self.dsBox_Momentum_Learning_Rate.setObjectName(u"dsBox_Momentum_Learning_Rate")
        self.dsBox_Momentum_Learning_Rate.setDecimals(3)
        self.dsBox_Momentum_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_Momentum_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_Momentum_Learning_Rate.setValue(0.010000000000000)

        self.horizontalLayout_22.addWidget(self.dsBox_Momentum_Learning_Rate)


        self.verticalLayout_14.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lbl_Momentum_Momentum = QLabel(self.grp_Momentum)
        self.lbl_Momentum_Momentum.setObjectName(u"lbl_Momentum_Momentum")

        self.horizontalLayout_23.addWidget(self.lbl_Momentum_Momentum)

        self.dsBox_Momentum_Momentum = QDoubleSpinBox(self.grp_Momentum)
        self.dsBox_Momentum_Momentum.setObjectName(u"dsBox_Momentum_Momentum")
        self.dsBox_Momentum_Momentum.setDecimals(3)
        self.dsBox_Momentum_Momentum.setMaximum(5.000000000000000)
        self.dsBox_Momentum_Momentum.setSingleStep(0.010000000000000)
        self.dsBox_Momentum_Momentum.setValue(0.900000000000000)

        self.horizontalLayout_23.addWidget(self.dsBox_Momentum_Momentum)


        self.verticalLayout_14.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_21.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_3 = QSpacerItem(20, 69, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.pBtn_Momentum_Reset = QPushButton(self.grp_Momentum)
        self.pBtn_Momentum_Reset.setObjectName(u"pBtn_Momentum_Reset")

        self.verticalLayout_11.addWidget(self.pBtn_Momentum_Reset)


        self.verticalLayout_12.addWidget(self.grp_Momentum)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_Momentum)
        self.page_Optimizer_Nesterov = QWidget()
        self.page_Optimizer_Nesterov.setObjectName(u"page_Optimizer_Nesterov")
        self.verticalLayout_17 = QVBoxLayout(self.page_Optimizer_Nesterov)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.grp_Nesterov = QGroupBox(self.page_Optimizer_Nesterov)
        self.grp_Nesterov.setObjectName(u"grp_Nesterov")
        self.verticalLayout_15 = QVBoxLayout(self.grp_Nesterov)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lbl_Nesterov_Learning_Rate = QLabel(self.grp_Nesterov)
        self.lbl_Nesterov_Learning_Rate.setObjectName(u"lbl_Nesterov_Learning_Rate")

        self.horizontalLayout_25.addWidget(self.lbl_Nesterov_Learning_Rate)

        self.dsBox_Nesterov_Learning_Rate = QDoubleSpinBox(self.grp_Nesterov)
        self.dsBox_Nesterov_Learning_Rate.setObjectName(u"dsBox_Nesterov_Learning_Rate")
        self.dsBox_Nesterov_Learning_Rate.setDecimals(3)
        self.dsBox_Nesterov_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_Nesterov_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_Nesterov_Learning_Rate.setValue(0.010000000000000)

        self.horizontalLayout_25.addWidget(self.dsBox_Nesterov_Learning_Rate)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lbl_Nesterov_Momentum = QLabel(self.grp_Nesterov)
        self.lbl_Nesterov_Momentum.setObjectName(u"lbl_Nesterov_Momentum")

        self.horizontalLayout_26.addWidget(self.lbl_Nesterov_Momentum)

        self.dsBox_Nesterov_Momentum = QDoubleSpinBox(self.grp_Nesterov)
        self.dsBox_Nesterov_Momentum.setObjectName(u"dsBox_Nesterov_Momentum")
        self.dsBox_Nesterov_Momentum.setDecimals(3)
        self.dsBox_Nesterov_Momentum.setMaximum(5.000000000000000)
        self.dsBox_Nesterov_Momentum.setSingleStep(0.010000000000000)
        self.dsBox_Nesterov_Momentum.setValue(0.900000000000000)

        self.horizontalLayout_26.addWidget(self.dsBox_Nesterov_Momentum)


        self.verticalLayout_16.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_24.addLayout(self.verticalLayout_16)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_4 = QSpacerItem(20, 69, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.pBtn_Nesterov_Reset = QPushButton(self.grp_Nesterov)
        self.pBtn_Nesterov_Reset.setObjectName(u"pBtn_Nesterov_Reset")

        self.verticalLayout_15.addWidget(self.pBtn_Nesterov_Reset)


        self.verticalLayout_17.addWidget(self.grp_Nesterov)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_Nesterov)
        self.page_Optimizer_RMSprop = QWidget()
        self.page_Optimizer_RMSprop.setObjectName(u"page_Optimizer_RMSprop")
        self.verticalLayout_20 = QVBoxLayout(self.page_Optimizer_RMSprop)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.grp_Optimizer_RMSprop = QGroupBox(self.page_Optimizer_RMSprop)
        self.grp_Optimizer_RMSprop.setObjectName(u"grp_Optimizer_RMSprop")
        self.verticalLayout_18 = QVBoxLayout(self.grp_Optimizer_RMSprop)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lbl_RMSprop_Learning_Rate = QLabel(self.grp_Optimizer_RMSprop)
        self.lbl_RMSprop_Learning_Rate.setObjectName(u"lbl_RMSprop_Learning_Rate")

        self.horizontalLayout_28.addWidget(self.lbl_RMSprop_Learning_Rate)

        self.dsBox_RMSprop_Learning_Rate = QDoubleSpinBox(self.grp_Optimizer_RMSprop)
        self.dsBox_RMSprop_Learning_Rate.setObjectName(u"dsBox_RMSprop_Learning_Rate")
        self.dsBox_RMSprop_Learning_Rate.setDecimals(3)
        self.dsBox_RMSprop_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_RMSprop_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_RMSprop_Learning_Rate.setValue(0.010000000000000)

        self.horizontalLayout_28.addWidget(self.dsBox_RMSprop_Learning_Rate)


        self.verticalLayout_19.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lbl_RMSprop_Alpha = QLabel(self.grp_Optimizer_RMSprop)
        self.lbl_RMSprop_Alpha.setObjectName(u"lbl_RMSprop_Alpha")

        self.horizontalLayout_29.addWidget(self.lbl_RMSprop_Alpha)

        self.dsBox_RMSprop_Alpha = QDoubleSpinBox(self.grp_Optimizer_RMSprop)
        self.dsBox_RMSprop_Alpha.setObjectName(u"dsBox_RMSprop_Alpha")
        self.dsBox_RMSprop_Alpha.setDecimals(3)
        self.dsBox_RMSprop_Alpha.setMaximum(5.000000000000000)
        self.dsBox_RMSprop_Alpha.setSingleStep(0.010000000000000)
        self.dsBox_RMSprop_Alpha.setValue(0.990000000000000)

        self.horizontalLayout_29.addWidget(self.dsBox_RMSprop_Alpha)


        self.verticalLayout_19.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lbl_RMSprop_Epsilon = QLabel(self.grp_Optimizer_RMSprop)
        self.lbl_RMSprop_Epsilon.setObjectName(u"lbl_RMSprop_Epsilon")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_RMSprop_Epsilon.sizePolicy().hasHeightForWidth())
        self.lbl_RMSprop_Epsilon.setSizePolicy(sizePolicy)

        self.horizontalLayout_30.addWidget(self.lbl_RMSprop_Epsilon)

        self.lEdit_RMSprop_Epsilon = QLineEdit(self.grp_Optimizer_RMSprop)
        self.lEdit_RMSprop_Epsilon.setObjectName(u"lEdit_RMSprop_Epsilon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lEdit_RMSprop_Epsilon.sizePolicy().hasHeightForWidth())
        self.lEdit_RMSprop_Epsilon.setSizePolicy(sizePolicy1)

        self.horizontalLayout_30.addWidget(self.lEdit_RMSprop_Epsilon)


        self.verticalLayout_19.addLayout(self.horizontalLayout_30)

        self.chBox_RMSprop_Centered = QCheckBox(self.grp_Optimizer_RMSprop)
        self.chBox_RMSprop_Centered.setObjectName(u"chBox_RMSprop_Centered")

        self.verticalLayout_19.addWidget(self.chBox_RMSprop_Centered)


        self.horizontalLayout_27.addLayout(self.verticalLayout_19)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_4)


        self.verticalLayout_18.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_5)

        self.pBtn_RMSprop_Reset = QPushButton(self.grp_Optimizer_RMSprop)
        self.pBtn_RMSprop_Reset.setObjectName(u"pBtn_RMSprop_Reset")

        self.verticalLayout_18.addWidget(self.pBtn_RMSprop_Reset)


        self.verticalLayout_20.addWidget(self.grp_Optimizer_RMSprop)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_RMSprop)
        self.page_Optimizer_Adadelta = QWidget()
        self.page_Optimizer_Adadelta.setObjectName(u"page_Optimizer_Adadelta")
        self.verticalLayout_23 = QVBoxLayout(self.page_Optimizer_Adadelta)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.grp_Adadelta = QGroupBox(self.page_Optimizer_Adadelta)
        self.grp_Adadelta.setObjectName(u"grp_Adadelta")
        self.verticalLayout_21 = QVBoxLayout(self.grp_Adadelta)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lbl_Adadelta_Learning_Rate = QLabel(self.grp_Adadelta)
        self.lbl_Adadelta_Learning_Rate.setObjectName(u"lbl_Adadelta_Learning_Rate")

        self.horizontalLayout_32.addWidget(self.lbl_Adadelta_Learning_Rate)

        self.dsBox_Adadelta_Learning_Rate = QDoubleSpinBox(self.grp_Adadelta)
        self.dsBox_Adadelta_Learning_Rate.setObjectName(u"dsBox_Adadelta_Learning_Rate")
        self.dsBox_Adadelta_Learning_Rate.setDecimals(3)
        self.dsBox_Adadelta_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_Adadelta_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_Adadelta_Learning_Rate.setValue(1.000000000000000)

        self.horizontalLayout_32.addWidget(self.dsBox_Adadelta_Learning_Rate)


        self.verticalLayout_22.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lbl_Adadelta_Rho = QLabel(self.grp_Adadelta)
        self.lbl_Adadelta_Rho.setObjectName(u"lbl_Adadelta_Rho")

        self.horizontalLayout_33.addWidget(self.lbl_Adadelta_Rho)

        self.dsBox_Adadelta_Rho = QDoubleSpinBox(self.grp_Adadelta)
        self.dsBox_Adadelta_Rho.setObjectName(u"dsBox_Adadelta_Rho")
        self.dsBox_Adadelta_Rho.setDecimals(3)
        self.dsBox_Adadelta_Rho.setMaximum(5.000000000000000)
        self.dsBox_Adadelta_Rho.setSingleStep(0.010000000000000)
        self.dsBox_Adadelta_Rho.setValue(0.950000000000000)

        self.horizontalLayout_33.addWidget(self.dsBox_Adadelta_Rho)


        self.verticalLayout_22.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.lbl_Adadelta_Epsilon = QLabel(self.grp_Adadelta)
        self.lbl_Adadelta_Epsilon.setObjectName(u"lbl_Adadelta_Epsilon")
        sizePolicy.setHeightForWidth(self.lbl_Adadelta_Epsilon.sizePolicy().hasHeightForWidth())
        self.lbl_Adadelta_Epsilon.setSizePolicy(sizePolicy)

        self.horizontalLayout_34.addWidget(self.lbl_Adadelta_Epsilon)

        self.lEdit_Adadelta_Epsilon = QLineEdit(self.grp_Adadelta)
        self.lEdit_Adadelta_Epsilon.setObjectName(u"lEdit_Adadelta_Epsilon")
        sizePolicy1.setHeightForWidth(self.lEdit_Adadelta_Epsilon.sizePolicy().hasHeightForWidth())
        self.lEdit_Adadelta_Epsilon.setSizePolicy(sizePolicy1)

        self.horizontalLayout_34.addWidget(self.lEdit_Adadelta_Epsilon)


        self.verticalLayout_22.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_31.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_5)


        self.verticalLayout_21.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.pBtn_Adadelta_Reset = QPushButton(self.grp_Adadelta)
        self.pBtn_Adadelta_Reset.setObjectName(u"pBtn_Adadelta_Reset")

        self.verticalLayout_21.addWidget(self.pBtn_Adadelta_Reset)


        self.verticalLayout_23.addWidget(self.grp_Adadelta)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_Adadelta)
        self.page_Optimizer_Adagrad = QWidget()
        self.page_Optimizer_Adagrad.setObjectName(u"page_Optimizer_Adagrad")
        self.verticalLayout_26 = QVBoxLayout(self.page_Optimizer_Adagrad)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.grp_Adagrad = QGroupBox(self.page_Optimizer_Adagrad)
        self.grp_Adagrad.setObjectName(u"grp_Adagrad")
        self.verticalLayout_24 = QVBoxLayout(self.grp_Adagrad)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.lbl_Adagrad_Learning_Rate = QLabel(self.grp_Adagrad)
        self.lbl_Adagrad_Learning_Rate.setObjectName(u"lbl_Adagrad_Learning_Rate")

        self.horizontalLayout_36.addWidget(self.lbl_Adagrad_Learning_Rate)

        self.dsBox_Adagrad_Learning_Rate = QDoubleSpinBox(self.grp_Adagrad)
        self.dsBox_Adagrad_Learning_Rate.setObjectName(u"dsBox_Adagrad_Learning_Rate")
        self.dsBox_Adagrad_Learning_Rate.setDecimals(3)
        self.dsBox_Adagrad_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_Adagrad_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_Adagrad_Learning_Rate.setValue(0.001000000000000)

        self.horizontalLayout_36.addWidget(self.dsBox_Adagrad_Learning_Rate)


        self.verticalLayout_25.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lbl_Adagrad_Decay = QLabel(self.grp_Adagrad)
        self.lbl_Adagrad_Decay.setObjectName(u"lbl_Adagrad_Decay")

        self.horizontalLayout_37.addWidget(self.lbl_Adagrad_Decay)

        self.dsBox_Adagrad_Decay = QDoubleSpinBox(self.grp_Adagrad)
        self.dsBox_Adagrad_Decay.setObjectName(u"dsBox_Adagrad_Decay")
        self.dsBox_Adagrad_Decay.setDecimals(3)
        self.dsBox_Adagrad_Decay.setMaximum(5.000000000000000)
        self.dsBox_Adagrad_Decay.setSingleStep(0.010000000000000)
        self.dsBox_Adagrad_Decay.setValue(0.950000000000000)

        self.horizontalLayout_37.addWidget(self.dsBox_Adagrad_Decay)


        self.verticalLayout_25.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.lbl_Adagrad_Epsilon = QLabel(self.grp_Adagrad)
        self.lbl_Adagrad_Epsilon.setObjectName(u"lbl_Adagrad_Epsilon")
        sizePolicy.setHeightForWidth(self.lbl_Adagrad_Epsilon.sizePolicy().hasHeightForWidth())
        self.lbl_Adagrad_Epsilon.setSizePolicy(sizePolicy)

        self.horizontalLayout_38.addWidget(self.lbl_Adagrad_Epsilon)

        self.lEdit_Adagrad_Epsilon = QLineEdit(self.grp_Adagrad)
        self.lEdit_Adagrad_Epsilon.setObjectName(u"lEdit_Adagrad_Epsilon")
        sizePolicy1.setHeightForWidth(self.lEdit_Adagrad_Epsilon.sizePolicy().hasHeightForWidth())
        self.lEdit_Adagrad_Epsilon.setSizePolicy(sizePolicy1)

        self.horizontalLayout_38.addWidget(self.lEdit_Adagrad_Epsilon)


        self.verticalLayout_25.addLayout(self.horizontalLayout_38)


        self.horizontalLayout_35.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_6)


        self.verticalLayout_24.addLayout(self.horizontalLayout_35)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_7)

        self.pBtn_Adagrad_Reset = QPushButton(self.grp_Adagrad)
        self.pBtn_Adagrad_Reset.setObjectName(u"pBtn_Adagrad_Reset")

        self.verticalLayout_24.addWidget(self.pBtn_Adagrad_Reset)


        self.verticalLayout_26.addWidget(self.grp_Adagrad)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_Adagrad)
        self.page_Optimizer_Adam = QWidget()
        self.page_Optimizer_Adam.setObjectName(u"page_Optimizer_Adam")
        self.verticalLayout_30 = QVBoxLayout(self.page_Optimizer_Adam)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.grp_Adam = QGroupBox(self.page_Optimizer_Adam)
        self.grp_Adam.setObjectName(u"grp_Adam")
        self.verticalLayout_28 = QVBoxLayout(self.grp_Adam)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.lbl_Adam_Learning_Rate = QLabel(self.grp_Adam)
        self.lbl_Adam_Learning_Rate.setObjectName(u"lbl_Adam_Learning_Rate")

        self.horizontalLayout_76.addWidget(self.lbl_Adam_Learning_Rate)

        self.dsBox_Adam_Learning_Rate = QDoubleSpinBox(self.grp_Adam)
        self.dsBox_Adam_Learning_Rate.setObjectName(u"dsBox_Adam_Learning_Rate")
        self.dsBox_Adam_Learning_Rate.setDecimals(3)
        self.dsBox_Adam_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_Adam_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_Adam_Learning_Rate.setValue(0.001000000000000)

        self.horizontalLayout_76.addWidget(self.dsBox_Adam_Learning_Rate)


        self.verticalLayout_29.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")

        self.verticalLayout_29.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.lbl_Adam_Beta1 = QLabel(self.grp_Adam)
        self.lbl_Adam_Beta1.setObjectName(u"lbl_Adam_Beta1")

        self.horizontalLayout_45.addWidget(self.lbl_Adam_Beta1)

        self.dsBox_Adam_Beta1 = QDoubleSpinBox(self.grp_Adam)
        self.dsBox_Adam_Beta1.setObjectName(u"dsBox_Adam_Beta1")
        self.dsBox_Adam_Beta1.setDecimals(3)
        self.dsBox_Adam_Beta1.setMaximum(5.000000000000000)
        self.dsBox_Adam_Beta1.setSingleStep(0.001000000000000)
        self.dsBox_Adam_Beta1.setValue(0.900000000000000)

        self.horizontalLayout_45.addWidget(self.dsBox_Adam_Beta1)

        self.lbl_Adam_Beta2 = QLabel(self.grp_Adam)
        self.lbl_Adam_Beta2.setObjectName(u"lbl_Adam_Beta2")

        self.horizontalLayout_45.addWidget(self.lbl_Adam_Beta2)

        self.dsBox_Adam_Beta2 = QDoubleSpinBox(self.grp_Adam)
        self.dsBox_Adam_Beta2.setObjectName(u"dsBox_Adam_Beta2")
        self.dsBox_Adam_Beta2.setDecimals(3)
        self.dsBox_Adam_Beta2.setMaximum(5.000000000000000)
        self.dsBox_Adam_Beta2.setSingleStep(0.001000000000000)
        self.dsBox_Adam_Beta2.setValue(0.999000000000000)

        self.horizontalLayout_45.addWidget(self.dsBox_Adam_Beta2)


        self.verticalLayout_29.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.lbl_Adam_Epsilon = QLabel(self.grp_Adam)
        self.lbl_Adam_Epsilon.setObjectName(u"lbl_Adam_Epsilon")

        self.horizontalLayout_46.addWidget(self.lbl_Adam_Epsilon)

        self.lEdit_Adam_Epsilon = QLineEdit(self.grp_Adam)
        self.lEdit_Adam_Epsilon.setObjectName(u"lEdit_Adam_Epsilon")

        self.horizontalLayout_46.addWidget(self.lEdit_Adam_Epsilon)


        self.verticalLayout_29.addLayout(self.horizontalLayout_46)

        self.chBox_Adam_AMSGrad = QCheckBox(self.grp_Adam)
        self.chBox_Adam_AMSGrad.setObjectName(u"chBox_Adam_AMSGrad")

        self.verticalLayout_29.addWidget(self.chBox_Adam_AMSGrad)


        self.horizontalLayout_43.addLayout(self.verticalLayout_29)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_7)


        self.verticalLayout_28.addLayout(self.horizontalLayout_43)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_8)

        self.pBtn_Adam_Reset = QPushButton(self.grp_Adam)
        self.pBtn_Adam_Reset.setObjectName(u"pBtn_Adam_Reset")

        self.verticalLayout_28.addWidget(self.pBtn_Adam_Reset)


        self.verticalLayout_30.addWidget(self.grp_Adam)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_Adam)
        self.page_Optimizer_Adamax = QWidget()
        self.page_Optimizer_Adamax.setObjectName(u"page_Optimizer_Adamax")
        self.verticalLayout_33 = QVBoxLayout(self.page_Optimizer_Adamax)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.grp_Adamax = QGroupBox(self.page_Optimizer_Adamax)
        self.grp_Adamax.setObjectName(u"grp_Adamax")
        self.verticalLayout_31 = QVBoxLayout(self.grp_Adamax)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.lbl_Adamax_Learning_Rate = QLabel(self.grp_Adamax)
        self.lbl_Adamax_Learning_Rate.setObjectName(u"lbl_Adamax_Learning_Rate")

        self.horizontalLayout_48.addWidget(self.lbl_Adamax_Learning_Rate)

        self.dsBox_Adamax_Learning_Rate = QDoubleSpinBox(self.grp_Adamax)
        self.dsBox_Adamax_Learning_Rate.setObjectName(u"dsBox_Adamax_Learning_Rate")
        self.dsBox_Adamax_Learning_Rate.setDecimals(3)
        self.dsBox_Adamax_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_Adamax_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_Adamax_Learning_Rate.setValue(0.001000000000000)

        self.horizontalLayout_48.addWidget(self.dsBox_Adamax_Learning_Rate)


        self.verticalLayout_32.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.lbl_Adamax_Beta1 = QLabel(self.grp_Adamax)
        self.lbl_Adamax_Beta1.setObjectName(u"lbl_Adamax_Beta1")

        self.horizontalLayout_49.addWidget(self.lbl_Adamax_Beta1)

        self.dsBox_Adamax_Beta1 = QDoubleSpinBox(self.grp_Adamax)
        self.dsBox_Adamax_Beta1.setObjectName(u"dsBox_Adamax_Beta1")
        self.dsBox_Adamax_Beta1.setDecimals(3)
        self.dsBox_Adamax_Beta1.setMaximum(5.000000000000000)
        self.dsBox_Adamax_Beta1.setSingleStep(0.001000000000000)
        self.dsBox_Adamax_Beta1.setValue(0.900000000000000)

        self.horizontalLayout_49.addWidget(self.dsBox_Adamax_Beta1)

        self.lbl_Adamax_Beta2 = QLabel(self.grp_Adamax)
        self.lbl_Adamax_Beta2.setObjectName(u"lbl_Adamax_Beta2")

        self.horizontalLayout_49.addWidget(self.lbl_Adamax_Beta2)

        self.dsBox_Adamax_Beta2 = QDoubleSpinBox(self.grp_Adamax)
        self.dsBox_Adamax_Beta2.setObjectName(u"dsBox_Adamax_Beta2")
        self.dsBox_Adamax_Beta2.setDecimals(3)
        self.dsBox_Adamax_Beta2.setMaximum(5.000000000000000)
        self.dsBox_Adamax_Beta2.setSingleStep(0.001000000000000)
        self.dsBox_Adamax_Beta2.setValue(0.999000000000000)

        self.horizontalLayout_49.addWidget(self.dsBox_Adamax_Beta2)


        self.verticalLayout_32.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.lbl_Adamax_Epsilon = QLabel(self.grp_Adamax)
        self.lbl_Adamax_Epsilon.setObjectName(u"lbl_Adamax_Epsilon")

        self.horizontalLayout_50.addWidget(self.lbl_Adamax_Epsilon)

        self.lEdit_Adamax_Epsilon = QLineEdit(self.grp_Adamax)
        self.lEdit_Adamax_Epsilon.setObjectName(u"lEdit_Adamax_Epsilon")

        self.horizontalLayout_50.addWidget(self.lEdit_Adamax_Epsilon)


        self.verticalLayout_32.addLayout(self.horizontalLayout_50)


        self.horizontalLayout_47.addLayout(self.verticalLayout_32)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_8)


        self.verticalLayout_31.addLayout(self.horizontalLayout_47)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_9)

        self.pBtn_Adamax_Reset = QPushButton(self.grp_Adamax)
        self.pBtn_Adamax_Reset.setObjectName(u"pBtn_Adamax_Reset")

        self.verticalLayout_31.addWidget(self.pBtn_Adamax_Reset)


        self.verticalLayout_33.addWidget(self.grp_Adamax)

        self.stackedWidget_Optimizer.addWidget(self.page_Optimizer_Adamax)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_27 = QVBoxLayout(self.page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.grp_AdaBound = QGroupBox(self.page)
        self.grp_AdaBound.setObjectName(u"grp_AdaBound")
        self.verticalLayout_34 = QVBoxLayout(self.grp_AdaBound)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.lbl_AdaBound_Alpha = QLabel(self.grp_AdaBound)
        self.lbl_AdaBound_Alpha.setObjectName(u"lbl_AdaBound_Alpha")

        self.horizontalLayout_52.addWidget(self.lbl_AdaBound_Alpha)

        self.dsBox_AdaBound_Alpha = QDoubleSpinBox(self.grp_AdaBound)
        self.dsBox_AdaBound_Alpha.setObjectName(u"dsBox_AdaBound_Alpha")
        self.dsBox_AdaBound_Alpha.setDecimals(3)
        self.dsBox_AdaBound_Alpha.setMaximum(1.000000000000000)
        self.dsBox_AdaBound_Alpha.setSingleStep(0.001000000000000)
        self.dsBox_AdaBound_Alpha.setValue(0.001000000000000)

        self.horizontalLayout_52.addWidget(self.dsBox_AdaBound_Alpha)


        self.verticalLayout_35.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.lbl_AdaBound_Beta1 = QLabel(self.grp_AdaBound)
        self.lbl_AdaBound_Beta1.setObjectName(u"lbl_AdaBound_Beta1")

        self.horizontalLayout_53.addWidget(self.lbl_AdaBound_Beta1)

        self.dsBox_AdaBound_Beta1 = QDoubleSpinBox(self.grp_AdaBound)
        self.dsBox_AdaBound_Beta1.setObjectName(u"dsBox_AdaBound_Beta1")
        self.dsBox_AdaBound_Beta1.setDecimals(3)
        self.dsBox_AdaBound_Beta1.setMaximum(5.000000000000000)
        self.dsBox_AdaBound_Beta1.setSingleStep(0.001000000000000)
        self.dsBox_AdaBound_Beta1.setValue(0.900000000000000)

        self.horizontalLayout_53.addWidget(self.dsBox_AdaBound_Beta1)

        self.lbl_AdaBound_Beta2 = QLabel(self.grp_AdaBound)
        self.lbl_AdaBound_Beta2.setObjectName(u"lbl_AdaBound_Beta2")

        self.horizontalLayout_53.addWidget(self.lbl_AdaBound_Beta2)

        self.dsBox_AdaBound_Beta2 = QDoubleSpinBox(self.grp_AdaBound)
        self.dsBox_AdaBound_Beta2.setObjectName(u"dsBox_AdaBound_Beta2")
        self.dsBox_AdaBound_Beta2.setDecimals(3)
        self.dsBox_AdaBound_Beta2.setMaximum(5.000000000000000)
        self.dsBox_AdaBound_Beta2.setSingleStep(0.001000000000000)
        self.dsBox_AdaBound_Beta2.setValue(0.999000000000000)

        self.horizontalLayout_53.addWidget(self.dsBox_AdaBound_Beta2)


        self.verticalLayout_35.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.lbl_AdaBound_Epsilon = QLabel(self.grp_AdaBound)
        self.lbl_AdaBound_Epsilon.setObjectName(u"lbl_AdaBound_Epsilon")

        self.horizontalLayout_54.addWidget(self.lbl_AdaBound_Epsilon)

        self.lEdit_AdaBound_Epsilon = QLineEdit(self.grp_AdaBound)
        self.lEdit_AdaBound_Epsilon.setObjectName(u"lEdit_AdaBound_Epsilon")

        self.horizontalLayout_54.addWidget(self.lEdit_AdaBound_Epsilon)


        self.verticalLayout_35.addLayout(self.horizontalLayout_54)


        self.horizontalLayout_51.addLayout(self.verticalLayout_35)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dsBox_AdaBound_Gamma = QDoubleSpinBox(self.grp_AdaBound)
        self.dsBox_AdaBound_Gamma.setObjectName(u"dsBox_AdaBound_Gamma")
        self.dsBox_AdaBound_Gamma.setDecimals(3)
        self.dsBox_AdaBound_Gamma.setMaximum(5.000000000000000)
        self.dsBox_AdaBound_Gamma.setSingleStep(0.001000000000000)
        self.dsBox_AdaBound_Gamma.setValue(0.001000000000000)

        self.gridLayout_4.addWidget(self.dsBox_AdaBound_Gamma, 1, 1, 1, 1)

        self.dsBox_AdaBound_FinalLR = QDoubleSpinBox(self.grp_AdaBound)
        self.dsBox_AdaBound_FinalLR.setObjectName(u"dsBox_AdaBound_FinalLR")
        self.dsBox_AdaBound_FinalLR.setDecimals(3)
        self.dsBox_AdaBound_FinalLR.setMaximum(5.000000000000000)
        self.dsBox_AdaBound_FinalLR.setSingleStep(0.001000000000000)
        self.dsBox_AdaBound_FinalLR.setValue(0.100000000000000)

        self.gridLayout_4.addWidget(self.dsBox_AdaBound_FinalLR, 0, 1, 1, 1)

        self.lbl_AdaBound_FinalLR = QLabel(self.grp_AdaBound)
        self.lbl_AdaBound_FinalLR.setObjectName(u"lbl_AdaBound_FinalLR")

        self.gridLayout_4.addWidget(self.lbl_AdaBound_FinalLR, 0, 0, 1, 1)

        self.lbl_AdaBound_Gamma = QLabel(self.grp_AdaBound)
        self.lbl_AdaBound_Gamma.setObjectName(u"lbl_AdaBound_Gamma")

        self.gridLayout_4.addWidget(self.lbl_AdaBound_Gamma, 1, 0, 1, 1)


        self.horizontalLayout_51.addLayout(self.gridLayout_4)


        self.verticalLayout_34.addLayout(self.horizontalLayout_51)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_10)

        self.pBtn_AdaBound_Reset = QPushButton(self.grp_AdaBound)
        self.pBtn_AdaBound_Reset.setObjectName(u"pBtn_AdaBound_Reset")

        self.verticalLayout_34.addWidget(self.pBtn_AdaBound_Reset)


        self.verticalLayout_27.addWidget(self.grp_AdaBound)

        self.stackedWidget_Optimizer.addWidget(self.page)

        self.verticalLayout_2.addWidget(self.stackedWidget_Optimizer)


        self.horizontalLayout_73.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lbl_Learning_Scheduler = QLabel(self.grp_Training_Parameters)
        self.lbl_Learning_Scheduler.setObjectName(u"lbl_Learning_Scheduler")

        self.horizontalLayout_18.addWidget(self.lbl_Learning_Scheduler)

        self.cBox_Learning_Scheduler = QComboBox(self.grp_Training_Parameters)
        self.cBox_Learning_Scheduler.addItem("")
        self.cBox_Learning_Scheduler.addItem("")
        self.cBox_Learning_Scheduler.addItem("")
        self.cBox_Learning_Scheduler.addItem("")
        self.cBox_Learning_Scheduler.addItem("")
        self.cBox_Learning_Scheduler.addItem("")
        self.cBox_Learning_Scheduler.setObjectName(u"cBox_Learning_Scheduler")

        self.horizontalLayout_18.addWidget(self.cBox_Learning_Scheduler)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.chBox_Scheduler_Warmup = QCheckBox(self.grp_Training_Parameters)
        self.chBox_Scheduler_Warmup.setObjectName(u"chBox_Scheduler_Warmup")

        self.horizontalLayout_40.addWidget(self.chBox_Scheduler_Warmup)

        self.sbox_Scheduler_Warmup_Range = QSpinBox(self.grp_Training_Parameters)
        self.sbox_Scheduler_Warmup_Range.setObjectName(u"sbox_Scheduler_Warmup_Range")
        self.sbox_Scheduler_Warmup_Range.setMaximum(100000)

        self.horizontalLayout_40.addWidget(self.sbox_Scheduler_Warmup_Range)

        self.cBox_Scheduler_Warmup_Unit = QComboBox(self.grp_Training_Parameters)
        self.cBox_Scheduler_Warmup_Unit.addItem("")
        self.cBox_Scheduler_Warmup_Unit.addItem("")
        self.cBox_Scheduler_Warmup_Unit.setObjectName(u"cBox_Scheduler_Warmup_Unit")

        self.horizontalLayout_40.addWidget(self.cBox_Scheduler_Warmup_Unit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_40)

        self.stackedWidget_Learning_Scheduler = QStackedWidget(self.grp_Training_Parameters)
        self.stackedWidget_Learning_Scheduler.setObjectName(u"stackedWidget_Learning_Scheduler")
        self.page_Scheduler_StepLR = QWidget()
        self.page_Scheduler_StepLR.setObjectName(u"page_Scheduler_StepLR")
        self.verticalLayout_37 = QVBoxLayout(self.page_Scheduler_StepLR)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.grp_Scheduler_StepLR = QGroupBox(self.page_Scheduler_StepLR)
        self.grp_Scheduler_StepLR.setObjectName(u"grp_Scheduler_StepLR")
        self.verticalLayout_36 = QVBoxLayout(self.grp_Scheduler_StepLR)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lbl_StepLR_Learning_Rate_Multiplier = QLabel(self.grp_Scheduler_StepLR)
        self.lbl_StepLR_Learning_Rate_Multiplier.setObjectName(u"lbl_StepLR_Learning_Rate_Multiplier")

        self.horizontalLayout_41.addWidget(self.lbl_StepLR_Learning_Rate_Multiplier)

        self.dsBox_StepLR_Learning_Rate_Multiplier = QDoubleSpinBox(self.grp_Scheduler_StepLR)
        self.dsBox_StepLR_Learning_Rate_Multiplier.setObjectName(u"dsBox_StepLR_Learning_Rate_Multiplier")
        self.dsBox_StepLR_Learning_Rate_Multiplier.setDecimals(3)
        self.dsBox_StepLR_Learning_Rate_Multiplier.setMaximum(5.000000000000000)
        self.dsBox_StepLR_Learning_Rate_Multiplier.setSingleStep(0.010000000000000)
        self.dsBox_StepLR_Learning_Rate_Multiplier.setValue(1.000000000000000)

        self.horizontalLayout_41.addWidget(self.dsBox_StepLR_Learning_Rate_Multiplier)


        self.verticalLayout_36.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.lbl_StepLR_Update_Interval = QLabel(self.grp_Scheduler_StepLR)
        self.lbl_StepLR_Update_Interval.setObjectName(u"lbl_StepLR_Update_Interval")

        self.horizontalLayout_42.addWidget(self.lbl_StepLR_Update_Interval)

        self.sBox_StepLR_Update_Interval = QSpinBox(self.grp_Scheduler_StepLR)
        self.sBox_StepLR_Update_Interval.setObjectName(u"sBox_StepLR_Update_Interval")
        self.sBox_StepLR_Update_Interval.setMaximum(10000)
        self.sBox_StepLR_Update_Interval.setValue(1)

        self.horizontalLayout_42.addWidget(self.sBox_StepLR_Update_Interval)

        self.cBox_StepLR_Update_Interval_Unit = QComboBox(self.grp_Scheduler_StepLR)
        self.cBox_StepLR_Update_Interval_Unit.addItem("")
        self.cBox_StepLR_Update_Interval_Unit.addItem("")
        self.cBox_StepLR_Update_Interval_Unit.setObjectName(u"cBox_StepLR_Update_Interval_Unit")

        self.horizontalLayout_42.addWidget(self.cBox_StepLR_Update_Interval_Unit)


        self.verticalLayout_36.addLayout(self.horizontalLayout_42)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_11)


        self.verticalLayout_37.addWidget(self.grp_Scheduler_StepLR)

        self.stackedWidget_Learning_Scheduler.addWidget(self.page_Scheduler_StepLR)
        self.page_Scheduler_MultiStepLR = QWidget()
        self.page_Scheduler_MultiStepLR.setObjectName(u"page_Scheduler_MultiStepLR")
        self.verticalLayout_39 = QVBoxLayout(self.page_Scheduler_MultiStepLR)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.grp_Scheduler_MultiStepLR = QGroupBox(self.page_Scheduler_MultiStepLR)
        self.grp_Scheduler_MultiStepLR.setObjectName(u"grp_Scheduler_MultiStepLR")
        self.verticalLayout_38 = QVBoxLayout(self.grp_Scheduler_MultiStepLR)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.lbl_MultiStepLR_Learning_Rate_Multiplier = QLabel(self.grp_Scheduler_MultiStepLR)
        self.lbl_MultiStepLR_Learning_Rate_Multiplier.setObjectName(u"lbl_MultiStepLR_Learning_Rate_Multiplier")

        self.horizontalLayout_55.addWidget(self.lbl_MultiStepLR_Learning_Rate_Multiplier)

        self.dsBox_MultiStepLR_Learning_Rate_Multiplier = QDoubleSpinBox(self.grp_Scheduler_MultiStepLR)
        self.dsBox_MultiStepLR_Learning_Rate_Multiplier.setObjectName(u"dsBox_MultiStepLR_Learning_Rate_Multiplier")
        self.dsBox_MultiStepLR_Learning_Rate_Multiplier.setDecimals(3)
        self.dsBox_MultiStepLR_Learning_Rate_Multiplier.setMaximum(5.000000000000000)
        self.dsBox_MultiStepLR_Learning_Rate_Multiplier.setSingleStep(0.010000000000000)
        self.dsBox_MultiStepLR_Learning_Rate_Multiplier.setValue(1.000000000000000)

        self.horizontalLayout_55.addWidget(self.dsBox_MultiStepLR_Learning_Rate_Multiplier)


        self.verticalLayout_38.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.lbl_MultiStepLR_Step = QLabel(self.grp_Scheduler_MultiStepLR)
        self.lbl_MultiStepLR_Step.setObjectName(u"lbl_MultiStepLR_Step")

        self.horizontalLayout_56.addWidget(self.lbl_MultiStepLR_Step)

        self.lEdit_MultiStepLR_Step_List = QLineEdit(self.grp_Scheduler_MultiStepLR)
        self.lEdit_MultiStepLR_Step_List.setObjectName(u"lEdit_MultiStepLR_Step_List")

        self.horizontalLayout_56.addWidget(self.lEdit_MultiStepLR_Step_List)

        self.cBox_StepLR_Step_Unit_2 = QComboBox(self.grp_Scheduler_MultiStepLR)
        self.cBox_StepLR_Step_Unit_2.addItem("")
        self.cBox_StepLR_Step_Unit_2.addItem("")
        self.cBox_StepLR_Step_Unit_2.setObjectName(u"cBox_StepLR_Step_Unit_2")

        self.horizontalLayout_56.addWidget(self.cBox_StepLR_Step_Unit_2)


        self.verticalLayout_38.addLayout(self.horizontalLayout_56)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_12)


        self.verticalLayout_39.addWidget(self.grp_Scheduler_MultiStepLR)

        self.stackedWidget_Learning_Scheduler.addWidget(self.page_Scheduler_MultiStepLR)
        self.page_Scheduler_ExponetialLR = QWidget()
        self.page_Scheduler_ExponetialLR.setObjectName(u"page_Scheduler_ExponetialLR")
        self.verticalLayout_41 = QVBoxLayout(self.page_Scheduler_ExponetialLR)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.grp_Scheduler_ExponentialLR = QGroupBox(self.page_Scheduler_ExponetialLR)
        self.grp_Scheduler_ExponentialLR.setObjectName(u"grp_Scheduler_ExponentialLR")
        self.verticalLayout_40 = QVBoxLayout(self.grp_Scheduler_ExponentialLR)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.lbl_ExponentialLR_Learning_Rate_Multiplier = QLabel(self.grp_Scheduler_ExponentialLR)
        self.lbl_ExponentialLR_Learning_Rate_Multiplier.setObjectName(u"lbl_ExponentialLR_Learning_Rate_Multiplier")

        self.horizontalLayout_57.addWidget(self.lbl_ExponentialLR_Learning_Rate_Multiplier)

        self.dsBox_ExponentialLR_Learning_Rate_Multiplier = QDoubleSpinBox(self.grp_Scheduler_ExponentialLR)
        self.dsBox_ExponentialLR_Learning_Rate_Multiplier.setObjectName(u"dsBox_ExponentialLR_Learning_Rate_Multiplier")
        self.dsBox_ExponentialLR_Learning_Rate_Multiplier.setDecimals(3)
        self.dsBox_ExponentialLR_Learning_Rate_Multiplier.setMaximum(5.000000000000000)
        self.dsBox_ExponentialLR_Learning_Rate_Multiplier.setSingleStep(0.010000000000000)
        self.dsBox_ExponentialLR_Learning_Rate_Multiplier.setValue(1.000000000000000)

        self.horizontalLayout_57.addWidget(self.dsBox_ExponentialLR_Learning_Rate_Multiplier)


        self.verticalLayout_40.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.lbl_ExponentialLR_Update_Interval = QLabel(self.grp_Scheduler_ExponentialLR)
        self.lbl_ExponentialLR_Update_Interval.setObjectName(u"lbl_ExponentialLR_Update_Interval")

        self.horizontalLayout_58.addWidget(self.lbl_ExponentialLR_Update_Interval)

        self.sBox_StepLR_Update_Interval_2 = QSpinBox(self.grp_Scheduler_ExponentialLR)
        self.sBox_StepLR_Update_Interval_2.setObjectName(u"sBox_StepLR_Update_Interval_2")
        self.sBox_StepLR_Update_Interval_2.setMaximum(10000)
        self.sBox_StepLR_Update_Interval_2.setValue(1)

        self.horizontalLayout_58.addWidget(self.sBox_StepLR_Update_Interval_2)

        self.cBox_ExponentialLR_Update_Interval_Unit = QComboBox(self.grp_Scheduler_ExponentialLR)
        self.cBox_ExponentialLR_Update_Interval_Unit.addItem("")
        self.cBox_ExponentialLR_Update_Interval_Unit.addItem("")
        self.cBox_ExponentialLR_Update_Interval_Unit.setObjectName(u"cBox_ExponentialLR_Update_Interval_Unit")

        self.horizontalLayout_58.addWidget(self.cBox_ExponentialLR_Update_Interval_Unit)


        self.verticalLayout_40.addLayout(self.horizontalLayout_58)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_13)


        self.verticalLayout_41.addWidget(self.grp_Scheduler_ExponentialLR)

        self.stackedWidget_Learning_Scheduler.addWidget(self.page_Scheduler_ExponetialLR)
        self.page_Scheduler_CosineAnnealingLR = QWidget()
        self.page_Scheduler_CosineAnnealingLR.setObjectName(u"page_Scheduler_CosineAnnealingLR")
        self.verticalLayout_42 = QVBoxLayout(self.page_Scheduler_CosineAnnealingLR)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.grp_Scheduler_CosineAnnealingLR = QGroupBox(self.page_Scheduler_CosineAnnealingLR)
        self.grp_Scheduler_CosineAnnealingLR.setObjectName(u"grp_Scheduler_CosineAnnealingLR")
        self.verticalLayout_43 = QVBoxLayout(self.grp_Scheduler_CosineAnnealingLR)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.lbl_CosineAnnealingLR_T_Max = QLabel(self.grp_Scheduler_CosineAnnealingLR)
        self.lbl_CosineAnnealingLR_T_Max.setObjectName(u"lbl_CosineAnnealingLR_T_Max")

        self.horizontalLayout_59.addWidget(self.lbl_CosineAnnealingLR_T_Max)

        self.sBox_CosineAnnealingLR_T_Max = QSpinBox(self.grp_Scheduler_CosineAnnealingLR)
        self.sBox_CosineAnnealingLR_T_Max.setObjectName(u"sBox_CosineAnnealingLR_T_Max")
        self.sBox_CosineAnnealingLR_T_Max.setMaximum(1000)
        self.sBox_CosineAnnealingLR_T_Max.setValue(100)

        self.horizontalLayout_59.addWidget(self.sBox_CosineAnnealingLR_T_Max)


        self.verticalLayout_43.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.lbl_CosineAnnealingLR_Eta_Min = QLabel(self.grp_Scheduler_CosineAnnealingLR)
        self.lbl_CosineAnnealingLR_Eta_Min.setObjectName(u"lbl_CosineAnnealingLR_Eta_Min")

        self.horizontalLayout_60.addWidget(self.lbl_CosineAnnealingLR_Eta_Min)

        self.dsBox_CosineAnnealingLR_Eta_Min = QDoubleSpinBox(self.grp_Scheduler_CosineAnnealingLR)
        self.dsBox_CosineAnnealingLR_Eta_Min.setObjectName(u"dsBox_CosineAnnealingLR_Eta_Min")
        self.dsBox_CosineAnnealingLR_Eta_Min.setDecimals(3)
        self.dsBox_CosineAnnealingLR_Eta_Min.setMaximum(1.000000000000000)
        self.dsBox_CosineAnnealingLR_Eta_Min.setSingleStep(0.001000000000000)
        self.dsBox_CosineAnnealingLR_Eta_Min.setValue(0.001000000000000)

        self.horizontalLayout_60.addWidget(self.dsBox_CosineAnnealingLR_Eta_Min)


        self.verticalLayout_43.addLayout(self.horizontalLayout_60)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_14)


        self.verticalLayout_42.addWidget(self.grp_Scheduler_CosineAnnealingLR)

        self.stackedWidget_Learning_Scheduler.addWidget(self.page_Scheduler_CosineAnnealingLR)
        self.page_Scheduler_CyclicLR = QWidget()
        self.page_Scheduler_CyclicLR.setObjectName(u"page_Scheduler_CyclicLR")
        self.verticalLayout_45 = QVBoxLayout(self.page_Scheduler_CyclicLR)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.grp_Scheduler_CyclicLR = QGroupBox(self.page_Scheduler_CyclicLR)
        self.grp_Scheduler_CyclicLR.setObjectName(u"grp_Scheduler_CyclicLR")
        self.verticalLayout_44 = QVBoxLayout(self.grp_Scheduler_CyclicLR)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.lbl_CyclicLR_Base_Learning_Rate = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Base_Learning_Rate.setObjectName(u"lbl_CyclicLR_Base_Learning_Rate")

        self.horizontalLayout_61.addWidget(self.lbl_CyclicLR_Base_Learning_Rate)

        self.dsBox_CyclicLR_Base_Learning_Rate = QDoubleSpinBox(self.grp_Scheduler_CyclicLR)
        self.dsBox_CyclicLR_Base_Learning_Rate.setObjectName(u"dsBox_CyclicLR_Base_Learning_Rate")
        self.dsBox_CyclicLR_Base_Learning_Rate.setDecimals(3)
        self.dsBox_CyclicLR_Base_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_CyclicLR_Base_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_CyclicLR_Base_Learning_Rate.setValue(0.001000000000000)

        self.horizontalLayout_61.addWidget(self.dsBox_CyclicLR_Base_Learning_Rate)


        self.gridLayout_2.addLayout(self.horizontalLayout_61, 0, 1, 1, 2)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.lbl_CyclicLR_Step_Up_Size = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Step_Up_Size.setObjectName(u"lbl_CyclicLR_Step_Up_Size")

        self.horizontalLayout_66.addWidget(self.lbl_CyclicLR_Step_Up_Size)

        self.sBox_CyclicLR_Step_Up_Size = QSpinBox(self.grp_Scheduler_CyclicLR)
        self.sBox_CyclicLR_Step_Up_Size.setObjectName(u"sBox_CyclicLR_Step_Up_Size")
        self.sBox_CyclicLR_Step_Up_Size.setMaximum(1000)
        self.sBox_CyclicLR_Step_Up_Size.setValue(50)
        self.sBox_CyclicLR_Step_Up_Size.setDisplayIntegerBase(10)

        self.horizontalLayout_66.addWidget(self.sBox_CyclicLR_Step_Up_Size)


        self.gridLayout_2.addLayout(self.horizontalLayout_66, 7, 1, 1, 2)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.lbl_CyclickLR_Scale_Mode = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclickLR_Scale_Mode.setObjectName(u"lbl_CyclickLR_Scale_Mode")

        self.horizontalLayout_64.addWidget(self.lbl_CyclickLR_Scale_Mode)

        self.cBox_CyclickLR_Scale_Mode = QComboBox(self.grp_Scheduler_CyclicLR)
        self.cBox_CyclickLR_Scale_Mode.addItem("")
        self.cBox_CyclickLR_Scale_Mode.addItem("")
        self.cBox_CyclickLR_Scale_Mode.setObjectName(u"cBox_CyclickLR_Scale_Mode")

        self.horizontalLayout_64.addWidget(self.cBox_CyclickLR_Scale_Mode)


        self.gridLayout_2.addLayout(self.horizontalLayout_64, 3, 1, 1, 2)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.lbl_CyclicLR_Step_Down_Size = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Step_Down_Size.setObjectName(u"lbl_CyclicLR_Step_Down_Size")

        self.horizontalLayout_68.addWidget(self.lbl_CyclicLR_Step_Down_Size)

        self.sBox_CyclicLR_Step_Down_Size = QSpinBox(self.grp_Scheduler_CyclicLR)
        self.sBox_CyclicLR_Step_Down_Size.setObjectName(u"sBox_CyclicLR_Step_Down_Size")
        self.sBox_CyclicLR_Step_Down_Size.setMaximum(1000)
        self.sBox_CyclicLR_Step_Down_Size.setValue(50)
        self.sBox_CyclicLR_Step_Down_Size.setDisplayIntegerBase(10)

        self.horizontalLayout_68.addWidget(self.sBox_CyclicLR_Step_Down_Size)


        self.gridLayout_2.addLayout(self.horizontalLayout_68, 8, 1, 1, 2)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.lbl_CyclicLR_Learning_Rate = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Learning_Rate.setObjectName(u"lbl_CyclicLR_Learning_Rate")

        self.horizontalLayout_62.addWidget(self.lbl_CyclicLR_Learning_Rate)

        self.dsBox_CyclicLR_Max_Learning_Rate = QDoubleSpinBox(self.grp_Scheduler_CyclicLR)
        self.dsBox_CyclicLR_Max_Learning_Rate.setObjectName(u"dsBox_CyclicLR_Max_Learning_Rate")
        self.dsBox_CyclicLR_Max_Learning_Rate.setDecimals(3)
        self.dsBox_CyclicLR_Max_Learning_Rate.setMaximum(1.000000000000000)
        self.dsBox_CyclicLR_Max_Learning_Rate.setSingleStep(0.001000000000000)
        self.dsBox_CyclicLR_Max_Learning_Rate.setValue(0.100000000000000)

        self.horizontalLayout_62.addWidget(self.dsBox_CyclicLR_Max_Learning_Rate)


        self.gridLayout_2.addLayout(self.horizontalLayout_62, 1, 1, 1, 2)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.lbl_CyclicLR_Mode = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Mode.setObjectName(u"lbl_CyclicLR_Mode")

        self.horizontalLayout_63.addWidget(self.lbl_CyclicLR_Mode)

        self.cBox_CyclicLR_Mode = QComboBox(self.grp_Scheduler_CyclicLR)
        self.cBox_CyclicLR_Mode.addItem("")
        self.cBox_CyclicLR_Mode.addItem("")
        self.cBox_CyclicLR_Mode.addItem("")
        self.cBox_CyclicLR_Mode.setObjectName(u"cBox_CyclicLR_Mode")

        self.horizontalLayout_63.addWidget(self.cBox_CyclicLR_Mode)


        self.gridLayout_2.addLayout(self.horizontalLayout_63, 2, 1, 1, 2)

        self.chBox_CyclickLR_Cycle_Momentum = QCheckBox(self.grp_Scheduler_CyclicLR)
        self.chBox_CyclickLR_Cycle_Momentum.setObjectName(u"chBox_CyclickLR_Cycle_Momentum")

        self.gridLayout_2.addWidget(self.chBox_CyclickLR_Cycle_Momentum, 5, 1, 1, 1)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label = QLabel(self.grp_Scheduler_CyclicLR)
        self.label.setObjectName(u"label")

        self.horizontalLayout_65.addWidget(self.label)

        self.dsBox_Gamma_Only_Exp_Range = QDoubleSpinBox(self.grp_Scheduler_CyclicLR)
        self.dsBox_Gamma_Only_Exp_Range.setObjectName(u"dsBox_Gamma_Only_Exp_Range")
        self.dsBox_Gamma_Only_Exp_Range.setDecimals(3)
        self.dsBox_Gamma_Only_Exp_Range.setMaximum(1.000000000000000)
        self.dsBox_Gamma_Only_Exp_Range.setSingleStep(0.001000000000000)
        self.dsBox_Gamma_Only_Exp_Range.setValue(0.995000000000000)

        self.horizontalLayout_65.addWidget(self.dsBox_Gamma_Only_Exp_Range)


        self.gridLayout_2.addLayout(self.horizontalLayout_65, 6, 1, 1, 1)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.lbl_CyclicLR_Base_Momentum = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Base_Momentum.setObjectName(u"lbl_CyclicLR_Base_Momentum")

        self.horizontalLayout_67.addWidget(self.lbl_CyclicLR_Base_Momentum)

        self.sBox_CyclicLR_Base_Momentum = QSpinBox(self.grp_Scheduler_CyclicLR)
        self.sBox_CyclicLR_Base_Momentum.setObjectName(u"sBox_CyclicLR_Base_Momentum")
        self.sBox_CyclicLR_Base_Momentum.setMaximum(1000)
        self.sBox_CyclicLR_Base_Momentum.setValue(100)
        self.sBox_CyclicLR_Base_Momentum.setDisplayIntegerBase(10)

        self.horizontalLayout_67.addWidget(self.sBox_CyclicLR_Base_Momentum)


        self.gridLayout_2.addLayout(self.horizontalLayout_67, 5, 2, 1, 1)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.lbl_CyclicLR_Max_Momentum = QLabel(self.grp_Scheduler_CyclicLR)
        self.lbl_CyclicLR_Max_Momentum.setObjectName(u"lbl_CyclicLR_Max_Momentum")

        self.horizontalLayout_69.addWidget(self.lbl_CyclicLR_Max_Momentum)

        self.sBox_CyclicLR_Max_Momentum = QSpinBox(self.grp_Scheduler_CyclicLR)
        self.sBox_CyclicLR_Max_Momentum.setObjectName(u"sBox_CyclicLR_Max_Momentum")
        self.sBox_CyclicLR_Max_Momentum.setMaximum(1000)
        self.sBox_CyclicLR_Max_Momentum.setValue(100)
        self.sBox_CyclicLR_Max_Momentum.setDisplayIntegerBase(10)

        self.horizontalLayout_69.addWidget(self.sBox_CyclicLR_Max_Momentum)


        self.gridLayout_2.addLayout(self.horizontalLayout_69, 6, 2, 1, 1)


        self.verticalLayout_44.addLayout(self.gridLayout_2)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_16)


        self.verticalLayout_45.addWidget(self.grp_Scheduler_CyclicLR)

        self.stackedWidget_Learning_Scheduler.addWidget(self.page_Scheduler_CyclicLR)
        self.page_Scheduler_CosineAnnealingWarmRestarts = QWidget()
        self.page_Scheduler_CosineAnnealingWarmRestarts.setObjectName(u"page_Scheduler_CosineAnnealingWarmRestarts")
        self.verticalLayout_47 = QVBoxLayout(self.page_Scheduler_CosineAnnealingWarmRestarts)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.grp_Scheduler_CosineAnnealingWarmRestarts = QGroupBox(self.page_Scheduler_CosineAnnealingWarmRestarts)
        self.grp_Scheduler_CosineAnnealingWarmRestarts.setObjectName(u"grp_Scheduler_CosineAnnealingWarmRestarts")
        self.verticalLayout_46 = QVBoxLayout(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.lbl_CosineAnnealingWarmRestarts_T_0 = QLabel(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.lbl_CosineAnnealingWarmRestarts_T_0.setObjectName(u"lbl_CosineAnnealingWarmRestarts_T_0")

        self.horizontalLayout_70.addWidget(self.lbl_CosineAnnealingWarmRestarts_T_0)

        self.sBox_CosineAnnealingWarmRestarts_T_0 = QSpinBox(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.sBox_CosineAnnealingWarmRestarts_T_0.setObjectName(u"sBox_CosineAnnealingWarmRestarts_T_0")
        self.sBox_CosineAnnealingWarmRestarts_T_0.setMaximum(1000)
        self.sBox_CosineAnnealingWarmRestarts_T_0.setValue(50)

        self.horizontalLayout_70.addWidget(self.sBox_CosineAnnealingWarmRestarts_T_0)


        self.verticalLayout_46.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.lbl_CosineAnnealingWarmRestarts_T_Multi = QLabel(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.lbl_CosineAnnealingWarmRestarts_T_Multi.setObjectName(u"lbl_CosineAnnealingWarmRestarts_T_Multi")

        self.horizontalLayout_71.addWidget(self.lbl_CosineAnnealingWarmRestarts_T_Multi)

        self.sBox_CosineAnnealingWarmRestarts_T_Multi = QSpinBox(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.sBox_CosineAnnealingWarmRestarts_T_Multi.setObjectName(u"sBox_CosineAnnealingWarmRestarts_T_Multi")
        self.sBox_CosineAnnealingWarmRestarts_T_Multi.setMaximum(1000)
        self.sBox_CosineAnnealingWarmRestarts_T_Multi.setValue(50)

        self.horizontalLayout_71.addWidget(self.sBox_CosineAnnealingWarmRestarts_T_Multi)


        self.verticalLayout_46.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.lbl_CosineAnnealingWarmRestarts_Eta_Min = QLabel(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.lbl_CosineAnnealingWarmRestarts_Eta_Min.setObjectName(u"lbl_CosineAnnealingWarmRestarts_Eta_Min")

        self.horizontalLayout_72.addWidget(self.lbl_CosineAnnealingWarmRestarts_Eta_Min)

        self.dsBox_CosineAnnealingWarmRestarts_Eta_Min = QDoubleSpinBox(self.grp_Scheduler_CosineAnnealingWarmRestarts)
        self.dsBox_CosineAnnealingWarmRestarts_Eta_Min.setObjectName(u"dsBox_CosineAnnealingWarmRestarts_Eta_Min")
        self.dsBox_CosineAnnealingWarmRestarts_Eta_Min.setDecimals(3)
        self.dsBox_CosineAnnealingWarmRestarts_Eta_Min.setMaximum(1.000000000000000)
        self.dsBox_CosineAnnealingWarmRestarts_Eta_Min.setSingleStep(0.001000000000000)
        self.dsBox_CosineAnnealingWarmRestarts_Eta_Min.setValue(0.001000000000000)

        self.horizontalLayout_72.addWidget(self.dsBox_CosineAnnealingWarmRestarts_Eta_Min)


        self.verticalLayout_46.addLayout(self.horizontalLayout_72)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_15)


        self.verticalLayout_47.addWidget(self.grp_Scheduler_CosineAnnealingWarmRestarts)

        self.stackedWidget_Learning_Scheduler.addWidget(self.page_Scheduler_CosineAnnealingWarmRestarts)

        self.verticalLayout_8.addWidget(self.stackedWidget_Learning_Scheduler)


        self.horizontalLayout_73.addLayout(self.verticalLayout_8)


        self.horizontalLayout_12.addWidget(self.grp_Training_Parameters)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.grp_Monitor = QGroupBox(DLImageRecognitionDialog)
        self.grp_Monitor.setObjectName(u"grp_Monitor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.grp_Monitor.sizePolicy().hasHeightForWidth())
        self.grp_Monitor.setSizePolicy(sizePolicy2)
        self.horizontalLayout_8 = QHBoxLayout(self.grp_Monitor)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tEdit_Monitor = QTextEdit(self.grp_Monitor)
        self.tEdit_Monitor.setObjectName(u"tEdit_Monitor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tEdit_Monitor.sizePolicy().hasHeightForWidth())
        self.tEdit_Monitor.setSizePolicy(sizePolicy3)
        self.tEdit_Monitor.setMinimumSize(QSize(0, 0))
        self.tEdit_Monitor.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.tEdit_Monitor)


        self.horizontalLayout_13.addWidget(self.grp_Monitor)

        self.grp_Learning_Curve = QGroupBox(DLImageRecognitionDialog)
        self.grp_Learning_Curve.setObjectName(u"grp_Learning_Curve")
        self.verticalLayout = QVBoxLayout(self.grp_Learning_Curve)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar_Learning_Curve = QProgressBar(self.grp_Learning_Curve)
        self.progressBar_Learning_Curve.setObjectName(u"progressBar_Learning_Curve")
        self.progressBar_Learning_Curve.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_Learning_Curve)

        self.widget_Learning_Curve_Loss = QWidget(self.grp_Learning_Curve)
        self.widget_Learning_Curve_Loss.setObjectName(u"widget_Learning_Curve_Loss")
        sizePolicy3.setHeightForWidth(self.widget_Learning_Curve_Loss.sizePolicy().hasHeightForWidth())
        self.widget_Learning_Curve_Loss.setSizePolicy(sizePolicy3)
        self.widget_Learning_Curve_Loss.setMinimumSize(QSize(0, 180))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.widget_Learning_Curve_Loss.setPalette(palette)
        self.widget_Learning_Curve_Loss.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.widget_Learning_Curve_Loss)


        self.horizontalLayout_13.addWidget(self.grp_Learning_Curve)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)


        self.retranslateUi(DLImageRecognitionDialog)

        self.stackedWidget_Optimizer.setCurrentIndex(0)
        self.stackedWidget_Learning_Scheduler.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DLImageRecognitionDialog)
    # setupUi

    def retranslateUi(self, DLImageRecognitionDialog):
        DLImageRecognitionDialog.setWindowTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"DLImageRecognitionDialog", None))
        self.grp_Dataset_Meta_CSV.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Dataset Meta CSV", None))
        self.lbl_Meta_CSV_Test.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"test Meta-CSV", None))
        self.tBtn_Meta_CSV_Test_File_Path.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"...", None))
        self.tBtn_Meta_CSV_Train_File_Path.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"...", None))
        self.lbl_Encode_Type.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Encode Type", None))
        self.tBtn_Meta_CSV_Validation_File_Path.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"...", None))
        self.cBox_Encode_Type.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"utf-8", None))
        self.cBox_Encode_Type.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"shift-jis", None))

        self.lbl_Meta_CSV_Train_Dir.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Train Meta-CSV", None))
        self.lbl_Meta_CSV_Validation_Dir.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Valid Meta-CSV", None))
        self.lbl_Header_Meta_CSV.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Header", None))
        self.rBtn_Header_ON.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"ON", None))
        self.rBtn_Header_OFF.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"OFF", None))
        self.lbl_Train_Count.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Train", None))
        self.lEdit_Train_Count.setPlaceholderText(QCoreApplication.translate("DLImageRecognitionDialog", u"Count", None))
        self.lbl_Validation_Count.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Validation", None))
        self.lEdit_Validation_Count.setPlaceholderText(QCoreApplication.translate("DLImageRecognitionDialog", u"Count", None))
        self.lbl_Test_Count.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"test", None))
        self.lEdit_Test_Count.setPlaceholderText(QCoreApplication.translate("DLImageRecognitionDialog", u"Count", None))
        self.grp_Operation.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Operation", None))
        self.pBtn_Data_Augmentation.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Data Augmentation", None))
        self.pBtn_Training_Init.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Init Training", None))
        self.pBtn_Training.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Start Training", None))
        self.pBtn_Training_Stop.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Stop Training", None))
        self.grp_Metrics.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Metrics", None))
        self.lbl_Inference_Time.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Inference Time [ms]", None))
        self.pBtn_ROC_Curve.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"ROC", None))
        self.pBtn_Confusion_Matrix.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Confusion Matrix", None))
        self.pBtn_Score.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Score", None))
        self.pBtn_Loss.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Loss", None))
        self.grp_PreTraining_Model.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"PreTraining Model", None))
        self.lbl_Final_Layer_Neuron.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Final Layer Neuron", None))
        self.sBox_Final_Layer_Neuron.setSuffix(QCoreApplication.translate("DLImageRecognitionDialog", u" Category", None))
        self.pBtn_Model_Architecture.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Architecture", None))
        self.cBox_PreTraining_Model.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"LeNet", None))
        self.cBox_PreTraining_Model.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"AlexNet", None))
        self.cBox_PreTraining_Model.setItemText(2, QCoreApplication.translate("DLImageRecognitionDialog", u"GoogleLeNet", None))
        self.cBox_PreTraining_Model.setItemText(3, QCoreApplication.translate("DLImageRecognitionDialog", u"VGG16 : ILSVRC2013", None))
        self.cBox_PreTraining_Model.setItemText(4, QCoreApplication.translate("DLImageRecognitionDialog", u"VGG19", None))
        self.cBox_PreTraining_Model.setItemText(5, QCoreApplication.translate("DLImageRecognitionDialog", u"ResNet50", None))
        self.cBox_PreTraining_Model.setItemText(6, QCoreApplication.translate("DLImageRecognitionDialog", u"ResNext50", None))
        self.cBox_PreTraining_Model.setItemText(7, QCoreApplication.translate("DLImageRecognitionDialog", u"InspectionV3", None))
        self.cBox_PreTraining_Model.setItemText(8, QCoreApplication.translate("DLImageRecognitionDialog", u"InspectionResNetV2", None))
        self.cBox_PreTraining_Model.setItemText(9, QCoreApplication.translate("DLImageRecognitionDialog", u"MobileNet", None))
        self.cBox_PreTraining_Model.setItemText(10, QCoreApplication.translate("DLImageRecognitionDialog", u"DenseNet", None))
        self.cBox_PreTraining_Model.setItemText(11, QCoreApplication.translate("DLImageRecognitionDialog", u"NASNet", None))
        self.cBox_PreTraining_Model.setItemText(12, QCoreApplication.translate("DLImageRecognitionDialog", u"MobileNetV2", None))
        self.cBox_PreTraining_Model.setItemText(13, QCoreApplication.translate("DLImageRecognitionDialog", u"Xception", None))

        self.lbl_Leaerning_Type.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Type", None))
        self.cBox_Learning_Type.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"Transfer Learning", None))
        self.cBox_Learning_Type.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"Fine Tuning", None))
        self.cBox_Learning_Type.setItemText(2, QCoreApplication.translate("DLImageRecognitionDialog", u"Full Learning", None))

        self.grp_Training_Parameters.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Training Parameters", None))
        self.lbl_Batch_Size.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Batch Size", None))
        self.lbl_Epochs.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epochs", None))
        self.lbl_Update_Interval.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Update Interval", None))
        self.sBox_Update_Interval.setSuffix(QCoreApplication.translate("DLImageRecognitionDialog", u" Iter", None))
        self.lbl_Weight_Decay.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Weight Decay", None))
        self.cBox_Optimizer.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"SGD", None))
        self.cBox_Optimizer.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"Momentum", None))
        self.cBox_Optimizer.setItemText(2, QCoreApplication.translate("DLImageRecognitionDialog", u"Nesterov", None))
        self.cBox_Optimizer.setItemText(3, QCoreApplication.translate("DLImageRecognitionDialog", u"RMSprop", None))
        self.cBox_Optimizer.setItemText(4, QCoreApplication.translate("DLImageRecognitionDialog", u"Adadelta", None))
        self.cBox_Optimizer.setItemText(5, QCoreApplication.translate("DLImageRecognitionDialog", u"Adagrad", None))
        self.cBox_Optimizer.setItemText(6, QCoreApplication.translate("DLImageRecognitionDialog", u"Adam", None))
        self.cBox_Optimizer.setItemText(7, QCoreApplication.translate("DLImageRecognitionDialog", u"Adamax", None))
        self.cBox_Optimizer.setItemText(8, QCoreApplication.translate("DLImageRecognitionDialog", u"AdaBound", None))

        self.grp_SGD.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"SGD", None))
        self.lbl_SGD_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.pBtn_SGD_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Momentum.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Momentum", None))
        self.lbl_Momentum_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_Momentum_Momentum.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Momentum", None))
        self.pBtn_Momentum_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Nesterov.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Nesterov", None))
        self.lbl_Nesterov_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_Nesterov_Momentum.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Momentum", None))
        self.pBtn_Nesterov_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Optimizer_RMSprop.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"RMSprop", None))
        self.lbl_RMSprop_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_RMSprop_Alpha.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Alpha", None))
        self.lbl_RMSprop_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epsilon", None))
        self.lEdit_RMSprop_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"1E-8", None))
        self.chBox_RMSprop_Centered.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Centered", None))
        self.pBtn_RMSprop_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Adadelta.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Adadelta", None))
        self.lbl_Adadelta_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_Adadelta_Rho.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Rho", None))
        self.lbl_Adadelta_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epsilon", None))
        self.lEdit_Adadelta_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"1E-6", None))
        self.pBtn_Adadelta_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Adagrad.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Adagrad", None))
        self.lbl_Adagrad_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_Adagrad_Decay.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Decay", None))
        self.lbl_Adagrad_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epsilon", None))
        self.lEdit_Adagrad_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"1E-10", None))
        self.pBtn_Adagrad_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Adam.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Adam", None))
        self.lbl_Adam_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_Adam_Beta1.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Beta1", None))
        self.lbl_Adam_Beta2.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Beta2", None))
        self.lbl_Adam_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epsilon", None))
        self.lEdit_Adam_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"1E-8", None))
        self.chBox_Adam_AMSGrad.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"AMSGrad", None))
        self.pBtn_Adam_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_Adamax.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Adamax", None))
        self.lbl_Adamax_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate", None))
        self.lbl_Adamax_Beta1.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Beta1", None))
        self.lbl_Adamax_Beta2.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Beta2", None))
        self.lbl_Adamax_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epsilon", None))
        self.lEdit_Adamax_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"1E-8", None))
        self.pBtn_Adamax_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.grp_AdaBound.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"AdaBound", None))
        self.lbl_AdaBound_Alpha.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Alpha", None))
        self.lbl_AdaBound_Beta1.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Beta1", None))
        self.lbl_AdaBound_Beta2.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Beta2", None))
        self.lbl_AdaBound_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Epsilon", None))
        self.lEdit_AdaBound_Epsilon.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"1E-8", None))
        self.lbl_AdaBound_FinalLR.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"FinalLR", None))
        self.lbl_AdaBound_Gamma.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Gamma", None))
        self.pBtn_AdaBound_Reset.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Reset", None))
        self.lbl_Learning_Scheduler.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Scheduler", None))
        self.cBox_Learning_Scheduler.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"StepLR", None))
        self.cBox_Learning_Scheduler.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"MuktiStepLR", None))
        self.cBox_Learning_Scheduler.setItemText(2, QCoreApplication.translate("DLImageRecognitionDialog", u"ExponentialLR", None))
        self.cBox_Learning_Scheduler.setItemText(3, QCoreApplication.translate("DLImageRecognitionDialog", u"CosineAnnealingLR", None))
        self.cBox_Learning_Scheduler.setItemText(4, QCoreApplication.translate("DLImageRecognitionDialog", u"CyclicLR", None))
        self.cBox_Learning_Scheduler.setItemText(5, QCoreApplication.translate("DLImageRecognitionDialog", u"CosineAnnealingWarmRestarts", None))

        self.chBox_Scheduler_Warmup.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Warmup", None))
        self.cBox_Scheduler_Warmup_Unit.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"epoch", None))
        self.cBox_Scheduler_Warmup_Unit.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"iter", None))

        self.grp_Scheduler_StepLR.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"StepLR", None))
        self.lbl_StepLR_Learning_Rate_Multiplier.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate Multiplier", None))
        self.lbl_StepLR_Update_Interval.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Update Interval", None))
        self.cBox_StepLR_Update_Interval_Unit.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"epoch", None))
        self.cBox_StepLR_Update_Interval_Unit.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"iter", None))

        self.grp_Scheduler_MultiStepLR.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"MultiStepLR", None))
        self.lbl_MultiStepLR_Learning_Rate_Multiplier.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate Multiplier", None))
        self.lbl_MultiStepLR_Step.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Step", None))
        self.lEdit_MultiStepLR_Step_List.setPlaceholderText(QCoreApplication.translate("DLImageRecognitionDialog", u"10, 20, ...", None))
        self.cBox_StepLR_Step_Unit_2.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"epoch", None))
        self.cBox_StepLR_Step_Unit_2.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"iter", None))

        self.grp_Scheduler_ExponentialLR.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Exponential", None))
        self.lbl_ExponentialLR_Learning_Rate_Multiplier.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Learning Rate Multiplier", None))
        self.lbl_ExponentialLR_Update_Interval.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Update Interval", None))
        self.cBox_ExponentialLR_Update_Interval_Unit.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"epoch", None))
        self.cBox_ExponentialLR_Update_Interval_Unit.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"iter", None))

        self.grp_Scheduler_CosineAnnealingLR.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"CosineAnnealingLR", None))
        self.lbl_CosineAnnealingLR_T_Max.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"T Max(\u534a\u5468\u671f\u306e\u30b9\u30c6\u30c3\u30d7\u30b5\u30a4\u30ba)", None))
        self.lbl_CosineAnnealingLR_Eta_Min.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Eta_Min(\u4e0b\u9650\u5b66\u7fd2\u7387)", None))
        self.grp_Scheduler_CyclicLR.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"CyclicLR", None))
        self.lbl_CyclicLR_Base_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Base_lr(\u4e0b\u9650\u5b66\u7fd2\u7387)", None))
        self.lbl_CyclicLR_Step_Up_Size.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Step Up Size(\u5b66\u7fd2\u7387\u4e0a\u6607\u306e\u30b5\u30a4\u30af\u30eb\u6570)", None))
        self.lbl_CyclickLR_Scale_Mode.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Scale Mode", None))
        self.cBox_CyclickLR_Scale_Mode.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"Epoch", None))
        self.cBox_CyclickLR_Scale_Mode.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"Iter", None))

        self.lbl_CyclicLR_Step_Down_Size.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Step Down Size(\u5b66\u7fd2\u7387\u6e1b\u5c11\u306e\u30b5\u30a4\u30af\u30eb\u6570)", None))
        self.lbl_CyclicLR_Learning_Rate.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Max_lr(\u4e0a\u9650\u5b66\u7fd2\u7387)", None))
        self.lbl_CyclicLR_Mode.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Mode", None))
        self.cBox_CyclicLR_Mode.setItemText(0, QCoreApplication.translate("DLImageRecognitionDialog", u"Triangular", None))
        self.cBox_CyclicLR_Mode.setItemText(1, QCoreApplication.translate("DLImageRecognitionDialog", u"Triangular2", None))
        self.cBox_CyclicLR_Mode.setItemText(2, QCoreApplication.translate("DLImageRecognitionDialog", u"Exp_Range", None))

        self.chBox_CyclickLR_Cycle_Momentum.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Cycle Momentum", None))
        self.label.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Gamma(Only Exp_Range)", None))
        self.lbl_CyclicLR_Base_Momentum.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Base Momentum", None))
        self.lbl_CyclicLR_Max_Momentum.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Max Momentum", None))
        self.grp_Scheduler_CosineAnnealingWarmRestarts.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"CosineAnnealingWarmRestarts", None))
        self.lbl_CosineAnnealingWarmRestarts_T_0.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"T_0(\u521d\u671f\u306e\u7e70\u308a\u8fd4\u3057\u56de\u6570)", None))
        self.lbl_CosineAnnealingWarmRestarts_T_Multi.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"T_Multi(\u30b5\u30a4\u30af\u30eb\u306e\u30b9\u30b1\u30fc\u30eb\u500d\u7387)", None))
        self.lbl_CosineAnnealingWarmRestarts_Eta_Min.setText(QCoreApplication.translate("DLImageRecognitionDialog", u"Eta min(\u4e0b\u9650\u5b66\u7fd2\u7387)", None))
        self.grp_Monitor.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"Monitor", None))
        self.grp_Learning_Curve.setTitle(QCoreApplication.translate("DLImageRecognitionDialog", u"\u5b66\u7fd2\u66f2\u7dda", None))
    # retranslateUi

