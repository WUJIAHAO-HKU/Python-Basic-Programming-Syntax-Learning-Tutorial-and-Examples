import requests
from lxml import etree
import pandas as pd

def fetch_data():
    url = "https://fanqienovel.com/rank/1_2_8"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding  # 解决可能的编码问题
    return response.text

def parse_data(html):
    tree = etree.HTML(html)
    novels = []
    for item in tree.xpath("//div[@class='muye-rank-book-list']/div[@class='rank-book-item']"):

        title_list = item.xpath(".//div[@class='title']/a/text()")
        title = title_list[0].strip() if title_list else ''
        
        author_list = item.xpath(".//div[@class='author']/a/span/text()")
        author = author_list[0].strip() if author_list else ''

        # 连载状态
        status_list = item.xpath(".//span[@class='book-item-footer-status']/text()")
        status = status_list[0].strip() if status_list else ''
        
        # 在读人数，文本例子：“在读：73.4万”
        readers_list = item.xpath(".//span[@class='book-item-count']/text()")
        readers = readers_list[0].strip() if readers_list else ''
        numbers = readers_list[1].strip() if readers_list else ''
        
        novels.append({
            "title": title,
            "author": author,
            "status": status,
            "readers": readers,
            "numbers": numbers
        })

    return novels

def save_to_csv(novels):
    df = pd.DataFrame(novels)
    df.to_csv("fanqie_novels.csv", index=False, encoding='utf-8')

def main():
    html = fetch_data()
    print(html.count('rank-book-item'))
    novels = parse_data(html)
    save_to_csv(novels)

if __name__ == "__main__":
    main()
