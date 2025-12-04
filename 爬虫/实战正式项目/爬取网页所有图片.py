import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = 'https://spiderbuf.cn/web-scraping-practice/scraping-images-from-web'# 'https://www.dangdang.com/'
response = requests.get(url)
response.encoding = response.apparent_encoding  # 解决编码问题
html = response.text

soup = BeautifulSoup(html, 'lxml')

# 找所有图片标签
img_tags = soup.find_all('img')

# 建个文件夹保存图片
os.makedirs('images', exist_ok=True)

for img in img_tags:
    img_url = img.get('src')
    # 拼接完整url，防止是相对路径
    img_full_url = urljoin(url, img_url)
    
    # 图片文件名，从url截取
    img_name = os.path.basename(img_full_url)
    
    # 请求图片
    img_resp = requests.get(img_full_url)
    
    if img_resp.status_code == 200:
        # 以二进制写入文件
        with open(os.path.join('images', img_name), 'wb') as f:
            f.write(img_resp.content)
        print(f"已保存图片：{img_name}")
    else:
        print(f"下载失败：{img_full_url}")
