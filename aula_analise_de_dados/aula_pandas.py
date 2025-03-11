import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.set_index("PassengerId", inplace=True)
df.describe()
print(df.loc[1])
print(df.loc[[1, 2], ["Name", "Sex", "Age"]])
print(df.loc[10:20])
print(df.loc[10:20:2])
print(df.loc[1: 10, ["Name", "Sex", "Age"]])
print(df.query("Age > 20").head())
print(df.query("Age > 20"))
print(df.head())