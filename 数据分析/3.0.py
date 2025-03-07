import pandas as pd

# 定义Excel文件路径
filename = "data.xlsx"

# 读取Excel文件到DataFrame
try:
    df = pd.read_excel(filename)
except FileNotFoundError:
    print(f"文件 {filename} 未找到，请检查路径是否正确。")
    exit()

# 筛选出DCGW的数据
DCGW = df[df['云实例'].astype(str).isin(["自用北京零区、三区", "自用信创北京一区、二区"]) & (df['网关类型'] == "DCGW")]

# 如果 DCGW 数据为空，提示并退出
if DCGW.empty:
    print("没有符合条件的 DCGW 数据。")
    exit()

# 强制转换列值为数值类型
DCGW.loc[:, "流量峰值/Gbps"] = pd.to_numeric(DCGW["流量峰值/Gbps"], errors='coerce')
DCGW.loc[:, "流量使用率/%"] = pd.to_numeric(DCGW["流量使用率/%"], errors='coerce')
DCGW.loc[:, "包量峰值/Wpps"] = pd.to_numeric(DCGW["包量峰值/Wpps"], errors='coerce')
DCGW.loc[:, "包量使用率/%"] = pd.to_numeric(DCGW["包量使用率/%"], errors='coerce')

# # 打印非关基区DCGW专线网关流量、包量峰值
# print("非关基区DCGW专线网关流量、包量峰值如下：")
max_traffic = max(DCGW["流量峰值/Gbps"])  # 15
max_traffic_row = DCGW[DCGW["流量峰值/Gbps"] == max_traffic]
# max_sum = str(max(max_traffic_row["流量使用率/%"].values[0] * 100, max_traffic_row["包量使用率/%"].values[0] * 100)) + "%"

# print(type(max_sum))
# print("集群带宽峰值：", str(max_traffic) + "Gbps",
#       "容量使用率：",str(max_traffic_row["流量使用率/%"].values[0] * 100) + "%",
#       "云实例名称:",max_traffic_row["云实例"].values[0],"集群/对象名称:",
#       "公共集群")

# 打印非关基区XGW专线网关流量、包量峰值
# print("非关基区XGW专线网关流量、包量峰值如下：")
# max_packets = max(DCGW["包量峰值/Wpps"])  # 15
# max_packets_row = DCGW[DCGW["包量峰值/Wpps"] == max_packets]
# print("集群带宽峰值：", str(max_packets) + "Wpps","容量使用率：",
#       str(max_packets_row["包量使用率/%"].values[0] * 100) + "%","云实例名称:",
#       max_packets_row["云实例"].values[0],"集群/对象名称:", "公共集群","峰值时间:",
#       max_packets_row["包量峰值时间"].values[0])