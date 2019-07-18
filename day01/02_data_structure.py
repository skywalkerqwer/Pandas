import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
s1 = pd.Series([90, 86, 70], index=['Leo', 'Kate', 'John'])
print(s1)
# 查找
# 通过绝对位置
print(s1[0])
# 通过标签
print(s1['Kate'])

# 2.numpy中的ndarray：
s2 = pd.Series(np.random.randn(5), index=list('ABCDE'))
print(s2)

# 3.数字创建
s3 = pd.Series(6)
print(s3)

# 4.创建一组DataFrame数据-date_range创建时间
date = pd.date_range(start='20100101', periods=6, freq='M')
print(date)
df = pd.DataFrame(index=date, columns=list('abcd'), data=np.random.randn(6, 4))
print(df)
# 数据的列名
print('_____________',df.columns)
# 数据的形状
print(df.shape)

# 查找DataFrame数据
# 单列、多列数据
print(df.a)
print(df[['a', 'b']])
# 选择行数据
print(df[0:3])
print(df.head(1))

# 行列同时选择
# 通过loc方式查找
print(df.loc['2010-01-31':'2010-4-30', ['a', 'b']])  # 标签查找
# 通过iloc方式查找
print(df.iloc[:4, [0, 1]])  # 绝对位置查找
# 通过ix方式查找
print(df.ix[:4, ['a', 'b']])  # 两者都可以接收
# 通过表达式查找
print(df.loc[df.index<'20100430'])
print('-'*50)
print(df.loc[:,df.columns=='b'])
