# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:27:05 2018

使用example.txt数据

@author: wangdongsong1229@163.com
"""

import json
import os

#获取当前路径
path = os.path.abspath(".") + "\example.txt"
print(type(path))
print(path)

records = [json.loads(line) for line in open(path)]
#print(type(records))
print(len(records))
for l in records:
    #print(l)
    try:
        print(l["c"])
    except:
        print("no c")

#通过列表推导式取时区字段
#并不是所有数据都有时区，增加if判断
time_zones = [record["tz"] for record in records if "tz" in record]
#print(time_zones)
#print(type(time_zones))


#统计时区并取前10个

"""
使用Python标准库
"""
counts = {}
for x in time_zones:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
#print(counts)


"""
使用pandas库
"""
from collections import defaultdict
counts = defaultdict(int) #所有值均会被初始化为0
for x in time_zones:
    counts[x] += 1
#print(counts)

"""
取前10
"""
topn = 10
value_key_pairs = [(count, tz) for tz, count in counts.items()]
sort = value_key_pairs.sort()
#print(sort[-topn:])

"""
标准库Counter类
"""
print("--------------------------")
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(2))

"""
对时区计数
"""
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

frame = DataFrame(records)
print(frame["tz"][:10])
#获取明细
tz_counts = frame["tz"].value_counts()
print(tz_counts)
#缺失值处理
clean_tz = frame["tz"].fillna("Missing")
clean_tz[clean_tz == ""] = "Unknown"
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
#用图形展示这些数据
tz_counts[:10].plot(kind="barh", rot=0)

#其它处理，示例如下：
print(frame["a"][1])
print(frame["a"][50])

#获取并解析User_Agent
user_agent_results = Series([x.split()[0] for x in frame.a.dropna()])
print(user_agent_results[:5])

#清除agent为空的数据
clean_frame = frame[frame.a.notnull()]
print("----", str(clean_frame["a"][0]))
operating_sys = np.where(clean_frame["a"].str.contains("Windows"), "Windows", "Not Windows")
print("++++", operating_sys[:5])

#对时区和操作系统分组计数
by_tz_os = clean_frame.groupby(["tz", operating_sys])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

#选择最常出现的时区
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
#按这个顺序take元素
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)