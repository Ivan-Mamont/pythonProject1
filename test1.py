


import numpy as np

import pandas as pd

file = 'test.xlsx'
xl = pd.ExcelFile(file)
df = xl.parse()
#df1 = df[['Date']]

#df.set_index(['Дата продажи'], drop=True, inplace=True)
#df.index = pd.DatetimeIndex(data=df.index)
print(df)

