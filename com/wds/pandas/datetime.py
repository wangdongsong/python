# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 20:30:04 2017

Pandas datetime

@author: wangdongsong1229@163.com
"""

import numpy as np
randn = np.random.randn
from pandas import *

#创建日期区间，从06/03/2015开始152个小时
range_date = date_range("6/3/2015", periods=152, freq="H")
range_date = date_range("6/3/2015 01:10:00", periods=152, freq="H")
#print(range_date)

#时间作为索引
ts = Series(randn(len(range_date)), index=range_date)
#print(ts.head)

#把索引值的频率更新为40分钟
converted = ts.asfreq("40Min", method="pad")
converted.head()
#ts.resample("D", how="mean")
dates = [datetime(2015, 6, 10), datetime(2015, 6, 11), datetime(2015, 6, 12)]
ts = Series(np.random.randn(3), dates)
#type(ts.index)
#print(ts.index)
#print(ts)


#转换时间戳
#print(to_datetime(Series(["Jul 31, 2014", "2015-01-08", None])))
#print(to_datetime(["1995/10/31", "2015.11.30"]))

#日期数值如果按照月-日-年形式，就用dayfirst=True
print(pandas.to_datetime(["01-01-2015 11:30"], dayfirst=True).date)
print(to_datetime(["01-01-2015","03-14-2007"], dayfirst=True).date)

#如果日期数值中有无效值，使用coerce=True转换成Nat
#print(to_datetime(["2012-07-11", "xyz"]))
print(to_datetime(["2012-07-11", "xyz"], errors="coerce").date)

#混合数据类型无法正确处理
#print(to_datetime([1, "1"]))

#纪元时间戳(Epoch timestamp : 整型与浮点型纪元时间戳可以转换成标准时间戳)
#默认使用纳秒，可以转换成秒与微秒
#初始时间为01/01/1970

print(to_datetime([1449720105, 1449806505], unit="s").date)

print(to_datetime([1349720105100], unit="ms").date)


print(to_datetime([8]).date)

print(to_datetime([8, 4.41], unit="s").date)

#取一定范围的日期

dates = [datetime(2015, 4, 10), datetime(2015, 4, 11), datetime(2015, 4, 12)]
index = DatetimeIndex(dates)
index = Index(dates)
print("index",index)

index = date_range("2010-1-1", periods=1700, freq="M")
print(index)

start = datetime(2005, 1,1)
end = datetime(2015, 1, 1)
print("start-end", date_range(start, end))