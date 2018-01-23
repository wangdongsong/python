# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:13:07 2018

使用replace.py中的类替换文本

@author: wangdongsong1229@163.com
"""

import nltk

from replace import RegexpReplacer

replacer = RegexpReplacer()

#文本替换
text = replacer.replace("Don't hesitate to ask questions")
print(text)
text = replacer.replace("She must've gone to the market but she didn't go")
print(text)

#先替换后切分
from nltk.tokenize import word_tokenize
before_text=word_tokenize("Don't hesitate to ask question")
print(before_text)
after=word_tokenize(replacer.replace("Don't hesitate to ask question"))
print(after)
