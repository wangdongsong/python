# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:32:25 2017

信号处理， scipy.signal

detrend函数是一个滤波函数，该函数从数据中沿着坐标轴去除常量或线性趋势，使得我们可以
看到高阶函数的效果

@author: wangdongsong1229@163.com
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 5, 100)
x = t + np.random.normal(size=100)
plt.plot(t, x, linewidth=3)
plt.show()
plt.plot(t, signal.detrend(x), linewidth=3)
plt.show()