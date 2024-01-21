#!/opt/anaconda3/bin/python
# ======================================================================
# combine_2_images_into_1_image.py
# 2枚の画像を合体させて1枚の画像を生成する
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
from PIL import Image
import os

# 白色のRGB
white_rgb = (255, 255, 255)
# 黒色のRGB
black_rgb = (0, 0, 0)


def combine_horizontally(image_left, image_right, dir_out, image_out,
                         debug=False):
    """combine_horizontally 横方向に2枚の画像を合体させた1枚の画像を生成する

    Args:
        image_left (str): 合体させる2枚の画像のうち左側
        image_right (str): 合体させる2枚の画像のうち右側
        dir_out (str): 2枚の画像を合体させて生成した1枚の画像を置くディレクトリ
        image_out (str): 2枚の画像を合体させて生成した1枚の画像のファイル名
        debug (bool, optional): debug用中間ファイルの生成(デフォルトはFalse)

    注意点:
        サイズが異なる場合には，小さい方に余白を追加して対応している
    """
    # 合体後の画像をまとめて格納する出力先ディレクトリが無い場合は作成
    if os.path.isdir(dir_out) is False:
        os.makedirs(dir_out)
    # 左右の画像ファイル(相対パス・拡張子付き)をPillow(PIL)で読み込み
    left = Image.open(image_left)
    right = Image.open(image_right)
    # ------------------------------------------------------------------
    # 横方向(左右)に2枚の画像を合体させた1枚の画像を生成する
    # ------------------------------------------------------------------
    # 横方向の合体によりできる新しい画像は，
    # 左の画像に右の画像を合体させて作るので，
    # 幅：左の画像の幅+右の画像の幅
    # 高さ：左の画像の高さ
    # となる．
    # このとき，高さを前もって合わせないとはみ出す箇所が除去された画像になってしまうため，
    # 高さを合わせてから合体させることが必要であり，
    # "左の画像の高さ == 右の画像の高さ"の場合には，そのまま合体
    # "左の画像の高さ > 右の画像の高さ"の場合には，右の画像の上下に余白を追加してから合体
    # "左の画像の高さ < 右の画像の高さ"の場合には，左の画像の上下に余白を追加してから合体
    # という操作の場合分けをしている．
    # ------------------------------------------------------------------
    if left.height == right.height:
        # --------------------------------------------------------------
        # "左の画像の高さ == 右の画像の高さ"の場合には，そのまま合体
        # --------------------------------------------------------------
        image_combined = \
            Image.new('RGB', (left.width + right.width, left.height))
        image_combined.paste(left, (0, 0))
        image_combined.paste(right, (left.width, 0))
        image_combined.save(dir_out + image_out)
    elif left.height > right.height:
        # --------------------------------------------------------------
        # "左の画像の高さ > 右の画像の高さ"の場合には，右の画像の上下に余白を追加してから合体
        # --------------------------------------------------------------
        right_resized_size = (right.width, left.height)
        right_resized_color = white_rgb
        right_resized = \
            Image.new('RGB', right_resized_size, right_resized_color)
        if debug is True:
            right_resized.save(dir_out + "right_background.png")
        coordinate = (0, (left.height - right.height) // 2)
        right_resized.paste(right, coordinate)
        if debug is True:
            right_resized.save(dir_out + "right_resized.png")
        image_combined = \
            Image.new('RGB', (left.width + right.width, left.height))
        image_combined.paste(left, (0, 0))
        image_combined.paste(right_resized, (left.width, 0))
        image_combined.save(dir_out + image_out)
    elif left.height < right.height:
        # --------------------------------------------------------------
        # "左の画像の高さ < 右の画像の高さ"の場合には，左の画像の上下に余白を追加してから合体
        # --------------------------------------------------------------
        left_resized_size = (left.width, right.height)
        left_resized_color = white_rgb
        left_resized = \
            Image.new('RGB', left_resized_size, left_resized_color)
        if debug is True:
            left_resized.save(dir_out + "left_background.png")
        coordinate = (0, (right.height - left.height) // 2)
        left_resized.paste(left, coordinate)
        if debug is True:
            left_resized.save(dir_out + "left_resized.png")
        image_combined = \
            Image.new('RGB', (left.width + right.width, left_resized.height))
        image_combined.paste(left_resized, (0, 0))
        image_combined.paste(right, (left.width, 0))
        image_combined.save(dir_out + image_out)
    # 横方向の合体が終了したことを報告する
    print(image_left + " + " + image_right + " --> " + dir_out + image_out)
    print("To combine horizontally is done")


def combine_vertically(image_top, image_bottom, dir_out, image_out,
                       debug=False):
    """combine_vertically 縦方向に2枚の画像を合体させた1枚の画像を生成する

    Args:
        image_top (str): 合体させる2枚の画像のうち上側
        image_bottom (str): 合体させる2枚の画像のうち下側
        dir_out (str): 2枚の画像を合体させて生成した1枚の画像を置くディレクトリ
        image_out (str): 2枚の画像を合体させて生成した1枚の画像のファイル名
        debug (bool, optional): debug用中間ファイルの生成(デフォルトはFalse)

    注意点:
        サイズが異なる場合には，小さい方に余白を追加して対応している
    """
    # 合体後の画像をまとめて格納する出力先ディレクトリが無い場合は作成
    if os.path.isdir(dir_out) is False:
        os.makedirs(dir_out)
    # 上下の画像ファイル(相対パス・拡張子付き)をPillow(PIL)で読み込み
    top = Image.open(image_top)
    bottom = Image.open(image_bottom)
    # ------------------------------------------------------------------
    # 縦方向(上下)に2枚の画像を合体させた1枚の画像を生成する
    # ------------------------------------------------------------------
    # 縦方向の合体によりできる新しい画像は，
    # 上の画像に下の画像を合体させて作るので，
    # 幅：上の画像の幅
    # 高さ：上の画像の高さ+下の画像の高さ
    # となる．
    # このとき，幅を前もって合わせないとはみ出す箇所が除去された画像になってしまうため，
    # 幅を合わせてから合体させることが必要であり，
    # "上の画像の幅 == 下の画像の高さ"の場合には，そのまま合体
    # "上の画像の幅 > 下の画像の高さ"の場合には，下の画像の左右に余白を追加してから合体
    # "上の画像の幅 < 下の画像の高さ"の場合には，上の画像の左右に余白を追加してから合体
    # という操作の場合分けをしている．
    # ------------------------------------------------------------------
    if top.width == bottom.width:
        # --------------------------------------------------------------
        # "上の画像の幅 == 下の画像の高さ"の場合には，そのまま合体
        # --------------------------------------------------------------
        image_combined = \
            Image.new('RGB', (top.width, top.height + bottom.height))
        image_combined.paste(top, (0, 0))
        image_combined.paste(bottom, (0, top.height))
        image_combined.save(dir_out + image_out)
    elif top.width > bottom.width:
        # --------------------------------------------------------------
        # "上の画像の幅 > 下の画像の高さ"の場合には，下の画像の左右に余白を追加してから合体
        # --------------------------------------------------------------
        bottom_resized_size = (top.width, bottom.height)
        bottom_resized_color = white_rgb
        bottom_resized = \
            Image.new('RGB', bottom_resized_size, bottom_resized_color)
        if debug is True:
            bottom_resized.save(dir_out + "bottom_background.png")
        coordinate = ((top.width - bottom.width) // 2, 0)
        bottom_resized.paste(bottom, coordinate)
        if debug is True:
            bottom_resized.save(dir_out + "bottom_resized.png")
        image_combined = \
            Image.new('RGB', (top.width, top.height + bottom.height))
        image_combined.paste(top, (0, 0))
        image_combined.paste(bottom_resized, (0, top.height))
        image_combined.save(dir_out + image_out)
    elif top.width < bottom.width:
        # --------------------------------------------------------------
        # "上の画像の幅 < 下の画像の高さ"の場合には，上の画像の左右に余白を追加してから合体
        # --------------------------------------------------------------
        top_resized_size = (bottom.width, top.height)
        top_resized_color = white_rgb
        top_resized = \
            Image.new('RGB', top_resized_size, top_resized_color)
        if debug is True:
            top_resized.save(dir_out + "top_background.png")
        coordinate = ((bottom.width - top.width) // 2, 0)
        top_resized.paste(top, coordinate)
        if debug is True:
            top_resized.save(dir_out + "top_resized.png")
        image_combined = \
            Image.new('RGB', (top_resized.width, top.height + bottom.height))
        image_combined.paste(top_resized, (0, 0))
        image_combined.paste(bottom, (0, top.height))
        image_combined.save(dir_out + image_out)
    # 縦方向の合体が終了したことを報告する
    print(image_top + " + " + image_bottom + " --> " + dir_out + image_out)
    print("To combine vertically is done")


# ----------------------------------------------------------------------
# 横方向(左右)に2枚の画像を合体させて1枚の画像を生成する
# ----------------------------------------------------------------------
# image_left (str): 合体させる2枚の画像のうち左側
# image_right (str): 合体させる2枚の画像のうち右側
# dir_out (str): 2枚の画像を合体させて生成した1枚の画像を置くディレクトリ
# image_out (str): 2枚の画像を合体させて生成した1枚の画像のファイル名
# debug (bool, optional): debug用中間ファイルの生成(デフォルトはFalse)
# ----------------------------------------------------------------------
image_left = "./src_images/1.png"
image_right = "./src_images/2.png"
dir_out = "./cmb_images/"
image_out = "combine_horizontally.png"
combine_horizontally(image_left, image_right, dir_out, image_out)


# ----------------------------------------------------------------------
# 縦方向(上下)に2枚の画像を合体させて1枚の画像を生成する
# ----------------------------------------------------------------------
# image_top (str): 合体させる2枚の画像のうち上側
# image_bottom (str): 合体させる2枚の画像のうち下側
# dir_out (str): 2枚の画像を合体させて生成した1枚の画像を置くディレクトリ
# image_out (str): 2枚の画像を合体させて生成した1枚の画像のファイル名
# debug (bool, optional): debug用中間ファイルの生成(デフォルトはFalse)
# ----------------------------------------------------------------------
image_top = "./src_images/1.png"
image_bottom = "./src_images/2.png"
dir_out = "./cmb_images/"
image_out = "combine_vertically.png"
combine_vertically(image_top, image_bottom, dir_out, image_out)
