# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_IDSVideoWindow.ui'
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

from draw_view import DrawView


class Ui_IDSVideoWindow(object):
    def setupUi(self, IDSVideoWindow):
        if IDSVideoWindow.objectName():
            IDSVideoWindow.setObjectName(u"IDSVideoWindow")
        IDSVideoWindow.resize(660, 437)
        self.centralwidget = QWidget(IDSVideoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lEdit_Image_Status = QLineEdit(self.centralwidget)
        self.lEdit_Image_Status.setObjectName(u"lEdit_Image_Status")
        self.lEdit_Image_Status.setReadOnly(True)

        self.gridLayout.addWidget(self.lEdit_Image_Status, 0, 0, 1, 1)

        self.lbl_Image_Scale = QLabel(self.centralwidget)
        self.lbl_Image_Scale.setObjectName(u"lbl_Image_Scale")

        self.gridLayout.addWidget(self.lbl_Image_Scale, 0, 1, 1, 1)

        self.gView = DrawView(self.centralwidget)
        self.gView.setObjectName(u"gView")

        self.gridLayout.addWidget(self.gView, 1, 0, 1, 2)

        IDSVideoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(IDSVideoWindow)
        self.statusbar.setObjectName(u"statusbar")
        IDSVideoWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(IDSVideoWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMaximumSize(QSize(218, 524287))
        self.dockWidget.setFloating(False)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.grp_Device = QGroupBox(self.dockWidgetContents)
        self.grp_Device.setObjectName(u"grp_Device")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp_Device.sizePolicy().hasHeightForWidth())
        self.grp_Device.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.grp_Device)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_Device_List = QLabel(self.grp_Device)
        self.lbl_Device_List.setObjectName(u"lbl_Device_List")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_Device_List.sizePolicy().hasHeightForWidth())
        self.lbl_Device_List.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.lbl_Device_List)

        self.pBtn_Search_Device_List = QPushButton(self.grp_Device)
        self.pBtn_Search_Device_List.setObjectName(u"pBtn_Search_Device_List")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pBtn_Search_Device_List.sizePolicy().hasHeightForWidth())
        self.pBtn_Search_Device_List.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.pBtn_Search_Device_List)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.listWidget_Device_List = QListWidget(self.grp_Device)
        self.listWidget_Device_List.setObjectName(u"listWidget_Device_List")
        sizePolicy1.setHeightForWidth(self.listWidget_Device_List.sizePolicy().hasHeightForWidth())
        self.listWidget_Device_List.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.listWidget_Device_List)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_Device_ID = QLabel(self.grp_Device)
        self.lbl_Device_ID.setObjectName(u"lbl_Device_ID")
        sizePolicy1.setHeightForWidth(self.lbl_Device_ID.sizePolicy().hasHeightForWidth())
        self.lbl_Device_ID.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lbl_Device_ID)

        self.lEdit_Device_ID = QLineEdit(self.grp_Device)
        self.lEdit_Device_ID.setObjectName(u"lEdit_Device_ID")
        sizePolicy2.setHeightForWidth(self.lEdit_Device_ID.sizePolicy().hasHeightForWidth())
        self.lEdit_Device_ID.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.lEdit_Device_ID)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.grp_Device)

        self.grp_Control = QGroupBox(self.dockWidgetContents)
        self.grp_Control.setObjectName(u"grp_Control")
        sizePolicy.setHeightForWidth(self.grp_Control.sizePolicy().hasHeightForWidth())
        self.grp_Control.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.grp_Control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_Read_Frame_Delay = QLabel(self.grp_Control)
        self.lbl_Read_Frame_Delay.setObjectName(u"lbl_Read_Frame_Delay")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_Read_Frame_Delay.sizePolicy().hasHeightForWidth())
        self.lbl_Read_Frame_Delay.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_Read_Frame_Delay)

        self.sBox_Read_Frame_Delay = QSpinBox(self.grp_Control)
        self.sBox_Read_Frame_Delay.setObjectName(u"sBox_Read_Frame_Delay")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sBox_Read_Frame_Delay.sizePolicy().hasHeightForWidth())
        self.sBox_Read_Frame_Delay.setSizePolicy(sizePolicy4)
        self.sBox_Read_Frame_Delay.setMaximum(500)
        self.sBox_Read_Frame_Delay.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sBox_Read_Frame_Delay)

        self.lbl_Paint_Timer_Interval = QLabel(self.grp_Control)
        self.lbl_Paint_Timer_Interval.setObjectName(u"lbl_Paint_Timer_Interval")
        sizePolicy3.setHeightForWidth(self.lbl_Paint_Timer_Interval.sizePolicy().hasHeightForWidth())
        self.lbl_Paint_Timer_Interval.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_Paint_Timer_Interval)

        self.sBox_Paint_Timer_Interval = QSpinBox(self.grp_Control)
        self.sBox_Paint_Timer_Interval.setObjectName(u"sBox_Paint_Timer_Interval")
        sizePolicy4.setHeightForWidth(self.sBox_Paint_Timer_Interval.sizePolicy().hasHeightForWidth())
        self.sBox_Paint_Timer_Interval.setSizePolicy(sizePolicy4)
        self.sBox_Paint_Timer_Interval.setMaximum(1000)
        self.sBox_Paint_Timer_Interval.setValue(30)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sBox_Paint_Timer_Interval)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.rBtn_Thread = QRadioButton(self.grp_Control)
        self.rBtn_Thread.setObjectName(u"rBtn_Thread")
        self.rBtn_Thread.setChecked(True)

        self.horizontalLayout_7.addWidget(self.rBtn_Thread)

        self.rBtn_Process = QRadioButton(self.grp_Control)
        self.rBtn_Process.setObjectName(u"rBtn_Process")

        self.horizontalLayout_7.addWidget(self.rBtn_Process)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cBox_FPS = QCheckBox(self.grp_Control)
        self.cBox_FPS.setObjectName(u"cBox_FPS")

        self.horizontalLayout_6.addWidget(self.cBox_FPS)

        self.cBox_Elapsed_Time = QCheckBox(self.grp_Control)
        self.cBox_Elapsed_Time.setObjectName(u"cBox_Elapsed_Time")

        self.horizontalLayout_6.addWidget(self.cBox_Elapsed_Time)

        self.cBox_Timestamp = QCheckBox(self.grp_Control)
        self.cBox_Timestamp.setObjectName(u"cBox_Timestamp")

        self.horizontalLayout_6.addWidget(self.cBox_Timestamp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pBtn_Start = QPushButton(self.grp_Control)
        self.pBtn_Start.setObjectName(u"pBtn_Start")
        sizePolicy4.setHeightForWidth(self.pBtn_Start.sizePolicy().hasHeightForWidth())
        self.pBtn_Start.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.pBtn_Start)

        self.pBtn_Stop = QPushButton(self.grp_Control)
        self.pBtn_Stop.setObjectName(u"pBtn_Stop")
        sizePolicy4.setHeightForWidth(self.pBtn_Stop.sizePolicy().hasHeightForWidth())
        self.pBtn_Stop.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.pBtn_Stop)

        self.pBtn_Snapshot = QPushButton(self.grp_Control)
        self.pBtn_Snapshot.setObjectName(u"pBtn_Snapshot")

        self.horizontalLayout_5.addWidget(self.pBtn_Snapshot)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_Timer_ID = QLabel(self.grp_Control)
        self.lbl_Timer_ID.setObjectName(u"lbl_Timer_ID")

        self.horizontalLayout_2.addWidget(self.lbl_Timer_ID)

        self.lEdit_Timer_ID = QLineEdit(self.grp_Control)
        self.lEdit_Timer_ID.setObjectName(u"lEdit_Timer_ID")
        sizePolicy4.setHeightForWidth(self.lEdit_Timer_ID.sizePolicy().hasHeightForWidth())
        self.lEdit_Timer_ID.setSizePolicy(sizePolicy4)
        self.lEdit_Timer_ID.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lEdit_Timer_ID)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_Timer_Type = QLabel(self.grp_Control)
        self.lbl_Timer_Type.setObjectName(u"lbl_Timer_Type")

        self.horizontalLayout_3.addWidget(self.lbl_Timer_Type)

        self.lEdit_Timer_Type = QLineEdit(self.grp_Control)
        self.lEdit_Timer_Type.setObjectName(u"lEdit_Timer_Type")
        self.lEdit_Timer_Type.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lEdit_Timer_Type)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.grp_Control)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.dockWidget.setWidget(self.dockWidgetContents)
        IDSVideoWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)
        self.toolBar = QToolBar(IDSVideoWindow)
        self.toolBar.setObjectName(u"toolBar")
        IDSVideoWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(IDSVideoWindow)

        QMetaObject.connectSlotsByName(IDSVideoWindow)
    # setupUi

    def retranslateUi(self, IDSVideoWindow):
        IDSVideoWindow.setWindowTitle(QCoreApplication.translate("IDSVideoWindow", u"IDSVideoWindow", None))
        self.lEdit_Image_Status.setPlaceholderText(QCoreApplication.translate("IDSVideoWindow", u"Image Status", None))
        self.lbl_Image_Scale.setText(QCoreApplication.translate("IDSVideoWindow", u"100%", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("IDSVideoWindow", u"Inspector@IDSVideoWindow", None))
        self.grp_Device.setTitle(QCoreApplication.translate("IDSVideoWindow", u"Device", None))
        self.lbl_Device_List.setText(QCoreApplication.translate("IDSVideoWindow", u"List of devices", None))
        self.pBtn_Search_Device_List.setText(QCoreApplication.translate("IDSVideoWindow", u"Search", None))
        self.lbl_Device_ID.setText(QCoreApplication.translate("IDSVideoWindow", u"Device ID", None))
        self.lEdit_Device_ID.setText(QCoreApplication.translate("IDSVideoWindow", u"0", None))
        self.grp_Control.setTitle(QCoreApplication.translate("IDSVideoWindow", u"Control", None))
        self.lbl_Read_Frame_Delay.setText(QCoreApplication.translate("IDSVideoWindow", u"Read Frame Delay [ms]", None))
        self.lbl_Paint_Timer_Interval.setText(QCoreApplication.translate("IDSVideoWindow", u"Paint Timer Interval [ms]", None))
        self.rBtn_Thread.setText(QCoreApplication.translate("IDSVideoWindow", u"Thread", None))
        self.rBtn_Process.setText(QCoreApplication.translate("IDSVideoWindow", u"Process", None))
        self.cBox_FPS.setText(QCoreApplication.translate("IDSVideoWindow", u"FPS", None))
        self.cBox_Elapsed_Time.setText(QCoreApplication.translate("IDSVideoWindow", u"Elapsed", None))
        self.cBox_Timestamp.setText(QCoreApplication.translate("IDSVideoWindow", u"Stamp", None))
        self.pBtn_Start.setText(QCoreApplication.translate("IDSVideoWindow", u"Start", None))
        self.pBtn_Stop.setText(QCoreApplication.translate("IDSVideoWindow", u"Stop", None))
        self.pBtn_Snapshot.setText(QCoreApplication.translate("IDSVideoWindow", u"Snapshot", None))
        self.lbl_Timer_ID.setText(QCoreApplication.translate("IDSVideoWindow", u"Timer ID", None))
        self.lEdit_Timer_ID.setPlaceholderText(QCoreApplication.translate("IDSVideoWindow", u"Timer ID", None))
        self.lbl_Timer_Type.setText(QCoreApplication.translate("IDSVideoWindow", u"Timer Type", None))
#if QT_CONFIG(tooltip)
        self.lEdit_Timer_Type.setToolTip(QCoreApplication.translate("IDSVideoWindow", u"Precision, Coarse(\u00b15%), VeryCoarse(sec)", None))
#endif // QT_CONFIG(tooltip)
        self.lEdit_Timer_Type.setPlaceholderText(QCoreApplication.translate("IDSVideoWindow", u"Accuracy on platform", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("IDSVideoWindow", u"toolBar", None))
    # retranslateUi

