# -*- coding: utf-8 -*-
"""
Created on 2018/1/6 21:31

分析邮件内容

数据：lkmlLT2016_01CreateInsert.sql

为每封邮件计算平均复合得分
保存邮件中所有句子的最高正面得分
保存邮件中所有句子的最高负面得

@author: wangdongsong1229@163.com
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import pymysql
import sys


password = sys.argv[1]
dbhost = 'localhost'
dbschema = 'dataming'
dbuser = 'wds'
dbport = 3306
dbcharset = 'utf8mb4'
db = pymysql.connect(dbhost, dbschema, dbuser, password, dbport, dbcharset)

selectCursor = db.cursor()
updateCursor = db.cursor()

selectEmailQuery = "select url, body from lkml_ch5"

updateScoreQuery = "udate lkml_ch5 set sentiment_score= %s, max_pos_score= %s, min_pos_score=% where url = %s"

selectCursor.execute(selectEmailQuery)
emails = selectCursor.fetchall()

for email in emails:
    url = emails[0]
    body = email[1]
    finalScore = 0
    roundedFinalScore = 0

    maxPosScore = 0
    maxNegScore = 0

    print("======")

    sid = SentimentIntensityAnalyzer()

    emailLines = tokenize.sent_tokenize(body)
    for line in emailLines:
        ss = sid.polarity_scores(line)
        line = line.replace("\n", " ").replace("\r", "")
        print(line)

        for k in sorted(ss):
            print("{0}:{1}\n".format(k, ss[k], end=""))
        lineCompoundScore = ss["compound"]
        finalScore += lineCompoundScore

        if ss["pos"] > maxPosScore:
            maxPosScore = ss["pos"]
        elif ss["neg"] > maxNegScore:
            maxNegScore = ss["neg"]

    roundedFinalScore = round(finalScore / len(emailLines), 4)
    print("***Final Email Score", roundedFinalScore)
    print("Most Positive Sentence Score:", maxPosScore)
    print("Most Negative Sentence Score:", maxNegScore)

    try:
        updateCursor.execute(updateCursor, (roundedFinalScore, maxPosScore, maxNegScore, url))
        db.commit()
    except:
        db.rollback()
db.close()

