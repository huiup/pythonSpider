import requests
from pprint import pprint
# requests爬取动态加载数据

# 指定url
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
url = 'https://movie.douban.com/j/chart/top_list'
# 设置请求参数,注：get请求用params，post用data
params = {
	'type': '5',
	'interval_id': '100:90',
	'action': '',
	'start': 0,
	'limit': 20,
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
response = requests.get(url=url,headers=headers,params=params)

# .json():返回的是字符串形式的json反序列化成的字典或列表对象
res_text = response.json()

for movie in res_text:
	name = movie['title']
	score = movie['score']
	print(name,score)
# pprint:可以格式化打印
pprint(res_text)