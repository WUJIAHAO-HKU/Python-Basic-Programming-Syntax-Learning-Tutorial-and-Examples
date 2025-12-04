#导入相关模块
import requests
import re
import json
from bs4 import BeautifulSoup
#发送请求，获取响应
response = requests.get("http://2019ncov.imicams.ac.cn/index.html")
#从响应中获取疫情数据
home_page = response.content.decode()
#print(home_page)

#使用beautifulsoup提取疫情数据
#构建对象
soup = BeautifulSoup(home_page,'lxml')
#根据id查找标签
script = soup.find(id="4")
#获取标签中文本信息
text = script.contents
print(text)


#使用正则表达式,提取json字符串
json_str = re.findall(r'\[.+\]',text)[0]
print(json_str)

#转换
nnn = json.loads(json_str)
print(nnn)