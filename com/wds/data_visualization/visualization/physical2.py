# -*- coding: utf-8 -*-
"""
Created on 2017/12/1 6:21

体育案例，数据原:qb_data.csv

线图

pyhsical的图转换X和Y轴

http://www.knapdata.com/python/qb_data.csv

@author: wangdongsong1229@163.com
"""

import os
import csv
import matplotlib.pyplot as plt

basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/qb_data.csv"

#csv have Name,Age,Year,Cmp,Att,Yds,TD

def num(s):
    try:
        return int(s)
    except ValueError:
        return 0


def getColors():
    colors = [(31, 119, 180),(1, 119, 10), (255, 119, 180),(31, 19, 20), (1, 19, 80),
              (0, 128, 0), (127, 127, 10), (255, 255, 0), (0, 0, 200), (140, 86, 70),
              (255, 191, 0), (172, 191, 201), (0, 128, 128), (125, 255, 0), (30, 30, 80),
              (31, 119, 180), (1, 119, 10), (255, 119, 180), (31, 19, 20), (1, 19, 80),
              (214, 39, 40), (206, 206, 116)
              ]

    for i in range(len(colors)):
        r, g, b = colors[i]
        colors[i] = (r / 255., g / 255., b / 255.)
    return colors

def getQbNames():
    qbnames = ['Peython Manning']
    name = ""
    i = 0
    with open(dataFilePath) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            if (row["Name"] != name and qbnames[i] != row["Name"]):
                qbnames.append(row["Name"])
                i = i + 1
    return qbnames

def readQbdata():
    resultdata = []
    with open(dataFilePath) as csvFile:
        reader = csv.DictReader(csvFile)
        resultdata = [row for row in reader]
    return resultdata

fdata = []
prevysum = 0

# function end

qbnames = getQbNames()
fdata = readQbdata()

i = 0
rank = 0
prevysum = 0
lastyr = 0
highrank=244
colorsData = getColors()

fig = plt.figure(figsize=(15,13))
ax = fig.add_subplot(111, facecolor="white")

plt.xlim(10, 744)
plt.ylim(1940, 2021)

colindex=0
lastage=20

for qbn in qbnames:
    x = []
    y = []
    prevysum = 0
    for row in fdata:
        if (row["Name"] == qbn and row["Year"] != "Career"):
            yrval = num(row["Year"])
            lastage = num(row["Age"])
            prevysum += num(row["TD"])
            lastyr = yrval
            y += [num(row["Year"])]
            x += [prevysum]
    print(y)
    print(x)
    if(rank < highrank):
        plt.plot(x, y, color = colorsData[colindex], label=qbn, linewidth=2.5)
        plt.legend(loc=0, prop={"size":10})
        colindex=(colindex+1) % 22
        plt.text(prevysum + 2, lastyr - 1, qbn+ "(" + str(prevysum) + "):" + str(lastage), fontsize=9)
    else:
        plt.plot(x, y, color = colorsData[20], label=qbn, linewidth=2.5)
        rank = rank + 1

plt.ylabel("Year", fontsize=18)
plt.xlabel("Cumulative Touch Downs", fontsize=18)
plt.title("Cumulative Touch Downs by Quarter Backs", fontsize=20)
plt.show()