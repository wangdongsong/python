# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:48:01 2017

空间数据结构和算法：scipy.spatial

最小的

@author: wangdongsong1229@163.com
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull


randpoints = np.random.rand(25, 2)
hull = ConvexHull(randpoints)


plt.plot(randpoints[:, 0], randpoints[:, 1], "x")

for simplex in hull.simplices:
    plt.plot(randpoints[simplex,0], randpoints[simplex,1], "k")

plt.show()