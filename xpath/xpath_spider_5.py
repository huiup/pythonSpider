# coding:utf-8
from lxml import etree
import requests
import os
# 使用xpath爬取站长网站下的免费简历模板
#下载rar压缩包

dir_name = 'jianli_dir'
if not os.path.exists(dir_name):
	os.mkdir(dir_name)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
url = 'http://sc.chinaz.com/jianli/free.html'

page_text = requests.get(url=url,headers=headers).text
# print(page_text)
tree = etree.HTML(page_text)
links_list = tree.xpath('//div[@id="container"]/div/a/@href')
for link in links_list:
	response = requests.get(url=link,headers=headers)
	response.encoding = 'utf-8'
	jianli_text = response.text

	tree = etree.HTML(jianli_text)
	down_link = tree.xpath('//*[@id="down"]/div[2]/ul/li[2]/a/@href')
	print(down_link)
	jianli_name = tree.xpath('//h1/text()')[0]+'.rar'
	jianli_data = requests.get(url=down_link[0],headers=headers).content
	with open(dir_name + "/" + jianli_name,'wb') as fp:
			fp.write(jianli_data)
	print(jianli_name,'下载成功！')
	




