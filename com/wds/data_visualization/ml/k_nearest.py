# -*- coding: utf-8 -*-
"""
Created on 2017/12/6 22:13

K邻近

数据源：fruits_data.csv

给一篮水果，只有苹果、香蕉和梨。假定只有红苹果，用颜色特征区分这些水果。也可以重量区分

苹果，形状在1和3之间，重量在6和7之间
梨，形状在2和4之间，重量在5和6之间
香港，形状在3和5之间，重量在7和9之间

@author: wangdongsong1229@163.com
"""
import csv
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import os
from math import sqrt, pow

count = 0
x = []
y = []
z = []

basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/fruits_data.csv"

with open(dataFilePath, "r") as csvf:
    reader = csv.reader(csvf, delimiter= ",")
    for row in reader:
        if count > 0:
            x.append(row[0])
            y.append(row[1])
            if (row[2] == "Apple") : z.append("r")
            elif (row[2] == "Pear") : z.append("g")
            else : z.append("y")
        count += 1

#plt.figure(figsize=(11,11))
fig, ax = plt.subplots()

recs = []
classes = ["Apples", "Pear", "Bananas"]
class_colors = ["r", "g", "y"]
ax.set_title("Apples, Bananas and Pear by Weight and Shape", fontsize=18)
ax.set_xlabel("Shape category number", fontsize=14)
ax.set_ylabel("Weight in ounces", fontsize=14)

#plt.scatter(x, y, s=600, c=z)

#挑选4个水果，无标签，x、y取值A（3.5，6.2），B（2.75， 6.2）， C（2.9，7.6）， D（2.4，7.2）
dist = []
def determineFruit(xv, yv, threshold_radius):
    for i in range(1, len(x)):
        xdif = pow(float(x[i]) - xv, 2)
        ydif = pow(float(y[i]) - yv, 2)
        sqrtdist = sqrt(xdif + ydif)

        if (xdif < threshold_radius and ydif < threshold_radius and sqrtdist < threshold_radius):
            dist.append(sqrtdist)
        else:
            dist.append(99)
    pear_count = 0
    apple_count = 0
    banana_count = 0
    for i in range(1, len(dist)):
        if dist[i] < threshold_radius:
            if z[i] == "g" : pear_count += 1
            if z[i] == "r" : apple_count += 1
            if z[i] == "y" : banana_count += 1

    if(apple_count >= pear_count and apple_count >= banana_count):
        return "apple"
    if(pear_count >= apple_count and pear_count >= banana_count):
        return "pear"
    if(banana_count >= apple_count and banana_count >= pear_count):
        return "banana"

dist = []
determine = determineFruit(3.5, 6.2, 1)
x.append(3.5)
y.append(6.2)
z.append("y")
ax.scatter(x, y, s=100, c=z)
ax.annotate("A", (x[len(x)  - 1 ], y[len(y) - 1]))


print(determine)

plt.show()


