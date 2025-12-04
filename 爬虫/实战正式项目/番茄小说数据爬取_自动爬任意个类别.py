import requests
from lxml import etree
import pandas as pd
import time

def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    return r.text

def get_categories(base_url, category_type = 0):
    while True:  # 使用循环
        category_type = int(input("输入【1.2.3.4】进行选择："))

        if 1 <= category_type <= 4:
            break  # 输入有效，退出循环
        else:
            print("输入的数字错误，请输入1 or 2 or 3 or 4")
            
    html = fetch_html(base_url)
    tree = etree.HTML(html)
    categories = {}
    # 根据大类选择不同的 XPath
    if category_type == 1:
        a_tags = tree.xpath("//div[@class='arco-menu-inline'][1]//span[@class='arco-menu-item-inner']/a")
        print(a_tags)
    elif category_type == 2:
        a_tags = tree.xpath("//div[@class='arco-menu-inline'][2]//span[@class='arco-menu-item-inner']/a")
    elif category_type == 3:
        a_tags = tree.xpath("//div[@class='arco-menu-inline'][3]//span[@class='arco-menu-item-inner']/a")
    elif category_type == 4:
        a_tags = tree.xpath("//div[@class='arco-menu-inline'][4]//span[@class='arco-menu-item-inner']/a")

    for a in a_tags:
        href = a.xpath("./@href")
        text = a.xpath("text()")
        if href and text:
            href = href[0].strip()
            text = text[0].strip()
            full_url = "https://fanqienovel.com" + href
            categories[text] = full_url
    return categories

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
        numbers = item.xpath(".//span[@class='book-item-count']/text()")
        numbers = numbers[1].strip() if readers else ''

        novels.append({
            'category': category,
            'title': title,
            'author': author,
            'status': status,
            'readers': readers,
            'numbers': numbers
        })
    return novels

def main():
    base_url = "https://fanqienovel.com/rank"
    print("请选择爬取的大类：\n\t1.男频阅读\n\t2.男频新书\n\t3.女频阅读\n\t4.女频新书\n")
    categories = get_categories(base_url, category_type = 0)
    print("当前可爬取的类别：")
    for i, (name, url) in enumerate(categories.items(), 1):
        print(f"{i}. {name} - {url}")

    n = int(input("请输入要爬取的类别数（例如输入3爬前三个类别）："))
    selected_items = list(categories.items())[:n]

    all_novels = []
    for category, url in selected_items:
        print(f'正在爬取类别：{category}，URL：{url}')
        html = fetch_html(url)
        novels = parse_data(html, category)
        all_novels.extend(novels)
        time.sleep(1)

    df = pd.DataFrame(all_novels)
    df.to_csv('fanqie_selected_categories.csv', index=False, encoding='utf-8')
    print('数据爬取完成，已保存 fanqie_selected_categories.csv')

if __name__ == "__main__":
    main()
