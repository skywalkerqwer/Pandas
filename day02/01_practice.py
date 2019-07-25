import numpy as np
import pandas as pd
# 创建DataFrame
df = pd.DataFrame([['Snow','M',22],['Tyrion','M',32],['Sansa','F',18],['Arya','F',14]], columns=['name','gender','age'])

df1=df.copy()  # 操作不可修改 做备份处理

# snow修改年龄
df1.loc[0,'age'] = 25
df1.iloc[0, 2] = 25
print(df1)
df1.at[0, 'age'] = 26
print(df1)
df1.iat[0, 2] = 27
print(df1)

# 给上个例子学生加上score一列。分别为：80，98，67，90
df1['score'] = [80, 98, 67, 90]
print(df1)

"""
在gender后面加一列city
1. list.insert(index, obj) 
2. index -- 对象 obj 需要插入的索引位置。
3. obj -- 要插入列表中的对象
"""
col_name = df1.columns.tolist()
print(col_name)
col_name.insert(2, 'city')
# 重置列索引
df1 = df1.reindex(columns=col_name)
print(df1)
df1['city'] = ['北京','上海','广州','深圳']
print(df1)

"""
# 给上个例子学生加上一行信息
# 1 创建一个DataFrame。要注意，在这里需加入index属性，lisa F 北京 19 100
# 2 开始插值。ignore_index=True,可以帮助忽略index，自动递增。
"""
print('*'*50)
new = pd.DataFrame(data={'name':'Lisa','gender':'F','city':'北京','age':19,'score':100},index=[4])
df1_new = df1.append(new, ignore_index=True)
print(df1_new)

print('*'*50)
df1_new = pd.concat([df1,new])
print(df1_new)

# print('删除功能练习')
# # 删除第0行
df2 = df1_new.drop(labels=0, axis=0)
print(df2)
# # 删除第score列
df3 = df1_new.drop(labels='score', axis=1)
print(df3)
# 对score列排序
df4 = df1_new.sort_values(by='score', ascending=False)  # T -> 升
print(df4)
