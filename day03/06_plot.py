import pandas as pd
import numpy as np
import matplotlib.pyplot as mp

# data = pd.Series(np.random.randn(1000), index=np.arange(1000))


data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list('ABCD'))


data = data.cumsum()
data.plot()
mp.show()