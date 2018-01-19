# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:27:05 2018



@author: wangdongsong1229@163.com
"""

import json
import os

#获取当前路径
path = os.path.abspath(".") + "\example.txt"
print(type(path))
print(path)

records = [json.loads(line) for line in open(path)]
print(type(records))
print(len(records))
for l in records:
    #print(l)
    try:
        print(l["c"])
    except:
        print("no c")