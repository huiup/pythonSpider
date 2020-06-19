# coding:utf-8
import execjs
import requests
'''
js加密：服务端客户端之间传输的是密文（非https加密，因为我们抓包是拿到客户端已经收到的数据，此时已经解密了）
js解密：还是通过加密的方法进行反解密
js混淆：对前端js代码逻辑进行加密保护，防止不法分子直接获取我们定义的重要数据及用来跟后端进行数据交互的函数等
    要区分js加密和js混淆，一个是保护数据的传输，一个是保护前端页面的代码逻辑
js反混淆：目前只提到了暴力破解js混淆：http://www.bm8.com.cn/jsConfusion/
js逆向：在py文件中执行js代码
使用 PyExecJS 模块（环境依赖：nodejs）来实现自动逆向
'''


# 初始化一个execjs
node = execjs.get()
 
# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'
 
# 编译js文件
file = 'jsCode.js'
ctx = node.compile(open(file,encoding='utf-8').read())
 
# 获取参数
js = 'getPostParamCode("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)

#发起post请求
url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response_text = requests.post(url,data={'d': params}).text
print(response_text)

#对加密的响应数据进行解密
# js = 'decodeData("{0}")'.format(response_text)
# decrypted_data = ctx.eval(js)# 返回的是解密后的原文数据
# print(decrypted_data)
# 因该网站已被玩坏，故执行会报错