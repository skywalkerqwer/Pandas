import numpy as np
import pandas as pd


# 核心代码，设置显示的最大列、宽等参数，
# 消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)


# 获取电影数据表格
users = pd.read_csv('../pd_data/users.dat',
                    header=None,  # 不使用文件中的某行作为列名称
                    names=['UserID', 'Gender','Age', 'Occupation', 'Zip-code'],  # 自定义列名称
                    sep='::',
                    engine='python')
print(users.head())  # 读取前5行数据


# 获取csv文件,定义列名为width,height,category
data = pd.read_csv('../pd_data/iris.csv',
                   header=None,
                   names=['width', 'height', 'category'],
                   engine='python')  # 默认分隔符为 ","
print(data.head())

# 修改
data.iloc[1, 2] = 1
data.to_csv('iris1.csv')  # 保存修改

# 获取表格文件
excel = pd.read_excel('data.xlsx')
print(excel)


