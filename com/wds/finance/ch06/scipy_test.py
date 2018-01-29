# -*- coding: utf-8 -*-
"""
Created on 2018/1/26 21:50

Scipy示例

@author: wangdongsong1229@163.com
"""
import scipy as sp

cashflows = [50, 40, 20, 10, 50]
x = sp.npv(0.1, cashflows)
print(x)
print(round(x, 2))
