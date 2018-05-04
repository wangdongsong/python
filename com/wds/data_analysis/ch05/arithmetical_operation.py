# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 09:35:59 2018

算术运算&数据对齐

@author: wangdongsong1229@163.com
"""

from pandas import Series
from pandas import DataFrame
import numpy as np
#import pandas as pd


s1 = Series([7.3, -2.5, 3.4, 1.5], index = ["a", "c", "d", "e"])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index = ["a", "c", "e", "f", "g"])

#print(s1 + s2)

df1 = DataFrame(np.arange(9).reshape((3, 3)), columns = list("bcd"), index = ["Ohio", "Texas", "Colorado"])
df2 = DataFrame(np.arange(12).reshape((4, 3)), columns = list("bde"), index = ["Utah", "Ohio", "Texas", "Oregon"])

#print(df1 + df2)

#在算术方法填充值

#print(df1.add(df2, fill_value = 0))
#print(df1.reindex(columns = df2.columns, fill_value = 0))


"""
DataFrame和Series之间的运算
"""


#广播计算
arr = np.arange(12).reshape((3, 4))
#print(arr - arr[0])

frame = DataFrame(np.arange(12.).reshape((4, 3)), columns = list("bde"), index = ["Utah", "Ohio", "Texas", "Oregon"])
series = frame.ix[0]
#print(series)

#默认情况下，DataFrame和Series之间的算术运算会将Series的索引匹配到DataFrame的列
#print(frame - series)

#如果某个索引值在DataFrame的列或Series的索引中找不到，则参与运算的两个对象就会被重新索引以形成并集
series2 = Series(range(3), index = ["b", "e", "f"])

#print(frame + series2)

#匹配行且在列上广播，则必须使用算术运算方法
series3 = frame["d"]

print(frame.sub(series3, axis = 0))

"""
函数应用和映射
"""
frame = DataFrame(np.random.randn(4, 3), columns = list("bde"), index = ["Utah", "Ohio", "Texas", "Oregon"])
f = lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.apply(f, axis = 1))
print(np.abs(frame))

#最大值、最小值
def f(x):
    return Series([x.min(), x.max()], index = ["min", "max"])

print(frame.apply(f))

#排序、排名
obj = Series(range(4), index = ["d", "a", "b", "c"])
print(obj.sort_index())
print(obj.sort_values())

#对于DataFrame，可以在任意一轴上的索引进行排序，默认升序
frame = DataFrame(np.arange(16).reshape((4, 4)), index = ["three", "one", "two", "four"], columns = ["d", "a", "b", "c"])
print(frame.sort_index())
print(frame.sort_index(axis = 1))
#按降序
print(frame.sort_index(axis = 1, ascending = False))

#指定列排序
print(frame.sort_values(by = "b", ascending = False))
print(frame.sort_values(by = ["b", "a"], ascending = False))

#排名
print(obj.rank())
print(obj.rank(method="first"))

"""
带有重复值的轴索引
"""
obj = Series(range(5), index = ["a", "a", "b", "b", "c"])
print(obj.index.is_unique)
print(obj["a"])

df = DataFrame(np.random.randn(4, 3), index = ["a", "a", "b", "b"])
print(df.ix["b"])