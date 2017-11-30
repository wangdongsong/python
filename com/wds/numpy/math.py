# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:34:12 2017

NumPy的数学模块

@author: wangdongsong1229@163.com
"""
import numpy as np
from numpy import linalg as LA

arr2d = np.array(((100,200,300), (111,222,333), (129, 461, 795)))
eigh_val, eig_vec = LA.eig(arr2d)

LA.norm(arr2d)
LA.det(arr2d)
LA.inv(arr2d)

arr1 = np.array([[2, 3], [3, 4]])
arr2 = np.array([4, 5])

results = np.linalg.solve(arr1, arr2)

print(results)

np.allclose(np.dot(arr1, results), arr2)