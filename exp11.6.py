#wap to create and work  with pandas series
import pandas as pd 
data=[10,20,30]
labels=['a','b','c']
series=pd.Series(data,index=labels)
print("pandas series:")
print(series)
print('values at label ''b:',series['b'])
