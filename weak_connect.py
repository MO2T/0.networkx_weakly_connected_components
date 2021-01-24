# -*- coding: utf-8 -*-
# 导入模块包
import numpy as np
import networkx as nx
import pandas as pd
from networkx.algorithms import community
import random
from datetime import datetime

# 弱连通算法开始
a = datetime.now()
print("弱连通开始计算", a)
# 建立一个新图
Graph = nx.DiGraph()
f = open('./data/rela.csv', encoding='utf-8')
s = []
for line in f:
    L1 = line.strip('\n')
    L2 = L1.split(',')
    Graph.add_weighted_edges_from([tuple([L2[0], L2[1], 1])])
    s.append(L2)
print('图节点信息：', Graph.number_of_nodes())
print('图关系信息：', Graph.number_of_edges())
# 划分社区
t = 0
result = pd.DataFrame(columns=['id', 'c_id'])
for i in nx.weakly_connected_components(Graph):
    r = pd.DataFrame(i)
    r.columns = ['id']
    r['c_id'] = t
    t = t + 1
    result = pd.concat([result, r])
print('社区个数为：', t)
b = datetime.now()
print('花费时间', (b - a).seconds, 's')
#print(nx.simple_cycles(Graph))