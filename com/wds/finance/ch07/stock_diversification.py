# -*- coding: utf-8 -*-
"""
Created on 2018/2/1 6:49

把不同的股票包含在投资组合里降低公司特有的风险

使用numpy模块的mean()和std()函数计算这个组合的均值、标准差和相关系数

@author: wangdongsong1229@163.com
"""

import numpy as np
import matplotlib.pyplot as plt

#股票A连续5年的收益
ret_A = np.array([0.102, -0.02, 0.213, 0.12, 0.13])
#股票A连续5年的收益
ret_B = np.array([0.1062, 0.23, 0.045, 0.234, 0.113])
port_EW = (ret_A + ret_B) / 2

plt.figtext(0.2, 0.65, "StockA")
plt.figtext(0.15, 0.4, "StockB")
plt.xlabel("Year")
plt.ylabel("Returns")

year = [2009, 2010, 2011, 2012, 2013]
plt.plot(year, ret_A, lw = 2)
plt.plot(year, ret_B, lw = 2)
plt.plot(year, port_EW, lw = 2)

plt.title(("Indiviudal stocks vs. an equal-weighted 2-stock portflio"))

plt.annotate("Equal-weighted Portfolio", xy = (2010, 0.1), xytext=(2011., 0), arrowprops = dict(facecolor = "black", shrink = 0.05),)

plt.ylim(-0.1, 0.3)

plt.show()




