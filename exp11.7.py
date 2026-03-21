#wap to create and manipulate a data frame 
import pandas as pd 
data = {
'name':['alice','bob','charlie'],
'age':[25,30,35],
'city':['New York','san francisco','los angeles']
}
df=pd.DataFrame(data)
print("DataFrame:")
print("\nage column:")
print(df['age'])
print("\n rows at index 1:")
print("df.i loc[1]")