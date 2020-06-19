import requests
from pprint import pprint
import os
 
dir_name = 'lushi_dir'
if not os.path.exists(dir_name):
	os.mkdir(dir_name)

url = 'https://hs.blizzard.cn/action/cards/query'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

# cardClass:职业
# [瞎子，德鲁伊，猎人，法师，圣骑士，牧师，潜行者，萨满，术士，战士，中立]
# cardClass = ['demonhunter','druid','hunter','mage','paladin','priest','rogue','shaman','warlock','warrior','neutral']
# cost:卡牌的费用
# cost = [0,1,2,3,4,5,6,7]
# p:分页(一次只请求8张卡，有多余的将放下一页)
params = {
	'cost': 7,
	'cardClass': 'neutral',
	'keywords': '',
	'standard': 1,
	't': '1587958960092',
	'cardSet': '',
	'p': 4
}
page_text = requests.post(url=url,headers=headers,params=params).json()
# pprint(page_text['cards'])
for card in page_text['cards']:
	img_title = card['name']
	img_url = card['imageUrl']
	img_path = dir_name+'/'+img_title+'.png'
	img_data = requests.get(url=img_url,headers=headers).content
	with open(img_path,'wb') as fp:
		fp.write(img_data)
	print(img_title+'下载成功！')
