<!-- 後に利用・活用する自分のためにも"後から見て分かる記録"をREADMEに書く -->

<!-- ここから本文 -->
# Image-Tools
- 画像を扱う際に役に立つかもしれないソースコード集です．
- [![python-shield]][python-url]で書かれています．
<!-- 表にした方が瞬時に概要を把握できるが手間がかかりすぎるのでしない -->

## [**add_margin_around_image.py**][add_margin_around_image.py-url]
画像の周囲(上下左右)に余白を付加する．
```console
l3on@MacBook:Image-Tools$ python add_margin_around_image.py 
----------------------------------------------------------------------
./src_images/1.png
Add top margin
Add bottom margin
Add left margin
Add right margin
Add margin:  ./src_images/1.png --> ./mgn_images/1.png
----------------------------------------------------------------------
./src_images/2.png
Add top margin
Add bottom margin
Add left margin
Add right margin
Add margin:  ./src_images/2.png --> ./mgn_images/2.png
----------------------------------------------------------------------
./src_images/3.png
Add top margin
Add bottom margin
Add left margin
Add right margin
Add margin:  ./src_images/3.png --> ./mgn_images/3.png
----------------------------------------------------------------------
Finished for all images
```

## [**combine_2_images_into_1_image.py**][combine_2_images_into_1_image.py-url]
2枚の画像を合体させて1枚の画像を生成する．
- 【横方向(左右)の合体】
  - 小さい方の画像の上下に余白を追加してから，横方向(左右)に2枚の画像を合体させ1枚の画像を生成．
- 【縦方向(上下)の合体】
  - 小さい方の画像の左右に余白を追加してから，縦方向(上下)に2枚の画像を合体させ1枚の画像を生成．
```console
l3on@MacBook:Image-Tools$ python combine_2_images_into_1_image.py 
./src_images/1.png + ./src_images/2.png --> ./cmb_images/combine_horizontally.png
To combine horizontally is done
./src_images/1.png + ./src_images/2.png --> ./cmb_images/combine_vertically.png
To combine vertically is done
```


## [**compress_image.py**][compress_image.py-url]
複数枚の画像を圧縮してファイルサイズを小さくする．(注意：画質が悪化する．)
```console
l3on@MacBook:Image-Tools$ python compress_image.py 
Compress:  ./src_images/1.png --> ./cmp_images/1.png
Compress:  ./src_images/2.png --> ./cmp_images/2.png
Compress:  ./src_images/3.png --> ./cmp_images/3.png
Finished for all images
```

## [**convert_image_to_pdf.py**][convert_image_to_pdf.py-url]
複数枚の画像を同じファイル名の複数個のpdfへ変換する．(1対1対応)
```console
l3on@MacBook:Image-Tools$ python convert_image_to_pdf.py 
Convert:  ./src_images/1.png --> ./dst_images/1.pdf
Convert:  ./src_images/2.png --> ./dst_images/2.pdf
Convert:  ./src_images/3.png --> ./dst_images/3.pdf
Finished for all images
```


## [**crop_image_by_hand.py**][crop_image_by_hand.py-url]
複数枚の画像を同じ長方形の画像へ切り抜く．
```console
l3on@MacBook:Image-Tools$ python crop_image_by_hand.py 
Crop:  ./src_images/1.png --> ./crp_images/1.png
Crop:  ./src_images/2.png --> ./crp_images/2.png
Crop:  ./src_images/3.png --> ./crp_images/3.png
Finished for all images
```

## [**print_coordinate_clicked_with_mouse.py**][print_coordinate_clicked_with_mouse.py-url]
マウスで左クリックした箇所の画像内の座標を表示する．
```console
l3on@MacBook:Image-Tools$ python print_coordinate_clicked_with_mouse.py
# ウィンドウが起動する
# ウィンドウ上で座標を知りたい箇所で左クリックすると，座標が表示される
# キーボード上のなんらかのキーを押すとウィンドウが閉じ，実行終了される
```


## [**print_image_size.py**][print_image_size.py-url]
複数枚の画像のサイズ(幅と高さ)とファイルサイズをターミナル上に表示する．
```console
l3on@MacBook:Image-Tools$ python print_image_size.py 
----------------------------------------------------------------------
./src_images/1.png
 width: 690,  height: 596
 0.24 MB
----------------------------------------------------------------------
./src_images/2.png
 width: 560,  height: 458
 0.52 MB
----------------------------------------------------------------------
./src_images/3.png
 width: 2704,  height: 2255
 3.09 MB
```

## このリポジトリについて
- 画像を扱う際に便利そうなソースコード集です．
- もしかしたら誰かの役に立つかもと思いpublic repositoryにしています．
- バグ等ありましたら本リポジトリの[Issues][issues-url]からお知らせいただけると嬉しいです．


<!-- 本README.mdで使用しているリンク -->
<!-- Pythonソースコード -->
[add_margin_around_image.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/add_margin_around_image.py
[combine_2_images_into_1_image.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/combine_2_images_into_1_image.py
[compress_image.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/compress_image.py
[convert_image_to_pdf.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/convert_image_to_pdf.py
[crop_image_by_hand.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/crop_image_by_hand.py
[print_coordinate_clicked_with_mouse.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/print_coordinate_clicked_with_mouse.py
[print_image_size.py-url]: https://github.com/L3onSW/Image-Tools/blob/main/print_image_size.py
<!-- Isuues -->
[issues-url]: https://github.com/L3onSW/Image-Tools/issues
<!-- License -->
[license-url]: https://github.com/L3onSW/Image-Tools/blob/master/UNLICENSE
<!-- Python -->
[python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://www.python.org
