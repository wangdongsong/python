# -*- coding: utf-8 -*-
"""
Created on 2018/2/6 20:52

pandas常用函数

@author: wangdongsong1229@163.com
"""



import pandas as pd
import scipy as sp

"""
生成一维时间序列
"""
#每一天相加
x = pd.date_range("2017/1/1", periods=30)
print(x)

data = pd.Series(sp.randn(len(x)), index=x)
print(data)
#输出前后各5个元素
print(data.head())
print(data.tail())

"""
使用日期变量
使用parse_dates或date_parse参数指定某一列作为日期列
"""
xdate = pd.read_csv("IBM.csv", index_col=0, parse_dates=True)
print(xdate[:2])

