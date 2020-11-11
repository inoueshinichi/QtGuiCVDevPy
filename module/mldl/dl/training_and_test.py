"""学習過程, テスト過程
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

def training_network_model(device_type: Any, network_model: Any, dataloader_dict: Dict,
                           criterion_loss: Any, optimizer: Any, params: List[Any]):
    """
    ネットワークモデルの学習
    :param device_type:
    :param network_model:
    :param dataloader_dict:
    :param criterion_loss:
    :param optimizer:
    :param params:
    :return:
    """
    pass

