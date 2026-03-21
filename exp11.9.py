import pandas as pd
data= {
    'math':[90,85,80,95],
    'science':[88,82,85,90],
    'english':[78,75,80,85]
}
df = pd.DataFrame(data)
print("DataFrame")
print(df)
corelation = df.corr()
print("\n correlation matrix:")
print(corelation)