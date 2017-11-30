# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:15:16 2017

SciPy 积分

@author: wangdongsong1229@163.com
"""

import numpy as np
from scipy import special
from scipy import integrate

result = integrate.quad(lambda x: special.jv(4, x), 0, 20)
print(result)

print("Gaussian integral", np.sqrt(np.pi), integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf))