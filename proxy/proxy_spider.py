'''
代理操作
在爬虫中,所谓的代理指的是什么?
	-就是代理服务器
代理服务器的作用是什么?
	-就是用来转发请求和响应。
在爬虫中为什么需要使用代理服务器?
	-如果我们的爬虫在短时间内对服务器发起了高频的请求,那么服务器会检测到这样的一个异常的行为请求,就会将
	该请求对应设备的ip禁掉,就以为这client设备无法对服务器端再次进行请求发送。(ip被禁掉了)
	如果ip被禁,我们就可以使用代理服务器进行请求转发,破解ip被禁的反爬机制。因为使用代理后,服务器端接受
	到的请求对应的ip地址就是代理服务器而不是我们真正的客户端的。
代理服务器分为不同的匿名度
	-透眀代理∶如果使用了该形式的代理,服务器端知道你使用了代理机制也知道你的真实ip。
	-匿名代理:知道你使用代理,但是不知道你的真实ip
	-高匿代理:不知道你使用了代理也不知道你的真实ip
代理的类型
	-https代理只能转发https协议的请求
	-http转发http的请求
代理服务器:
	-快代理
	-西祠代理
	-goubanJla
	-精灵代理
'''
# 添加代理(池)只需在get()中添加相应的参数即可
import random
import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
# 模板如下
# proxy_list = 从网站上购买的代理列表
http_proxy = {}  # 代理池
for proxy in http_proxy:
    dic = {
        'https': proxy
    }
    http_proxy.append(dic)

# 格式如下：proxies接收一个字典：proxies={'http':'118.112.195.229:9999'}
response = requests.get(url=url, headers=headers,
                        proxies=random.choice(http_proxy))
res_text = response.text
print(res_text)
# ~~~
