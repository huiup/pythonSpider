import requests
'''
问题:基于之前一样的操作，我们没有请求到我们想要的数据
原因:我们没有严格意义上模拟浏览器发请求。
	-处理:可以将浏览器发请求携带的请求头,全部粘贴在 headers字典中,将 headers作用
		到requests的请求操作中即可。
cookie的处理方式
	-方式1:手动处理
		-将抓包工具中的 Cookie粘贴在 headers中
		-弊端: cookie如果过了有效时长则该方式失效。
	-方式2:自动处理
		-基于 Session对象实现自动处理。
		-如何获取一个 session对象: requests. Session返回一个 session对象。
		session对象的作用:
			-该对象可以向 requests一样调用get和post发起指定的请求。只不过如果在
				使用 session发请求的过程中如果产生了 cookie,则 cookie会被自动
				存储到该 session对象中,那么就意味着下次再次使用 session对象发
				起请求,则该次请求就是携带 cookie进行的请求发送。
			-在爬虫中使用 session的时候, session对象至少会被使用几次?
				两次:第一次使用 session是为了将 cookie捕获且存储到 session对象
					中。下次的时候就是携带coke进行的请求发送。
'''
# 自动获取cookie
main_url = 'https://xueqiu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
# 创建session对象
session = requests.Session()
# 第一次使用session捕获且存储cookie，猜测对雪球网的首页发起的请求可能会产生cookie
session.get(url=main_url, headers=headers)  # 捕获且存储cookie

url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=41795&size=15'
# 携带cookie发起请求
response = session.get(url=url, headers=headers).json()
print(response)


# 手动设置cookie
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
#     'Cookie': 'aliyungf_tc=AQAAAB9B2XQ8DwkATXHMAWIMazfrqRet; acw_tc=2760821b15878953416051719e4b105b74e4f29e8b6c8af5704006efbebcc6; xq_a_token=48575b79f8efa6d34166cc7bdc5abb09fd83ce63; xqat=48575b79f8efa6d34166cc7bdc5abb09fd83ce63; xq_r_token=7dcc6339975b01fbc2c14240ce55a3a20bdb7873; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4OTY4MjczMCwiY3RtIjoxNTg3ODk1MzEyNDUwLCJjaWQiOiJkOWQwbjRBWnVwIn0.Sih44M_vSp5f-__35UgiL4509d3pH0606HrYY1oGenYIiMQ-bQnPwNu9VWP8Dy0L3ctl4gYay_TW6BoMqwhODauaGvk5AqqgpfSRiBwmLdVufPJVfCjGX233yN7byHijTejRIsqDu_XsAgbVILnNMfutRg-JtrBzckJsmvT_UY7F2adGRTPX3zzM8ynqZAdy-73MxxI9rJwY_v9ROeAD94cfdoju_jbV3jtt15Kz9HXjipYe4s_BnK_G0nIG7uVqqOLCYdx48dgymqIO6BTPrqq0oiFDmEQQ1mjvPhEe-tc_X1uqjo6sJFxqYyLMyzk5U7Zu95FHYur5g921Ogy6XQ; u=591587895341614; device_id=24700f9f1986800ab4fcc880530dd0ed'
#     }
# url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=41795&size=15'
# # 携带cookie发起请求
# response = requests.get(url=url,headers=headers).json()
# print(response)
