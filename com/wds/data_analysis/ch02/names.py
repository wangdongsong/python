# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:42:50 2018

1880-2010年间全美婴儿姓名

数据源：yob1880.txt

@author: wangdongsong1229@163.com
"""

import pandas as pd
import os

#数据文件以逗号分隔，使用read_csv的方式处理
names1880 = pd.read_csv("yob1880.txt", names=["names", "sex", "births"])

print(names1880[:2])

#年births统计数据
births1880 = names1880.groupby("sex").births.sum()
print(births1880)


"""
读取所有文件
"""
#2016为最后一个年度
years = range(1880, 2017)

pieces = []
columns = ["name", "sex", "births"]

for year in years:
    path = os.path.abspath(".") + "/names/yob%d.txt" % year
    #print(path)
    frame = pd.read_csv(path, names = columns)
    
    frame["year"] = year
    #print(type(frame))
    pieces.append(frame)

#将数据整合到单个DataFrame中
#concat默认按行将多个DataFrame组合到一起
#必须指定ignore_index=True，不需要保留原始行号，得到全的数据
names = pd.concat(pieces, ignore_index = True)
#print(type(pieces))

#按年份分组，对性别做sum聚合
total_births = names.pivot_table("births", rows = "year", cols = "sex", aggfunc = sum)
print(total_births)