"""データの前処理
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

# 自作
cwd = os.getcwd()
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

from module.mldl.dl.data_argmentation import (
    image_argmentation
)

"""
OK 画像用前処理
-- 時系列用前処理
-- 
"""



class ImagePreprocessing():
    """
    1枚画像用前処理クラス
    """

    def __init__(self, input_image_size: Tuple[int,int], train_desc:str, validation_desc:str, test_desc:str):
        """
        前処理.
        前処理の内容は文字列で渡して，eval()関数を用いて実体化させる.
        前処理の記述は, Pytorchの前処理に基づく.
        :param input_image_size:
        :param train_desc:      トレーニングデータに対する前処理の記述(str).
        :param validation_desc: 検証データに対する前処理の記述(str)
        :param test_desc:       テストデータに対する前処理の記述(str)
        """
        self.data_preprocessing = {
            'train': transforms.Compose([*eval(train_desc)]), # 注意) eval(str)がタプルを返すので*でアンパックする
            'validation': transforms.Compose([*eval(validation_desc)]),
            'test': transforms.Compose([*eval(test_desc)])
        }

        """
        i.e
        self.data_preprocessing = {
            'train': transforms.Compose([
                transforms.Lambda(lambda gray_img: gray_img.convert('RGB')),
                transforms.Resize(size=input_image_size, interpolation=Image.BILINEAR),  # PIL形式(h, w, c)をリサイズ
                # transforms.RandomVerticalFlip(),                # ランダムに垂直フリップ
                transforms.ToTensor(),                            # テンソル形式に変換
                transforms.Lambda(lambda tensor: tensor / 255.0)  # 0-1に正規化
            ]),
            'val': transforms.Compose([
                transforms.Lambda(lambda gray_img: gray_img.convert('RGB')),
                transforms.Resize(size=input_image_size, interpolation=Image.BILINEAR),  # PIL形式(h, w, c)をリサイズ
                transforms.ToTensor(),
                transforms.Lambda(lambda tensor: tensor / 255.0)
            ]),
            'test': transforms.Compose([
                transforms.Lambda(lambda gray_img: gray_img.convert('RGB')),
                transforms.Resize(size=input_image_size, interpolation=Image.BILINEAR),  # PIL形式(h, w, c)をリサイズ
                transforms.ToTensor(),
                transforms.Lambda(lambda tensor: tensor / 255.0)
            ])
        }
        """

    def __call__(self, image, phase):
        """
        前処理を実行.
        :param image:
        :param phase:
        :return:
        """
        return self.data_preprocessing[phase](image)

