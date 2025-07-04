import pandas as pd

# 文件名定义
r_f_name = "jh.csv"
w_f_name = pd.Timestamp.now().strftime("%Y%m%d") + ".xlsx"

# 读取数据，指定编码
df = pd.read_csv(r_f_name, encoding="gbk")

# 筛选包含“北京”或“稻香湖”，且包含“DC”或“dc”的短信
condition = df["Content"].str.contains("北京|稻香湖", regex=True, na=False) & df[
    "Content"
].str.contains("DC|dc", regex=True, na=False)
dc_bj = df[condition]

# 要筛选的关键词及对应sheet名称
keywords = {
    "XGW": "dc_bj_xgw",
    "DCGW": "dc_bj_dcgw",
    "DCGWNAT": "dc_bj_dcgwnat",
    "SXGW": "dc_bj_sxgw",
}

# 使用ExcelWriter一次写入多个sheet，避免文件被覆盖
with pd.ExcelWriter(w_f_name) as writer:
    for kw, sheet in keywords.items():
        # 筛选包含关键词的短信
        df_filtered = dc_bj[dc_bj["Content"].str.contains(kw, regex=True, na=False)]
        # 导出到对应sheet
        df_filtered.to_excel(writer, sheet_name=sheet, index=False)

# 正则匹配IP地址
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# 从包含“XGW”的短信中提取IP地址
dc_bj_xgw = dc_bj[dc_bj["Content"].str.contains("XGW|xgw", regex=True, na=False)]
ip_series = dc_bj_xgw["Content"].str.extractall(f"({ip_pattern})")[0]

# 统计出现次数最多的前10个IP地址
top_10_ip = ip_series.value_counts().head(10)

print(top_10_ip)
