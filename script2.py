print('loading specific libraries')
import pandas as pd
import os

print('settings')
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


print('Create second dataframe : df2')
df2 = pd.DataFrame({'b': [5, 2, 0], 'a': [1, 2, 8]}, columns = ['b', 'a'], index = [2, 1, 0])

print('Call first dataframe : df1 using OS')

df1 = pd.DataFrame({'a': [1, 3, 4], 'b': [5, 3, 1]}, columns = ['a', 'b'])
print(df1)


if 'df1' in locals() and 'df2' in locals():
    print(df1 + df2)
else:
    print("df1 or df2 is not defined properly.")
