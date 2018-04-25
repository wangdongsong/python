# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:22:52 2018

索引对象

pandas的索引对象管理轴标签、轴名称等其它元数据

@author: wangdongsong1229@163.com
"""

from pandas import Series 
import numpy as np
import pandas as pd

obj = Series(range(3), index = ["a", "b", "c"])

#index对象不可修改
#正因为index对象不可修改，才能使Index对象在多个数据结构之间安全共享
index = obj.index

print(index[1:])

index = pd.Index(np.arange(3))

obj2 = Series([1.5, -2.5, 0], index = index)

print(obj2.index is index)

#index有append、diff、intersection、union等操作