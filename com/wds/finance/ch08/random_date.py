# -*- coding: utf-8 -*-
"""
Created on 2018/2/4 9:22

使用Pandas模块随机生产date数组序列

@author: wangdongsong1229@163.com
"""

import numpy as np
import pandas as pd

dates = pd.date_range("20171201", periods=5)
x = pd.DataFrame(np.random.rand(5, 2), index=dates, columns=("A", "B"))
print(x)

#计算两列数的基本统计信息，包括平均值、标准方差、四分位数、最大、最小等
print(x.describe())

"""
使用时间序列的平均值来代替序列中的默认值（NAN），可以使用mean和fillna函数实现
"""
numSeries = pd.Series([0.1, -0.1, np.nan, 0.2, 0.1, 0.1])
print(numSeries)

m = np.mean(numSeries)
print("mean:", m)

#使用序列的平均值填充nan所在的位置
numSeries = numSeries.fillna(m)
print(numSeries)
