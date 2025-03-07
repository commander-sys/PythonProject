import pandas as pd

# 定义Excel文件路径
filename = "data.xlsx"
# 读取Excel文件到DataFrame
df = pd.read_excel(filename)

# 筛选符合条件的行
DCGW = df[df['云实例'].astype(str).isin(["自用北京零区、三区", "自用信创北京一区、二区"]) & (df['网关类型'] == "DCGW")]

# 检查 DCGW 是否为空
if DCGW.empty:
    print("没有符合条件的 DCGW 数据")
else:
    print("success")
# 计算最大流量使用率和包量使用率
ZM_DCGW_TRAFFIC = DCGW["流量使用率/%"].max()
ZM_DCGW_PACKETS = DCGW["包量使用率/%"].max()

# 判断最忙集群的依据
if ZM_DCGW_TRAFFIC > ZM_DCGW_PACKETS:
    ZM_JQ1 = "流量使用率/%"
    ZM_JQ2 = str(ZM_DCGW_TRAFFIC * 100) + "%"
else:
    ZM_JQ1 = "包量使用率/%"
    ZM_JQ2 = str(ZM_DCGW_PACKETS * 100) + "%"

# 筛选最忙集群
s = DCGW.loc[DCGW[ZM_JQ1] == ZM_JQ2, :]

# 输出结果
print("最忙集群的详细信息：")
print(s)
