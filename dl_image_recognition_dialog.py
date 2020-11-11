"""画像認識用ダイアログ"""

# 標準
import os
import sys
import pathlib
import shutil
import math
import time
from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Callable,
    Any,
    TypeVar,
    Generic,
    NoReturn
)
from threading import Thread

# サードパーティ
import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm
from PIL import Image
import cv2

import torch                          # 基本モジュール
from torch.autograd import Variable   # 自動微分用
import torch.nn as nn                 # ネットワーク構築用
import torch.nn.functional as F       # ネットワーク用の関数群
import torch.optim as optim           # 最適化関数
from torch.utils import data          # データセット読み込み関連
from torchvision import (             # 組み込み画像関連
    datasets,
    models,
    transforms
)


from PySide2.QtGui import (
    QTextCursor,
    QColor,
    QPainter
)
from PySide2.QtCore import (
    Signal,
    Slot,
    Qt
)
from PySide2.QtWidgets import (
    QWidget,
    QFileDialog,
    QDialog,
    QMessageBox,
    QHBoxLayout
)
from PySide2.QtCharts import QtCharts


# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_DLImageRecognitionDialog import Ui_DLImageRecognitionDialog
from module.mldl.dl.model import pytorch_pretraining_models
from module.mldl.dl import pytorch_preprocessing
from module.mldl.dl.dataset.pytorch_dataset import (
    OneImageDataset,
    make_dataset_for_pytorch,
    make_dataloader_for_pytorch
)



class DLImageRecognitionDialog(QDialog):

    singal_post_message_to_monitor = Signal(str)
    signal_update_learning_curve = Signal(int, float, float, float, float)

    def __init__(self, parent:QWidget=None):
        super(DLImageRecognitionDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_DLImageRecognitionDialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # Closeされたときに自動でメモリ削除

        # Signal/Slot
        self._toolbar_connection()
        self._menubar_connection()
        self._ui_connection()
        self._custom_connection()

        self.current_dir = None

        # Meta-CSV Paths
        self.encoding = None
        self.meta_csv_paths = {'train': None, 'validation': None, 'test': None}
        self.file_counts = {'train': None, 'validation': None, 'test': None}

        # Pre-Training Model
        self.model_name = ""
        self.pre_training_model = None
        self.params_to_update = []

        # Training Config
        self.device_type = None
        self.optimizer = None
        self.criterion_loss = None
        self.epochs = 0
        self.batch_size = 0
        self.update_interval = 0
        self.preprocessing = None
        self.dataset_dict = None
        self.dataloader_dict = None
        self.training_thread = None
        self.is_training = True

        # Monitor
        self.ui.tEdit_Monitor.setReadOnly(True)

        # QChart
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.series_loss_train = QtCharts.QLineSeries()
        self.series_acc_train = QtCharts.QLineSeries()
        self.series_loss_val = QtCharts.QLineSeries()
        self.series_acc_val = QtCharts.QLineSeries()
        self.axis_x_epoch = QtCharts.QValueAxis()
        self.axis_x_tickcount = 10
        self.axis_x_epoch_max = self.axis_x_tickcount
        self.axis_y_loss = QtCharts.QValueAxis()
        self.axis_y_loss_tickcount = 10
        self.axis_y_loss_max = 1.0
        self.axis_y_acc = QtCharts.QValueAxis()
        self.axis_y_acc_tickcount = 10
        self.axis_y_acc_max = 1.0
        self.__init_chart()

        # QChart View
        self.view_chart = QtCharts.QChartView(self.chart)
        self.view_chart.setRenderHint(QPainter.Antialiasing)

        self.layout_view_chart = QHBoxLayout()
        self.layout_view_chart.addWidget(self.view_chart)
        self.ui.widget_Learning_Curve_Loss.setLayout(self.layout_view_chart)


    def _toolbar_connection(self):
        """
        ToolBarに関するSignal/Slotの接続
        :return:
        """
        pass

    def _menubar_connection(self):
        """
        MenuBarに関するSignal/Slotの接続
        :return:
        """
        pass

    def _ui_connection(self):
        """
        UIに関するSignal/Slotの接続
        :return:
        """
        """dataset Meta CSV"""
        # Get Train Meta-CSV Path
        self.ui.tBtn_Meta_CSV_Train_File_Path.clicked.connect(self._get_meta_csv)
        # Get Validation Meta-CSV Path
        self.ui.tBtn_Meta_CSV_Validation_File_Path.clicked.connect(self._get_meta_csv)
        # Get test Meta-CSV Path
        self.ui.tBtn_Meta_CSV_Test_File_Path.clicked.connect(self._get_meta_csv)

        """Operation"""
        # Data Argmentation
        # self.ui.pBtn_Data_Augmentation.clicked.connect(self._data_argmentation)
        # Init
        self.ui.pBtn_Training_Init.clicked.connect(self._init_training)
        # Training
        self.ui.pBtn_Training.clicked.connect(self._training)
        # Stop
        self.ui.pBtn_Training_Stop.clicked.connect(self._stop_training)

        """Metrics"""
        pass

        """PreTraining Model"""
        # 学習済みモデルを選択して，出力レイヤーのニューロン数を問題に合わせて付け替える.
        self.ui.pBtn_Model_Architecture.clicked.connect(self._select_and_modify_pretraining_model)

        """Training Parameters"""
        # Optimizer
        self.ui.cBox_Optimizer.currentIndexChanged.connect(self._select_optimizer)
        # Learning Scheduler
        self.ui.cBox_Learning_Scheduler.currentIndexChanged.connect(self._select_learning_scheduler)


    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        # Worker-ThreadからMain-ThreadのQTextEditにメッセージをポスト
        self.singal_post_message_to_monitor.connect(self._print_monitoring)

        # Worker-ThreadからMain-ThreadのQChartの更新
        self.signal_update_learning_curve.connect(self.__update_learning_curve)


    def __init_chart(self):
        """
        QChartの初期化
        :return:
        """

        # name
        self.series_loss_train.setName("train loss")
        self.series_acc_train.setName("train acc")
        self.series_loss_val.setName("validation loss")
        self.series_acc_val.setName("validation acc")

        # color
        self.series_loss_train.setColor(QColor(Qt.blue))
        self.series_acc_train.setColor(QColor(Qt.red))
        self.series_loss_val.setColor(QColor(Qt.cyan))
        self.series_acc_val.setColor(QColor(Qt.magenta))

        # add_series
        self.chart.addSeries(self.series_loss_train)
        self.chart.addSeries(self.series_acc_train)
        self.chart.addSeries(self.series_loss_val)
        self.chart.addSeries(self.series_acc_val)

        # axis_x_epoch
        self.axis_x_epoch = QtCharts.QValueAxis()
        self.axis_x_epoch.setTickCount(self.axis_x_tickcount)
        self.axis_x_epoch.setRange(0, self.axis_x_epoch_max)
        self.axis_x_epoch.setMin(0)
        self.axis_x_epoch.setMax(self.axis_x_epoch_max)
        self.axis_x_epoch.setLabelFormat("%d")
        self.axis_x_epoch.setTitleText("Epoch")
        self.chart.addAxis(self.axis_x_epoch, Qt.AlignBottom)
        self.series_loss_train.attachAxis(self.axis_x_epoch)
        self.series_acc_train.attachAxis(self.axis_x_epoch)
        self.series_loss_val.attachAxis(self.axis_x_epoch)
        self.series_acc_val.attachAxis(self.axis_x_epoch)

        # axis_y_loss
        self.axis_y_loss = QtCharts.QValueAxis()
        self.axis_y_loss.setTickCount(10)
        self.axis_y_loss.setLabelFormat("%.2f")
        self.axis_y_loss.setTitleText("Loss")
        self.chart.addAxis(self.axis_y_loss, Qt.AlignLeft)
        self.series_loss_train.attachAxis(self.axis_y_loss)
        self.series_loss_val.attachAxis(self.axis_y_loss)

        # axis_y_acc
        self.axis_y_acc = QtCharts.QValueAxis()
        self.axis_y_acc.setTickCount(10)
        self.axis_y_acc.setLabelFormat("%.2f")
        self.axis_y_acc.setTitleText("Accuracy")
        self.chart.addAxis(self.axis_y_acc, Qt.AlignRight)
        self.series_acc_train.attachAxis(self.axis_y_acc)
        self.series_acc_val.attachAxis(self.axis_y_acc)


    @Slot(int, float, float, float, float)
    def __update_learning_curve(self, epoch, train_loss, train_acc, val_loss, val_acc):
        """
        学習曲線(QChart)の更新
        :return:
        """
        self.series_loss_train.append(epoch, train_loss)
        self.series_acc_train.append(epoch, train_acc)
        self.series_loss_val.append(epoch, val_loss)
        self.series_acc_val.append(epoch, val_acc)

        if (epoch % self.axis_x_tickcount) == 0:
            self.axis_x_epoch_max += self.axis_x_tickcount
            self.axis_x_epoch.setRange(0, self.axis_x_epoch_max)
            self.axis_x_epoch.setMin(0)
            self.axis_x_epoch.setMax(self.axis_x_epoch_max)

        loss_large = train_loss if train_loss > val_loss else val_loss
        if self.axis_y_loss_max < loss_large:
            loss_chunk = loss_large / self.axis_y_loss_tickcount
            self.axis_y_loss_max = loss_chunk * (self.axis_y_loss_tickcount + 1)
            self.axis_y_loss.setRange(0, self.axis_y_loss_max)
            self.axis_y_loss.setMin(0)
            self.axis_y_loss.setMax(self.axis_y_loss_max)

        self._print_monitoring("Epoch {0:d}/{1:d} TRAIN -> Loss: {2:.4f} Acc: {3:.4f}, " \
                               "VALIDATION -> Loss: {4:.4f}, Acc: {5:4f}".format(
                                epoch, self.epochs, train_loss, train_acc, val_loss, val_acc))

        value_max = self.ui.tEdit_Monitor.verticalScrollBar().maximum()
        self.ui.tEdit_Monitor.verticalScrollBar().setValue(value_max)


    def _print_monitoring(self, message:str):
        """
        UI-Monitor出力と標準出力を行う
        :param message:
        :return:
        """
        print(message)
        self.ui.tEdit_Monitor.append(message)

    def _get_meta_csv(self):
        """
        Meta-CSVファイルのパスを取得
        :return:
        """
        if self.current_dir is None:
            self.current_dir = os.getcwd()

        caption = ""
        meta_csv_path = ""
        if self.sender() == self.ui.tBtn_Meta_CSV_Train_File_Path:
            caption = "Train Meta CSV の選択"
            meta_csv_path, _ = QFileDialog.getOpenFileName(self, caption, self.current_dir, filter="CSVファイル (*.csv)")
            if meta_csv_path == "":
                return
            self.meta_csv_paths['train'] = meta_csv_path

        if self.sender() == self.ui.tBtn_Meta_CSV_Validation_File_Path:
            caption = "Validation Meta CSV の選択"
            meta_csv_path, _ = QFileDialog.getOpenFileName(self, caption, self.current_dir, filter="CSVファイル (*.csv)")
            if meta_csv_path == "":
                return
            self.meta_csv_paths['validation'] = meta_csv_path

        if self.sender() == self.ui.tBtn_Meta_CSV_Test_File_Path:
            caption = "test Meta CSV の選択"
            meta_csv_path, _ = QFileDialog.getOpenFileName(self, caption, self.current_dir, filter="CSVファイル (*.csv)")
            if meta_csv_path == "":
                return
            self.meta_csv_paths['test'] = meta_csv_path

        if meta_csv_path != "":
            self.current_dir = os.path.dirname(meta_csv_path)

        try:
            if self.sender() == self.ui.tBtn_Meta_CSV_Train_File_Path:
                # Train ファイルパス
                self.ui.lEdit_Meta_CSV_Train_File_Path.setText(meta_csv_path)
            if self.sender() == self.ui.tBtn_Meta_CSV_Validation_File_Path:
                # Validation ファイルパス
                self.ui.lEdit_Meta_CSV_Validation_File_Path.setText(meta_csv_path)
            if self.sender() == self.ui.tBtn_Meta_CSV_Test_File_Path:
                # test ファイルパス
                self.ui.lEdit_Meta_CSV_Test_File_Path.setText(meta_csv_path)

            # 登録されたファイルパスの数を取得
            encode_type = self.ui.cBox_Encode_Type.currentText()
            header = 'infer' if self.ui.rBtn_Header_ON.isChecked() else None
            meta_csv_df = pd.read_csv(meta_csv_path, delimiter=',', encoding=encode_type, header=header)
            self.encoding = encode_type
            print(str(meta_csv_df))

            if self.sender() == self.ui.tBtn_Meta_CSV_Train_File_Path:
                self.file_counts['train'] = meta_csv_df.shape[0]  # 行数
                self.ui.lEdit_Train_Count.setText(str(self.file_counts['train']))

            if self.sender() == self.ui.tBtn_Meta_CSV_Validation_File_Path:
                self.file_counts['validation'] = meta_csv_df.shape[0]  # 行数
                self.ui.lEdit_Validation_Count.setText(str(self.file_counts['validation']))

            if self.sender() == self.ui.tBtn_Meta_CSV_Test_File_Path:
                self.file_counts['test'] = meta_csv_df.shape[0]  # 行数
                self.ui.lEdit_Test_Count.setText(str(self.file_counts['test']))

        except UnicodeDecodeError as e:
            QMessageBox.warning(self, "Error Encoding", str(e), QMessageBox.Ok)
        finally:
            self._print_monitoring("ファイル読み込み処理を終了.")


    @Slot()
    def _select_and_modify_pretraining_model(self):
        """
        学習済みモデルを選択して，解きたい問題に合わせて出力レイヤーのニューロン数を返る.
        そして，モデル構成(Architecture)を表示する.
        :return:
        """
        # Model
        model_name = self.ui.cBox_PreTraining_Model.currentText()
        pre_training_model = None
        architecture = ""
        params_to_update = []

        # Last Layer
        last_layer_neuron = self.ui.sBox_Final_Layer_Neuron.value()

        # Learning Type
        learning_type = self.ui.cBox_Learning_Type.currentText().lower()

        # 学習済みモデルを取得
        if model_name == "VGG16 : ILSVRC2013":
            pre_training_model, params_to_update, architecture \
                = pytorch_pretraining_models.load_vgg16_for_ILSVRC2013(last_layer_num=last_layer_neuron,
                                                                       learning_type=learning_type)
        self.model_name = model_name
        self.pre_training_model = pre_training_model
        self.params_to_update = params_to_update
        self.ui.tEdit_ModelStructure.setText(architecture)

    @Slot(int)
    def _select_optimizer(self, optimizer_index: int):
        """
        オプティマイザーを選択
        :param optimizer_name:
        :return:
        """
        self.ui.stackedWidget_Optimizer.setCurrentIndex(optimizer_index)

        # 未実装のオプティマイザ
        optimizer_name = self.ui.cBox_Optimizer.currentText()
        if optimizer_name.lower() == 'adabound':
            QMessageBox.warning(self, "未実装のOptimizer", "No Implimantation yet.", QMessageBox.Ok)



    @Slot(int)
    def _select_learning_scheduler(self, scheduler_index: int):
        """
        学習率のスケジューラを選択
        :param scheduler_name:
        :return:
        """
        self.ui.stackedWidget_Learning_Scheduler.setCurrentIndex(scheduler_index)


    @Slot()
    def _init_training(self):
        """
        学習条件を設定する
        :return:
        """
        # 前処理の定義を読み込む
        train_desc = "transforms.Lambda(lambda gray_img: gray_img.convert('RGB')),"\
                     "transforms.Resize(size=input_image_size, interpolation=Image.BILINEAR),"\
                     "transforms.ToTensor(),"\
                     "transforms.Lambda(lambda tensor: tensor / 255.0)"

        validation_desc = "transforms.Lambda(lambda gray_img: gray_img.convert('RGB')),"\
                          "transforms.Resize(size=input_image_size, interpolation=Image.BILINEAR),"\
                          "transforms.ToTensor(),"\
                          "transforms.Lambda(lambda tensor: tensor / 255.0)"

        test_desc = "transforms.Lambda(lambda gray_img: gray_img.convert('RGB')),"\
                    "transforms.Resize(size=input_image_size, interpolation=Image.BILINEAR),"\
                    "transforms.ToTensor(),"\
                    "transforms.Lambda(lambda tensor: tensor / 255.0)"
        preprocessing = pytorch_preprocessing.ImagePreprocessing(input_image_size=(300, 300),
                                                                 train_desc=train_desc,
                                                                 validation_desc=validation_desc,
                                                                 test_desc=test_desc)
        self.preprocessing = preprocessing
        self._print_monitoring("Prepared preprocessing.")

        # データセットの作成
        if self.meta_csv_paths['train'] is None or \
           self.meta_csv_paths['validation'] is None or \
           self.meta_csv_paths['test'] is None:
            color_current = self.ui.tEdit_Monitor.textColor()
            self.ui.tEdit_Monitor.setTextColor(QColor(255, 0, 0))
            self._print_monitoring("No meta-csv path. Stop `init`phase.")
            self.ui.tEdit_Monitor.setTextColor(color_current)
            return


        dataset_dict = make_dataset_for_pytorch(pytorch_dataset_klass=OneImageDataset,
                                                meta_csv_train_path=self.meta_csv_paths['train'],
                                                meta_csv_validation_path=self.meta_csv_paths['validation'],
                                                preprocessing=preprocessing,
                                                encoding=self.encoding)
        self.dataset_dict = dataset_dict
        self._print_monitoring(f"Dataset: {dataset_dict}")

        # データローダーの作成
        self.batch_size = self.ui.sBox_Batch_Size.value()
        dataloader_dict = make_dataloader_for_pytorch(batch_size=self.batch_size,
                                                      train_dataset=dataset_dict['train'],
                                                      validation_dataset=dataset_dict['validation'])
        self.dataloader_dict = dataloader_dict
        self._print_monitoring(f"Dataloader: {dataloader_dict}")


        # デバイス(CPU or GPU)の選択
        messages_list = []
        if torch.cuda.is_available():
            messages_list.append('CUDA（GPU）が利用できる環境です.')
            messages_list.append(f'CUDAデバイス数： {torch.cuda.device_count()}')
            messages_list.append(f'現在のCUDAデバイス番号： {torch.cuda.current_device()}')  # ※0スタート
            messages_list.append(f'1番目のCUDAデバイス名： {torch.cuda.get_device_name(0)}')  # 例「Tesla T4」
            torch.backends.cudnn.deterministic = True  # GPU計算が決定論的 or NOT. benchmark=Falseにすること
            torch.backends.cudnn.benchmark = False  # ネットワークの順伝播及び逆伝搬関数の計算手法が固定であれば、高速化される.
            cuda_device_number = torch.cuda.current_device()
            self.device_type = torch.device("cuda:{0}".format(cuda_device_number))
        else:
            self.device_type = torch.device("cpu")

        messages_list.append(f"使用デバイス: {self.device_type}")
        for msg in messages_list:
            self._print_monitoring(msg)

        # モデルはPreTraining ModelのUIで作成済みのはず
        model_name = self.model_name
        pre_training_model = self.pre_training_model
        params_to_update = self.params_to_update
        if model_name == "":
            color_current = self.ui.tEdit_Monitor.textColor()
            self.ui.tEdit_Monitor.setTextColor(QColor(255, 0, 0))
            self._print_monitoring("No pre-training model. Stop `init` phase.")
            self.ui.tEdit_Monitor.setTextColor(color_current)
            return


        # モデル状態を学習モードに変更
        pre_training_model.train()
        self._print_monitoring(f"{model_name} : 学習モードに移行")


        # 多クラス分類用のクロスエントロピー誤差(注意: pytorchはLoss関数の中にsoftmax()関数が入っている!
        # モデルの最終出力がスカラー(1値)のSigmoid()への入力で2値分類を行う場合，torch.nn.BCEWithLogitsLoss()を使おう。
        criterion_loss = nn.CrossEntropyLoss(reduction='mean')
        self.criterion_loss = criterion_loss


        # 最適化手法
        optimizer_name = self.ui.cBox_Optimizer.currentText()
        self.epochs = self.ui.sBox_Epochs.value()
        self.update_interval = self.ui.sBox_Update_Interval.value()
        weight_decay = self.ui.dsBox_Weight_Decay.value()

        if optimizer_name.lower() == 'sgd':
            lr = self.ui.dsBox_SGD_Learning_Rate.value()
            self.optimizer = optim.SGD(params=params_to_update,
                                       lr=lr,
                                       nesterov=False,
                                       weight_decay=weight_decay)

        elif optimizer_name.lower() == 'momentum':
            lr = self.ui.dsBox_Momentum_Learning_Rate.value()
            momentum = self.ui.dsBox_Momentum_Momentum.value()
            self.optimizer = optim.SGD(params=params_to_update,
                                       lr=lr,
                                       momentum=momentum,
                                       nesterov=False,
                                       weight_decay=weight_decay)

        elif optimizer_name.lower() == 'nesterov':
            lr = self.ui.dsBox_Nesterov_Learning_Rate.value()
            momentum = self.ui.dsBox_Nesterov_Momentum.value()
            self.optimizer = optim.SGD(params=params_to_update,
                                       lr=lr,
                                       momentum=momentum,
                                       nesterov=True,
                                       weight_decay=weight_decay)

        elif optimizer_name.lower() == 'rmsprop':
            lr = self.ui.dsBox_RMSprop_Learning_Rate.value()
            decay = self.ui.dsBox_RMSprop_Alpha.value()
            epsilon_text = self.ui.lEdit_RMSprop_Epsilon.text()
            epsilon = eval(epsilon_text.lower())
            is_centered = self.ui.chBox_RMSprop_Centered.isChecked()
            self.optimizer = optim.RMSprop(params=params_to_update,
                                           lr=lr,
                                           alpha=decay,
                                           eps=epsilon, # 1E-8
                                           centered=is_centered, # Default False. If True, compute the centered RMSProp, the gradient is normalized by an estimation of its variance
                                           weight_decay=weight_decay)

        elif optimizer_name.lower() == 'adadelta':
            lr = self.ui.dsBox_Adadelta_Learning_Rate.value()
            rho = self.ui.dsBox_Adadelta_Rho.value()
            epsilon_text = self.ui.lEdit_Adadelta_Epsilon.text()
            epsilon = eval(epsilon_text.lower()) # 1E-6
            self.optimizer = optim.Adadelta(params=params_to_update,
                                            lr=lr,
                                            rho=rho,
                                            esp=epsilon,
                                            weight_decay=weight_decay)

        elif optimizer_name.lower() == 'adagrad':
            lr = self.ui.dsBox_Adagrad_Learning_Rate.value()
            decay = self.ui.dsBox_Adagrad_Decay.value()
            epsilon_text = self.ui.lEdit_Adagrad_Epsilon.text()
            epsilon = eval(epsilon_text.lower()) # 1E-10
            self.optimizer = optim.Adagrad(params=params_to_update,
                                           lr=lr,
                                           lr_decay=decay,
                                           eps=epsilon,
                                           weight_decay=weight_decay)

        elif optimizer_name.lower() == 'adam':
            lr = self.ui.dsBox_Adam_Learning_Rate.value()
            beta1 = self.ui.dsBox_Adam_Beta1.value()
            beta2 = self.ui.dsBox_Adam_Beta2.value()
            epsilon_text = self.ui.lEdit_Adam_Epsilon.text()
            epsilon = eval(epsilon_text.lower()) # 1E-8
            is_amsgrad = self.ui.chBox_Adam_AMSGrad.isChecked() # False
            self.optimizer = optim.Adam(params=params_to_update,
                                        lr=lr,
                                        betas=(beta1, beta2),
                                        eps=epsilon,
                                        amsgrad=is_amsgrad,
                                        weight_decay=weight_decay)

        elif optimizer_name.lower() == 'adamax':
            lr = self.ui.dsBox_Adamax_Learning_Rate.value()
            beta1 = self.ui.dsBox_Adamax_Beta1.value()
            beta2 = self.ui.dsBox_Adamax_Beta2.value()
            epsilon_text = self.ui.lEdit_Adamax_Epsilon.text()
            epsilon = eval(epsilon_text.lower())  # 1E-8
            self.optimizer = optim.Adamax(params=params_to_update,
                                          lr=lr,
                                          betas=(beta1, beta2),
                                          eps=epsilon,
                                          weight_decay=weight_decay)

        elif optimizer_name.lower() == 'adabound':
            self._print_monitoring("Yet, No Implementation.")
            pass
            return
        else:
            color_current = self.ui.tEdit_Monitor.textColor()
            self.ui.tEdit_Monitor.setTextColor(QColor(255, 0, 0))
            self._print_monitoring("Invalid optimizer. Stop `init`phase.")
            self.ui.tEdit_Monitor.setTextColor(color_current)
            return

        self._print_monitoring(f"Optimizer: {self.optimizer}")
        self._print_monitoring("学習準備が整いました.")


        # 複数GPUによる計算が可能な場合
        if torch.cuda.is_available():
            device_count = torch.cuda.device_count()
            if device_count > 1:
                self._print_monitoring(f"{device_count}GPUs. 複数GPUを用いた並列計算の設定を行います.")

        # 設定されたデバイス上のメモリにネットワークオブジェクトを展開
        pre_training_model.to(self.device_type)


    def __thread_loop(self):
        """
        学習をGUIのメインスレッドから切り離して処理するための関数
        :return:
        """
        device_type = self.device_type
        pre_training_model = self.pre_training_model
        params_to_update = self.params_to_update
        criterion_loss = self.criterion_loss
        epochs = self.epochs
        batch_size = self.batch_size
        update_interval = self.update_interval
        dataloader_dict = self.dataloader_dict
        optimizer = self.optimizer

        train_losses = []
        train_accuracies = []
        validation_losses = []
        validation_accuracies = []

        self.singal_post_message_to_monitor.emit("---------- Training Start ----------")

        for epoch in range(epochs):
            # train-phase -> validation-phase
            for phase in ['train', 'validation']:
                if phase == 'train':
                    pre_training_model.train()  # 訓練モードのモデル
                else:
                    pre_training_model.eval()  # 検証モードのモデル

                epoch_loss = 0.0
                epoch_correct = 0

                # 未学習時の検証性能を確かめるため、epoch=0の訓練では未学習のモデルを使用する
                if (epoch == 0) and (phase == 'train'):
                    self.singal_post_message_to_monitor.emit("First training is skipped.")
                    continue

                # データローダからミニバッチを取り出すループ
                for inputs, labels in dataloader_dict[phase]:  # tqdm(dataloader_dict[phase]):

                    # GPUが利用できるならGPUのメモリにデータを転送する
                    inputs = inputs.to(device_type)
                    labels = labels.to(device_type)

                    # 各パラメータの勾配の初期化
                    optimizer.zero_grad()

                    with torch.set_grad_enabled(phase == 'train'):
                        # 順伝播
                        outputs = pre_training_model(inputs)  # 出力
                        minibatch_loss = criterion_loss(outputs, labels)  # 誤差

                        # 予測ラベル
                        _, preds = torch.max(outputs, 1)  # 予測ラベル

                        # 訓練時は逆誤差伝播
                        if phase == 'train':
                            minibatch_loss.backward()  # 各パラメータの勾配を求める
                            optimizer.step()  # 算出した勾配から各パラメータを更新

                        # epoch_lossの更新
                        batch_loss = minibatch_loss * inputs.size(0)  # batch_size平均loss * バッチサイズ = バッチサイズのloss
                        epoch_loss += batch_loss.double().item()  # torch.double -> python double

                        # epoch_correctの更新
                        batch_correct = torch.sum(preds == labels.data)
                        epoch_correct += batch_correct.double().item()  # torch.double -> python double
                # end of for inputs, labels in tqdm(dataloader_dict[phase]):

                # epochごとのlossと正解率を表示
                epoch_loss = epoch_loss / len(dataloader_dict[phase].dataset)
                epoch_accuracy = epoch_correct / len(dataloader_dict[phase].dataset)

                if phase == 'train':
                    train_losses.append(epoch_loss)
                    train_accuracies.append(epoch_accuracy)
                else:
                    validation_losses.append(epoch_loss)
                    validation_accuracies.append(epoch_accuracy)

            # スコア出力
            if epoch == 0:
                train_loss = 0
                train_acc = 0
                val_loss = validation_losses[-1]
                val_acc = validation_accuracies[-1]
            else:
                train_loss = train_losses[-1]
                train_acc = train_accuracies[-1]
                val_loss = validation_losses[-1]
                val_acc = validation_accuracies[-1]

            # Main-ThreadにあるUiのQChart(学習曲線)を更新する
            self.signal_update_learning_curve.emit(epoch + 1, train_loss, train_acc, val_loss, val_acc)

            # 学習を止める
            if not self.is_training:
                self.singal_post_message_to_monitor.emit("Stop training...")
                break

        # end of for epoch in range(epochs):

        self.singal_post_message_to_monitor.emit("---------- Training Finish ----------")
        self.singal_post_message_to_monitor.emit("Worker-thread end.")


    @Slot()
    def _training(self):
        """
        学習フェーズ
        'train'と'validation'を交互に繰り返す.
        誤差(Loss)と正解率(Accuracy)
        :return:
        """
        # daemonスレッド: 残っているスレッドがデーモンスレッドだけになった時に Python プログラム全体を終了させる
        self.training_thread = Thread(target=self.__thread_loop,
                                      args=(),
                                      name="Thread of dl training.",
                                      daemon=True)

        self.is_training = True
        self.training_thread.start()
        self._print_monitoring("Worker-thread start.")
        self._print_monitoring(f"Running of worker-thread is {self.training_thread.is_alive()}.")


    @Slot()
    def _stop_training(self):
        """
        Worker-Threadでの学習をストップする.
        :return:
        """
        # Worker-Threadのforループでbreakして，そのままWorker-Threadを抜ける
        self.is_training = False

