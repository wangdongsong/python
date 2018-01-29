# -*- coding: utf-8 -*-
"""
Created on 2018/1/27 11:56

正弦和余弦

@author: wangdongsong1229@163.com
"""

from pylab import *
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

C, S = np.cos(x), np.sin(x)

plot(x, C)
plot(x, S)

show()


