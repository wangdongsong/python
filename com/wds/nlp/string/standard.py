# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 06:51:37 2017

字符：标准化

@author: wangdongsong1229@163.com
"""

import re
import string

# 1.2.1 消除标点符号

text = [" It is a pleasant evening.", " Guests, who came from US arrived at the venue", "Food was tasy."]
from nltk.tokenize import word_tokenize
tokenized_docs = [word_tokenize(doc) for doc in text]
print(tokenized_docs, "\n")
#上述代码切分之后，将文本中的标点符号删除
x = re.compile("[%s]" % re.escape(string.punctuation))
tokenized_docs_no_punctuation = []
for review in tokenized_docs:
    new_review = []
    for token in review:
        new_token = x.sub(u"", token)
        if not new_token == u"":
            new_review.append(new_token)
    tokenized_docs_no_punctuation.append(new_review)

print(tokenized_docs_no_punctuation)

# 1.2.2 文本的大小写转换
# 通过lower和upper函数

text = "HAWork is KeY to SUCCESS"
print(text.lower())
print(text.upper())

# 1.2.3 处理停止词
# 停止词是指在执行信息检索或其它自然语言任务时需要被过滤掉的词，这些词对理解句子整体意思没多大意义。
# 消除停止词在NLP中被认为至关重要 的标准化任务之一

from nltk.corpus import stopwords

stops = set(stopwords.words("english"))
words = ["Don't", "hesitate", "to", "ask", "question"]
stop_word = [word for word in words if word not in stops]
print(stop_word)