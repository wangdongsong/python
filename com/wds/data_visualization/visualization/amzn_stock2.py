# -*- coding: utf-8 -*-
"""
Created on 2017/12/3 15:01

amzn stock 图
数据源：AMZN.csv

@author: wangdongsong1229@163.com
"""
from pylab import plotfile, show, gca
import os
import matplotlib.cbook as cbook


basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/AMZN.csv"
fname = cbook.get_sample_data(dataFilePath, asfileobj=False)
plotfile(fname, (0,4,6), plotfuncs={6:'bar'})
show()