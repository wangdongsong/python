# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 06:51:37 2017

字符：标准化

@author: wangdongsong1229@163.com
"""

# 1.2.1 消除标点符号

text = [" It is a pleasant evening.", " Guests, who came from US arrived at the venue", "Food was tasy."]
from nltk.tokenize import word_tokenize
tokenized_docs = [word_tokenize(doc) for doc in text]
print(tokenized_docs)
