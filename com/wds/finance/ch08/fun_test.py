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


"""
使用DataFrame数据类型
"""
#使用read_csv或read_table函数从外部文本文件输入数据时，得到的数据就是DataFrame类型
df = pd.DataFrame(sp.random.rand(8, 1), columns = ["A"], dtype="float32")
print(df)

#日志作为索引
index = pd.date_range("2017/1/1", periods=8)
cc = ["A", "B", "C"]
#print(type(cc))
df = pd.DataFrame(sp.random.rand(8, 3), index=index, columns=cc)
print(df)

#对IBM财经数据中日期和调整后的收盘价感兴趣，可以以日期作为索引变量
#使用0，6两列，0作为索引
xdate = pd.read_csv("IBM.csv", usecols=[0, 6], index_col=0)
print(xdate.head())
