import requests

url = "https://www.1905.com/vod/list/n_1_a_4/o3p1.html#/"
response = requests.get(url)
response.encoding = "utf-8"
print(response.text)
