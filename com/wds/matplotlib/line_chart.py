# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:27:08 2017

线图

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
from sympy import cos, sin
from numpy import arange
import numpy as np

var = arange(0., 100, 0.2)
cos_var = np.cos(var)
sin_var = np.sin(var)
plt.plot(var, cos_var, "b-*", label="cosine")
plt.plot(var, sin_var, "r-.", label="sine")
plt.legend(loc="upper left")
plt.xlabel("xaxis")
plt.ylabel("yaxis")
plt.show()
