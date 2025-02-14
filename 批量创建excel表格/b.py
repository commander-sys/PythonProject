import psutil
import time
import csv
from datetime import datetime

# 记录数据的文件名
output_file = "windows_process_usage.csv"

# 初始化 CSV 文件并添加表头
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Timestamp', 'PID', 'Process Name', 'CPU Usage (%)', 'Memory Usage (MB)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# 每 5 秒获取一次进程数据
try:
    while True:
        # 获取当前时间戳
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 获取所有进程
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                # 获取进程信息
                pid = proc.info['pid']
                name = proc.info['name']
                cpu_usage = proc.info['cpu_percent']  # CPU 使用率
                memory_usage = proc.info['memory_info'].rss / (1024 * 1024)  # 将内存从字节转换为 MB

                # 只记录用户进程，不包括系统进程
                if name.lower() not in ['system', 'idle', 'services', 'svchost']:
                    # 打印进程信息
                    print(f"Timestamp: {timestamp}, PID: {pid}, Name: {name}, CPU: {cpu_usage}%, Memory: {memory_usage}MB")

                    # 将数据写入 CSV 文件
                    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({
                            'Timestamp': timestamp,
                            'PID': pid,
                            'Process Name': name,
                            'CPU Usage (%)': cpu_usage,
                            'Memory Usage (MB)': memory_usage
                        })

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # 跳过无法访问的进程
                continue

        # 等待 5 秒
        time.sleep(5)

except KeyboardInterrupt:
    print("程序终止。")
