# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:27:42 2017

傅里叶变换 scipy.fftpack

对实数或复数据序列的离散傅里叶变换和离散傅里叶变换可以分别用fft和ifft函数计算，fft是指快速傅里叶变换

@author: wangdongsong1229@163.com
"""

import numpy as np
from scipy.fftpack import fft, ifft

x = np.random.random_sample(5)
y = fft (x)
print(y)

yinv = ifft(y)
print(yinv)