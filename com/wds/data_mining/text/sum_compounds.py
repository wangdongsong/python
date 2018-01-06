# -*- coding: utf-8 -*-
"""
Created on 2018/1/6 21:19

计算每行的情绪，加总复合得分，除以消息数量

@author: wangdongsong1229@163.com
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

basePath1 = os.path.abspath(".") + "/data/ubuntu.txt"

with open(basePath1, encoding="utf-8") as ubuntu:
    ubuntuLines = [line.strip() for line in ubuntu.readlines()]
ubuntu.close()

basePath2 = os.path.abspath(".") + "/data/ubuntu-devel.txt"
with open(basePath2, encoding="utf-8") as ubuntuDevel:
    ubuntuDevelLines = [line.strip() for line in ubuntuDevel.readlines()]
ubuntuDevel.close()

listOfChannels = [ubuntuLines, ubuntuDevelLines]
sid = SentimentIntensityAnalyzer()
for channel in listOfChannels:
    finalScore = 0
    for line in channel:
        ss = sid.polarity_scores(line)
        score = ss["compound"]
        finalScore = finalScore + score
        roundedFinalScore = round(finalScore / len(channel), 4)
    print("Score", roundedFinalScore)

