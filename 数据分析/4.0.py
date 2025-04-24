import pandas as pd

# 定义Excel文件路径
filename = "data.xlsx"
# 读取Excel文件到DataFrame
df = pd.read_excel(filename)

DCGW = df[df['云实例'].astype(str).isin(["自用北京零区、三区", "自用信创北京一区、二区"]) & (df['网关类型'] == "DCGW")]

# print(DCGW)

# 最忙集群为：
ZM_DCGW_TRAFFIC = DCGW["流量使用率/%"].max()
ZM_DCGW_PACKETS = DCGW["包量使用率/%"].max()

if ZM_DCGW_TRAFFIC > ZM_DCGW_PACKETS:
    ZM_JQ1 = "流量使用率/%"
    ZM_JQ2 = ZM_DCGW_TRAFFIC
else:
    ZM_JQ1 = "包量使用率/%"
    ZM_JQ2 = ZM_DCGW_PACKETS

    s = DCGW.loc[DCGW[ZM_JQ1] == ZM_JQ2, :]

print(s['云实例'].values[0])
