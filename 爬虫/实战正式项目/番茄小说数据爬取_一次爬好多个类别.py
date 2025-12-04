import requests
from lxml import etree
import pandas as pd
import time

def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    return r.text

def parse_data(html, category):
    tree = etree.HTML(html)
    novels = []
    items = tree.xpath("//div[@class='muye-rank-book-list']/div[@class='rank-book-item']")
    for item in items:
        title = item.xpath(".//div[@class='title']/a/text()")
        title = title[0].strip() if title else ''
        author = item.xpath(".//div[@class='author']/a/span/text()")
        author = author[0].strip() if author else ''
        status = item.xpath(".//span[@class='book-item-footer-status']/text()")
        status = status[0].strip() if status else ''
        readers = item.xpath(".//span[@class='book-item-count']/text()")
        readers = readers[0].strip() if readers else ''

        novels.append({
            'category': category,   # 加个字段标明类别
            'title': title,
            'author': author,
            'status': status,
            'readers': readers
        })
    return novels

def main():
    # 多个类别链接和分类名，你可以继续添加需要爬的类别和对应url
    categories = {
        '科幻末世': 'https://fanqienovel.com/rank/1_2_8',
        '都市日常': 'https://fanqienovel.com/rank/1_2_261',
        '都市修真': 'https://fanqienovel.com/rank/1_2_124',
        '都市高武': 'https://fanqienovel.com/rank/1_2_1014',
    }

    all_novels = []
    for category, url in categories.items():
        print(f'正在爬取类别：{category}，URL：{url}')
        html = fetch_html(url)
        novels = parse_data(html, category)
        all_novels.extend(novels)
        time.sleep(1)  # 适当休眠，避免请求过快被封

    df = pd.DataFrame(all_novels)
    df.to_csv('fanqie_multiple_categories.csv', index=False, encoding='utf-8')
    print('数据爬取完成，已保存fanqie_multiple_categories.csv')

if __name__ == "__main__":
    main()
