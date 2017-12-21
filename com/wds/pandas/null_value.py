# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 08:38:19 2017

处理缺失数据，缺失数据是指数据为空(null)或没有，通常用Na*表示缺失数据，*表示数值类型。

例如：N表示数值（NaN），T表示缺失时间值（NaT）

@author: wangdongsong1229@163.com
"""

import numpy as np
randn = np.random.randn
from pandas import *

df = DataFrame(randn(8, 4), index=["I", "II", "III", "IV", "VI", "VII", "VIII", "X"], columns = ["A", "B", "C", "D"])

df["E"] = "Dummy"
df["F"] = df["A"] > 0.5
print(df)

#通过增加索引来引入缺失值
df2 = df.reindex(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"])
print(df2)
print(df2["A"])


#检查是否存在缺失值
isnull(df2["A"])
df2["D"].notnull()

df3 = df.copy()
df3["timestamp"] = Timestamp("20120711")
print(df3)

#把timestamp列缺失值设置为NaT
df3.ix[["I", "III", "VIII"], ["A", "timestamp"]] = np.nan
print(df3)

#使用finllna方法填充缺失值
print(df2)
df2.fillna(0) #填充索引缺失值为0
df2["D"].fillna("missing") #为某一列填充缺失值