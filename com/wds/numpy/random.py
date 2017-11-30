# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:39:23 2017

NumPy随机抽样

@author: wangdongsong1229@163.com
"""
import numpy as np

np.random.permutation(10)
np.random.permutation(10)
np.random.randint(20, 50, size=10)
np.random.random_sample(10)
np.random.chisquare(5, 10)  # 自由度

alpha, location_param = 4., 2

s = np.random.pareto(alpha, 10) + location_param

s = np.random.standard_normal(20)

mean, std_deviation = 4., 2

s = np.random.lognormal(mean, std_deviation, 10)