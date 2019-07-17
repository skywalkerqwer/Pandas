import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
s1  = pd.Series([90,86,70],index=['Leo','Kate','John'])
print(s1)
# 2.numpy中的ndarray：
s2 = pd.Series(np.random.randn(5),index=list('ABCDE'))
print(s2)
# 3.数字创建
s3 = pd.Series(6)
print(s3)
# 4.创建一组DataFrame数据-date_range创建时间
date = pd.date_range(start='20100101', periods=6,freq='M')
print(date)
df = pd.DataFrame(index=date, columns=list('abcd'), data=np.random.randn(6,4))
print(df)
