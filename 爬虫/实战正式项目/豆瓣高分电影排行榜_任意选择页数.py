import requests
from lxml import etree
import pandas as pd

def fetch_data(page_num):
    start = (page_num - 1) * 25
    url = f"https://movie.douban.com/top250?start={start}&filter="
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text


def parse_data(html):
    tree = etree.HTML(html)
    movies = []
    for item in tree.xpath("//div[@class='item']"):
        # 标题和评分部分保持不变
        title = item.xpath(".//span[@class='title'][1]/text()")[0]
        rating = item.xpath(".//span[@class='rating_num']/text()")[0]
        
        # 取第1个<p>标签的所有文本，通常是导演主演和时间国家信息
        p_texts = item.xpath(".//div[@class='bd']/p[1]/text()")
        # p_texts 是一个列表，包含多段文本，比如：
        # ['\n导演: 弗兰克·德拉邦特 Frank Darabont\xa0\xa0\xa0主演: 蒂姆·罗宾斯 Tim Robbins / ...', '\n1994\xa0/\xa0美国\xa0/\xa0犯罪 剧情']
        
        # 提取时间和国家信息，通常在第2个文本元素里（索引1）
        if len(p_texts) > 1:
            time_country = p_texts[1].strip()
            # time_country 示例: "1994 / 美国 / 犯罪 剧情"
            parts = time_country.split(" / ")
            year = parts[0] if len(parts) > 0 else ''
            country = parts[1] if len(parts) > 1 else ''
        else:
            year = ''
            country = ''
        
        # 评价人数在 <div class="bd"> 下的第1个div里面的span最后一个， xpath选取：
        people_text = item.xpath(".//div[@class='bd']/div[1]/span[last()]/text()")
        # people_text 例：['3165877人评价']
        if people_text:
            # 取数字部分
            people_num = people_text[0].replace("人评价", "").strip()
        else:
            people_num = ''
        
        movies.append({
            "title": title,
            "rating": rating,
            "year": year,
            "country": country,
            "people_num": people_num
        })
    return movies

def save_to_csv(movies):
    df = pd.DataFrame(movies)
    df.to_csv("douban_movies.csv", index=False, encoding='utf-8')

def main():
    total_pages = int(input("请输入要爬取的页数（每页25条）："))
    all_movies = []
    for i in range(1, total_pages + 1):
        print(f"正在爬取第 {i} 页...")
        html = fetch_data(i)
        movies = parse_data(html)
        all_movies.extend(movies)
    save_to_csv(all_movies)
    print("爬取完成，数据已保存到douban_movies.csv")

if __name__ == "__main__":
    main()
