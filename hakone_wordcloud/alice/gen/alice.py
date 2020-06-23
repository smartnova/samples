#!/usr/bin/env python

from os import path
from PIL import Image
import numpy as np
import os

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
text = open(path.join(d, 'alice.txt')).read()
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

wc.generate(text)

with open(path.join(d, 'alice.svg'), 'w') as w:
    w.write(wc.to_svg())
