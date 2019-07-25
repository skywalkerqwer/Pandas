"""
合并DF
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.zeros((3, 4)), columns=list('abcd'), index=[1,2,3],dtype='int8')
df2 = pd.DataFrame(np.ones((3, 4)), columns=list('bcde'), index=[2,3,4], dtype='int8')
print(df1)
print(df2)
print('*' * 50)

res1 = pd.concat([df1, df2], join='outer', ignore_index=True, sort=True)
print(res1)

res2 = pd.concat([df1, df2], join='inner', ignore_index=True)
print(res2)

# 左右合并
res3 = pd.concat([df1, df2], axis=1)
print(res3)
# 给定合并依据的index
res3 = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(res3)
