import pandas as pd
from scrapy.spiders.sitemap import regex

df = pd.read_csv('jh.csv',encoding='gbk')

bj = df[df['Content'].str.contains('北京|稻香湖',regex=True,na=False)  ]
# wh = df[df['Content'].str.contains('武汉|南湖',regex=True,na=False)]
# nm = df[df['Content'].str.contains('内蒙')]

# print(bj.count().Number)
# print(wh.count().Number)
# print(nm.count().Number)
#
# print(df.count().Number)

bj.to_excel('bj.xlsx')
# wh.to_excel('wh.xlsx')
# nm.to_excel('ne.xlsx')

dc = bj[bj['Content'].str.contains('DC|dc',regex=True,na=False)  ]
print(dc.count().Number)
# print(dc['Content'])
print(df.columns)

ip_pattern = r'(\b\d{1,3}(?:\.\d{1,3}){3}\b)'
ip_list = dc['Content'].str.extract(ip_pattern)
# ip_list.to_excel('ip.xlsx')
ip_sum = ip_list[0].value_counts().head(5)

print(ip_list.drop_duplicates(ubset=[0]))