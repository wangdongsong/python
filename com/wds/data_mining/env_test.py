# -*- coding: utf-8 -*-
"""
Created on 2017/12/17 17:45

环境测试

@author: wangdongsong1229@163.com
"""

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)
print(type(digits.data))
