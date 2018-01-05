# -*- coding: utf-8 -*-
"""
Created on 2018/1/4 6:12

网络参数

@author: wangdongsong1229@163.com
"""

import networkx as nx


g = nx.read_weighted_edgelist("data/edgelist24.csv")
degree = nx.degree(g)
g2 = g.copy()
d2 = nx.degree(g2)
for n in g2.nodes():
    if d2[n] <= 1:
        g.remove_node(n)

g2numNodes = nx.number_of_nodes(g)
g2numEdges = nx.number_of_edges(g)
print("g2numNodes:", g2numNodes)
print("g2numEdges:", g2numEdges)

d3 = nx.degree(g)
nx.draw(g,  node_size=[v * 10 for v in d3.values()])
