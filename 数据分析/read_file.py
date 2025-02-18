import pandas as pd

# 定义Excel文件路径
filename = "data.xlsx"

# 读取Excel文件到DataFrame
df = pd.read_excel(filename)

# 打印DataFrame内容（调试用）
# print(df)

# 筛选符合条件的行：'云实例'列中包含指定值的行
# 使用isin()函数检查'云实例'列是否包含以下值：
# "自用北京零区、三区", "自用信创北京一区、二区", "自用北京一区、二区"
filter1_condition = df['云实例'].isin(["自用北京零区、三区", "自用信创北京一区、二区", "自用北京一区、二区"])
filter_df = df[filter1_condition]

# 根据筛选条件提取符合条件的行
#筛选出DCGW
filter_dcgw = filter_df['网关类型'] .isin(["DCGW"])
DCGW_SUM = filter_df[filter_dcgw]

for index, row in DCGW_SUM.iterrows():
    if  row['流量使用率/%'] > row['包量使用率/%']:
        print( row['流量使用率/%'])
    else:
        print( row['包量使用率/%'])

#筛选出XGW
filter_xgw = filter_df['网关类型'].isin(["XGW"])
XGW_SUM = filter_df[filter_xgw]
for index, row in XGW_SUM.iterrows():
    if  row['流量使用率/%'] > row['包量使用率/%']:
        ( row['流量使用率/%'])
    else:
        print( row['包量使用率/%'])

# 将筛选后的DataFrame保存到新的Excel文件
# filter_df.to_excel("test.xlsx", index=False)  # index=False表示不保存行索引
