import requests
from lxml import etree
import time


def main(offset):
    url = 'https://movie.douban.com/top250?start={}'.format(offset)
    html = get_page(url)
    print('内容为：', html)
    if html:
        # 解析页面
        parse_page(html)


def get_page(url):
    proxies = {
        "http": "http://113.195.23.52:9999",
        "http":"113.124.86.33:9999",
        "http":"49.234.46.87:8888",
        "http":"113.195.23.52:9999",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, proxies={"http": "http://160.20.166.242:3127"})
    return res.text


def parse_page(html):
    data = []
    tree = etree.HTML(html)
    li_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for li in li_list:
        res = {
            'index': li.xpath('./div/div[1]/em/text()'),
            'title': li.xpath('./div/div[2]/div[1]/a/span[1]/text()'),
            'img': li.xpath('./div/div[1]/a/img/@src'),
            'actor': li.xpath('./div/div[2]/div[2]/p[1]/text()'),
            'score': li.xpath('./div/div[2]/div[2]/div/span[2]/text()'),
        }
        print(res)


def write_file(data):
    pass


if __name__ == '__main__':
    # main(0)
    for x in range(1):
        main(offset=x * 25)
        time.sleep(4)
