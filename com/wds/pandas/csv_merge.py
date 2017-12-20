# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:08:39 2017

pandas处理CSV merge

@author: wangdongsong1229@163.com
"""

import numpy as np
randn = np.random.randn
from pandas import *
import os

basePath = os.path.abspath(".")

userDataFilePath = basePath + "/resources/BX-Users.csv"
user_columns = ["User-ID", "Location", "Age"]
users = read_csv(userDataFilePath, sep=";", names=user_columns)

bookRatingDataFilePath = basePath + "/resources/BX-Book-Ratings.csv"
rating_columns = ["User-ID", "ISBN", "Rating"]
ratings = read_csv(bookRatingDataFilePath, sep=";", names=rating_columns)

bookDataFilePath = basePath + "/resources/BX-Books.csv"
book_columns = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-S"]
books = read_csv(bookDataFilePath, sep=";", names=book_columns, usecols = range(6))

#创建合并的DataFrame
book_ratings = merge(books, ratings)
users_ratings = merge(book_ratings, users)

most_rated = users_ratings.groupby("Book-Title")#.size().sort_values(ascending=False)[:25]

print("most_rated=", most_rated)

#print(users_ratings.Title.value_counts()[:17])

#按照评分等级Rating与均值mean排序
book_stats = users_ratings.groupby("Book-Title").agg({"Rating":[np.size, np.mean]})
print(book_stats.head())
