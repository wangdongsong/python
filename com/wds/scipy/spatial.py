# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:48:01 2017

空间数据结构和算法：scipy.spatial

Delaunay三解剖分

@author: wangdongsong1229@163.com
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import scipy.spatial as spa

arr_pt = np.array([[0, 0,], [0, 1.1], [1, 0], [1, 1]])
arr1 = np.array([0., 0., 1., 1.])
arr2 = np.array([0., 1.1, 0., 1.])

triangle_result = spa.Delaunay(arr_pt)
plt.triplot(arr1, arr2, triangle_result.simplices.copy())
plt.show()

plt.plot(arr1, arr2, "ro")
plt.show()