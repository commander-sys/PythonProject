import  pandas as pd

df = pd.read_excel("1.xlsx")

'''
df['Time'].dt.date 是 pandas 的 datetime 访问器（.dt）的一部分，用于提取日期部分。.dt 访问器提供了许多方法来处理日期时间数据。以下是 .dt 访问器的主要方法列表：

year - 提取年份
month - 提取月份
day - 提取日
hour - 提取小时
minute - 提取分钟
second - 提取秒
microsecond - 提取微秒
nanosecond - 提取纳秒
date - 提取日期部分
time - 提取时间部分
dayofweek - 返回星期几（0=周一，6=周日）
dayofyear - 返回一年中的第几天
weekofyear - 返回一年中的第几周
is_month_start - 判断是否为月初
is_month_end - 判断是否为月末
is_quarter_start - 判断是否为季度初
is_quarter_end - 判断是否为季度末
is_year_start - 判断是否为年初
is_year_end - 判断是否为年末
days_in_month - 返回该月的天数
tz - 返回时区信息
normalize - 将时间标准化为午夜时间
strftime - 格式化日期时间
floor - 向下取整
ceil - 向上取整
round - 四舍五入
总计有 26 个方法。这些方法可以帮助你轻松地处理和分析日期时间数据。如果你需要更详细的信息，可以查看 pandas 
官方文档或使用 help(pd.Series.dt) 查看帮助信息
'''

# df.set_index("Time",inplace=True)
# print(df.columns)
df['Time'] = pd.to_datetime(df['Time'])
date1 = df['Time'].dt.date
date2 = df['Time'].dt.time
date3 = df['Time'].dt.year
date4 = df['Time'].dt.month
date5 = df['Time'].dt.day
date6 = df['Time'].dt.hour
date7 = df['Time'].dt.minute
date8 = df['Time'].dt.second
date9 = df['Time'].dt.microsecond
date10 = df['Time'].dt.nanosecond

print(date1)
print(date2)
print(date3)
print(date4)
print(date5)
print(date6)
print(date7)
print(date8)
print(date9)
print(date10)