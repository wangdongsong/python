# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:44:13 2018

MoviesLens 1M数据集

使用movies.dat、ratings.dat、users.dat三个数据源文件

@author: wangdongsong1229@163.com
"""

import pandas as pd

#不使用engine参数时，默认使用c，会出现警告信息
unames = ["user_id", "gender", "age", "occupation", "zip"]
users = pd.read_table("users.dat", sep = "::", header = None, names = unames, engine = "python")

rnames = ["user_id", "movies_id", "rating", "timestamp"]
ratings = pd.read_table("ratings.dat", sep = "::", header = None, names = rnames, engine = "python")

mnames = ["movies_id", "title", "genres"]
movies = pd.read_table("movies.dat", sep = "::", header = None, names = mnames, engine = "python")

#读取user前两行数据
#print(users[:2])

#print(ratings[:2])

#print(movies[:2])

"""
根据性别和年龄计算某部电影的平均得分
"""

#根据相同的列做数据合并
data = pd.merge(pd.merge(ratings, users), movies)

#print(data[:2])
#print(data)
#print(type(data))

#根据索引获取数据
#print(data.ix[0])

#按性别计算每部电影的平均得分，使用pivot_table
mean_ratings = data.pivot_table("rating", index = "title", columns = "gender", aggfunc = "mean")
#print(mean_ratings[:5])

#过滤评分数据不过250的电影，首先对title分组，再使用size方法得到电影分组大小series对象
ratings_by_title = data.groupby("title").size()
#print(ratings_by_title[:5])

#过滤
active_titles = ratings_by_title.index[ratings_by_title >= 2500]
#print(active_titles)
#print(len(active_titles))

#通过索引方式获取电影评分数据大于2500的电影评分
#mean_ratings = ratings_by_title.ix[active_titles]
#print(mean_ratings[:5])
mean_ratings = mean_ratings.ix[active_titles]
#print(mean_ratings[:5])

#print(mean_ratings["F"])
#了解女性观众喜欢的电影，对F列降序排列
#print(mean_ratings.columns)
#print(type(mean_ratings))
top_female_ratings = mean_ratings.sort_values(by = "F", ascending = False)
print(top_female_ratings)