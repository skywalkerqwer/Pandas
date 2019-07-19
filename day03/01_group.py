import pandas as pd
import numpy as np
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
print(df)
# data1列数据，按key1来进行分组
g1 = df['data1'].groupby(df['key1'])
print(g1)  # g1 -> 分组对象
print(g1.mean())

# 一次传入多个数组 按照key1，key2分组计算
g2 = df['data1'].groupby([df['key1'], df['key2']])
print(g2.sum())

# 可以将列名（可以是字符串、数字或其他Python对象）用作分组
g3 = df.groupby('key1')  # 默认将数值型数据进行分组
print(g3.sum())

# 多个列名
g4 = df.groupby(['key1', 'key2'])
print(g4.sum())
