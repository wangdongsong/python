# -*- coding: utf-8 -*-
"""
Created on 2017/12/2 21:48

美国死亡率，按年龄分组

数据源:mortality2.csv

@author: wangdongsong1229@163.com
"""
import csv
import os
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(15, 13))
plt.ylim(35, 102)
plt.xlim(1965, 2015)

colors = ["#168cf8", "#169cf9", "#170cf0", "#171cf1", "#172cf2", "#173cf3", "#255cf9"]
label = ["< 25", " 25-44", "45-54", "55-64", "65-74", "75-84", ">85"]


basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/mortality2.csv"
with open(dataFilePath) as csvFile:
    mortdata = [row for row in csv.reader(csvFile)]

x = []
for row in mortdata:
    yrval = int(row[0])
    if (yrval == 1969):
        y = [[row[1]],[row[2]],[row[3]],[row[4]],[row[5]],[row[6]],[row[7]]]
    else:
        for col in range (0, 7):
            print(y)
            y[col] += [row[col + 1]]
    x += [yrval]

for col in range(0, 7):
    if (col == 1):
        plt.plot(x, y[col], color=colors[col], label=label[col], linewidth=3.8)
    else:
        plt.plot(x, y[col], color=colors[col], label=label[col], linewidth=2)

plt.legend(loc=0, prop={"size":10})
plt.show()