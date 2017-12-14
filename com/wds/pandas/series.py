# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:11:19 2017

Pandas Seris

@author: wangdongsong1229@163.com
"""

import numpy as np 
from pandas import *

randn = np.random.randn

s = Series(randn(10), index = ['I', "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"])
s
s.index

Series(randn(10))

d = {"a":0., "e": 1., "i": 2.}
print(Series(d))
Series(d, index=["e", "i", "o", "a"])

# Series用标量值创建
Series(6., index =["a", "e", "i", "o", "u", "y"])
Series([10, 20, 30, 40], index=["a", "e", "i", "o"])
Series({"a":10, "e":20, "i":30})
s.get("VI")

s = Series(np.random.randn(5), name="RandomSeries")