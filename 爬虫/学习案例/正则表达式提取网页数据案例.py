#导入相关模块
import requests
import re
from bs4 import BeautifulSoup
#发送请求，获取响应
response = requests.get("https://www.w3cschool.cn/article/39055478.html")
#从响应中获取疫情数据
home_page = response.content.decode()
#print(home_page)

#使用beautifulsoup提取疫情数据
#构建对象
soup = BeautifulSoup(home_page,'lxml')
#根据id查找标签
script = soup.find(id = "toolbar")
# 检查 script 是否为 None
#print(script)
if script:
    # 获取标签中文本信息
    text = script.text
    print(text)
else:
    print("没有找到标题为 '创始人' 的元素")

