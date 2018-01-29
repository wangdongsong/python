# -*- coding: utf-8 -*-
"""
Created on 2018/1/29 22:20

NPV函数完成净现值

@author: wangdongsong1229@163.com
"""

import scipy as sp
import matplotlib.pyplot as plt

cashFlows = [504, -432, -432, -432, 832]
rate = []
npv = []
x = [0, 0.3]
y = [0, 0]
for i in range(1, 30):
    rate.append(0.01 * i)
    npv.append(sp.npv(0.01 * i, cashFlows))

plt.plot(x, y)
plt.plot(rate, npv)
plt.show()

