import requests

#发送请求，获取响应
response = requests.get("http://2019ncov.imicams.ac.cn/index.html")

#获取响应数据
#print(response.encoding)
#print(response.text)
print(response.content.decode())