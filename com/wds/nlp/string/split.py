# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:13:34 2017

切分

@author: wangdongsong1229@163.com
"""

import nltk

# 1.1.1 将文文本切换为句子
text = "Welcome readers. I hope you find it interesting. Please do reply."
from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))

# 要切分大指的句子，使用tokenize()函数进行切分
punkt_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
print(punkt_tokenizer.tokenize(text))


# 1.1.2 其它语言文本的切分
french_tokenizer = nltk.data.load("tokenizers/punkt/french.pickle")
# 逗号不分，句号分
print(french_tokenizer.tokenize("Deux agressions en quelques jours. volia ce"))

# 1.1.3 将句子切分为单词 word_tokenize
word_text = nltk.word_tokenize("PierreVinken, 59 years old, will join as a nonexecutive director on Nov. 29.")
print(word_text)
print(type(word_text)) #list

# 也可以使用TreebankWordTokenizer实现，包含标点符号
#r = input("Please write a text")
#print("The length of text is ", len(nltk.word_tokenize(r)), "words")

# 1.1.4 TreebankWordTokenizer执行切分
from nltk.tokenize import TreebankWordTokenizer
treeTokenizer = TreebankWordTokenizer()
#标点符号和最后一个单词为一个元素
print(treeTokenizer.tokenize("Have a nice day. I hope you find the book interesting"))


#WordPunctTokenizer 通过分离标点来实现切分，每个单词都会被保留。
from nltk.tokenize import WordPunctTokenizer
wordpunct_tokenizer = WordPunctTokenizer()
print(wordpunct_tokenizer.tokenize("Dont't hesitate to ask questions, 193 adb"))

# 1.1.5 使用正则表达式实现切分
# RegexpTokenizer
from nltk.tokenize import RegexpTokenizer
regexp_tokenizer = RegexpTokenizer("[\w]+")
#不包含标点符号
print(regexp_tokenizer.tokenize("Don't hesitate to ask questions"))

#不实例化的方式
from nltk.tokenize import regexp_tokenize
sent = "Don't hesitate to ask questions"
print(regexp_tokenize(sent, pattern="\w+|\$[\d\.]+|\S+"))

# 通过空格切分
regexp_tokenizer = RegexpTokenizer("\s+", gaps=True)
print(regexp_tokenizer.tokenize("Don't hesitate to ask questions"))

# 筛选以大写字母开头的单词
sent = " she Secured 90.56% in class X. She is a student"
capt = RegexpTokenizer("[A-Z]\w+")
print(capt.tokenize(sent))
# 通过RegexpTokenizer子类实现
from  nltk.tokenize import BlanklineTokenizer
print(BlanklineTokenizer().tokenize(sent))

#字符串切分可以通过空格、间隔、换行来完成
from nltk.tokenize import WhitespaceTokenizer
print(WhitespaceTokenizer().tokenize(sent))

# nltk.tokenize.util模块通过返回元组形式的序列来执行切分，该序列为标识符在语句中的位置和偏移量
print("span", list(WhitespaceTokenizer().span_tokenize(sent)))
# 跨度
from nltk.tokenize.util import spans_to_relative
print(list(spans_to_relative(WhitespaceTokenizer().span_tokenize(sent))))