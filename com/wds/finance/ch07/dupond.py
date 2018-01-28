# -*- coding: utf-8 -*-
"""
Created on 2018/1/28 10:31

杜邦等式图示：绘制与比率分析相关的图形

@author: wangdongsong1229@163.com
"""

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

ticker = "Ticker"
name1 = "profitMargin"
name2 = "assetTurnover"
name3 = "equitMultiplier"

scale = 7

raw_data = {ticker: ["IBM", "DELL", "WMT"],
            name1: [0.1589 * scale, 0.0417 * scale, 0.036 * scale],
            name2: [0.8766, 1.1977, 2.31],
            name3: [6.32, 4.45, 2.6604]}

print(type(raw_data))
print(type(raw_data[ticker]))

df = pd.DataFrame(raw_data, columns = [ticker, name1, name2, name3])
f, ax1 = plt.subplots(1, figsize = (10, 5))
w = 0.75
x = [i + 1 for i in range(len(df[name1]))]

tick_pos = [i + (w / 2.) for i in x]
ax1.bar(x, df[name1], width = w, label = name1, alpha = 0.5, color = "blue")
ax1.bar(x, df[name2], width = w, bottom = df[name1], label = name2, alpha = 0.5, color = "red")
ax1.bar(x, df[name3], width = w, bottom = [i + j for i, j in zip(df[name1], df[name2])], label = name3, alpha = 0.5, color = "green")

plt.xticks(tick_pos, df[ticker])
plt.ylabel("Dupoint Identity")
plt.xlabel("Different tickers")
plt.legend(loc="upper right")
plt.title("Dupont Identity for 3 firms")
plt.xlim([min(tick_pos) - w, max(tick_pos) + w])
plt.show()
