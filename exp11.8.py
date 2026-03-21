#wap to read csv and json files
import pandas as pd 
df_csv=pd.read_csv('sample.csv')
print(df_csv)
df_json=pd.read_json('sample.json')
print("\n DataFrame from json:")
print(df_json)