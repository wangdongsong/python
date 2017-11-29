# -*- coding: utf-8 -*-
"""
Created on 2017/11/29 23:00

核密度估计图（kernel Density Estimation）

@author: wangdongsong1229@163.com
"""

from numpy.random import randn
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_palette("hls")
mpl.rc("figure", figsize=(10, 6))
data = randn(250)
plt.title("KDE", fontsize=20)
sns.distplot(data, color="#ff8000")
plt.show()


