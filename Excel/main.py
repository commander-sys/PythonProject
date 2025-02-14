import  pandas as pd

df1 = pd.read_excel('a.xls',sheet_name="Sheet1",names=['姓名1','年龄1'])
df2 = pd.read_excel('a.xls',sheet_name="Sheet1",names=['姓名2','年龄2'])

print(df1,'\n',df2)