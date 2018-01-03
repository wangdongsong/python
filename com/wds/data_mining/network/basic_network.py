# -*- coding: utf-8 -*-
"""
Created on 2018/1/3 20:46

简单的网络指标

@author: wangdongsong1229@163.com
"""

import networkx as nx
import operator

# 读入数据，并保存为一个图变量
g = nx.read_weighted_edgelist("data/edgelist24.csv")
# 生成一个Python字典，元素是节点及其度数
degree = nx.degree(g)
# 节点数量、网络的边数、最小度数、最大度数
numNodes = nx.number_of_nodes(g)
numEdges = nx.number_of_edges(g)
minDegree = min(degree.items())
maxDegree = max(degree.values())

# 共有719个节点，1519条边，最小度数为1，最大度数为30
print("numNodes:", numNodes)
print("numEdges:", numEdges)
print("minDegree:", minDegree)
print("maxDegree:", maxDegree)

# 从最高度数开始排序，打印度数最高达到10个节点
degreeSorted = sorted(degree.items(), key=operator.itemgetter(1), reverse=True)
print(degreeSorted[0:9])