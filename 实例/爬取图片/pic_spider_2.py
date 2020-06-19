# coding:utf-8
import re
import requests
import os
# 使用正则爬取网络美女图片（案例需要QAQ）
dir_name = 'img_lib'
if not os.path.exists(dir_name):
	os.mkdir(dir_name)
url = 'http://www.521609.com/qingchunmeinv'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
page_text = response.text
# 正则方法
ex = '<li>.*?<img src="(.*?)" width=.*?></li>'
img_url_list = re.findall(ex,page_text,re.S)
for src in img_url_list:
	img_url = 'http://www.521609.com'+src
	# /uploads/allimg/110715/1093002H94-1-lp.jpg
	img_path = dir_name+'/'+src.split('/')[-1]
	res_img_data = requests.get(url=img_url,headers=headers).content
	with open(img_path,'wb') as f:
		f.write(res_img_data)
	print(img_path,'下载成功！')


