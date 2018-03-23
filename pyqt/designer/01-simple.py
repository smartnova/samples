#!/usr/bin/env python3

# 上の行はこのファイルが Python 3 インタプリタのありかを指定しています．
# この指定に加え，Linux/Mac でこのファイルに実行属性を与える(`chmod a+x simple.py`)と単に `./simple.py ...` のように起動できるようになります．Windows の場合は，`.py` 拡張子を処理するためのデフォルトアプリケーションを登録すれば，同じようなことができるかもしれません．

# このプログラムは指定した UI ファイルを表示します．

import sys

from PyQt5 import QtWidgets, uic
'''
二つのパッケージを読み込みます．

- QtWidgets は PyQt の GUI 部品．

- uic は PyQt 用の UI Compiler．QtDesigner で作成した UI 仕様を Python のコードに自動変換する．生成されるコードに興味があったら，`pyuic5 01-default.ui` のように Python 用の UI コンパイラを使ってみて下さい．
'''

# GUI アプリケーションを起動するときのお約束の一行．
app = QtWidgets.QApplication(sys.argv)

# 一般的なアプリケーション向けのウィンドウを構成する（以下の図を参照）
# http://doc.qt.io/qt-5/qmainwindow.html#details
window = QtWidgets.QMainWindow()

# QtDesignerで作成したGUI部品の仕様をPythonのプログラムに自動変換
uic.loadUi('01-default.ui' if len(sys.argv) <= 1 else sys.argv[1], window)

# 全画面表示
window.show()
# window.showFullScreen()

# お約束の一行．
# イベント処理をする無限ループが動き続け，exit が呼ばれると停止する．
sys.exit(app.exec_())
