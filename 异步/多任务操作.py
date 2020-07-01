#  coding:utf-8
import asyncio
import time
import requests

'''
asyncio.wait()的作用：
    - 将任务列表中的任务对象赋予可被挂起的权限。只有任务对象被赋予了可被挂起的权限后，该任务对象才可以被挂起
        - 挂起：将当前的任务对象交出cpu的使用权
'''


async def get_request(url):
    print('正在请求的url：', url)
    await asyncio.sleep(2)  # 支持异步模块的代码
    print('请求结束：', url)
    return 'huihuiya'


urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com'
]

if __name__ == '__main__':
    start = time.time()
    tasks = []
    # 1.创建协程对象
    for url in urls:
        c = get_request(url)
        # 2.创建任务对象
        task = asyncio.ensure_future(c)
        tasks.append(task)
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(tasks)  # 不能直接把列表作为参数
    # 必须使用asyncio.wait方法对tasks进行封装才可
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时：', time.time() - start)
