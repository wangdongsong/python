# -*- coding: utf-8 -*-
"""
Created on 2017/12/8 6:46

主成分分析-sklearn

@author: wangdongsong1229@163.com
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = load_iris()
X = data.data

X[:, 0] /= 2.54

X[:, 1] /= 100

from sklearn.decomposition import PCA

def scikit_pca(X):
    X_std = StandardScaler().fit_transform((X))

    sklearn_pca = PCA(n_components=2)
    X_transf = sklearn_pca.fit_transform(X_std)

    plt.figure(figsize=(11, 11))
    plt.scatter(X_transf[:, 0], X_transf[:, 1], s=600, color="#8383c4", alpha=0.54)
    plt.title("PCA via scikit-learn (useing SVD)", fontsize=20)
    plt.xlabel("Petal Width", fontsize=15)
    plt.ylabel("Sepal Length", fontsize=15)
    plt.show()

scikit_pca(X)
