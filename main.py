import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/evi_d/Downloads/finance_liquor_sales 2016-2019.csv')

zc = df.groupby('zip_code')
print(zc.agg({'bottles_sold':'sum'}))

df= pd.DataFrame(df,columns=['store_name','sale_dollars', 'sale_dollars_percentage'])
df['sale_dollars_percentage'] = (df['sale_dollars'] /
                      df['sale_dollars'].sum()) * 100
print (df)
