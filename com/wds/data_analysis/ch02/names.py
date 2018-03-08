# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:42:50 2018

1880-2010年间全美婴儿姓名

数据源：yob1880.txt

@author: wangdongsong1229@163.com
"""

import pandas as pd
import numpy as np
import os

#数据文件以逗号分隔，使用read_csv的方式处理
names1880 = pd.read_csv("yob1880.txt", names=["names", "sex", "births"])

print(names1880[:2])

#年births统计数据
births1880 = names1880.groupby("sex").births.sum()
#print(births1880)


"""
读取所有文件
"""
#2016为最后一个年度
years = range(1880, 2017)

pieces = []
columns = ["name", "sex", "births"]

for year in years:
    path = os.path.abspath(".") + "/names/yob%d.txt" % year
    #print(path)
    frame = pd.read_csv(path, names = columns)
    
    frame["year"] = year
    #print(type(frame))
    pieces.append(frame)

#将数据整合到单个DataFrame中
#concat默认按行将多个DataFrame组合到一起
#必须指定ignore_index=True，不需要保留原始行号，得到全的数据
names = pd.concat(pieces, ignore_index = True)
#print(type(pieces))

#按年份分组，对性别做sum聚合
total_births = names.pivot_table("births", index = "year", columns = "sex", aggfunc = sum)
#print(total_births)


#插入一个prop列，用于存放指定名字的婴儿数相对于总出生数的比例。
#0.02表示每100个婴儿中有2个取了当前的名字
#births是整数，在计算分工时 ，将分子、分母转换成浮点数
def add_prop(group):
    #整数除法会向下调整
    births = group.births.astype(float)
    
    group["prop"] = births / births.sum()
    
    return group

add_names = names.groupby(["year", "sex"]).apply(add_prop)
#print(names[:2])

#处理prop比例时，做一般性检查，验证所有分组的prop的总和是否为1
isOne = np.allclose(add_names.groupby(["year", "sex"]).prop.sum(), 1)
print(isOne)


#获取Top1000数据子集
#针对sex/year组合的前1000个名字

def get_top1000(group):
    #return group.sort_index(by="births", ascending=False)[:1000]
    return group.sort_values(by="births", ascending=False)[:1000]

grouped1000 = add_names.groupby(["year", "sex"])
top1000 = grouped1000.apply(get_top1000)

#print(top1000[:2])

"""
分析命名趋势
"""
#将Top1000的名字分为男女两个部分
boys = top1000[top1000.sex == "M"]
girls = top1000[top1000.sex == "F"]

#按年和name统计
total_births = top1000.pivot_table("births", index = "year", columns = "name", aggfunc = sum)

subset = total_births [["John", "Harry", "Mary", "Marilyn"]]
subset.plot(subplots = True, figsize = (12, 10), grid = False, title = "Number of births per year")

"""
评估命名多样性的增长

从《分析命名趋势》图中可以看出取常见名字的越来越少
1980年后起相同的常见的名字越来越少，可以从数据中行到验证，一个办法是计算最流行的1000个名字所占的比例，按year和sex进行聚合并绘图
"""
table = top1000.pivot_table("prop", index = "year", columns = "sex", aggfunc = sum)
table.plot(title = "Sum of table1000.prop by year and sex", yticks = np.linspace(0, 1.2, 13), xticks = range(1880, 2020, 10))

#另一种方法：计算占总出生人数前50%的不同名字的数量，只考虑2010年男孩的名字
#df = boys[boys.year == 2010]
#prop_cumsum = df.sort_index(by = "prop", ascending = False).prop.cumsum()
#prop_cumsum.searchsorted(0.5) + 1

def get_quantile_count(group, q = 0.5):
    group = group.sort_index(by = "prop", ascending=False)
    #特别说明，后面要取[0]，数据类型为object
    return group.prop.cumsum().searchsorted(q)[0]

diversity = top1000.groupby(["year", "sex"]).apply(get_quantile_count)
diversity = diversity.unstack("sex")
print(diversity.head())

diversity.plot(title = "Number of popular names in top 50%")













