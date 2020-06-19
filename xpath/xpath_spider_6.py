# coding:utf-8
from lxml import etree
import requests
import os
# 站长素材中的高清图片下载：
# 	-反爬机制：图片懒加载（广泛应用在一些图片网站中）
# 	即：只有当图片被显示在浏览器可视化范围之内才会将ing标签中的伪属性(即本例中的src2)变成真正的属性。
# 	如果是requests发起的请求，requests请求是没有可视化范围的，因此我们要解析的是img伪属性的属性值

dir_name = 'img_dir'
if not os.path.exists(dir_name):
	os.mkdir(dir_name)
url = 'http://sc.chinaz.com/tupian/faxingtupian.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
img_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
title_list = tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
# 转为字典
list_dict = dict(zip(title_list,img_list))
for title,url in list_dict.items():
	img_path = dir_name + '/' + title + '.jpg'
	img_data = requests.get(url=url,headers=headers).content
	with open(img_path,'wb') as f:
		f.write(img_data)
	print(title,'爬取完毕！')
