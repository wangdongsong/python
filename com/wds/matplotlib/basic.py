# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:24:29 2017

matplotlib画图

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt

#半径
r = [1.5, 2.0, 3.5, 4.0, 5.5, 6.0]

#圆的面积
a = [7.06858, 12.56637, 38.48447, 50.26544, 95.03309, 113.09724]

plt.plot(r, a)
plt.xlabel("Radius")
plt.ylabel("Area")
plt.title("Area of Circle")
plt.show()

