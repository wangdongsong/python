import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#使用resources/ucdavis.csv
#print(os.path.abspath(".."))
basePath = os.path.abspath("..")
dataFilePath = basePath + "/resources/ucdavis.csv"
print(dataFilePath)
students = pd.read_csv(dataFilePath)
g = sns.FacetGrid(students, hue="gender", palette="Set1", size=6)
g.map(plt.scatter, "gpa", "computer", s=250, linewidth=0.65, edgecolor="white")
g.add_legend()
#Pycharm必须调用，不然无法显示图片
plt.show()