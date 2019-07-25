"""
处理NAN数据
"""
import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1] = np.nan
print(df)
print('*' * 50)

# 删除NAN
df1 = df.dropna(axis=0, how='any')  # 有一个NAN就删除
print(df1)
df2 = df.dropna(axis=0, how='all')  # 一行/列元素全是NAN才删除
print(df2)

# 填充NAN
df3 = df.fillna(value='NUM', )  # 用value填充NAN
print(df3)

# 判断每个元素是否为NAN
print(df.isnull())
print(df.isna())

# 判断DataFrame中是否包含NAN
print(np.any(df.isna())==True)
print(np.any(df.isnull())==True)
