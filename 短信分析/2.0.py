import  pandas as pd

df = pd.read_excel("1.xlsx")



df.set_index("Time",inplace=True)
print(df.index)