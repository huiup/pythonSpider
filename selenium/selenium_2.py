# coding:utf-8
from selenium import webdriver
from time import sleep
from lxml import etree

# 捕获动态加载的数据：药监局为例(http://125.35.6.84:81/xk/)
url = 'http://125.35.6.84:81/xk/'
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get(url)
# 一个存储每一页数据的列表
page_text_list = []
sleep(1)	
# 捕获到当前页面对应的页面源码数据
page_text = bro.page_source # page_source：获取当前页面全部加载完毕后对应的所有数据
page_text_list.append(page_text)# 加入第一页的数据
# 点击下一页
for x in range(2):
	next_page = bro.find_element_by_xpath('//*[@id="pageIto_next"]')
	next_page.click()
	sleep(1)
	page_text_list.append(bro.page_source)
for page_text in page_text_list:
	tree = etree.HTML(page_text)
	li_list = tree.xpath('//*[@id="gzlist"]/li')
	for li in li_list:
		name = li.xpath('./dl/@title')
		print(name)

sleep(2)
bro.quit()

