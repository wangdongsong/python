# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:36:26 2017

scipy.spatial

KDTree

@author: wangdongsong1229@163.com
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

vertx = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
tree_create = KDTree(vertx)
tree_create.query([1.1, 1.1])
x_vals = np.linspace(0.5, 3.5, 31)
y_vals = np.linspace(0.5, 3.5, 33)
xgrid, ygrid = np.meshgrid(x_vals, y_vals)

xy = np.c_[xgrid.ravel(), ygrid.ravel()]

plt.pcolor(x_vals, y_vals, tree_create.query(xy)[1].reshape(33, 31))
#plt.plot(points[:, 0], points[:, 1], "ko")
plt.show()
