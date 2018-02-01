# -*- coding: utf-8 -*-
"""
Created on 2018/2/1 21:39

雅虎财经历史数据

@author: wangdongsong1229@163.com
"""
import matplotlib.finance as finance
import datetime

date1 = datetime.date(2013,1,1)
date2 = datetime.date.today()

price = finance.fetch_historical_yahoo("IBM", date1, date2)

print(price)