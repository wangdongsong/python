# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:46:46 2017

sympy 符号、表达式和基本运算

@author: wangdongsong1229@163.com
"""

from sympy import collect, expand, factor, simplify
from sympy import Symbol, symbols
from sympy import sin, cos

x, y, a, b, c, d = symbols("x y a b c d")
expr = 5 * x ** 2 + 2 * b * x ** 2 + cos(x) + 51 * x ** 2
simplify(expr)
factor(x ** 2 + x -30)

collect(x ** 3 + a * x * 2 + b * x ** 2 + c * x + d, x)
expr = sin(x) * sin(x) + cos(x) * cos(x)
expr
expr.subs({x:5, y:25})
expr.subs({x:5, y:25}).n()