# coding:utf-8
# 基于线程池的异步爬虫
import requests
import time
# 导入线程池模块
from multiprocessing.dummy import Pool

urls = [
    'http://127.0.0.1:5000/hui',
    'http://127.0.0.1:5000/index',
    'http://127.0.0.1:5000/bobo'
]


def get_request(url):
    page_text = requests.get(url=url).text
    return page_text


def parse(text):
    print(text)


# 同步代码
# if __name__ == '__main__':
#     start = time.time()
#     for url in urls:
#         a = get_request(url)
#     print('总耗时：', time.time() - start)  # 总耗时： 6.013944387435913

# 异步代码
if __name__ == '__main__':
    start = time.time()
    # 3表示开启线程的数量
    pool = Pool(3)
    # Pool.map(callback,alist)
    # 使用get_request作为回调函数，基于异步的形式对urls列表中的每一个列表元素进行操作
    # 保证回调函数必须要有一个参数和返回值
    # 两个map之间是串行
    result_list = pool.map(get_request, urls)
    pri = pool.map(parse, result_list)
    # print(result_list)
    print('总耗时：', time.time() - start)  # 总耗时： 2.0133843421936035
