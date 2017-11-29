# -*- coding: utf-8 -*-

import numpy as np
x = np.array([4, 432, 21], int)
print(x)

x2d = np.array(((100, 200,300), (111,222,333), (123, 456, 789), (555, 555, 555)))
print(x2d)

#3 * 3
print(x2d.shape)

#数据类型
print(x2d.dtype)

#每项的大小，是指数组中每个元素的字节长度
print(x2d.itemsize)

#维度
print(x2d.ndim)

#Python缓存对象，指向数组数据的起始位置
print(x2d.data)

# 数组切片
print(x2d[1:, 1])

# 循环
for row in x2d:
    print(row)


# 数据变形与转换
print("数据变形与转换")
print(x2d)
x2d.ravel
print("--ravel--")
print(x2d)
print("--resize(3,6)--")
x2d.resize((4, 3))
print(x2d)
print("--reshape(3,3)--")
x2d.reshape(4, 3)
print(x2d)
print("--shape--")
x2d.shape=(6, 2)
print(x2d)

