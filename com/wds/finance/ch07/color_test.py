# -*- coding: utf-8 -*-
"""
Created on 2018/1/31 21:16

有效使用颜色

@author: wangdongsong1229@163.com
"""
import matplotlib.pyplot as plt
import numpy as np

A_EPS = (5.02, 4.54, 4.18, 3.73)
B_EPS = (1.35, 1.88, 1.35, 0.73)

ind = np.arange(len(A_EPS))
width = 0.40

fig, ax = plt.subplots()
A_Std = B_Std = (2, 2, 2, 2)

rects1 = ax.bar(ind, A_EPS, width, color = "r", yerr = A_Std)
rects2 = ax.bar(ind + width, B_EPS, width, color = "y", yerr = B_Std)

ax.set_ylabel("EPS")
ax.set_xlabel("Year")
ax.set_title("Diluted EPS ... Items")
print(ind + width)
ax.set_xticks(ind + width)
ax.set_xticklabels(("2012", "2011", "2010", "2009"))
ax.legend((rects1[0], rects2[0], ("W-Mart", "DELL")))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, "%d"%int(height), ha = "center", va = "bottom")

autolabel(rects1)
autolabel(rects2)

plt.show()


