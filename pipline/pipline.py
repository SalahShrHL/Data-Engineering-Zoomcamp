import sys
import pandas as pd


day = int(sys.argv[1])

print(f"Running pipeline for month {day}")



df = pd.DataFrame({"A": [1, 2,5], "B": [3, 4,7]})
df["month"] = day 
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")