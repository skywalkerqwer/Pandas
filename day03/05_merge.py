import pandas as pd
import numpy as np

left = pd.DataFrame({
    'key1': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
})
right = pd.DataFrame({
    'key1': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
})
print(left)
print(right)
print('*' * 50)

# 依照key<column>合并
res = pd.merge(left, right, on='key1')
print(res)

# 增加key2
print('-' * 50)
left['key2'] = ['K0', 'K1', 'K0', 'K1']
right['key2'] = ['K0', 'K0', 'K0', 'K0']
print(left)
print(right)
print('-' * 50)

# how:['left','right','outer','inner']
# 依照多个key合并时默认按照inner方法只考虑有相同key的行进行合并
res = pd.merge(left, right, on=['key1', 'key2'])
print(res)
print(pd.merge(left, right, how='outer', indicator=True))
print(pd.merge(left, right, how='left'))
print(pd.merge(left, right, how='right'))

"""
按照index合并
"""
print('='*50)
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']},
    index=['K0', 'K1', 'K2'])

df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']},
    index=['K0', 'K2', 'K3']
)
print(df1)
print(df2)
print('='*50)

print(pd.merge(df1, df2, left_index=True, right_index=True, how='outer'))
print('.'*30)
print(pd.merge(df1, df2, left_index=True,right_index=True, how='inner'))


"""
特殊处理
"""
print('='*50)
boys = pd.DataFrame({
    'name':['bob', 'alex', 'john'],
    'age': [22, 23, 19]
})
girls = pd.DataFrame({
    'name':['bob', 'alex', 'kate'],
    'age': [22, 18, 19]
})

# 避免无法区分两个df的column
print(pd.merge(boys, girls, on='name', suffixes=['_boy', '_girl'], how='inner'))
print(pd.merge(boys, girls, on='name', suffixes=['_boy', '_girl'], how='outer'))



