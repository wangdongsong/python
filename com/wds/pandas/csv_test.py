# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:08:39 2017

pandas处理CSV文件

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
book_columns = ["ISBN", "Book-Titile", "Book-Author", "Year-Of-Publication", "Publisher", "Image-URL-S"]
books = read_csv(bookDataFilePath, sep=";", names=book_columns, usecols = range(6))

print(books)
print(books.dtypes)

print(users.describe())

print(books.head(10))

print(books.tail(8))

print(books[5:10])

print("Location-----------", users["Location"].head())