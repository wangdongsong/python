# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:59:23 2017

datetime index

@author: wangdongsong1229@163.com
"""

import numpy as np
randn = np.random.randn
from pandas import *
from pandas.tseries.offsets import *

start = datetime(2015, 1, 1)
end = datetime(2015, 1, 1)
rng = date_range(start, end, freq = "BM")

ts = Series(randn(len(rng)), index=rng)
print(ts.index)
ts[:8].index
ts[::1].index
  
#可以直接用日期和字符串作为索引
ts['8/29/2012']
ts[datetime(2012, 7, 11):]
ts["2012"]
ts["2012-7"]

dft = DataFrame(randn(50000, 1),columns=["X"], index=date_range('20050101', periods=50000, freq='T'))
print(dft)
print(dft["2005"])