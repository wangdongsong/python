# -*- coding: utf-8 -*-
"""
Created on 2018/1/28 10:59

净现值图示曲线

净现值（NPV）：描述一个项目的净现值和折现率（或资本成本）之间的关系

NPV = PV（所有现金收入） - PV（所有现金支出）

@author: wangdongsong1229@163.com
"""
import scipy as sp
from matplotlib.pyplot import *

cashFlows = [-200, 80, 90, 100]
rate = []
npv = []
x = (0, 0.7)
y = (0, 0)
for i in range(1, 70):
    rate.append(0.01 * i)
    npv.append(sp.npv(0.01 * i, cashFlows))

plot(rate, npv)
plot(x, y)
show()


