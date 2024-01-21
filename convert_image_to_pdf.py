#!/opt/anaconda3/bin/python
# ======================================================================
# convert_image_to_pdf.py
# 画像を同じファイル名のpdfに変換する
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
import os
import img2pdf


def convert_image2pdf(indir, outdir, extension="png"):
    """convert_image2pdf 複数枚の画像を同じファイル名の複数個のpdfに変換する

    Args:
        indir (str): 変換前の画像ファイルをまとめて置いているディレクトリ
        outdir (str): pdfに変換したものをまとめて置くディレクトリ
        extension (str, optional): 変換前の拡張子(デフォルトは"png")

    注意点:
        画像とpdfの対応は1対1
        同じディレクトリの同じ拡張子であれば1枚以上に対して実行可能
        動作例: indir/1.画像 --> outdir/1.pdf, indir/2.画像 --> outdir/2.pdf
    """
    # 変換前(元の拡張子)の画像ファイルをパスなし・拡張子付きで全て取得
    images = sorted(os.listdir(indir))
    images = [name for name in images if name.split(".")[-1] in [extension]]
    # pdfをまとめて格納する出力先ディレクトリが無い場合は作成
    if os.path.isdir(outdir) is False:
        os.makedirs(outdir)
    # 画像1枚ずつに対してpdfへの変換を実施
    for i in range(len(images)):
        # 画像ファイル名(パス無し・拡張子付き)を1つ取得
        image = images[i]
        # 画像ファイル名(パス無し・拡張子無し)を1つ取得
        file_name = os.path.splitext(image)[0]
        # pdfファイル名を定義(画像ファイル名(パス無し・拡張子無し)に".pdf"を付加)
        image_pdf = file_name + ".pdf"
        # 変換前(元の拡張子)の画像ファイル(相対パス・拡張子付き)を1つ取得
        image_src = os.path.join(indir, image)
        # 変換後のpdfファイル(相対パス・拡張子付き)を1つ取得
        image_dst = os.path.join(outdir, image_pdf)
        # 画像をpdfに変換
        with open(image_dst, "wb") as f:
            f.write(img2pdf.convert(image_src))
        # どの画像がpdfに変換されたのか表示
        print("Convert: ", image_src + " --> " + image_dst)
    # 全ての画像についてpdfへの変換が終了したことを報告する
    print("Finished for all images")


# ----------------------------------------------------------------------
# "indir/ファイル名.png" を "outdir/ファイル名.pdf" に変換する
# ----------------------------------------------------------------------
indir = "./src_images/"
outdir = "./dst_images/"
convert_image2pdf(indir, outdir)
