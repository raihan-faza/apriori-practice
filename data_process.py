import pandas as pd

df = pd.read_csv("online_retail.csv")
print(df.info)
print(df.describe)
print(df.isna().sum())
