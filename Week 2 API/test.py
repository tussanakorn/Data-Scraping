import pandas as pd

df =  pd.read_json('today_data.json')
query = df['Deaths'] == 1
print(df[query])