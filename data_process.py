import pandas as pd

# explore dataset
df = pd.read_csv("online_retail.csv")
print(df.info())
print(df.describe)
print(df.isna().sum())

# cleaning dataset
## removing extra space
df["Description"] = df["Description"].str.strip()
print(df["Description"])

## drop null/nan values
df.dropna(inplace=True)
print(df.info())

# encoding data
