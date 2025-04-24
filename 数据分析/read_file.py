import requests  as re


url = "https://www.w3school.com.cn"

response = re.get(url)
status = response.status_code

if status == 200:
    print("请求成功")
else:
    print("请求失败")