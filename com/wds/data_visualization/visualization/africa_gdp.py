# -*- coding: utf-8 -*-
"""
Created on 2017/12/3 12:06

非洲GDP排名，方形图

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
import matplotlib.cm
import random
import squarify

x = 0
y = 0
width = 950.
height = 733.
norm_x = 1000
norm_y = 1000

fig = plt.figure(figsize=(15, 13))
ax = fig.add_subplot(111, axisbg="white")

initvalues = [285.4, 118.4, 173, 140.6, 91.4, 75.5, 62.3, 39.6, 29.4, 28.5, 26.2, 22.2]
values = initvalues
labels = ["South Aftrica", "Egypt", "Nigeria", "Algeria", "Morocco", "Angola", "Libya", "Tunisia", "Kenya", "Ethiopia", "Ghana", "Cameron"]

colors = [(31, 119, 180),(1, 119, 10), (255, 119, 180),(31, 19, 20), (1, 19, 80),
              (0, 128, 0), (127, 127, 10), (255, 200, 0), (0, 100, 200), (140, 86, 70),
              (255, 191, 250), (172, 191, 201)]

for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r / 255., g / 255., b / 255. )

values.sort(reverse=True)
values = squarify.normalize_sizes(values, width, height)
rects = squarify.padded_squarify(values, x, y, width, height)

cmap = matplotlib.cm.get_cmap()

color = [cmap(random.random()) for i in range(len(values))]
x = [rect["x"] for rect in rects]
y = [rect["y"] for rect in rects]
dx = [rect["dx"] for rect in rects]
dy = [rect["dy"] for rect in rects]

ax.bar(x, dy, width=dx, bottom=y, color=colors, label=labels)

va = "center"
idx = 1
#print(len(rects))
for l, r, v in zip(labels, rects, initvalues):
    x, y, dx, dy = r["x"], r["y"], r["dx"], r["dy"]
    ax.text(x + dx / 20, y + dy / 2 + 10, str(idx) + "-> " + l, va = "center", ha="center", color="white", fontsize=10)
    ax.text(x + dx / 20, y + dy / 2 - 30, "($" + str(v) + "b)", va = "center", ha="center", color="white", fontsize=12)
    idx = idx + 1
    #print(idx)

# ax.set_xlim(0, norm_x)
# ax.set_ylim(0, norm_y)
plt.show()