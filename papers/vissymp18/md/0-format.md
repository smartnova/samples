An Example of the Manuscript for\
the Visualization Symposium Japan (Times New Roman 16pt)

―Subtitle (Times New Roman 14pt)―

Taro KASHIKA and Hanako JOHO

##### ABSTRACT {#abstract .af1}

This template is a guide to prepare manuscript for Visualization
Symposium Japan. Here, please write the abstract serving as an index and
as a summary of the present paper. It should be as long as approximately
150 words. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*《150語程度の英文ABSTRACT及び5語以下のKeywordsを記入してください．文字の大きさは10pt，字体はCentury，行間は１行分
(シングルスペース) です．》

Keywords: Visualization, Digital image processing,
\*\*\<5語以下\>\*\*, \*\*\*\*\*, \*\*\*\*\*

# 序　論

本原稿は，可視化情報シンポジウムの原稿テンプレートです．原稿執筆にはこのテンプレートをご使用ください．原稿サイズはA4版とし，ページ数は任意ですがファイルサイズは5MB以下としてください．ページ余白は，上25mm，左20mm，右20mm，下20mmとし，ヘッダーおよびフッダーは入れず，表題は3行目から始めてください．

# 文字及び改行

## 文字の大きさと改行

使用言語は日本語または英語とします．和文原稿の場合，題目，著者名，所属を和文で書き，続けて題目，著者名の英文名を記入してください．英文原稿の場合，題目，著者名の英文名を記入してください．なお，[和題・英題は講演申込時と同じであることが必要です]{.underline}
(異なる場合，プログラムや講演論文集の目次には講演申込時の題目が使用されます)．

著者名は11pt，1行に36字以内で右寄せとし，これを越える場合は改行してください．本文は9ptの2段組みとし，片側25字×50行，段間は10mmを基準としてください．章間の行間は2行分
(ダブルスペース)
とし，その中央に章名を10ptで記し，節間は行を空けないようにしてください．

## 字　体

題名，章・節名はゴシック体，本文は明朝体，英文題名，著者名はTimes New
Roman, 本文中の英文はCenturyとします.参考文献^1)^ は8ptで表記ください．

- *強調*

- **とても強調**

# 図　表

本文中の図表の表記には，下記Fig.1と Table
1のように，図表には通し番号をふり，図表番号はゴシック体，図表題はCenturyで書きます．キャプションは表の場合は上部に，図の場合は下部に記し，説明文は英文で表記してください．

  : Table 1: Sample of table

  Table            | Table
  :--------------- | :---------------
  1                | 2

表 [Sample of table] を参照のこと。

![Figure 1: PacificVis PC meeting](md/pvis-party.jpg)

# 原稿提出

本テンプレートで作成した講演原稿 (PDF形式) と，調査票
(PDF形式，必ず押印したものをお願いします)
をシンポジウムHPの案内に従って提出して下さい．

# 数式

二点$\mathbf p, \mathbf {p'}$を結ぶふたつの制御点列$\mathbb{e}$と$\mathbb {e'}$について。。。

`macros.tex` に定義したようなTeXマクロにも対応しています。

二点$\v p, \v \pp$を結ぶふたつの制御点列$\E e$と$\E \ep$について。。。

以上で定義した三つの指標がいずれも一定値以上出会った場合に限り，束化圧があるものと評価する．このことは閾値 ($\theta_a, \theta_l, \theta_p$) を用いて以下のように定式化される：

$\Cae, \Cae, \Cle$

$$
C(\E e, \E \ep) =
\begin {cases}
\Cae \Cpe \Cle & \Cae > \theta_a \text { かつ } \\
               & \Cpe > \theta_p \text { かつ } \\
               & \Cle > \theta_l \\
0              & \text {その他の場合}
\end{cases}
$$

$$\begin {align}
F_{\v e_i} =
  & - \sum_{\v e'_i \neq \v e_i} C(P^{-1}\E e_i, P^{-1}\E e'_i)\frac{\v e_i- \v{e'}_i}{(|\v e_i-\v e'_i| + \alpha)^2} \\
  & -k\left(|{\v e_i} - \v e_{i-1}| - \ell_{\E e}\right)\frac{\v e_i - \v e_{i-1}}{|\v e_i - \v e_{i-1}|} \\
  & -k\left(|\v e_i - \v e_{i+1}| - \ell_{\E e}\right)\frac{\v e_i - \v e_{i+1}}{|\v e_i - \v e_{i+1}|}
\end {align}
$$

$$\begin {align}
C^{\text {High}}(\E x, \E {x'}) & = \\
& \begin {cases}
\Cax \Clx \Cpx & \text {※ 束化圧が高い場合} \\
0 & \text {その他の場合}
\end {cases} \\
\text {ただし、※の条件は} \\
    \Cax > \theta_a \text { \& }
    \Clx > \theta_l \text { \& }
    \Cpx > \theta_p
\end {align}$$

# その他

## 文献の引用

この例題では、`library.bib` 文献データベースとし、文献引用のスタイルにシカゴスタイルを指定して文献リストと文献の引用をしている。`.csl`ファイルを別のものに指定すれば、他の引用形式にも対応できる。文献の引用方法は LaTeX の `\cite {...}` コマンドとは異なる。以下を参考にすること。

[@kashika-1997-visualization-technique; @kashika-1999-an-example-of-the-manuscript-for-vsj-journal] は英語の文献で[@kashika-1999-a-japanese-example-of-the-manuscript-for-vsj-journal]は日本語の文献である.
