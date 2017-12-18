# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:38:50 2017

Panel

Panel数据结构有三个组成部分-项目（item），主轴（major axis）和次轴（minor axis）

items：指的是Panel里每个DataFrame的数据项
major axis：指的是每个DataFrame的索引（行标签）
minor axis：指的是每个DataFrame的列

@author: wangdongsong1229@163.com
"""


import numpy as np
randn = np.random.randn
from pandas import *

#通过带标签的三维数组创建Panel
workpanel = Panel(randn(2, 3, 5), items=["Firstitem", "SecondItem"], 
                 major_axis=date_range("1/1/2010", periods =3),
                 minor_axis=["A", "B", "C", "D", "E"]
                 )

print(workpanel)

#通过值是DataFrame的Python字典创建Panel
data = {"FirstItem": DataFrame(randn(4, 3)),
        "SecondItem" : DataFrame(randn(4, 2))}

Panel(data)

#orient=minor表示用DataFrame的列名作为Panel
Panel.from_dict(data, orient="minor")

df = DataFrame({"x":["one", "two", "three", "four"], "y": np.random.randn(4)})
print(df)

print(workpanel["Firstitem"])