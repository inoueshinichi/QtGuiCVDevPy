"""学習済みモデルの関数群
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

def load_vgg16_for_ILSVRC2013(last_layer_num: int, learning_type: str) -> Tuple[Any, Any, str]:
    """
    ILSVRC2013 で学習されたVgg16モデルを読み込む
    :return: Tuple[Any, Any, str]
    Any(1): ネットワークモデル
    Any(2): 学習を行う
    """

    # "Transfer Learning" or "Fine Tuning" or "Full Learning"
    use_pretrained = None
    if learning_type == "full learning":
        use_pretrained = False
    else:
        use_pretrained = True

    # 学習済みモデルの読み込み
    vgg16_net = models.vgg16(pretrained=use_pretrained)
    # モデル構成を表示
    print("VGG16 trained ILSVRC2013: ", vgg16_net)
    # 解きたい問題に合わせて出力層のニューロン数を変更
    vgg16_net.classifier[6] = nn.Linear(in_features=4096, out_features=last_layer_num)
    # 修正部分のモデル構成
    print("最終出力層の付け替え完了: ", vgg16_net.classifier[6])


    # "Transfer Learning"で学習させるパラメータをparams_to_updateに格納する
    params_to_update = []
    if learning_type == "transfer learning":
        # 学習させるパラメータ名
        update_param_names = ["classifier.6.weight", "classifier.6.bias"]
        # 学習させるパラメータ以外は勾配計算をなくし、変化しないように設定
        for name, param in vgg16_net.named_parameters():
            if name in update_param_names:
                param.requires_grad = True
                params_to_update.append(param)
                print(name)
            else:
                param.requires_grad = False

        # params_to_updateの中身を確認
        print('-------------------')
        print(params_to_update)
    else:
        # 全パラメータの学習
        for name, param in vgg16_net.named_parameters():
            param.requires_grad = True
            params_to_update.append(param)

    return vgg16_net, params_to_update, str(vgg16_net)