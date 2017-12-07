# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:30:54 2017

傅里叶变换 scipy.fftpack 三下正弦函数

@author: wangdongsong1229@163.com
"""


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.fftpack import fft, ifft

x = np.linspace(0.0, 1, 500)
y = np.sin(100 * np.pi *x) + 0.5 * np.sin(150 * np.pi * x) + 0.75 * np.sin(200 * np.pi * x)
yf = fft(y)
xf = np.linspace(0.0, 0.1, 250)
plt.plot(xf, 2.0 / 200 * np.abs(yf[0:500/2]))
plt.grid()
plt.show()