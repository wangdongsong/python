# -*- coding: utf-8 -*-
"""
Created on 2018/1/28 9:49

简单利率：不考虑利息的利息
复合利率：考虑利息的利息

@author: wangdongsong1229@163.com
"""

import numpy as np
from matplotlib.pyplot import *
from pylab import *

pv = 1000 #当前值
r = 0.08 #周期利率
n = 10 #周期

#等差序列
t = np.linspace(0, n, n)
print(len(t))

#生成10个值的序列
y1 = np.ones(len(t)) * pv
print(y1)

y2 = pv * (1 + r * t)
print(y2)

y3 = pv * (1 + r) ** t
print(y3)

title("Simple vs. compounded interest rates")
xlabel("Number of years")
ylabel("Values")

#x轴的取值范围
xlim(0, 11)
#y轴的取值范围
ylim(800, 2200)

plot(t, y1, "b-") #b代表黑色
plot(t, y2, "g--") #g，绿色
plot(t, y3, "r-") #r，红色
show()