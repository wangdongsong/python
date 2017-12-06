# -*- coding: utf-8 -*-
"""
Created on 2017/12/4 22:15

k-最邻近算法

K-最邻近算法不用从训练集数据中建立模型，它逐一比较无标签数据和每一个有标签数据，然后，取最相似的数据部分（最近的邻居），并查看其标签

@author: wangdongsong1229@163.com
"""

from numpy import random, argsort, sqrt
from pylab import plot, show
import matplotlib.pyplot as plt

def knn_search(x, data, K):
    """ k nearest neighbors"""
    ndata = data.shape[1]
    K = K if K < ndata else ndata
    sqd = sqrt(((data -x[:,:ndata]) ** 2).sum(axis=0))
    idx = argsort(sqd) # sorting
    return idx[:K]

#random dataset
data = random.rand(2, 200)
#query point
x = random.rand(2, 1)

print(x)
neig_idx=knn_search(x, data, 10)

plt.figure(figsize=(12, 12))
# plotting the data and the input point
plot(data[0,:],data[1,:],'o',  x[0,0],x[1,0],'o', color='#9a88a1', markersize=20)

# highlighting the neighbours
plot(data[0,neig_idx],data[1,neig_idx],'o',  markerfacecolor='#BBE4B4',markersize=22,markeredgewidth=1)

show()
