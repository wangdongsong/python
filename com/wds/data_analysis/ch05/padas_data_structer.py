# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:18:26 2018

padas的数据结构介绍

@author: wangdongsong1229@163.com
"""

from pandas import Series, DataFrame
import pandas as pd

"""
Series
"""

obj = Series([4, 7, 0.5, 3])
#print(obj)

#取值
#print(obj.values)
#取索引
#print(obj.index)

#创建对各个数据点的索引数据
obj2 = Series([4, 7, -1, 3], index = ["a", "b", "c", "d"])
#print(obj2)

#通过索引获取值
#print(obj2["a"])

#NumPy运算都会保留索引和值之间的链接
#print(obj2[obj2 > 3])
#print(obj2 * 2)

#Series可以看成一个定长的有序字典
#print("b" in obj2)
#print("e" in obj2)

#可以使用字典创建Series
sdata = {"oa": 100, "ob":200, "oc": 300, "od":400, "0e": 500}
obj3 = Series(sdata)
#print(sdata)

#只传入一个字典，则结果Series中的索引就是原字典的键
#oa有对应的值，其它值为NaN，即缺失值
states = ["oc", "ob", "lc", "oa", "le"]
obj4 = Series(sdata, index = states)
#print(obj4)

#缺失值检查
#print(pd.isnull(obj4))
#print(pd.notnull(obj4))
#print(obj4.isnull())

#算术运算中自动对齐不同索引数据
#print(obj3 + obj4)

obj4.name = "population"
obj4.index.name = "state"

#print(obj4)
#print("#####")
#通过索引的赋值方式修改
obj4.index = ["ac", "ab", "bc", "ba", "le"]
#print(obj4)

"""
DataFrame
"""

#创建，等长列或NumPy数组
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002],
                "pop": [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

#指定frame的序列
frame = DataFrame(data, columns = ["year", "state", "pop"])

#如果传入的列不存在，就会产生NaN值
frame2 = DataFrame(data, columns = ["year", "state", "pop", "debt"], index = ["one", "two", "three", "four", "five"])

#print(frame.columns)

#通过类似字典的方式将DataFrame的列获取为一个Series，纵向获取，列
print(frame2["state"])
print(frame.year)

#横向获取数据，行
print(frame2.ix["three"])
