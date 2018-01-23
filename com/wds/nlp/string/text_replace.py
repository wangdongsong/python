# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:13:07 2018

使用replace.py中的类替换文本

@author: wangdongsong1229@163.com
"""

import nltk

from replace import RegexpReplacer

replacer = RegexpReplacer()

text = replacer.replace("Don't hesitate to ask questions")
print(text)

text = replacer.replace("She must've gone to the market but she didn't go")
print(text)