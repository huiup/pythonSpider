#  coding:utf-8

import asyncio
import time
import aiohttp
import requests
from lxml import etree

urls = [
    'http://127.0.0.1:5000/hui',
    'http://127.0.0.1:5000/index',
    'http://127.0.0.1:5000/bobo'
]
data_list = []

# async def get_request(url):
#     # requests是一个不支持异步的模块
#     page_text = requests.get(url=url).text
#     return page_text

async def get_request(url):
    # 实例化一个请求对象
    async with aiohttp.ClientSession() as sess:
        # 调用get发起请求，返回一个响应对象
        # get/post(url,headers,params/data,proxy="http://ip:port")，此处参数除了proxy的格式不同，其它都与requests模块一样
        # get使用params，post使用data
        async with await sess.get(url=url) as response:
            # text():获取字符串形式的响应数据
            # read()：获取byte类型的响应数据
            page_text = await response.text()
            return page_text


# 解析函数
def parse(t):
    # 获取请求到的页面源码数据
    page_text = t.result()
    tree = etree.HTML(page_text)
    parse_text = tree.xpath('//*[@id="hui"]/text()')[0]
    print(parse_text)


if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(parse)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时：', time.time() - start)
