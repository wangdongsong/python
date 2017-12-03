# -*- coding: utf-8 -*-
"""
Created on 2017/12/3 15:54

第三种方法

@author: wangdongsong1229@163.com
"""

ticker="GOOG"
import matplotlib.finance as finance
import matplotlib.mlab as mlab
import datetime

startdate = datetime.date(2014, 4, 12)
today =  enddate = datetime.date.today()

fh = finance.fetch_historical_yahoo(ticker, startdate, enddate)
r = mlab.csv2rec(fh); fh.close()
r.sort()
print(r[:2])
