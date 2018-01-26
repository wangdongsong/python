# -*- coding: utf-8 -*-
"""
Created on 2018/1/26 21:40

NumPy示例

@author: wangdongsong1229@163.com
"""
import numpy as np

#2 * 3
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
print(np.size(x))
print(np.shape(x))
print(np.size(x, 0))

print(np.std(x))

total = x.sum()
print(total)