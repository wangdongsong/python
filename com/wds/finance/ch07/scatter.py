# -*- coding: utf-8 -*-
"""
Created on 2018/1/28 9:44

散点图

@author: wangdongsong1229@163.com
"""
from pylab import *
import numpy as np

n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
scatter(x, y)
show()
