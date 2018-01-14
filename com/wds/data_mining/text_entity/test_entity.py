# -*- coding: utf-8 -*-
"""
Created on 2018/1/14 11:09

文本中的命名实体识别

@author: wangdongsong1229@163.com
"""

import nltk
import pprint
import os

basePath = os.path.abspath(".") + "/data/apacheMeetingMinutes.txt"

with open(basePath, "r", encoding="utf-8") as sampleFile:
    text = sampleFile.read()

en = {}
try:
    sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
    sentences = sent_detector.tokenize(text.strip())
    for sentence in sentences:
        tokenized = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokenized)
        chunked = nltk.ne_chunk(tagged)

        for tree in chunked:
            if hasattr(tree, "label"):
                ne = " ".join(c[0] for c in tree.leaves())
                en[ne] = [tree.label(), " ".join(c[1] for c in tree.leaves())]
except Exception as e:
    print(str(e))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(en)