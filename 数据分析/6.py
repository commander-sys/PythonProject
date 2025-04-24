import pandas as pd

df = pd.read_excel("data.xlsx")

# print(df.columns)

result = df[df['云实例'].str.contains('北京')]

print(result)