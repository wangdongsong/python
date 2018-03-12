# -*- coding: utf-8 -*-
"""

NumPy基础

Created on Fri Mar  9 16:17:18 2018

@author: wangdongsong1229@163.com
"""

import numpy as np

"""
NumPy的ndarray：一种多维数组对象
"""

"""
ndarry创建
"""

data = ([0.9, 0.2, 0.8],
        [0.5, -0.1, 0.7])

data_array = np.array(data)

print(data_array * 10)
#shape表示各维度大小的元组
#dtype数组数据类型的对象
print(data_array.shape)
print(data_array.dtype)

data1 = [1, 2, 3, 4, 5]
data_array1 = np.array(data1)

print(data_array1 * 10)
print(data_array1.shape)
print(data_array1.dtype)

print(np.zeros(10))
print(np.zeros((2, 3)))

#返回未初始化的垃圾值
print(np.empty((2, 2)))


"""
ndarray的数据类型
"""

arr1 = np.array([1, 2, 3], dtype = np.float32)
arr2 = np.array([1, 2, 3], dtype = np.int32)
print(arr1, arr2)

#类型转换
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)


#浮点数转换成整数后，则小数部分被截断
arr = np.array([1.2, 3.3, -2.6])
print(arr)
print(arr.astype(np.int32))

#字符串全是数字，则可以转为数值形式
numeric_strings = np.array(["1.23", "2.6", "-3.1"], dtype = np.string_)
print(numeric_strings.astype(float))