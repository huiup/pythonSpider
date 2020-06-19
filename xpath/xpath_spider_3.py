# coding:utf-8
from lxml import etree
import requests
import os
# 使用xpath爬取图片和文字(多页)

dir_name = 'xpath_img_lib'
if not os.path.exists(dir_name):
	os.mkdir(dir_name)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

# 定义一个通用的url模板(不可变)
url = 'http://pic.netbian.com/4kdongman/index_%d.html'
for page in range(6):
	if page == 1:
		new_url = 'http://pic.netbian.com/4kdongman/'
	else:
		new_url = format(url%page)

	response = requests.get(url=new_url,headers=headers)
	response.encoding = "gbk"
	page_text = response.text
	# 解析图片名称和图片
	tree = etree.HTML(page_text)
	# 定位到li标签
	li_list = tree.xpath('//div[@class="slist"]/ul/li')
	# t = tree.xpath('//*[@id="m')
	for li in li_list:
		# 进行局部xpath解析
		img_title = li.xpath('./a/img/@alt')[0]+'.jpg'
		img_url = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
		img_data = requests.get(url=img_url,headers=headers).content
		print(img_url)
		img_path = dir_name + '/' + img_title
		with open(img_path,'wb') as fp:
			fp.write(img_data)
		print('下载保存'+img_title+'成功！')
