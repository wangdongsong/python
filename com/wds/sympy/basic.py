# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:46:46 2017

sympy 符号、表达式和基本运算

@author: wangdongsong1229@163.com
"""

from __future__ import division
from sympy import *

x, y, z = symbols("x y z")
m1, m1, m2, m3, m4 = symbols("m0:5")
x1 = Symbol("x1")
x1 + 500
y = 22 / 7

print(y)

x = sin(50)
print(x)
print(pi.evalf()) #默认精度15位
print(pi.evalf(50))

print(x.n())
print(x.n(20))
