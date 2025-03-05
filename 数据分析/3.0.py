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

# 打印非关基区DCGW专线网关流量、包量峰值
print("非关基区DCGW专线网关流量、包量峰值如下：")
print("集群流量峰值为：", str(max(DCGW["流量峰值/Gbps"])) + "Gbps", "流量使用率为：", str(max(DCGW["流量使用率/%"]) * 100) + "%", "峰值时间为：", max(DCGW["流量峰值时间"]))
print("集群包量峰值为：", str(max(DCGW["包量峰值/Wpps"])) + "Wpps", "包量使用率为：", str(max(DCGW["包量使用率/%"]) * 100) + "%")

# 找到流量峰值最大的集群
max_dcgw_traffic = max(DCGW["流量使用率/%"])
max_dcgw_packets = max(DCGW["包量使用率/%"])
if max_dcgw_traffic > max_dcgw_packets:
    print("最忙集群为：", DCGW[DCGW["流量使用率/%"] == max_dcgw_traffic]["流量使用率/%"].values[0])
else:
    print("最忙集群为：", DCGW[DCGW["包量使用率/%"] == max_dcgw_packets]["包量使用率/%"].values[0])