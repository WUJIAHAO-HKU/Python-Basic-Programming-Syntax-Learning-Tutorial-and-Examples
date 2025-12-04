import requests
from lxml import etree
import pandas as pd

def fetch_data():
    url = "https://movie.douban.com/top250"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text

def parse_data(html):
    tree = etree.HTML(html)
    movies = []
    for item in tree.xpath("//div[@class='item']"):
        title = item.xpath(".//span[@class='title'][1]/text()")[0]
        rating = item.xpath(".//span[@class='rating_num']/text()")[0]
        movies.append({"title": title, "rating": rating})
    return movies

def save_to_csv(movies):
    df = pd.DataFrame(movies)
    df.to_csv("douban_movies.csv", index=False, encoding='utf-8')

def main():
    html = fetch_data()
    movies = parse_data(html)
    save_to_csv(movies)

if __name__ == "__main__":
    main()