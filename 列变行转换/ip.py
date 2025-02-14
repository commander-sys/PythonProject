import pandas as pd

# 定义文件路径
file_path = 'iplist.xlsx'

# 读取 Excel 文件，指定 sheet 名为 'Sheet1'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 获取需要合并的列名列表
merge_names = list(df.loc[:,"ip":].columns.values)

# 定义一个函数，用于合并行中的多个列值
def merge_cols(x):
    """
    x 是一个行 Series，把它们按分隔符合并

    参数:
    x (pandas.Series): 包含需要合并的列值的行

    返回:
    str: 合并后的字符串
    """
    # 删除为空的列
    x = x[x.notna()]
    # 使用 x.values 合并
    y = x.values
    # 合并后的列表，每个元素是“IP”
    result = []
    for idx in range(0, len(y), 1):
        # 使用竖线作为“IP”之间的分割符
        result.append(f"{y[idx]}")
    return "#".join(result)

# 添加新列，把待合并的所有列变成一个大字符串
df["merge"] = df.loc[:,"ip":].apply(merge_cols, axis=1)

# 把不用的列删除
df.drop(merge_names, axis=1, inplace=True)

# 使用 explode 把一列变多行
# 先将 merge 列变成 list 的形式
df["merge"] = df["merge"].str.split('#')

# 执行 explode 变成多行
df_explode = df.explode("merge")

# 将结果输出到新的 Excel 文件中
df_explode.to_excel('ip_major.xlsx', index=False)

# 打印结果
print(df_explode)
