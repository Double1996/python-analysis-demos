import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('douban.csv')

# 按照豆瓣评分排序，并查看排名钱5的电影
df.sort_values('豆瓣评分', ascending=False).head()

# 豆瓣评分超过9.5分
df[df['豆瓣评分'] > 9.5]

# 上榜次数最多的导演们
df['导演'].value_counts()
