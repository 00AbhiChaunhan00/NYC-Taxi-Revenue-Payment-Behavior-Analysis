import pandas as pd 

df=pd.read_parquet("yellow_taxi_cleaned.parquet")
print(df.head(5))