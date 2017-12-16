# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:20:18 2017

正在分布直方图

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
from numpy.random import normal

sample_gauss = normal(size=500)

plt.hist(sample_gauss, bins=10)
plt.title("Histogram Representing Gaussian numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()