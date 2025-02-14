import pandas as pd
df = pd.read_excel('data.xlsx',sheet_name='data',usecols=['Content','Time'])
#
# print(type(df))
tj = input("请输入过滤的内容：")

s = df[df['Content'].str.contains(tj,na=True)]

s1 = s[s['Content'].str.contains('OSPF',na=True)]

s1.to_excel('s1.xlsx')

print(s1)