# -*- coding: utf-8 -*-
"""
Created on 2017/12/2 17:11

美国死亡率案例

数据源：mortality1.csv

@author: wangdongsong1229@163.com
"""

import csv
import matplotlib.pyplot as plt
import os

plt.figure(figsize=(15, 13))
# 异常信息，当设置Y的刻度时无法显示图片
#plt.ylim(-2)
plt.xlim(1965, 2020)

basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/mortality1.csv"
with open(dataFilePath) as csvFile:
    mortdata = [row for row in csv.DictReader(csvFile)]

x = []
males_y = []
females_y = []

every_y = []
yrval = 1968
for row in mortdata:
    x += [yrval]
    males_y += [row["Males"]]
    females_y += [row["Females"]]
    every_y += [row["Everyone"]]
    yrval = yrval + 1

# print(males_y)
# print(females_y)
print(every_y)
print(x)

plt.plot(x, males_y, color="#1a61c3", label="Males", lineWidth=1.8)
plt.plot(x, females_y, color="#bc108d", label="Females", lineWidth=1.8)
plt.plot(x, every_y, color="#747e8a", label="Everyone", lineWidth=1.8)
plt.legend(loc=0, prop={"size":10})
plt.show()
