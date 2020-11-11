"""Pytorch用のデータセット
"""

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


"""
-- ファイルセット作成関数
-- データセット作成関数
-- データローダー作成関数
-- 1枚画像用データセット
-- 時系列用データセット
-- 物体検出用データセット
-- セマンティックセグメンテーション用データセット
-- 
"""

def make_filepath_for_pytorch(meta_csv_path:str, phase:str='train', encoding:str='utf-8') \
        -> Union[Dict[str, List[Any]], None]:
    """
    meta_csvに記述してあるファイルパスを抽出してファイルパスのリストを作成
    :param meta_csv_path:
    :param header:
    :param phase:
    :return:
    """
    try:
        # Meta-CSVファイルの読み込み
        meta_csv_df = pd.read_csv(meta_csv_path, sep=',', header=None, encoding=encoding) # None: ヘッダなし, 数値: ヘッダの行番号
        # record: 0:index, 1:path, 2:label

        # 各行のデータをリストに入れる
        index_list = []
        path_list = []
        label_list = []
        for record in meta_csv_df.itertuples(name=None):
            # 行番号
            index_list.append(record[0])

            # ファイルパス
            file_path_obj = pathlib.Path(record[1])
            path_list.append(str(file_path_obj)) # 区切り文字がOSによって自動的に変換される. Win32:\\, macOS:/, Linux:/

            # ラベル
            if phase == 'train' or phase == 'validation':
                label_list.append(record[2])

        data_dict = {"index": index_list, "path": path_list, "label": label_list}

    except BaseException as e:
        print("Meta-CSVファイルの読み込みに失敗しました.")
        print(e)
        data_dict = None

    return data_dict



def make_dataset_for_pytorch(pytorch_dataset_klass:Any, preprocessing:Any, meta_csv_train_path:str,\
                             meta_csv_validation_path:str, encoding:str)\
        -> Dict[str, Any]:
    """
    Pytorch用データセットを作成
    :param pytorch_dataset_klass:
    :param preprocessing:
    :param meta_csv_train_path:
    :param train_header_row:
    :param meta_csv_validation_path:
    :param validation_header_row:
    :return:
    """
    # make file path list
    train_dict = make_filepath_for_pytorch(meta_csv_path=meta_csv_train_path, phase='train', encoding=encoding)
    validation_dict = make_filepath_for_pytorch(meta_csv_path=meta_csv_validation_path, phase='validation', encoding=encoding)
    print("train_num: {}, validation_num: {}".format(len(train_dict["index"]), len(validation_dict['index'])))

    # make Dataset
    train_dataset = pytorch_dataset_klass(file_list=train_dict['path'],
                                          label_list=train_dict['label'],
                                          preprocessing=preprocessing,
                                          phase='train')
    validation_dataset = pytorch_dataset_klass(file_list=validation_dict['path'],
                                               label_list=validation_dict['label'],
                                               preprocessing=preprocessing,
                                               phase='validation')
    print("train_dataset: {}, validation_dataset: {}".format(type(train_dataset), type(validation_dataset)))

    dataset_dict = {'train': train_dataset, 'validation': validation_dataset}
    return dataset_dict


def make_dataloader_for_pytorch(batch_size:int, train_dataset:Any, validation_dataset:Any) -> Dict[str, Any]:
    """
    Pytorch用のデータローダーを作成.
    :param batch_size:
    :param train_dataset:
    :param validation_dataset:
    :return:
    """
    # train
    train_dataloader = data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    # validation
    validation_dataloader = data.DataLoader(dataset=validation_dataset, batch_size=batch_size, shuffle=False)

    dataloader_dict = {"train": train_dataloader, "validation": validation_dataloader}
    return dataloader_dict


class OneImageDataset(data.Dataset):

    def __init__(self, file_list:List[str], label_list:List[int], preprocessing:Any=None, phase:str='train'):
        """
        Pytorchデータセット作成に必要なパラメータを設定
        :param file_list:
        :param label_list:
        :param preprocessing:
        :param phase: 'train', 'validation', 'test'
        """
        self.file_list = file_list  # ファイルパス
        self.label_list = label_list  # ラベルパス
        self.preprocessing = preprocessing  # 前処理クラス
        self.phase = phase  # フェイズ

    def __len__(self) -> int:
        """
        Datasetの派生クラスに必要な関数(1)
        ファイル数を返す.
        :return:
        """
        return len(self.file_list)

    def __getitem__(self, item_index) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Datasetの派生クラスに必要な関数(2)
        :param item:
        :return:
        """
        # 画像ファイルを記憶デバイスから読み込む
        img_load = Image.open(self.file_list[item_index])

        # 前処理
        img_preprocess_tensor = self.preprocessing(img_load, self.phase)

        # ラベルの取得
        label_tensor = torch.tensor(self.label_list[item_index], dtype=torch.long)

        return img_preprocess_tensor, label_tensor

