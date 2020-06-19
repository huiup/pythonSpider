# coding:utf-8
from lxml import etree
import requests
# 爬取网站城市
url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
# hot_cities = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
# all_cities = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
# 可以用"|"把两者合并
cities = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div[2]/li/a/text()')

print(cities)