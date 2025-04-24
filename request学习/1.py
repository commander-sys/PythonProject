import requests

# 配置参数
api_key = "7861a33e089c49aba501f629ef0b58bf"  # 在控制台获取（32位字符串）
location_id = "101010100"  # 北京城市ID
api_url = "https://pc6vhecxya.re.qweatherapi.com/v7/weather/now"  # 免费版使用devapi域名

# 构建请求参数
params = {
    "location": location_id,
    "key": api_key  # 关键参数：和风API必须通过key传递认证
}

# 发送请求
try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # 检查HTTP错误

    # 解析响应
    weather_data = response.json()
    print(f"当前天气: {weather_data['now']['text']}, 温度: {weather_data['now']['temp']}℃")

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except ValueError as e:
    print(f"JSON解析失败: {e}")
