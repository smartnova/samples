#!/usr/bin/env python3

# 上の行はこのファイルが Python 3 インタプリタのありかを指定しています．
# この指定に加え，Linux/Mac でこのファイルに実行属性を与える(`chmod a+x simple.py`)と単に `./simple.py ...` のように起動できるようになります．Windows の場合は，`.py` 拡張子を処理するためのデフォルトアプリケーションを登録すれば，同じようなことができるかもしれません．

import sys

# PyQt5.QtWidgets は PyQt の GUI 部品を利用するためのパッケージ
from PyQt5 import QtWidgets

# GUI アプリケーションを起動するときのお約束の一行．
app = QtWidgets.QApplication(sys.argv)

# 一般的なアプリケーション向けのウィンドウを構成する（以下の図を参照）
# http://doc.qt.io/qt-5/qmainwindow.html#details
window = QtWidgets.QMainWindow()

# 画面表示
# window.showFullScreen() # 全画面表示の場合
window.show()

# お約束の一行．
# イベント処理をする無限ループが動き続け，exit が呼ばれると停止する．
sys.exit(app.exec_())
