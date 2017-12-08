# -*- coding: utf-8 -*-
"""
Created on 2017/12/7 22:33

主成分分析（principal component analysis, PCA）

源数据：height_weight.csv

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
import csv
import os

gender = []
x = []
y = []

basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/height_weight.csv"

with open(dataFilePath) as csvf:
    reader = csv.reader(csvf, delimiter = ",")
    count = 0
    for row in reader:
        if count > 0:
            if row[0] == "f" : gender.append(0)
            else: gender.append(1)

            height = float(row[1])
            weight = float(row[2])

            x.append(height)
            y.append(height)
        count += 1

plt.figure(figsize=(11, 11))
plt.scatter(y, x, c=gender, s = 300)
plt.grid(True)
plt.xlabel("Weight", fontsize=18)
plt.ylabel("Height", fontsize=18)

plt.title("Height vs Weight (College Stuednts)", fontsize=20)
plt.legend()
plt.show()


