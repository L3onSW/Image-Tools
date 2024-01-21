#!/opt/anaconda3/bin/python
# ======================================================================
# compress_image.py
# 画像のサイズを小さくしつつ品質も変更することで圧縮する
# 注意：当然だが画質が悪くなる！！
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
import os
from PIL import Image


def compress_image(indir, outdir, shrink, quality, extension="png"):
    """compress_image 複数枚の画像のサイズを小さくしつつ品質も変更することで圧縮する

    Args:
        indir (str): 圧縮前の画像ファイルをまとめて置いているディレクトリ
        outdir (str): 圧縮後の画像ファイルをまとめて置くディレクトリ
        shrink (int): 何倍に縮小するかを定義(3だと1/3のサイズに縮小する)
        quality (int): 圧縮後の品質
        extension (str, optional): 変換前の拡張子(デフォルトは"png")

    注意点:
        圧縮前の画像と圧縮後の対応は1対1
        同じディレクトリの同じ拡張子であれば1枚以上に対して実行可能
        動作例: indir/1.画像 --> outdir/1.画像, indir/2.画像 --> outdir/2.画像
    """
    # 変換前(元の拡張子)の画像ファイルをパスなし・拡張子付きで全て取得
    images = sorted(os.listdir(indir))
    images = [name for name in images if name.split(".")[-1] in [extension]]
    # 圧縮後の画像をまとめて格納する出力先ディレクトリが無い場合は作成
    if os.path.isdir(outdir) is False:
        os.makedirs(outdir)
    # 画像1枚ずつに対して圧縮を実施
    for i in range(len(images)):
        # 画像ファイル名(パス無し・拡張子付き)を1つ取得
        image = images[i]
        # 圧縮前の画像ファイル(相対パス・拡張子付き)を1つ取得
        image_src = os.path.join(indir, image)
        # 圧縮後の画像ファイル(相対パス・拡張子付き)を1つ定義
        image_dst = os.path.join(outdir, image)
        # 圧縮前の画像ファイル(相対パス・拡張子付き)をPillow(PIL)で読み込み
        image_src_PIL = Image.open(image_src)
        # 幅(w:width)と高さ(h:height)を取得
        w, h = image_src_PIL.size
        # 縮小(shrink)した幅(w:width)縮小した高さ(h:height)を定義
        w_shrink = w // shrink
        h_shrink = h // shrink
        # 画像サイズを縮小(shrink)した幅(w:width)縮小した高さ(h:height)に縮小
        image_shrink_PIL = image_src_PIL.resize((w_shrink, h_shrink))
        # 縮小した画像をqualityの質で保存
        image_shrink_PIL.save(image_dst, quality=quality, optimize=True)
        # どの画像が圧縮されたのか表示
        print("Compress: ", image_src + " --> " + image_dst)
    # 全ての画像について圧縮が終了したことを報告する
    print("Finished for all images")


# ----------------------------------------------------------------------
# サイズを1/6に縮小し,保存する画像の品質を50にする
# indir/画像 --> outdir/画像
# 注意：画質悪くなるのでパラメータの値は調整が必要...
# ----------------------------------------------------------------------
shrink = 6
quality = 50
indir = "./src_images/"
outdir = "./cmp_images/"
compress_image(indir, outdir, shrink, quality)
