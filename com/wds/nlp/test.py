# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 22:35:59 2017

@author: wangdongsong1229@163.com
"""

import nltk

text = "Welocome raders. I hope you find it innteresting. Please do reply."
from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))