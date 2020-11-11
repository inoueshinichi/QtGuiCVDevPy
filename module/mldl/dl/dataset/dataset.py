"""
データセット作成に関する関数群
"""

# 標準
import os
import shutil
import pathlib
import csv
import re
from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Any,
    NoReturn,
    Generic,
    Callable,
    TypeVar
)

# サードパーティ
import numpy as np


# 自作



"""
OK labeling_dataset
-- make_meta_csv_dataset
"""

def labeling_dataset(raw_data_dir: str, labeled_csv_dir: str, label: str, encoding: str = "utf-8")\
        -> Tuple[Union[int, None], Union[List[str], None]]:
    """
    指定したディレクトリにある生データからラベル付けしたcsvデータを指定のディレクトリに作成
    :param raw_data_dir: 生データ(.BMP, .CSVなど)を保存しているディレクトリ
    :param labeled_csv_dir: ラベル付けしたcsvデータ(.csv)を保存するディレクトリ
    :param label: ラベル('0', '1' or 'OK', 'NG')
    :return:
    """
    data_dir_obj = pathlib.Path(raw_data_dir)
    csv_dir_obj = pathlib.Path(labeled_csv_dir)

    if data_dir_obj.is_dir() and csv_dir_obj.is_dir():
        file_paths = [str(path_obj) for path_obj in data_dir_obj.iterdir()
                      if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

        if not file_paths:
            return None, None

        csv_paths = [str(path_obj) for path_obj in csv_dir_obj.iterdir()
                      if path_obj.is_file() and not str(path_obj).split(os.sep)[-1].startswith('.')]

        if csv_paths:
            # ファイルの削除(ディレクトリは消さない)
            for exist_path in csv_paths:
                os.remove(exist_path)
            """以下，ディレクトリの削除と生成に関して，
               shutil.rmtree()を行った直後に
               Windowsではmkdir()のタイミングで[WinError 5]が発生し，
               ディレクトリの作成に失敗することがある。
            """
            # # 中身のあるディレクトリごと削除
            # shutil.rmtree(csv_dir_obj)
            # # ディレクトリの作成
            # csv_dir_obj.mkdir()

        file_count = 0
        for path in file_paths:
            filename = path.split(os.sep)[-1]
            name, ext = filename.split('.')
            csv_path_obj = csv_dir_obj / pathlib.Path(name + ".csv")

            with csv_path_obj.open(mode='w', encoding=encoding) as f:
                writer = csv.writer(f)
                writer.writerow([path, label])
                file_count += 1
                csv_paths.append(str(csv_path_obj))

        return file_count, csv_paths

    else:
        return None, None


if __name__ == "__main__":
    raw_data_dir = "C:\\Users\\井上真一\\Desktop\\test_csv\\raw_data"
    csv_data_dir = "C:\\Users\\井上真一\\Desktop\\test_csv\\csv_data"

    count = labeling_dataset(raw_data_dir, csv_data_dir, label="1", encoding='shift-jis')