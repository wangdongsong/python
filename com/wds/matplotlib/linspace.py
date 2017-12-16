# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:28:29 2017

高等线图 linspace函数生成的线性空间矢量

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
from numpy import *

x = linspace(0, 10.5, 40)
y = linspace(1, 8, 30)

(X, Y) = meshgrid(x, y)
func = exp(-((X-2.5) ** 2 + (Y-4)**2)/4) - exp(-((X-7.5) ** 2 + (Y - 4) ** 2) /4)
contr = plt.contour(x, y, func)
plt.clabel(contr)
plt.xlabel("x")
plt.ylabel("y")
plt.show()