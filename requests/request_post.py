import requests
from pprint import pprint
# post爬取分页数据(kfc的餐厅位置数据(ajax))

# 指定url
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
for page in range(1,9):# 共有8页
	data = {
		'cname': '',
		'pid': '' ,
		'keyword': '北京',
		'pageIndex': str(page),
		'pageSize': '10',
	}
	headers = {
	    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
	}
	response = requests.post(url=url,headers=headers,data=data)

	# .json():返回的是字符串形式的json反序列化成的字典或列表对象
	res_text = response.json()

	# pprint:可以格式化打印
	# pprint(res_text)
	for dic in res_text['Table1']:
		store_name = dic['storeName']
		addr = dic['addressDetail']
		print(store_name,addr)
