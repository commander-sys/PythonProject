import pandas as pd
import difflib

df = pd.read_csv("jh.csv", on_bad_lines="skip")
df['Time'] = pd.to_datetime(df['Time'])  # 确保Time列是datetime类型


# 筛选出符合条件的数据
filtered_data = df[(df["Time"] > pd.to_datetime("2025/3/6 00:00:00")) &
                   (df["Time"] < pd.to_datetime("2025/3/7 00:00:00"))]

df['match_score'] = df['Content'].apply(lambda x: difflib.SequenceMatcher(None, "稻香湖信创-DCGW-拨测告警", x).ratio())
# 筛选相似度大于 0.8 的结果
result = df[df['match_score'] > 0.8 ]
print(result.values())
# filtered_data.to_excel("1.xlsx")

# print(filtered_data)