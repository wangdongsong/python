# -*- coding: utf-8 -*-
"""
Created on 2017/12/7 6:28

逻辑斯谛回归

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
import matplotlib
import random, fnmatch
import numpy as np
import scipy, scipy.stats
import pandas as pd

x = np.linspace(-10, 10, 100)
y1 = 1.0 / (1.0 + np.exp(-x))
y2 = 1.0 / (1.0 + np.exp(-x/2))
y3 = 1.0 / (1.0 + np.exp(-x/10))

plt.title("Sigmoid Functions vs LineSpace")
plt.plot(x, y1, "r-", lw=2)
plt.plot(x, y2, "g-", lw=2)
plt.plot(x, y3, "b-", lw=2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
