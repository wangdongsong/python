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


# 函数在积分时需要额外的参数，例如变量进行乘或乘方的因子，那么这些参数可以作为变量传入

def integrand(x, a, b, c):
    return a*x*x + b*x +c

a = 3
b = 4
c = 1
result = integrate.quad(integrand, 0, np.inf, args=(a, b, c))

#二重积分、三重积分

def integrandl(t, x, n):
    return np.exp(-x * t) / t ** n

n = 4
result = integrate.dblquad(lambda t, x: integrandl(t, x, n), 0, np.inf, lambda x:0, lambda x: np.inf)

# 高斯积分

def integrand2(x, a, b):
    return a *x + b

a = 2
b = 1
fixed_result = integrate.fixed_quad(integrand2, 0, 1, args=(a, b))
result = integrate.quadrature(integrand2, 0, 1, args=(a, b))
