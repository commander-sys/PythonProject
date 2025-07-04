import pandas as pd

# 正则匹配IP地址
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# 文件名定义
r_f_name = "jh.csv"
w_f_name = pd.Timestamp.now().strftime("%Y%m%d") + ".xlsx"

# 读取CSV数据
df = pd.read_csv(r_f_name, on_bad_lines="skip")

# ============ STEP 1：筛选包含“北京/稻香湖” 且 含 “DC/dc” 且有IP 的短信 ============
condition_beijing_dc = df["Content"].str.contains(
    "北京|稻香湖", regex=True, na=False
) & df["Content"].str.contains("DC|dc", regex=True, na=False)
condition_ip = df["Content"].str.contains(ip_pattern, regex=True, na=False)

filtered_df = df[condition_beijing_dc & condition_ip].copy()

# 提取第一个匹配到的IP写入新列
filtered_df["IP"] = filtered_df["Content"].str.extract(f"({ip_pattern})")

# 提取指定列
dc_bj = filtered_df[["Time", "IP", "Content"]]

# ============ STEP 2：根据关键字提取子集并写入不同Sheet ============
keywords = {
    "XGW": "dc_bj_xgw",
    "DCGW": "dc_bj_dcgw",
    "DCGWNAT": "dc_bj_dcgwnat",
    "SXGW": "dc_bj_sxgw",
}

# 存储子DataFrame用于后续处理
subsets = {}

for kw, sheet_name in keywords.items():
    subset = dc_bj[dc_bj["Content"].str.contains(kw, regex=True, na=False)].copy()
    subsets[sheet_name] = subset

# ============ STEP 3：提取所有IP（含重复）并统计Top10 ============
ip_series = dc_bj["Content"].str.extractall(f"({ip_pattern})")[0]
top_10_ip = ip_series.value_counts().head(10)

# ============ STEP 4：写入Excel多Sheet ============
with pd.ExcelWriter(w_f_name) as writer:
    # 原始筛选结果
    dc_bj.to_excel(writer, sheet_name="dc_bj_all", index=False)

    # 各子集
    for sheet_name, subset in subsets.items():
        subset.to_excel(writer, sheet_name=sheet_name, index=False)

    # Top IP 统计
    top_10_ip.to_frame(name="次数").to_excel(writer, sheet_name="top10_ip")
