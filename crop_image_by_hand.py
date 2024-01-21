#!/opt/anaconda3/bin/python
# ======================================================================
# crop_image_by_hand.py
# 複数枚の画像を同じ長方形の画像へ切り抜く
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
from PIL import Image
import os

# 切り抜き後の画像の領域を定義するための左上と右下の座標を格納する辞書
pixel_coordinates = {}


def crop_image_byhand(indir, outdir, pixel_coordinates, extension="png"):
    """crop_image_byhand 複数枚の画像を同じ長方形の画像へ切り抜く

    Args:
        indir (str): 切り抜き前の画像ファイルをまとめて置いているディレクトリ
        outdir (str): 切り抜き後の画像ファイルをまとめて置くディレクトリ
        pixel_coordinates (辞書{'str' : int}): 切り抜き後の左上と右下の座標
        extension (str, optional): 変換前の拡張子(デフォルトは"png")
    """
    # 圧縮後の画像をまとめて格納する出力先ディレクトリが無い場合は作成
    if os.path.isdir(outdir) is False:
        os.makedirs(outdir)
    # 変換前(元の拡張子)の画像ファイルをパスなし・拡張子付きで全て取得
    images = sorted(os.listdir(indir))
    images = [name for name in images if name.split(".")[-1] in [extension]]
    # 画像1枚ずつに対して不要な部分の切り抜き(crop)を実施
    for i in range(len(images)):
        # 画像ファイル名(パス無し・拡張子付き)を1つ取得
        image = images[i]
        # 切り抜き前の画像ファイル(相対パス・拡張子付き)を1つ取得
        image_src = os.path.join(indir, image)
        # 切り抜き後の画像ファイル(相対パス・拡張子付き)を1つ定義
        image_dst = os.path.join(outdir, image)
        # 切り抜き前の画像ファイル(相対パス・拡張子付き)をPillow(PIL)で読み込み
        image_src_PIL = Image.open(image_src)
        # 切り抜き後の画像の領域を左上と右下の座標で定義
        image_area_rectangle = (pixel_coordinates["upper left x"],
                                pixel_coordinates["upper left y"],
                                pixel_coordinates["lower right x"],
                                pixel_coordinates["lower right y"])
        # 切り抜きを実施
        image_crop_PIL = image_src_PIL.crop(image_area_rectangle)
        # 切り抜き後の画像を保存
        image_crop_PIL.save(image_dst)
        # どの画像が切り抜きされたのか表示
        print("Crop: ", image_src + " --> " + image_dst)
    # 全ての画像について切り抜きが終了したことを報告する
    print("Finished for all images")


# ----------------------------------------------------------------------
# 複数枚の画像を同じ長方形の画像へ切り抜く
# indir/画像 --> outdir/画像
# 注意：辞書のkeyは変えずに使用すること(関数内で使うため)
# ----------------------------------------------------------------------
indir = "./src_images/"
outdir = "./crp_images/"
pixel_coordinates["upper left x"] = 0
pixel_coordinates["upper left y"] = 0
pixel_coordinates["lower right x"] = 100
pixel_coordinates["lower right y"] = 100
crop_image_byhand(indir, outdir, pixel_coordinates)
