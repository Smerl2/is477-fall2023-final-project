import pandas as pd 

df = pd.read_csv('data/online_retail.csv')

print(df)

print(df['UnitPrice'].describe())


