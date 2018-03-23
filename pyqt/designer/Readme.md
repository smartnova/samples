# QtDesignerを利用したGUIアプリケーション作成の例題

ユーザインタフェイスはQt Designerを用いて描いたものを`*.ui`ファイルに保存しています．このとき`QMainWindow`の`whatsThis`にそのUI構成の概略を記述しました．実行しているときに`Shift+F1`を押すと説明が表示されるので参考にして下さい．

## `00-simple.py`: 6行で開くウィンドウ

## `01-simple.py`: Qt Designerで描いが画面を開く

`./simple.py ***.ui` のように起動すると指定したUIファイルを元に構成された画面が表示されます．

- `./simple.py 01-default.ui`: 空のウィンドウ

- `./simple.py 02-widgets.ui`: スライダで図形の色を調整できる．

    描画は `drawing02.py` で定義されている `Drawing02` クラスが担当している．スライダを動かすと，このクラスの `setColor` メソッドが動くように UI ファイルで調整してある．

    レイアウトマネージャを利用しているため，ウィンドウの大きさを変更しても，レイアウトが崩れない．

## `*.ui`

Qt Desigerで描いたGUI部品の情報をXML形式で保存したもの．
