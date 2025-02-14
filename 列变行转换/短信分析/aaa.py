import pandas as pd

# 示例数据
data = {'字段': ['苹果', '香蕉', '苹果香蕉', '梨子', '橘子']}
df = pd.DataFrame(data)

print(type(df))

# 模糊匹配包含 "苹果" 的字段
result = df[df['字段'].str.contains('苹果', na=False)]
print(result)
