# -*- coding: utf-8 -*-
"""
Created on 2018/1/6 21:12

@author: wangdongsong1229@163.com
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

basePath = os.path.abspath(".") + "/data/ubuntu.txt"
#print(basePath)

with open(basePath, encoding="utf-8") as ubuntu:
    ubuntulines = [line.strip() for line in ubuntu.readlines()]
ubuntu.close()

sid = SentimentIntensityAnalyzer()
finalScore = 0

for line in ubuntulines[0:20]:
    print(line)
    ss = sid.polarity_scores(line)
    for k in sorted(ss):
        print("{0}: {1}\n".format(k, ss[k]), end="")
    print()
