# coding:utf-8
import requests
# 爬取网络图片

img_url = 'http://bbs.orzice.com/data/attachment/forum/201802/14/102510j91highd9zieecdh.jpg'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
response = requests.get(url=img_url,headers=headers)
# content返回的是二进制形式的数据
img_data = response.content
with open('1.jpg','wb') as f:
	f.write(img_data)

