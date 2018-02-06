# -*- coding: utf-8 -*-
"""
Created on 2018/2/6 21:58

计算回报率

@author: wangdongsong1229@163.com
"""

import numpy as np
import pandas as pd

#假定如下4个价格
p = np.array([1, 1.1, 0.9, 1.05])

#输出前n-1个价格
print(p[:-1])

#输出后n-1个价格
print(p[1:])

#回报率计算
#价格顺序从左到右，回报率计算方式：第n个价格-(n-1)/第n-1个价格，例如(1.1 - 1) / 1 = 10%
#所在价格顺序重要
#以上面的顺序为价格，计算回报算如下
ret = (p[1:] - p[:-1]) / p [:-1]
print(ret)

xdate = pd.read_csv("IBM.csv",  usecols=[1, 4], skip_blank_lines=True)
print(xdate[:2])

xret = xdate[1:] - xdate[:-1] / xdate[:-1]
print("###", xret)