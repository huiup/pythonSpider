import requests

# 测试ip是否可用

proxies = {
    "http": "http://125.108.118.223:9000",
    # "https": "https://113.195.23.184:9999"
}
req = requests.get('http://icanhazip.com/', proxies=proxies)
print(req.text)