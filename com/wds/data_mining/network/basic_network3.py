# -*- coding: utf-8 -*-
"""
Created on 2018/1/4 6:38

分析子图

@author: wangdongsong1229@163.com
"""

import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_weighted_edgelist("data/edgelist24.csv")
degree = nx.degree(g)
#是否完全连通
print(nx.is_connected(g))
#查看网络图中有多少数量的子图（非连通）
print(nx.number_connected_components(g))
#取出每个连通的成分子图，按照其中的节点数排序
graphs = list(nx.connected_component_subgraphs(g))
graphsSorted = sorted(graphs, key=len, reverse=True)
for graph in graphsSorted[0:5]:
    #输出子图的节点数
    print("num nodes:", nx.number_of_nodes(graph))
    #输出度数
    print("degree:", nx.degree(graph))

i = 0
for graph in graphsSorted[0:5]:
    i += 1
    print("num nodes in graph", i, ":", nx.number_of_nodes(graph))
    graphDegree = nx.degree(graph)

    #画图
    f1 = plt.figure()
    nx.draw(graph, node_sizes=[v * 10 for v in graphDegree.values()], with_labels=True, font_size=8)
    filename1 = "graphLabels" + str(i) + ".png"
    f1.savefig(filename1)

f2 = plt.figure()
nx.draw(graph, node_size=[v * 10 for v in graphDegree.values()])
filename2 = "graph" + str(i) + ".png"
f2.savefig(filename2)