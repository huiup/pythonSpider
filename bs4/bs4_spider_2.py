# coding:utf-8
from bs4 import BeautifulSoup
import lxml
import requests
from urllib.parse import urljoin
# 用bs4爬取小说

main_url = 'http://shicimingju.com/book/sanguoyanyi.html'
headers = {
	    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
	}
fp = open('sanguo.txt','w',encoding='utf-8')
page_text = requests.get(url=main_url,headers=headers).text
soup = BeautifulSoup(page_text,'lxml')
# 定位到所有符合要求的a标签
a_list = soup.select('.book-mulu > ul > li > a')
# print(a_list) # <a href="/book/sanguoyanyi/1.html">第一回·宴桃园豪杰三结义  斩黄巾英雄首立功</a>
for a in a_list:
	title = a.text
	# url = 'http://shicimingju.com'+a['href']
	url = urljoin(main_url,a['href'])
	# 对章节内容页发起请求解析出内容
	page_text_data = requests.get(url=url,headers=headers).text
	soup = BeautifulSoup(page_text_data,'lxml')
	div_tag = soup.find('div',class_='chapter_content')
	content = div_tag.text
	fp.write(title+':'+content+'\n')
	print(title,'读取完毕！')
fp.close()