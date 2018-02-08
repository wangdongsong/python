# -*- coding: utf-8 -*-
"""
Created on 2018/2/1 21:39

雅虎财经历史数据

@author: wangdongsong1229@163.com
"""
import matplotlib.finance as finance
import datetime
import pandas as pd

date1 = datetime.date(2013,1,1)
date2 = datetime.date.today()

#finance.urlopen()
price = finance.quotes_historical_yahoo_ochl("IBM", date1, date2)
#price = finance.urlopen("https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1514902230&period2=1517580630&interval=1d&events=history&crumb=spaq.8Gf0aV")
print(price)
"""
name = ["Date", "Open","High","Low","Close","Adj Close","Volume"]
ibm_data = pd.read_csv("IBM.csv", header = 0)
print(type(ibm_data))
print(ibm_data["High"] - ibm_data["Low"])
print(ibm_data["Date"])
print(ibm_data["Close"])
"""