# -*- coding: utf-8 -*-
"""
Created on 2018/2/4 10:24

statsmodels模块示例

在统计学中，普通最小二乘法（OLS）用于估计线性回归模型参数的一个常用方法

目标是选择参数使得观测值和模型的预测值之间的差值的平方之和最小

@author: wangdongsong1229@163.com
"""

import numpy as np
import statsmodels.api as sm

y = [1, 2, 3, 4, 2, 3, 4]
x = range(1, 8)
x = sm.add_constant(x)

result = sm.OLS(y, x).fit()
print((result.params))

