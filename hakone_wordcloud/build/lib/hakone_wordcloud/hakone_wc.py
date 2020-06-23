#!/usr/bin/env python3

import os, os.path
import pandas as pd
import sys
from wordcloud import WordCloud
import xml.etree.ElementTree as ET

RICTY_DIMINISHED_BOLD = None
for font in [f'{os.environ["HOME"]}/Library/Fonts/RictyDiminished-Bold.ttf',
             r"C:\Windows\Fonts\RictyDiminished-master\RictyDiminished-Bold.ttf"]:
    if os.path.exists(font): RICTY_DIMINISHED_BOLD = font
assert RICTY_DIMINISHED_BOLD is not None   # 'RictyDiminished-Boldフォントが見つかりません。

BLACKLIST = set(["箱根駅伝", "区間", "記録", "選手", "監督"])
NS = { 'svg': 'http://www.w3.org/2000/svg' }

def main():
    wc = WordCloud(font_path=RICTY_DIMINISHED_BOLD, background_color='white', width=800, height=600)
    os.makedirs('svg', exist_ok=True)

    sheets = pd.read_excel('topics.xlsx', sheet_name=None)
    for sheet_name in list(sheets.keys()):
        print(sheet_name)
        sheet = sheets[sheet_name]
        sheet = sheet[~sheet['term'].isin(BLACKLIST)]
        wc.fit_words(dict(zip(sheet['term'], sheet['value'])))

        # word cloud内の text 要素の並びを逆順にすることで重要な語が hover に反応しない問題を修正
        root = ET.fromstring(wc.to_svg())
        texts = root.findall('svg:text', namespaces=NS)
        for text in texts: root.remove(text)
        for text in reversed(texts): root.append(text)
        with open(f'svg/topic{sheet_name}.svg', 'w', encoding='utf-8') as w:
            w.write(ET.tostring(root, encoding='unicode'))

if __name__ == '__main__':
    main()
