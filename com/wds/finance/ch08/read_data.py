# -*- coding: utf-8 -*-
"""
Created on 2018/2/5 22:12

@author: wangdongsong1229@163.com
"""

import pandas as pd
import os

p = os.path.abspath(".") + "\IBM.csv"
print(p)
f = pd.read_csv(p)
print(f[:2])
