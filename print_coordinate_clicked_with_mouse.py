#!/opt/anaconda3/bin/python
# ======================================================================
# print_coordinate_clicked_with_mouse.py
# マウスで左クリックした箇所の画像内の座標を表示する
#
# 参考文献：
# http://opencv.jp/opencv-2.2/py/highgui_user_interface.html
# https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
#
# Created on 2024/01/21, author: L3onSW
# ======================================================================
import cv2
import numpy as np
import sys

# 白色のBGR(OpenCVはBGRを使うため)
white_bgr = (255, 255, 255)
# 黒色のBGR(OpenCVはBGRを使うため)
black_bgr = (0, 0, 0)

# マウスイベントのコールバック変数内に渡す引数を格納する辞書
mouse_callback_param = {}


def mouse_callback_print_coordinate(event, x, y, flags, param=None):
    """mouse_callback_print_coordinate マウスイベントのコールバック関数

    Args: (以下の5つはOpenCV側で指定されたものである)
        event (str): マウスイベント(マウスによる何らかの操作)
        x : マウスイベントが発生したx座標
        y : マウスイベントが発生したy座標
        flags : マウスイベント発生時の動作
        param (dict): setMouseCallback()の第3引数から
                        本コールバック関数内に辞書にして引数を渡す
    """
    # ------------------------------------------------------------------
    # マウスイベントのコールバック変数内に渡す引数を格納する辞書であるparamについて
    # 設定されてない項目に適用される値を定義
    # ------------------------------------------------------------------
    # 辞書のkeyに"im_cv2"が無い場合は異常終了
    if "im_cv2" not in param.keys():
        print("Error: 関数print_coordinate_clicked_with_mouse")
        print("の中でparam[\"im_cv2\"]の値を代入してから")
        print("コールバック関数mouse_callback_print_coordinate")
        print("に渡すようにしてください．")
        sys.exit(1)
    im = param["im_cv2"]
    # 座標を1つずつ表示する(False)か複数を重ねて表示する(True)か
    if "multiple coordinates" not in param.keys():
        param["multiple coordinates"] = False
    # ウィンドウの名前
    if "window name" not in param.keys():
        param["window name"] = "Print Coordinate Clicked with Mouse"
    # ------------------------------------------------------------------
    # マウスイベントのコールバック変数内に渡す引数を格納する辞書であるparamについて
    # cv2.circle()の引数
    # の値を設定
    # ------------------------------------------------------------------
    # radius: 円の半径[px(ピクセル)]
    if "circle radius" not in param.keys():
        param["circle radius"] = 10
    # color: 円の色(ただしBGR形式)
    if "circle color" not in param.keys():
        param["circle color"] = white_bgr
    # thickness: 線の太さ[px(ピクセル)]，負の数にすると塗りつぶし
    if "circle thickness" not in param.keys():
        param["circle thickness"] = -1
    # lineType: 線の描画方法(OpenCV独自のものを3択から選ぶ)
    # cv2.LINE_4 または cv2.LINE_8 または cv2.LINE_AA
    if "circle lineType" not in param.keys():
        param["circle lineType"] = cv2.LINE_8
    # 座標の少数部分のビット数，デフォルトは0
    if "circle shift" not in param.keys():
        param["circle shift"] = 0
    # ------------------------------------------------------------------
    # マウスイベントのコールバック変数内に渡す引数を格納する辞書であるparamについて
    # cv2.putText()の引数
    # の値を設定
    # ------------------------------------------------------------------
    # fontFace: フォントの種類(OpenCV独自のものから選ぶ)
    if "putText fontFace" not in param.keys():
        param["putText fontFace"] = cv2.FONT_HERSHEY_PLAIN
    # fontScale:文字の縮尺(1.0を基準にfloat型で指定)
    if "putText fontScale" not in param.keys():
        param["putText fontScale"] = 1.5
    # color: 文字の色(ただし，BGR形式)
    if "putText color" not in param.keys():
        param["putText color"] = white_bgr
    # thickness: 文字の太さ[px(ピクセル)]
    if "putText thickness" not in param.keys():
        param["putText thickness"] = 2
    # lineType: 線の描画方法(OpenCV独自のものを3択から選ぶ)
    # cv2.LINE_4 または cv2.LINE_8 または cv2.LINE_AA
    if "putText lineType" not in param.keys():
        param["putText lineType"] = cv2.LINE_8
    # putText bottomLeftOrigin: 画像データの原点をどこに置くか
    # Falseだと左上，Trueだと左下になる
    if "putText bottomLeftOrigin" not in param.keys():
        param["putText bottomLeftOrigin"] = False
    # ------------------------------------------------------------------
    # マウスイベント左クリック(押下)したときに以下の動作をする
    # 左クリックした点に丸を描き，その右横に座標の文字列を表示する
    # ------------------------------------------------------------------
    if event == cv2.EVENT_LBUTTONDOWN:
        # --------------------------------------------------------------
        # 座標を1つずつ表示する場合(左クリックするたびに背景の画像が更新される)
        # --------------------------------------------------------------
        if param["multiple coordinates"] is False:
            # マウスで左クリックするたびに表示する画像を切り替えるために
            # 元画像のコピーを生成
            im_copy = np.copy(im)
            # マウスで左クリックした座標に丸を描く
            cv2.circle(img=im_copy,
                       center=(x, y),
                       radius=param["circle radius"],
                       color=param["circle color"],
                       thickness=param["circle thickness"],
                       lineType=param["circle lineType"],
                       shift=param["circle shift"])
            # 座標を見やすく表示する文字列
            coordinate = "(x,y)=(" + str(x) + "," + str(y) + ")"
            # 座標の文字列をウィンドウ上に表示
            cv2.putText(img=im_copy,
                        text=coordinate,
                        org=(x+10, y+10),
                        fontFace=param["putText fontFace"],
                        fontScale=param["putText fontScale"],
                        color=param["putText color"],
                        thickness=param["putText thickness"],
                        lineType=param["putText lineType"],
                        bottomLeftOrigin=param["putText bottomLeftOrigin"])
            # 画像をwindow上に表示する
            cv2.imshow(param["window name"], im_copy)
        # --------------------------------------------------------------
        # 座標を複数重ねて表示する場合
        # --------------------------------------------------------------
        elif param["multiple coordinates"] is True:
            # マウスで左クリックした座標に丸を描く
            cv2.circle(img=im,
                       center=(x, y),
                       radius=param["circle radius"],
                       color=param["circle color"],
                       thickness=param["circle thickness"],
                       lineType=param["circle lineType"],
                       shift=param["circle shift"])
            # 座標を見やすく表示する文字列
            coordinate = "(x,y)=(" + str(x) + "," + str(y) + ")"
            # 座標の文字列をウィンドウ上に表示
            cv2.putText(img=im,
                        text=coordinate,
                        org=(x+10, y+10),
                        fontFace=param["putText fontFace"],
                        fontScale=param["putText fontScale"],
                        color=param["putText color"],
                        thickness=param["putText thickness"],
                        lineType=param["putText lineType"],
                        bottomLeftOrigin=param["putText bottomLeftOrigin"])
            # 画像をwindow上に表示する
            cv2.imshow(param["window name"], im)


def print_coordinate_clicked_with_mouse(image, mouse_callback_param=None):
    """print_coordinate_clicked_with_mouse
                マウスで左クリックした箇所の画像内の座標を表示する

    Args:
        image (str): 座標を表示したい画像ファイル名
        mouse_callback_param (dict, optional): デフォルトはNone.
    """
    # 画像ファイルをOpenCVで読み込み
    im = cv2.imread(image, cv2.IMREAD_COLOR)
    # マウスで画像をクリックするのに使う，後に起動させるウィンドウの名前
    window_name = "Print Coordinate Clicked with Mouse"
    # 画像をwindow上に表示する
    cv2.imshow(window_name, im)
    # 第1引数ウィンドウ(window_name)上で
    # マウスイベント(マウスによる何らかの操作)が発生したとき
    # 第2引数コールバック関数(print_coordinate)を呼び出す
    # 第3引数paramでコールバック変数内で操作するための引数を渡す
    mouse_callback_param = {}
    mouse_callback_param["im_cv2"] = im  # これが無いと画像をコールバック関数で扱えない
    cv2.setMouseCallback(window_name,
                         mouse_callback_print_coordinate,
                         mouse_callback_param)
    # キーボードが押されるまで待つ(0以外ならms(ミリセカンド)待つ)ため，
    # キーボード上でなんらかのキーを押すとウィンドウが閉じる
    cv2.waitKey(0)
    # 開いているすべてのウィンドウを閉じる
    cv2.destroyAllWindows()


# ----------------------------------------------------------------------
# マウスで左クリックした箇所の画像内の座標を表示する
# ----------------------------------------------------------------------
image = "./src_images/2.png"
print_coordinate_clicked_with_mouse(image)
