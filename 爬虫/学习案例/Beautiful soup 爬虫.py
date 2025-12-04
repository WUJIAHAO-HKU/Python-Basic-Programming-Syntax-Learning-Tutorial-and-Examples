#导入模块
from bs4 import BeautifulSoup
#创建对象
html = """<html>
  <head>
    <title>The Dormouse's story</title>
  </head>
  <body>
    <p class="title">
      <b>The Dormouse's story</b>
    </p>
    <p class="story">
      Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
      and they lived at the bottom of a well.
    </p>
  </body>
</html>
"""
soup = BeautifulSoup(html,"lxml")

#一、根据标签名查找
title = soup.find('title')
print(title)
a = soup.find('a')
print(a)

#查找所有的a标签
a_s = soup.find_all('a')
print(a_s)

#二、根据属性进行查找
#查找id为link1的标签
#方式一：通过命名参数进行指定的
a = soup.find(id = 'link1')
print(a)
#方式二：使用attrs来指定属性字典，进行查找
a = soup.find(attrs = {"id":"link1"})
print(a)

#三、根据文本内容进行查找
text = soup.find(text = 'Elsie')
print(text)

#Tag 对象 ：该对象对应于原始文档中的XML或HTML标签
print(type(a))
print('标签名', a.name)
print('标签所有属性', a.attrs)
print('标签文本内容', a.text)
