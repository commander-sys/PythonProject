import difflib

file1 = 'a.txt'
file2 = 'b.txt'

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    diff = difflib.ndiff(f1.readlines(), f2.readlines())

# 输出差异
for line in diff:
    print(line)