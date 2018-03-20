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

#print(data_array * 10)
#shape表示各维度大小的元组
#dtype数组数据类型的对象
#print(data_array.shape)
#print(data_array.dtype)

data1 = [1, 2, 3, 4, 5]
data_array1 = np.array(data1)

#print(data_array1 * 10)
#print(data_array1.shape)
#print(data_array1.dtype)

#print(np.zeros(10))
#print(np.zeros((2, 3)))

#返回未初始化的垃圾值
#print(np.empty((2, 2)))


"""
ndarray的数据类型
"""

arr1 = np.array([1, 2, 3], dtype = np.float32)
arr2 = np.array([1, 2, 3], dtype = np.int32)
#print(arr1, arr2)

#类型转换
arr = np.array([1, 2, 3, 4, 5])
#print(arr.dtype)
float_arr = arr.astype(np.float64)
#print(float_arr.dtype)


#浮点数转换成整数后，则小数部分被截断
arr = np.array([1.2, 3.3, -2.6])
#print(arr)
#print(arr.astype(np.int32))

#字符串全是数字，则可以转为数值形式
numeric_strings = np.array(["1.23", "2.6", "-3.1"], dtype = np.string_)
#print(numeric_strings.astype(float))


"""
数组和标量之间的运算
"""
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
#print(arr)
#print(arr * arr)
#print(arr + arr)
#print(arr ** 0.5)


"""
基本的索引和切片
"""
arr = np.arange(10)
#print(arr)
#print(arr[5])
#print(arr[5:8])
#赋值，修改原始数值
arr[5:8] = 10
#print(arr)

#arr_slice并非复制
#修改arr_slice的值时会同步修改arr的值
arr_slice = arr[5:8]
arr_slice[:] = 64
#print(arr_slice)
#print(arr)

#多维数组中，索引位置上的元素不再是标量，而是一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(arr2d)
#print(arr2d[2])
#获取数组中的单个元素
#print(arr2d[2][0])

#2 * 2 * 3高维数组
#根据索引取值时，如果省略后面的索引，则返回对象是一个低维的ndarray
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#取到的是2*3数组的数据
#print(arr3d[0])
#复制，不会修改原来数据
old_values = arr3d[0].copy()
arr3d[0] = 42
#print(arr3d)
arr3d[0] = old_values
#print(arr3d)

#print(arr3d[1, 0])

"""
切片索引
"""
#print(arr[1:6])
#高维数组索引切片
#print(arr2d)
#print(arr2d[:1])
#print(arr2d[:1, :3])
#print(arr2d[1,:])
#纵向取第一列
#print(arr2d[:, 1])


"""
布尔索引
"""
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
#随机生成7行4列的正态数据分布
data = np.random.rand(7, 4)
#print(data)
#假定name中的每个名字对应data中的一行数据。7个名字，7行数据
#取出对应Bob所对应的所有行
#名字为Bob的为True，其它为False
#print(names == "Bob")
#取出对应行的数据
#print(data[names == "Bob"])
#布尔索引切片
#print(data[names == "Bob", :1])
#取出非Bob名字所对应的行，两种方法
#print(names != "Bob")
#print(data[ ~(names == "Bob")])
#print(data[ ~(names == "Bob"), 1])

mask = (names == "Bob") | (names == "Will")
#print(data[mask])

#应用，将所有负值变为0
data[data < 0.5] = 0
#print(data)
data[names != "Joe" ] = 7
#print(data)


"""
花式索引
Fancy Indexing
"""
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

#选取特定子集
subarr = arr[[4, 3, 0, 6]]
print(subarr)
#负数索引
subarr = arr[[-7, -1]]
print(subarr)

arr = np.arange(32).reshape((8, 4))
#取出 的数据为(1, 0), (5, 3), (7, 1), (2, 2)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
#取出区域（1，0）， （1， 3）， （1， 1）， （1，2）.....
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
