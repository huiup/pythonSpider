import requests
# requests的简单使用

# 指定url
url = 'https://www.sogou.com/sogou'
params = {
    'query': 'jay'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
}
response = requests.get(url=url, headers=headers, params=params)
# 可以查看(设置)编码
# print(response.encoding)
response.encoding = 'utf-8'
# text:返回的是字符串形式的数据
res_text = response.text
# 持久化存储
with open('sogou.html', 'w', encoding='utf-8') as f:
    f.write(res_text)
