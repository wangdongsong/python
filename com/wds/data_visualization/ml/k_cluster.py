# -*- coding: utf-8 -*-
"""
Created on 2017/12/8 22:38

K-均值聚类

@author: wangdongsong1229@163.com
"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
import os

x = []
y = []

basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/cluster_input.csv"
with open(dataFilePath, "r") as csvf:
    reader = csv.reader(csvf, delimiter=",")
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

data = []
for i in range(0, 120):
    data.append([x[i], y[i]])

plt.figure(figsize=(10, 10))
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xlabel("X values", fontsize=14)
plt.ylabel("Y values", fontsize=14)
plt.title("Before Clustering", fontsize=20)

plt.plot(x, y, "k", color="#0080ff", markersize=35, alpha=0.6)

kmeans = KMeans(init="k-means++", n_clusters=3, n_init=10)
kmeans.fit(data)
plt.figure(figsize=(10, 10))

plt.xlabel("X values", fontsize=14)
plt.ylabel("Y values", fontsize=14)
plt.title("After K-Means Clustering (from scikit-learn)", fontsize=20)

plt.plot(x, y, "k", color="#0080ff", markersize=35, alpha=0.6)

centroids = kmeans.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=200, linewidths=3, color="b", zorder=10)
plt.show()
