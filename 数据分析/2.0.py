import pandas as pd

# 定义Excel文件路径
filename = "data.xlsx"

# 读取Excel文件到DataFrame
df = pd.read_excel(filename)

# 筛选出DCGW的数据
DCGW = df[df['云实例'].isin(["自用北京零区、三区", "自用信创北京一区、二区"]) & (df['网关类型'] == "DCGW")]

# 打印非关基区DCGW专线网关流量、包量峰值
print("非关基区DCGW专线网关流量、包量峰值如下：")
print("集群流量峰值为：", str(max(DCGW["流量峰值/Gbps"])) + "Gbps","容量使用率为：",str(max(DCGW["流量使用率/%"]) * 100) + "%","峰值时间为：",max(DCGW["流量峰值时间"]))
print("集群包量峰值为：", str(max(DCGW["包量峰值/Wpps"])) + "Wpps","容量使用率为：",str(max(DCGW["包量使用率/%"]) * 100) + "%")

# 找到流量峰值最大的集群
max_dcgw_traffic = max(DCGW["流量使用率/%"])
# 找到包量峰值最大的集群
max_dcgw_packets = max(DCGW["包量使用率/%"])
if max_dcgw_traffic > max_dcgw_packets:
    print("最忙集群为：", DCGW[DCGW["流量使用率/%"] == max_dcgw_traffic]["流量使用率/%"].values[0])
else:
    print("最忙集群为：", DCGW[DCGW["包量使用率/%"] == max_dcgw_packets]["包量使用率/%"].values[0])


print("------------------------------------")

# 打印关基区XGW专线网关流量、包量峰值
# XGW = df[df['云实例'].isin(["自用北京一区、二区"]) & (df['网关类型'] == "XGW")]
# print("关基区XGW专线网关流量、包量峰值如下：")
# print("集群流量峰值为：", max(XGW["流量峰值/Gbps"]), "Gbps")
# print("集群包量峰值为：", max(XGW["包量峰值/Wpps"]), "Wpps")
# # 找到流量峰值最大的集群
# max_xgw_traffic = max(XGW["流量使用率/%"])
# # 找到包量峰值最大的集群
# max_xgw_packets = max(XGW["包量使用率/%"])
# s2 = str(max(max_xgw_traffic, max_xgw_packets) * 100) + "%"
# print(s2)