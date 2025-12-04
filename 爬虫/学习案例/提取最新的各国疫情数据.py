#导入相关模块
import requests
import re
from bs4 import BeautifulSoup
#发送请求，获取响应
response = requests.get("http://2019ncov.imicams.ac.cn/index.html")
#从响应中获取疫情数据
response.encoding = response.apparent_encoding  # 解决可能的编码问题
home_page = response.content.decode()
#print(home_page)

#使用beautifulsoup提取疫情数据
#构建对象
soup = BeautifulSoup(home_page,'lxml')
#根据id查找标签
script = soup.find(id="knowledge")
#获取标签中文本信息
text = script.contents
print(text)
