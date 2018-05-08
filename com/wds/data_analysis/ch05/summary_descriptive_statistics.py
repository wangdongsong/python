# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:44:26 2018

汇总和计算描述统计

用于从Series中提取单个值（sum或mean）或从DataFrame的行或列中提取一个Series

@author: wangdongsong1229@163.com
"""

from pandas import DataFrame
from pandas import Series
import numpy as np

df = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index = ["a", "b", "c", "d"], columns = ["one", "two"])

#sum，按列
print(df.sum())
#sum，按行，Nan值变为零
print(df.sum(axis = 1))
#sum，按行，有Nan值是，不参数计算，结果为Nan值
print(df.sum(axis = 1, skipna = False))

#间接统计，返回最大值的索引
print(df.idxmax())
#最小值的索引
print(df.idxmin())

#描述性统计汇总
print(df.describe())

"""
相关系数及协方差
"""
#import pandas.io.data as web
import pandas_datareader.data as web
import datetime

all_data = {}
start = datetime.datetime(2017, 1, 1) # or start = '1/1/2016'
end = datetime.date.today()

for ticker in ["AAPL", "IBM", "MSFT", "GOOG"]:
    all_data[ticker] = web.get_data_yahoo(ticker, start, end)
    
price = DataFrame({tic: data["Adj Close"] for tic, data in all_data.iteritems()})
returns = price.pct_change()

