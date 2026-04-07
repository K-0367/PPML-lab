#convert the series from string to numeric with error handelinh
import pandas as pd
s= pd.Series(['10','20','abc','30'])
s_numeric = pd.to_numeric(s, errors='coerce')
print(s_numeric)

'''errors='coerce' will convert non-numeric values to NaN (Not a Number) instead of raising an error.
 This allows the conversion to proceed without interruption, and you can handle the NaN values as needed later in your code.'''

#convert mixed type series to datetime with error handling
import pandas as pd 
s = pd.Series(['2021-01-01', '2021-02-30', '2021-03-15'])
s_datetime = pd.to_datetime(s, errors='coerce')
print(s_datetime)

#convert numeric string with commas to floats
import pandas as pd
s = pd.Series(['1,000', '2,500', '3,000'])
s_float = s.str.replace(',', '').astype(float)
print(s_float)

#