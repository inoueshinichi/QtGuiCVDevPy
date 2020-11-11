"""便利ヘルパー関数などをまとめて定義
"""

# 標準
import os
import sys
import re
import time
import datetime
from typing import Dict, List, Tuple, Union, Any

# サードパーティ
import numpy as np
from matplotlib import pyplot as plt

# 自作
cwd = os.getcwd()
ui_dir = "/".join([cwd, "ui"])
sys.path.append(ui_dir)
module_dir = "/".join([cwd, "module"])
sys.path.append(module_dir)

def new_serial_number_filename(filename:str, filename_list:List[str]) -> str:
    """
    最新の連番付きファイル名を取得
    連番の付け方: name(-番号).拡張子
    ※番号の最大値+1を新たなインデックスにするので，途中歯抜けになっている番号は無視する
    :param filename: 連番を確認するファイル名
    :param filename_list: 連番されたfilenameのリスト
    :return: 最新の連番ファイル名
    """
    pattern0 = r"^.+\..+$"
    m0 = re.match(pattern0, filename)
    if m0:
        # 拡張子付きの場合
        pattern1 = r"^(?P<name>.+)(?P<index>-[0-9]+)\.(?P<ext>.+)$"
        m1 = re.match(pattern1, filename)
        if m1:
            name = m1.group('name')
            ext = m1.group('ext')
        else:
            name, ext = filename.split('.')

        pattern2 = r"^((?P<core_name>{0})|(?P<name_with_index>{0}-[0-9]+))\..+$".format(name)
        count = 0
        index_list = []
        for serial_number_name in filename_list:
            m2 = re.match(pattern2, serial_number_name)
            if m2:
                count += 1
                name_with_index = m2.group('name_with_index')
                if name_with_index:
                    index = int(serial_number_name.split('-')[-1].split('.')[0])
                    index_list.append(index)

        if count > 0:
            if len(index_list) > 0:
                index_max = max(index_list)
                last_filename = name + "-" + str(index_max + 1) + "." + ext
            else:
                last_filename = name + "-" + str(count) + "." + ext
        else:
            last_filename = filename

    else:
        # 拡張子がない場合
        pattern3 = r"^(?P<name>.+)(?P<index>-[0-9]+)$"
        m3 = re.match(pattern3, filename)
        if m3:
            name = m3.group('name')
        else:
            name = filename

        pattern4 = r"^((?P<core_name>{0})|(?P<name_with_index>{0}-[0-9]+))$".format(name)
        count = 0
        index_list = []
        for serial_number_name in filename_list:
            m4 = re.match(pattern4, serial_number_name)
            if m4:
                count += 1
                name_with_index = m4.group('name_with_index')
                if name_with_index:
                    index = int(serial_number_name.split('-')[-1].split('.')[0])
                    index_list.append(index)

        if count > 0:
            if len(index_list) > 0:
                index_max = max(index_list)
                last_filename = name + "-" + str(index_max + 1)
            else:
                last_filename = name + "-" + str(count)
        else:
            last_filename = filename

    return last_filename