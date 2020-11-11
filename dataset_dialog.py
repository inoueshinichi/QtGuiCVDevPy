"""データセット操作用のダイアログ
"""

# 標準
import os
import shutil
import sys
import pathlib
import csv
import math

# サードパーティ
from sklearn.model_selection import train_test_split
from PySide2.QtCore import (
    Slot,
    Qt
)
from PySide2.QtWidgets import (
    QWidget,
    QFileDialog,
    QDialog,
    QMessageBox,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem
)

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from ui.ui_DatasetDialog import Ui_DatasetDialog
from module.mldl.dl.dataset import dataset


class DatasetDialog(QDialog):

    def __init__(self, parent:QWidget=None):

        super(DatasetDialog, self).__init__(parent)

        # 親
        self.main_win = parent

        # UI
        self.ui = Ui_DatasetDialog()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)  # Closeされたときに自動でメモリ削除

        # 数値ラベリング: TableWidget
        self.raw_data_header_list = ["Ext", "FilePath"]
        self.ui.tableWidget_Raw_Data_Dir.setColumnCount(len(self.raw_data_header_list))
        self.ui.tableWidget_Raw_Data_Dir.setHorizontalHeaderLabels(self.raw_data_header_list)
        self.ui.tableWidget_Raw_Data_Dir.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableWidget_Raw_Data_Dir.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_Raw_Data_Dir.setEditTriggers(QTableWidget.NoEditTriggers)

        # 自動分割: TableWidget
        self.auto_split_header_list = ["FileCount", "FilePath"]
        self.ui.tableWidget_All_Directory.setColumnCount(len(self.auto_split_header_list))
        self.ui.tableWidget_All_Directory.setHorizontalHeaderLabels(self.auto_split_header_list)
        self.ui.tableWidget_All_Directory.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableWidget_All_Directory.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_All_Directory.setEditTriggers(QTableWidget.NoEditTriggers)

        self.train_validation_test_header_list = ["Category", "All", "Train", "Validation", "test"]
        self.ui.tableWidget_Train_Validation_Test.setColumnCount(len(self.train_validation_test_header_list))
        self.ui.tableWidget_Train_Validation_Test.setHorizontalHeaderLabels(self.train_validation_test_header_list)
        self.ui.tableWidget_Train_Validation_Test.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableWidget_Train_Validation_Test.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_Train_Validation_Test.setEditTriggers(QTableWidget.NoEditTriggers)


        # Files
        self.file_paths = []
        self.csv_paths = []
        self.target_file_paths = []

        # Signal/Slot
        self._toolbar_connection()
        self._menubar_connection()
        self._ui_connection()
        self._custom_connection()



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

        """数値ラベリング"""
        # Get Raw Data Dir
        self.ui.tBtn_Raw_Data_Dir.clicked.connect(self._get_raw_data_dir)
        # Get Csv Data Dir
        self.ui.tBtn_Csv_Data_Dir.clicked.connect(self._get_csv_data_dir)
        # Labeling
        self.ui.pBtn_Labeling.clicked.connect(self._labeling_annotation)

        """手動分割(Target -> A B)"""
        # Get Target Dir
        self.ui.tBtn_Target_Directory_Path.clicked.connect(self._get_target_dir)
        # Get A Dir
        self.ui.tBtn_A_Directory_Path.clicked.connect(self._get_a_dir)
        # Get B Dir
        self.ui.tBtn_B_Directory_Path.clicked.connect(self._get_b_dir)
        # Split Target to A and B
        self.ui.pBtn_Split_Target_To_A_B.clicked.connect(self._split_target_to_a_and_b)

        """自動分割(All -> Train Validation test)"""
        # Get Directories whose files are splited.
        self.ui.tBtn_All_Directory.clicked.connect(self._get_directories_whose_files_are_splited)
        # Get Output Directory Path for dataset(Train Validation test)
        self.ui.tBtn_Output_Directory.clicked.connect(self._get_output_directory_for_dataset)
        # Split Labeled dataset to Train Validation test
        self.ui.pBtn_Split_All_To_Train_Validation_Test.clicked.connect(self._split_all_to_train_validation_test)
        # Make Meta CSV
        self.ui.pBtn_Make_Meta_CSV.clicked.connect(self._make_meta_csv_files)


    def _custom_connection(self):
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        pass

    @Slot()
    def _get_raw_data_dir(self):
        """
        生データを保存したディレクトリパスを取得する
        :return:
        """
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "生データを保存したディレクトリ",
                                                    os.getcwd())

        if dir_path:
            self.ui.lEdit_Raw_Data_Dir.setText(dir_path)

            # ファイルパスを取得(再帰なし)
            dir_path_obj = pathlib.Path(dir_path)
            self.file_paths = [str(path_obj) for path_obj in dir_path_obj.iterdir()
                          if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

            file_count = len(self.file_paths)
            # file_names = list(map(lambda x: x.split(os.sep)[-1], self.file_paths))

            # テーブルの初期化
            self.ui.tableWidget_Raw_Data_Dir.clearContents()
            self.ui.tableWidget_Raw_Data_Dir.setRowCount(file_count)
            for row, path in enumerate(self.file_paths):
                name, ext = path.split(os.sep)[-1].split('.')
                item_ext = QTableWidgetItem(ext)
                self.ui.tableWidget_Raw_Data_Dir.setItem(row, self.raw_data_header_list.index("Ext"), item_ext)
                item_path = QTableWidgetItem(path)
                self.ui.tableWidget_Raw_Data_Dir.setItem(row, self.raw_data_header_list.index("FilePath"), item_path)

            self.ui.lEdit_Raw_Data_Count.setText(str(file_count))


    @Slot()
    def _get_csv_data_dir(self):
        """
        csvファイルを保存するディレクトリパスを取得する
        :return:
        """
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "CSVファイルを保存するディレクトリ",
                                                    os.getcwd())

        if dir_path:
            self.ui.lEdit_Csv_Data_Dir.setText(dir_path)

    @Slot()
    def _labeling_annotation(self):
        """
        ラベリングする
        :return:
        """
        raw_data_dir = self.ui.lEdit_Raw_Data_Dir.text()
        csv_data_dir = self.ui.lEdit_Csv_Data_Dir.text()

        if raw_data_dir and csv_data_dir:
            label_str = self.ui.lEdit_Raw_Data_Label.text()
            valid_count, self.csv_paths = dataset.labeling_dataset(raw_data_dir,
                                                                   csv_data_dir,
                                                                   label=label_str,
                                                                   encoding='shift-jis') # UTF-8にすると，csvファイル内の日本語が文字化けする

            self.ui.lEdit_Valid_Raw_Data_Count.setText(str(valid_count))
        else:
            QMessageBox.warning(self, "Invalid Directory Path", "ディレクトリパスが設定されていません.", QMessageBox.Ok)

    @Slot()
    def _get_target_dir(self):
        """
        Targetディレクトリパスを取得する
        :return:
        """
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "Targetディレクトリ",
                                                    os.getcwd())

        if dir_path:
            self.ui.lEdit_Target_Directory_Path.setText(dir_path)

            dir_path_obj = pathlib.Path(dir_path)
            self.target_file_paths = [str(path_obj) for path_obj in dir_path_obj.iterdir()
                          if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

            target_file_count = len(self.target_file_paths)
            self.ui.lEdit_Target_Num.setText(str(target_file_count))

    @Slot()
    def _get_a_dir(self):
        """
        Aディレクトリパスを取得する
        :return:
        """
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "Aディレクトリ",
                                                    os.getcwd())

        if dir_path:
            self.ui.lEdit_A_Directory_Path.setText(dir_path)


    @Slot()
    def _get_b_dir(self):
        """
        Aディレクトリパスを取得する
        :return:
        """
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "Bディレクトリ",
                                                    os.getcwd())

        if dir_path:
            self.ui.lEdit_B_Directory_Path.setText(dir_path)


    @Slot()
    def _split_target_to_a_and_b(self):
        """
        ファイル分割: Target -> A, B
        :return:
        """
        target_dir = self.ui.lEdit_Target_Directory_Path.text()
        a_dir = self.ui.lEdit_A_Directory_Path.text()
        b_dir = self.ui.lEdit_B_Directory_Path.text()

        if target_dir and a_dir and b_dir:
            # Bへの配分
            b_percent = self.ui.cBox_B_Percentage.currentText().rstrip('%')
            b_percent = int(b_percent) / 100.0

            # Shuffle or Not
            is_shuffle = self.ui.chBox_Manual_Shuffle.isChecked()

            a_file_paths, b_file_paths = train_test_split(self.target_file_paths, test_size=b_percent, shuffle=is_shuffle)
            # bは切り上げとなる. e.g 10 * 0.25 = 2.5 -> 3

            self.ui.lEdit_A_Num.setText(str(len(a_file_paths)))
            self.ui.lEdit_B_Num.setText(str(len(b_file_paths)))

            # ディレクトリがない場合，作成。既にコピー先にファイルがある場合，削除
            for dst_dir in [a_dir, b_dir]:
                dir_path_obj = pathlib.Path(dst_dir)

                if not dir_path_obj.exists():
                    dir_path_obj.mkdir()
                else:
                    file_paths = [str(path_obj) for path_obj in dir_path_obj.iterdir()
                              if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

                    if file_paths:
                        # ファイルの削除(ディレクトリは消さない)
                        for exist_path in file_paths:
                            os.remove(exist_path)
                        """以下，ディレクトリの削除と生成に関して，
                           shutil.rmtree()を行った直後に
                           Windowsではmkdir()のタイミングで[WinError 5]が発生し，
                           ディレクトリの作成に失敗することがある。
                        """
                        # # 中身のあるディレクトリごと削除
                        # shutil.rmtree(dir_path_obj)
                        # # ディレクトリの作成
                        # dir_path_obj.mkdir()

            # ファイルコピー
            for dst_dir, src_file_paths in zip([a_dir, b_dir], [a_file_paths, b_file_paths]):
                for src_path in src_file_paths:
                    # コピー元ファイル名
                    filename = src_path.split(os.sep)[-1]
                    # コピー先ファイルパス
                    copyed_path = dst_dir + os.sep + filename
                    # コピー(メタデータはコピーされない)
                    shutil.copyfile(src=src_path, dst=copyed_path)

    @Slot()
    def _get_directories_whose_files_are_splited(self):
        """
        Train, Validation, Testに分割するファイルを保存している
        アノテーション済みの複数ディレクトリを選択
        :return:
        """
        # フォルダ選択時に親ディレクトリも取得してしまうので，使わない
        # file_dialog = QFileDialog(caption="アノテーション済みの複数ディレクトリを選択")
        # file_dialog.setFileMode(QFileDialog.DirectoryOnly)
        # # file_dialog.setFileMode(QFileDialog.Directory)
        # # file_dialog.setOption(QFileDialog.ShowDirsOnly, True)
        # # file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        # file_list_view = file_dialog.findChild(QListView, 'listView')
        # if file_list_view:
        #     file_list_view.setSelectionMode(QAbstractItemView.MultiSelection)
        # file_tree_view = file_dialog.findChild(QTreeView, "treeView")
        # if file_tree_view:
        #     file_tree_view.setSelectionMode(QAbstractItemView.MultiSelection)
        #
        # dir_paths = ""
        # if file_dialog.exec_():
        #     dir_paths = file_dialog.selectedFiles()

        dir_path_parent = QFileDialog.getExistingDirectory(self, "ディレクトリの選択", options=QFileDialog.DontUseNativeDialog)
        dir_paths = []
        if dir_path_parent:
            dir_path_parent_obj = pathlib.Path(dir_path_parent)
            for path_obj in dir_path_parent_obj.iterdir():
                if path_obj.is_dir():
                    dir_paths.append(str(path_obj))

        # Tableの初期化
        self.ui.tableWidget_All_Directory.clearContents()
        self.ui.tableWidget_All_Directory.setRowCount(0)

        if dir_paths:
            self.ui.tableWidget_All_Directory.setRowCount(len(dir_paths)) # 行数を設定

            for row, dir_path in enumerate(dir_paths):
                dir_path_obj = pathlib.Path(dir_path)
                file_paths = [str(path_obj) for path_obj in dir_path_obj.iterdir()
                              if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

                file_count = len(file_paths)
                item_file_count = QTableWidgetItem(str(file_count))
                self.ui.tableWidget_All_Directory.setItem(row,
                                                          self.auto_split_header_list.index("FileCount"),
                                                          item_file_count)

                item_dir_path = QTableWidgetItem(dir_path)
                self.ui.tableWidget_All_Directory.setItem(row,
                                                          self.auto_split_header_list.index("FilePath"),
                                                          item_dir_path)

    @Slot()
    def _get_output_directory_for_dataset(self):
        """
        カテゴリー毎にアノテーションされた複数ディレクトリをTrain, Validation, Testに
        分割して保存するディレクトリパスを取得する
        :return:
        """
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "データセットを保存するディレクトリを選択",
                                                    os.getcwd())

        if dir_path:
            self.ui.lEdit_Output_Directory_Path.setText(dir_path)

    @Slot()
    def _split_all_to_train_validation_test(self):
        """
        アノテーション済みの複数ディレクトリをカテゴリー別にTrain, Validation, Testに分割する
        :return:
        """
        output_dir = self.ui.lEdit_Output_Directory_Path.text()
        output_dir_obj = pathlib.Path(output_dir)
        if output_dir_obj.exists():
            row_count = self.ui.tableWidget_All_Directory.rowCount()
            self.ui.tableWidget_Train_Validation_Test.clearContents()
            self.ui.tableWidget_Train_Validation_Test.setRowCount(row_count)

            dir_name_list = []
            file_paths_train_dict = {}
            file_paths_validation_dict = {}
            file_paths_test_dict = {}

            for row in range(row_count):
                # File Count
                item_file_count = self.ui.tableWidget_All_Directory.item(row, self.auto_split_header_list.index("FileCount"))
                file_count = int(item_file_count.data(Qt.EditRole))

                # Directory path
                item_dir_path = self.ui.tableWidget_All_Directory.item(row, self.auto_split_header_list.index("FilePath"))
                dir_path = item_dir_path.data(Qt.EditRole)

                # File
                dir_path_obj = pathlib.Path(dir_path)
                file_paths = [str(path_obj) for path_obj in dir_path_obj.iterdir()
                              if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

                # All -> Train, test
                test_percentage = self.ui.cBox_Test_Percentage.currentText().rstrip('%')
                test_percentage = int(test_percentage) / 100.0
                count_tmp_test = math.ceil(len(file_paths) * test_percentage) # 切り上げ
                count_tmp_train = len(file_paths) - count_tmp_test
                if count_tmp_train > 0:
                    file_paths_train, file_paths_test = train_test_split(file_paths, test_size=test_percentage)
                    # file_paths_testは切り上げとなる. e.g 10 * 0.25 = 2.5 -> 3
                else:
                    dir_name = str(dir_path_obj).split(os.sep)[-1]
                    count_tmp_all = file_count
                    QMessageBox.critical(self, "Error Train File Count.",
                                         "Trainデータを確保できません.\nDir:{0}, All:{1}, Train:{2}, test:{3}, {4}%".format(
                                             dir_name,
                                             count_tmp_all,
                                             count_tmp_train,
                                             count_tmp_test,
                                             self.ui.cBox_Test_Percentage.currentText().rstrip('%')
                                         ),
                                         QMessageBox.Ok)
                    self.ui.tableWidget_Train_Validation_Test.clearContents()
                    self.ui.tableWidget_Train_Validation_Test.setRowCount(0)
                    return

                # Train -> PureTrain, Validation
                validation_percentage = self.ui.cBox_Validation_Percentage.currentText().rstrip('%')
                validation_percentage = int(validation_percentage) / 100.0
                count_tmp_validation = math.ceil(len(file_paths_train) * validation_percentage)
                count_tmp_pure_train = len(file_paths_train) - count_tmp_validation
                if count_tmp_pure_train > 0:
                    file_paths_train, file_paths_validation = train_test_split(file_paths_train, test_size=validation_percentage)
                else:
                    dir_name = str(dir_path_obj).split(os.sep)[-1]
                    count_tmp_train = len(file_paths_train)
                    QMessageBox.critical(self, "Error PureTrain File Count.",
                                         "PureTrainデータを確保できません.\nDir:{0}, Train:{1}, PureTrain:{2}, Validation:{3}, {4}%".format(
                                             dir_name,
                                             count_tmp_train,
                                             count_tmp_pure_train,
                                             count_tmp_validation,
                                             self.ui.cBox_Validation_Percentage.currentText().rstrip('%')
                                         ),
                                         QMessageBox.Ok)
                    self.ui.tableWidget_Train_Validation_Test.clearContents()
                    self.ui.tableWidget_Train_Validation_Test.setRowCount(0)
                    return

                file_count_train = len(file_paths_train)
                file_count_validation = len(file_paths_validation)
                file_count_test = len(file_paths_test)

                # ディレクトリ名
                dir_name = str(dir_path_obj).split(os.sep)[-1]
                item_dir_name = QTableWidgetItem(dir_name)
                self.ui.tableWidget_Train_Validation_Test.setItem(row,
                                                                  self.train_validation_test_header_list.index("Category"),
                                                                  item_dir_name)

                # All File Count
                item_file_count_all = QTableWidgetItem(str(file_count))
                self.ui.tableWidget_Train_Validation_Test.setItem(row,
                                                                  self.train_validation_test_header_list.index("All"),
                                                                  item_file_count_all)

                # Train File Count
                item_file_count_train = QTableWidgetItem(str(file_count_train))
                self.ui.tableWidget_Train_Validation_Test.setItem(row,
                                                                  self.train_validation_test_header_list.index("Train"),
                                                                  item_file_count_train)

                # Validation File Count
                item_file_count_validation = QTableWidgetItem(str(file_count_validation))
                self.ui.tableWidget_Train_Validation_Test.setItem(row,
                                                                  self.train_validation_test_header_list.index("Validation"),
                                                                  item_file_count_validation)

                # test File Count
                item_file_count_test = QTableWidgetItem(str(file_count_test))
                self.ui.tableWidget_Train_Validation_Test.setItem(row,
                                                                  self.train_validation_test_header_list.index("test"),
                                                                  item_file_count_test)

                # Append
                dir_name_list.append(dir_name)
                file_paths_train_dict[dir_name] = file_paths_train
                file_paths_validation_dict[dir_name] = file_paths_validation
                file_paths_test_dict[dir_name] = file_paths_test


            """ファイルシステム上でのデータセットの構築"""
            train_dir_path_obj_list = []
            validation_dir_path_obj_list = []
            test_dir_path_obj_list = []
            for i, dir_name in enumerate(dir_name_list):
                dataset_name = dir_name + "_dataset"
                categorical_dataset_path_obj = output_dir_obj / pathlib.Path(dataset_name)
                if not categorical_dataset_path_obj.exists():
                    categorical_dataset_path_obj.mkdir()
                else:
                    # 以前に作ったファイル・ディレクトリを削除
                    for path_obj in categorical_dataset_path_obj.iterdir():
                        if path_obj.is_file():
                            path_obj.unlink()
                        if path_obj.is_dir():
                            shutil.rmtree(path_obj)

                # Gen Train Dir
                train_dir_path_obj = categorical_dataset_path_obj / pathlib.Path("train")
                train_dir_path_obj.mkdir()
                train_dir_path_obj_list.append(train_dir_path_obj)

                # Gen Validation Dir
                validation_dir_path_obj = categorical_dataset_path_obj / pathlib.Path("validation")
                validation_dir_path_obj.mkdir()
                validation_dir_path_obj_list.append(validation_dir_path_obj)

                # Gen test Dir
                test_dir_path_obj = categorical_dataset_path_obj / pathlib.Path("test")
                test_dir_path_obj.mkdir()
                test_dir_path_obj_list.append(test_dir_path_obj)

                # Copy Train Data
                for train_file_path in file_paths_train_dict[dir_name]:
                    train_file_path_obj = pathlib.Path(train_file_path)
                    filename = os.path.basename(train_file_path)
                    copied_train_file_path_obj = train_dir_path_obj / pathlib.Path(filename)
                    shutil.copyfile(src=str(train_file_path_obj), dst=str(copied_train_file_path_obj))

                # Copy Validation Data
                for validation_file_path in file_paths_validation_dict[dir_name]:
                    validation_file_path_obj = pathlib.Path(validation_file_path)
                    filename = os.path.basename(validation_file_path)
                    copied_validation_file_path_obj = validation_dir_path_obj / pathlib.Path(filename)
                    shutil.copyfile(src=str(validation_file_path_obj), dst=str(copied_validation_file_path_obj))

                # Copy test Data
                for test_file_path in file_paths_test_dict[dir_name]:
                    test_file_path_obj = pathlib.Path(test_file_path)
                    filename = os.path.basename(test_file_path)
                    copied_test_file_path_obj = test_dir_path_obj / pathlib.Path(filename)
                    shutil.copyfile(src=str(test_file_path_obj), dst=str(copied_test_file_path_obj))

            # ディレクトリチェック
            _ = QFileDialog.getOpenFileNames(self, "データ分割の成功", dir=output_dir)

    @Slot()
    def _make_meta_csv_files(self):
        """
        カテゴリー毎に分けられたTrain, Validation, Testディレクトリから
        カテゴリーを混ぜたTrain, Validation, Test用のMeta CSV ファイルを作成する
        :return:
        """
        dataset_type = self.ui.cBox_Dataset_Type.currentText()

        categorical_train_dir_paths_obj = []
        categorical_validation_dir_paths_obj = []
        categorical_test_dir_paths_obj = []

        output_dir = self.ui.lEdit_Output_Directory_Path.text()
        output_dir_obj = pathlib.Path(output_dir)
        if output_dir == "":
            QMessageBox.critical(self, "Error Meta CSV Directory",
                                 "Meta CSV ファイルを保存するディレクトリが指定されていません.",
                                 QMessageBox.Ok)
            return

        if output_dir_obj.exists():
            # カテゴリー毎に分けられたディレクトリ内にある"train", "validation", "test" ディレクトリのパスを回収
            for path_obj in output_dir_obj.iterdir():
                if path_obj.is_dir():
                    for sub_path_obj in path_obj.iterdir():
                        name = os.path.basename(str(sub_path_obj))
                        if sub_path_obj.is_dir():
                            if name == "train":
                                categorical_train_dir_paths_obj.append(sub_path_obj)
                            if name == "validation":
                                categorical_validation_dir_paths_obj.append(sub_path_obj)
                            if name == "test":
                                categorical_test_dir_paths_obj.append(sub_path_obj)


        if dataset_type.lower() == "train":

            # Train File Paths を回収
            mix_train_file_paths_obj = []
            for train_dir_path_obj in categorical_train_dir_paths_obj:
                for train_file_path_obj in train_dir_path_obj.iterdir():
                    if train_file_path_obj.is_file():
                        filename = os.path.basename(str(train_file_path_obj))
                        # ext = os.path.splitext(filename)
                        _, ext = filename.split('.')
                        if ext.lower() == "csv":
                            mix_train_file_paths_obj.append(train_file_path_obj)
                        else:
                            QMessageBox.critical(self, "Error Train's File Suffix",
                                                 "ファイル名がアノテーション済み.csvファイルではありません",
                                                 QMessageBox.Ok)
                            return

            # Meta CSV for Train を生成
            meta_csv_path_obj_train = output_dir_obj / pathlib.Path("train_meta_csv.csv")
            with open(str(meta_csv_path_obj_train), mode='w',
                      newline="") as fw:  # newline=""をしないと，csvに空行が入る
                writer = csv.writer(fw, delimiter=',')
                data_records = []
                for train_path_obj in mix_train_file_paths_obj:
                    with open(str(train_path_obj), mode='r') as fr:
                        reader = csv.reader(fr, delimiter=',')
                        col_list = next(reader)  # 1行目だけ取得
                        # print(col_list)
                        # raw_data_path = col_list[0] # 1列目: ファイルパス
                        # label = col_list[1] # 2列目: ラベル
                        data_records.append(col_list)

                writer.writerows(data_records)
            QMessageBox.information(self, "Meta CSV for Train", "train_meta_csv.csvを作成しました.", QMessageBox.Ok)

        elif dataset_type.lower() == "validation":

            # Validation File Paths を回収
            mix_validation_file_paths_obj = []
            for validation_dir_path_obj in categorical_validation_dir_paths_obj:
                for validation_file_path_obj in validation_dir_path_obj.iterdir():
                    if validation_file_path_obj.is_file():
                        filename = os.path.basename(str(validation_file_path_obj))
                        # ext = os.path.splitext(filename)
                        _, ext = filename.split('.')
                        if ext.lower() == "csv":
                            mix_validation_file_paths_obj.append(validation_file_path_obj)
                        else:
                            QMessageBox.critical(self, "Error Validation's File Suffix",
                                                 "ファイル名がアノテーション済み.csvファイルではありません",
                                                 QMessageBox.Ok)
                            return

            # Meta CSV for Validation を生成
            meta_csv_path_obj_validation = output_dir_obj / pathlib.Path("validation_meta_csv.csv")
            with open(str(meta_csv_path_obj_validation), mode='w',
                      newline="") as fw:  # newline=""をしないと，csvに空行が入る
                writer = csv.writer(fw, delimiter=',')
                data_records = []
                for validation_path_obj in mix_validation_file_paths_obj:
                    with open(str(validation_path_obj), mode='r') as fr:
                        reader = csv.reader(fr, delimiter=',')
                        col_list = next(reader)  # 1行目だけ取得
                        # print(col_list)
                        # raw_data_path = col_list[0] # 1列目: ファイルパス
                        # label = col_list[1] # 2列目: ラベル
                        data_records.append(col_list)

                writer.writerows(data_records)
            QMessageBox.information(self, "Meta CSV for Validation", "validation_meta_csv.csvを作成しました.", QMessageBox.Ok)

        else: # test

            # test File Paths を回収
            mix_test_file_paths_obj = []
            for test_dir_path_obj in categorical_test_dir_paths_obj:
                for test_file_path_obj in test_dir_path_obj.iterdir():
                    if test_file_path_obj.is_file():
                        filename = os.path.basename(str(test_file_path_obj))
                        # ext = os.path.splitext(filename)
                        _, ext = filename.split('.')
                        if ext.lower() == "csv":
                            mix_test_file_paths_obj.append(test_file_path_obj)
                        else:
                            QMessageBox.critical(self, "Error test's File Suffix",
                                                 "ファイル名がアノテーション済み.csvファイルではありません",
                                                 QMessageBox.Ok)
                            return

            # Meta CSV for test を生成
            meta_csv_path_obj_test = output_dir_obj / pathlib.Path("test_meta_csv.csv")
            with open(str(meta_csv_path_obj_test), mode='w', newline="") as fw: # newline=""をしないと，csvに空行が入る
                writer = csv.writer(fw, delimiter=',')
                data_records = []
                for test_path_obj in mix_test_file_paths_obj:
                    with open(str(test_path_obj), mode='r') as fr:
                        reader = csv.reader(fr, delimiter=',')
                        col_list = next(reader)  # 1行目だけ取得
                        # print(col_list)
                        # raw_data_path = col_list[0] # 1列目: ファイルパス
                        # label = col_list[1] # 2列目: ラベル
                        data_records.append(col_list)

                writer.writerows(data_records)
            QMessageBox.information(self, "Meta CSV for test", "test_meta_csv.csvを作成しました.", QMessageBox.Ok)
