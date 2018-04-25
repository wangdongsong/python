# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:03:47 2018

DataFrame、Series基本操作

@author: wangdongsong1229@163.com
"""

from pandas import Series
from pandas import DataFrame
#import pandas
import numpy as np

"""

重新索引 reindex、ix

"""

#重新索引，reindex
obj = Series([4.5, 7.2, -5.3, 3.6], index = ["d", "b", "a", "c"])
#print(obj)
obj.reindex()
#print(obj)


#obj reindex填充值为0
obj2 = obj.reindex(["a", "b", "c", "d", "e"])
#print(obj2)
obj2 = obj.reindex(["a", "b", "c", "d", "e"], fill_value = 0)
#print(obj2)

#重新索引时插值处理
obj3 = Series(["blue", "purple", "yellow"], index = [0, 2, 4])
#print(obj3)
obj4 = obj3.reindex(range(6), method = "pad")
#print(obj4)

#修改行、列索引
frame = DataFrame(np.arange(9).reshape((3, 3)), index = ["a", "c", "d"], columns = ["Ohio", "Texas", "California"])
#print(frame)
#frame增加b的行索引
frame2 = frame.reindex(["a", "b", "c", "d"])
#print(frame2)
#reindex列索引
states = ["Texas", "Utah", "California"]
frame3 = frame.reindex(columns=states)
#print(frame3)

#同时对行、列进行重新索引，而插值只能按行应用
frame4 = frame.reindex(index = ["a", "b", "c", "d"], method = "ffill", columns = states)
#print(frame4)

frame5 = frame.reindex(index = ["a", "b", "c", "d"], columns = states)
#print(frame5)
frame6 = frame.ix[["a", "b", "c", "d"], states]
#print(frame6)

"""

丢弃指定轴上的项

"""
obj = Series(np.arange(5), index = ["a", "b", "c", "d", "e"])
drop_obj = obj.drop("c")
drop_obj = obj.drop(["b", "d"])

#对于DataFrame，可以删除任意轴上的索引值
data = DataFrame(np.arange(16).reshape((4, 4)), index = ["Ohio", "Colorado", "Utah", "New York"], columns = ["one", "tow", "three", "four"])
data2 = data.drop(["Ohio", "Colorado"])


"""

"""