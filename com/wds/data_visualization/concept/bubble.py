# -*- coding: utf-8 -*-
"""
Created on 2017/11/29 22:37

气泡图

@author: wangdongsong1229@163.com
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

#使用resources/ucdavis.csv
#print(os.path.abspath(".."))
basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/ucdavis.csv"

sns.set(style="whitegrid")
mov = pd.read_csv(dataFilePath)

x = mov.tv
y = mov.computer
z = mov.gpa

cm = plt.cm.get_cmap()
fig, ax = plt.subplots(figsize=(12, 10))

sc = ax.scatter(x, y, s=z*3, c=z, cmap=cm, linewidth=0.2, alpha=0.5)
ax.grid()
fig.colorbar(sc)

ax.set_xlabel("tv", fontsize=14)
ax.set_ylabel("computer", fontsize=14)

plt.show()

