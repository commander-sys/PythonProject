# 这是一个短信分析的脚本，读取短信内容，过滤北京DC产品相关的短信，提取出DCGW、XGW、SXGW、DCGWNAT相关的短信，统计出各网关 相关的短信中IP地址出现次数最多的5个IP地址。
# 导入pandas库，用于数据处理和分析，将其重命名为pd以便后续使用
import pandas as pd
# 导入numpy库，用于数值计算，将其重命名为np以便后续使用，当前代码中未使用该库
import numpy as np
r_f_name = 'jh.csv'
w_f_name = str((pd.Timestamp.now()).strftime('%Y%m%d')) + ".xlsx"

# 读取CSV文件'jh.csv'，使用'gbk'编码，将数据存储到DataFrame对象df中
df = pd.read_csv(r_f_name, encoding='gbk')
# 定义过滤条件，筛选出短信内容中同时包含“北京”或“稻香湖”以及“DC”或“dc”的记录
condition = (df["Content"].str.contains("北京|稻香湖", regex=True, na=False) & df["Content"].str.contains("DC|dc",regex=True, na=False))
# 根据上述条件筛选出符合要求的记录，存储到新的DataFrame对象dc_bj中
dc_bj = df[condition]
# 从dc_bj中进一步筛选出短信内容包含“XGW”或“xgw”的记录，存储到新的DataFrame对象dc_bj_xgw中
dc_bj_xgw = dc_bj[dc_bj["Content"].str.contains("XGW|xgw", regex=True, na=False)]
xgw = dc_bj_xgw.to_excel(w_f_name,sheet_name='dc_bj_xgw',index=False)
# 从dc_bj_xgw中进一步筛选出短信内容包含“DCGW”的记录，存储到新的DataFrame对象dc_bj_xgw_dcgw中
dc_bj_dcgw = dc_bj[dc_bj["Content"].str.contains("DCGW", regex=True, na=False)]
dcgw = dc_bj_dcgw.to_excel(w_f_name,sheet_name='dc_bj_dcgw',index=False)
# 从dc_bj_xgw中进一步筛选出短信内容包含“DCGWNAT”的记录，存储到新的DataFrame对象dc_bj_xgw_dcgwnat中
dc_bj_dcgwnat = dc_bj[dc_bj["Content"].str.contains("DCGWNAT", regex=True, na=False)]
dcgwnat = dc_bj_dcgwnat.to_excel(w_f_name,sheet_name='dc_bj_dcgwnat',index=False)
# 从dc_bj_xgw中进一步筛选出短信内容包含“SXGW”的记录，存储到新的DataFrame对象dc_bj_xgw_sxgw中
dc_bj_sxgw = dc_bj[dc_bj["Content"].str.contains("SXGW", regex=True, na=False)]
sxgw = dc_bj_sxgw.to_excel(w_f_name,sheet_name='dc_bj_sxgw',index=False)
# 定义IP地址的正则表达式模式
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
# 从dc_bj_xgw的短信内容列中提取所有匹配IP地址模式的字符串，存储到新的DataFrame对象ip_list中
ip_list = dc_bj_xgw["Content"].str.extract(f'({ip_pattern})')
# 统计每个IP地址出现的次数，并取出现次数最多的前5个IP地址，存储到Series对象top_5_ip中
top_5_ip = ip_list.value_counts().head(10)
print(type(top_5_ip))
