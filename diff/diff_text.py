#coding:utf-8
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # 读取文件的每一行
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # 计算两个文件的最大行数
        max_lines = max(len(lines1), len(lines2))

        # 比较文件的每一行
        for i in range(max_lines):
            line1 = lines1[i] if i < len(lines1) else ""
            line2 = lines2[i] if i < len(lines2) else ""

            if line1 != line2:
                print(f"Line {i + 1}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")
                print("-" * 40)

# 使用函数来比较两个文件
compare_files('D:\\PythonProject\\diff\\r1.txt', 'D:\\PythonProject\\diff\\r2.txt')
