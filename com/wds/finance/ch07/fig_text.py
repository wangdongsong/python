# -*- coding: utf-8 -*-
"""
Created on 2018/1/28 10:10

为图片配文字说明

@author: wangdongsong1229@163.com
"""
from pylab import *
x = [0, 1, 2]
y = [2, 4, 6]

plot(x, y)
figtext(0.2, 0.7, "North & West")
figtext(0.7, 0.2, "East & South")

show()
