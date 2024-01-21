#!/opt/anaconda3/bin/python
# ======================================================================
# print_image_size.py
# 複数枚の画像サイズ(幅と高さ)とファイルサイズをターミナル上に表示する
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
from PIL import Image
import os
import sys


def print_image_size(indir, extension="png", unit="MB"):
    """crop_image_byhand 複数枚の画像サイズ(幅と高さ)とファイルサイズを表示する

    Args:
        indir (str): サイズを表示したい画像ファイルをまとめて置いているディレクトリ
        extension (str, optional): 変換前の拡張子(デフォルトは"png")
        unit (str, optional): 表示するファイルサイズの単位(デフォルトは"MB")
    """
    # 変換前(元の拡張子)の画像ファイルをパスなし・拡張子付きで全て取得
    images = sorted(os.listdir(indir))
    images = [name for name in images if name.split(".")[-1] in [extension]]
    # 画像1枚ずつに対して不要な部分の切り抜き(crop)を実施
    for i in range(len(images)):
        # 結果を見やすくするための区切り線の表示
        print("-" * 70)
        # 画像ファイル名(パス無し・拡張子付き)を1つ取得
        image = images[i]
        # 画像ファイル(相対パス・拡張子付き)を1つ取得
        image_src = os.path.join(indir, image)
        print(image_src)
        # 画像ファイル(相対パス・拡張子付き)をPillow(PIL)で読み込み
        image_PIL = Image.open(image_src)
        w, h = image_PIL.size
        print(" width:", w, end=", ")
        print(" height:", h)
        # 画像ファイルのファイルサイズ(Byte)を取得
        image_file_size_byte = os.path.getsize(image_src)
        if unit == "B":
            # 単位B(Byte)で表示
            print(f" {image_file_size_byte} B")
        elif unit == "KB":
            # 単位B(Byte)をKBに変換(小数点以下2位で四捨五入)してから表示
            image_file_size_KB = round(image_file_size_byte / 1024, 2)
            print(f" {image_file_size_KB} KB")
        elif unit == "MB":
            # 単位B(Byte)をMBに変換(小数点以下2位で四捨五入)してから表示
            image_file_size_MB = round(image_file_size_byte / (1024**2), 2)
            print(f" {image_file_size_MB} MB")
        elif unit == "GB":
            # 単位B(Byte)をGBに変換(小数点以下2位で四捨五入)してから表示
            image_file_size_GB = round(image_file_size_byte / (1024**3), 2)
            print(f" {image_file_size_GB} GB")
        else:
            # 変数unitの指定が間違っている場合は異常終了
            print(" Please set the variable ", end="")
            print("\"unit\" to \"B\", \"KB\", \"MB\", or \"GB\".")
            sys.exit(1)


# ----------------------------------------------------------------------
# 複数枚の画像サイズ(幅と高さ)とファイルサイズをターミナル上に表示する
# ----------------------------------------------------------------------
indir = "./src_images/"
print_image_size(indir)
