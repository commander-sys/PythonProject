import random
import string


def generate_random_text(num_lines, line_length):
    # 定义可选的字符集（字母和数字）
    characters = string.ascii_letters + string.digits

    # 生成指定数量的行，每行长度为 line_length
    with open('random_text.txt', 'w') as file:
        for _ in range(num_lines):
            random_line = ''.join(random.choice(characters) for _ in range(line_length))
            file.write(random_line + '\n')


# 生成 40,000 行，每行长度为 100 个字符
generate_random_text(50000, 100)
