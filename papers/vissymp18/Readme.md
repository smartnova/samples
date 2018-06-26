---
title: 講演申し込み
url: http://www.visualization.jp/symp2018/
---

---

# 重要な期日

シンポジウム
: 9/14-16

講演申込開始日
: 平成30年2月26日（月）

講演申込締切日
: 平成30年4月27日（金）

本論文投稿開始日
: 平成30年5月7日（月）

本論文投稿締切日
: 平成30年6月29日（金）

# このテンプレートの使い方

- 必要なソフトウェア: `pandoc`, `pandoc-citeproc`

    いずれも `brew install`

- `Makefile` を適宜修正。たぶん、`vjs18-wakita.docx` を別な名前にするだけでよい。

- `vsj18.md` を修正して論文を執筆

- Word でできあがったファイルを開く。(e.g., `open vsj18-wakita.docs`)

    - 一部、デザインが崩れているところもあるが、提出直前に対応する。

# 提出直前の作業

以下は主として Word でスタイルウィンドウを使っての作業

1. スタイルウィンドウを表示してから **一覧** を「作業中の文書に含まれるスタイル」にすると、膨大なスタイルを見なくてもすむので作業が楽。

1. スタイルの適用

    | 箇所 | スタイル名 |
    | :--- | :--------- |
    | 英文タイトル | 表題 (English) |
    | （もしもあるのなら）英文副題 | 副題 (English) |
    | 英文著者名 | Author (English) |
    | `ABSTRACT` | Abstract heading |
    | アブストラクトの内容 | Abstract |
    | Keywords | Keywords |
    | `Keywords:` （見出し） | Keywords Header |
    | 参　考　文　献 | 参考文献見出し |

    Keywords Header を適用するときは、まず、この段落に Keywords スタイルを適用すること。次に、`Keywords:` の文字列の範囲を選択してから、その箇所に Keywords Header を適用する。

1. ２カラム化

    1. 新しい **区切りセクション** の開始
    
        Word文書の１カラムの領域と２カラムの領域をWordの **セクション区切り** で分割する。２カラム指定の準備
    
        1. 第1節の先頭の文字の左をクリック

        1. 挿入メニュー、区切り、セクション区切り（現在の位置から新しいセクション）

    1. **レイアウト**タブの**段組み**で２段を指定

# FAQ

1. Markdown ファイルを複数に分割できませんか？

    できます。追加のMarkdownを作成してから `Makefile` の `MARKDOWN=vsj18.md` と書かれている行に、所定の Markdown ファイルの名前を追加して下さい。

    `MARKDOWN=vsj18.md md/1-introduction.md ... 5-summary.md`

2. 編集しながらプレビューしたいです。

    `bin/macdown` を使って下さい。このコマンドは`vsj18.md`と`md/*.md`の変化を検知すると自動的に HTML を作り直します。さらにGoogle Chrome を起動して、当該HTMLを開き、そのHTMLが更新するたびに自動的に再読み込みさせます。テキストエディタには依存していないので、どんな環境でも利用できると思います。ただし、Mac 限定。

    `fswatch` と `chrome-cli` が必要です。どちらも `brew install` できます。

3. 文献の引用スタイルを変更したいです。

    `etc/*.csl` が文献の引用スタイルの定義ファイルたちです。pandoc はデフォルトで Chicago フォーマットを採用しているようです。これを他のスタイルに変更したい場合は `Makefile` の pandoc を呼び出している箇所に `--csl=etc/ieee.csl \` のような行を追加して下さい。ほかのスタイルを利用したい場合は、[スタイルはごまんとある](https://github.com/citation-style-language/styles)ので適宜、拾ってきて試して下さい。
