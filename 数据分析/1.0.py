import pandas as pd

# 定义Excel文件路径
filename = "data.xlsx"

# 读取Excel文件到DataFrame
df = pd.read_excel(filename)
#DCGW专线
#1、次筛选出DCGW的数据
DCGW = df[df['云实例'].isin(["自用北京零区、三区", "自用信创北京一区、二区",]) & (df['网关类型'] == ("DCGW"))]

# print("非关基区DCGW专线网关流量、包量峰值如下：")
# print("集群流量峰值为：",max(DCGW["流量峰值/Gbps"]) ,"Gbps")
# print("集群包量峰值为：",max(DCGW["包量峰值/Wpps"]),"Wpps")
print("最忙集群为：",DCGW[DCGW["流量峰值/Gbps"] == max(DCGW["流量峰值/Gbps"],DCGW["包量峰值/Wpps"])]["云实例"].values[0])

print("---------------------------------------------------------")
#裸金属
#1、次筛选出XGW的数据
# XGW = df[df['云实例'].isin(["自用北京零区、三区", "自用信创北京一区、二区",]) & (df['网关类型'] == ("XGW"))]
# print("非关基区XGW裸金属网关流量、包量峰值如下：")
# print("集群流量峰值为：",max(XGW["流量峰值/Gbps"]),"Gbps")
# print("集群包量峰值为：",max(XGW["包量峰值/Wpps"]),"Wpps")