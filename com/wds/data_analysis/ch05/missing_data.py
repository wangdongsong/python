# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:39:27 2018

处理缺失值

@author: wangdongsong1229@163.com
"""

from pandas import Series
from pandas import DataFrame
import numpy as np
from numpy import nan as NA

string_data = Series(["aardvardk", "artichoke", np.nan, "avocado"])

print(string_data.isnull())

string_data[0] = None
           
print(string_data.isnull)


#滤除缺失数据
data = Series([1, NA, 3.5, NA, 7])
print(data.dropna())

#也可以通过布尔表达式索引达到同样的交易
print(data[data.notnull()])


"""
DataFrame处理缺失值
"""
data = DataFrame([[1, 6.5, 3], [1, NA, NA], [NA, NA, NA], [NA, 6.5, 3]])

#dropna默认丢弃任何含NA值的行
cleaned = data.dropna()

#传入how=all将只丢弃全为NA的行
how_all = data.dropna(how = "all")

#丢弃列
data[4] = NA
col_all = data.dropna(axis = 1, how = "all")

#过滤涉及时间序列的数据
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
thresh_data = df.dropna(thresh = 3)


"""
填充缺失数据
"""
#fillna方法
df.fillna(0)