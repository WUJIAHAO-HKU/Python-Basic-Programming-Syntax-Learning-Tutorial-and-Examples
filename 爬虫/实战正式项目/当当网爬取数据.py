from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_book_titles(url):
    # Chrome无头浏览器配置
    options = Options()
    options.add_argument('--headless')  # 无界面模式
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("window-size=1920,1080")  # 设置窗口大小，防止有些元素加载失败
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # 等待页面加载和js执行完成
    time.sleep(15)

    html = driver.page_source
    print(html)
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    titles = []
    # 选所有 div.name 下面 a标签的title属性
    a_tags = soup.select('div.name a[title]')
    for a in a_tags:
        titles.append(a['title'].strip())
    return titles

if __name__ == '__main__':
    base_url = 'https://e.dangdang.com/classification_list_page.html?category=JSJWL&dimension=dd_sale&order=0'
    all_titles = []
    max_pages = 5
    max_total_titles = 5  # 你想爬取的最大书名数

    for page in range(1, max_pages + 1):
        if len(all_titles) >= max_total_titles:
            print(f'已达到最大爬取书名数量 {max_total_titles}，停止爬取')
            break

        url = f'{base_url}&page_index={page}'
        print(f'正在抓取第{page}页，URL={url}')
        titles = get_book_titles(url)
        if not titles:
            print('未抓取到书名，可能页面结构变更或已无更多内容')
            break
        
        # 如果当前页加上已有书名超过最大目标，只取需要数量部分 
        remaining_slots = max_total_titles - len(all_titles)
        if len(titles) > remaining_slots:
            titles = titles[:remaining_slots]

        print(f'本页找到书名数：{len(titles)}')
        all_titles.extend(titles)
        time.sleep(2)

    print(f'共抓取到 {len(all_titles)} 本书：')
    for i, title in enumerate(all_titles, 1):
        print(f'{i}. {title}')
