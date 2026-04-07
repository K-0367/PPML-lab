#create a pandas series 
import pandas as pd
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)

#create DataFrame from a dictionary
import pandas as pd
data = {
    "Name": ["Ram", "Shyam", "Radha"],
    "Age": [20, 21, 19],
    "City": ["Delhi", "Mumbai", "Kolkata"]
}
df = pd.DataFrame(data)
print(df)

#Load CSV and show info 
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head())
print(df.info())

#select rows and column 
import pandas as pd
df = pd.read_csv("data.csv")
print(df["Name"])

#add new column
df["Country"] = ["India", "India", "India"]
print(df)

#delete column 
import pandas as pd
df = pd.read_csv("data.csv")
df.drop("City", axis=1)
print(df)

#handle missing values
df = df.fillna(0)
print(df)

#sorting
df = df.sort_values("Age")
print(df)

#groupby
print(df.groupby("City")["Age"].mean())

#merge DataFrames
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Ram", "Shyam", "Radha"]})
df2 = pd.DataFrame({"ID": [1, 2, 3], "Age": [20, 21, 19]})
merged_df = pd.merge(df1, df2, on="ID")
print(merged_df)

#concatenate
print(pd.concat([df1,df2]))

#correlation
print(df.corr(numeric_only=True))

