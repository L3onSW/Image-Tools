#!/opt/anaconda3/bin/python
# ======================================================================
# add_margin_around_image.py
# 画像の周囲(上下左右)に余白を付加する
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
from PIL import Image
import os

# 白色のRGB
white_rgb = (255, 255, 255)
# 黒色のRGB
black_rgb = (0, 0, 0)

# 周囲(上下左右)に余白を付加する(True)または付加しない(False)を格納する辞書
margin = {}
# 周囲(上下左右)に付加する余白のサイズを格納する辞書(デフォルトの値は関数内に表記)
margin_size = {}


def add_margin_around_image(indir, outdir, margin=None,
                            extension="png", margin_size=None):
    """add_margin_around_image _summary_

    Args:
        indir (str): 余白を付加したい画像をまとめて置いているディレクトリ
        outdir (str): 余白を付加した画像をまとめて置くディレクトリ
        margin (dict, optional): 各方向(上下左右)に余白を付加するかどうか，デフォルトはTrue.
        extension (str, optional): 画像ファイルの拡張子，デフォルトは"png".
        margin_size (dict, optional): 各方向(上下左右)の余白の大きさ，デフォルトは全方向10.
    """
    # 上下左右に余白を付加するかどうかが定義されていない場合は，
    # 上下左右すべてに余白を付加する設定にする
    if margin is None:
        margin = {}
        margin["top"] = True
        margin["bottom"] = True
        margin["left"] = True
        margin["right"] = True
    # 上下左右の余白のサイズが定義されていない場合は定義する
    # なおここの値はあまりいじらないように思うのでハードコーディングで済ます
    if margin_size is None:
        margin_size = {}
        margin_size["top"] = 10
        margin_size["bottom"] = 10
        margin_size["left"] = 10
        margin_size["right"] = 10
    # 合体後の画像をまとめて格納する出力先ディレクトリが無い場合は作成
    if os.path.isdir(outdir) is False:
        os.makedirs(outdir)
    # 変換前(元の拡張子)の画像ファイルをパスなし・拡張子付きで全て取得
    images = sorted(os.listdir(indir))
    images = [name for name in images if name.split(".")[-1] in [extension]]
    # 画像1枚ずつに対して周囲(上下左右)に余白を付加する
    for i in range(len(images)):
        # 結果を見やすくするための区切り線の表示
        print("-" * 70)
        # 画像ファイル名(パス無し・拡張子付き)を1つ取得
        image = images[i]
        # 画像ファイル(相対パス・拡張子付き)を1つ取得
        image_src = os.path.join(indir, image)
        print(image_src)
        # 余白付加後の画像ファイル(相対パス・拡張子付き)を1つ定義
        image_dst = os.path.join(outdir, image)
        # 画像ファイル(相対パス・拡張子付き)をPillow(PIL)で読み込み
        image_src_PIL = Image.open(image_src)
        # 余白を付加するための画像を元の画像そのままをコピーして作成する
        image_dst_PIL = image_src_PIL.copy()
        image_dst_PIL.save(image_dst)
        # 周囲(上下左右)の必要な箇所に余白を付加
        # --------------------------------------------------------------
        # 上に余白を付加
        # --------------------------------------------------------------
        if margin["top"] is True:
            # 画像ファイル(相対パス・拡張子付き)を1つ取得
            image_src_PIL = Image.open(image_dst)
            # 余白付加後の幅と高さを定義
            width = image_src_PIL.width
            height = image_src_PIL.height + margin_size["top"]
            # 余白の色を定義
            color = white_rgb
            # 上に余白を付加した画像を生成(余白の色の画像に元の画像を貼り付けて生成する)
            top_margin_combined = Image.new('RGB', (width, height), color)
            coordinate = (0, margin_size["top"])
            top_margin_combined.paste(image_src_PIL, coordinate)
            top_margin_combined.save(image_dst)
            # 上に余白を付加したことを報告
            print("Add top margin")
        # --------------------------------------------------------------
        # 下に余白を付加
        # --------------------------------------------------------------
        if margin["bottom"] is True:
            # 画像ファイル(相対パス・拡張子付き)を1つ取得
            image_src_PIL = Image.open(image_dst)
            # 余白付加後の幅と高さを定義
            width = image_src_PIL.width
            height = image_src_PIL.height + margin_size["bottom"]
            # 余白の色を定義
            color = white_rgb
            # 下に余白を付加した画像を生成(余白の色の画像に元の画像を貼り付けて生成する)
            bottom_margin_combined = Image.new('RGB', (width, height), color)
            coordinate = (0, 0)
            bottom_margin_combined.paste(image_src_PIL, coordinate)
            bottom_margin_combined.save(image_dst)
            # 下に余白を付加したことを報告
            print("Add bottom margin")
        # --------------------------------------------------------------
        # 左に余白を付加
        # --------------------------------------------------------------
        if margin["left"] is True:
            # 画像ファイル(相対パス・拡張子付き)を1つ取得
            image_src_PIL = Image.open(image_dst)
            # 余白付加後の幅と高さを定義
            width = image_src_PIL.width + margin_size["left"]
            height = image_src_PIL.height
            # 余白の色を定義
            color = white_rgb
            # 左に余白を付加した画像を生成(余白の色の画像に元の画像を貼り付けて生成する)
            left_margin_combined = Image.new('RGB', (width, height), color)
            coordinate = (margin_size["left"], 0)
            left_margin_combined.paste(image_src_PIL, coordinate)
            left_margin_combined.save(image_dst)
            # 左に余白を付加したことを報告
            print("Add left margin")
        # --------------------------------------------------------------
        # 右に余白を付加
        # --------------------------------------------------------------
        if margin["right"] is True:
            # 画像ファイル(相対パス・拡張子付き)を1つ取得
            image_src_PIL = Image.open(image_dst)
            # 余白付加後の幅と高さを定義
            width = image_src_PIL.width + margin_size["right"]
            height = image_src_PIL.height
            # 余白の色を定義
            color = white_rgb
            # 右に余白を付加した画像を生成(余白の色の画像に元の画像を貼り付けて生成する)
            right_margin_combined = Image.new('RGB', (width, height), color)
            coordinate = (0, 0)
            right_margin_combined.paste(image_src_PIL, coordinate)
            right_margin_combined.save(image_dst)
            # 右に余白を付加したことを報告
            print("Add right margin")
        # どの画像に余白が付加されたのか表示
        print("Add margin: ", image_src + " --> " + image_dst)
    # 結果を見やすくするための区切り線の表示
    print("-" * 70)
    # 全ての画像について余白の付加が終了したことを報告する
    print("Finished for all images")


# ----------------------------------------------------------------------
# 画像の周囲(上下左右)に余白を付加する
# ----------------------------------------------------------------------
indir = "./src_images/"
outdir = "./mgn_images/"
margin["top"] = True
margin["bottom"] = True
margin["left"] = True
margin["right"] = True
add_margin_around_image(indir, outdir, margin)
