#  coding:utf-8
import asyncio
import time

'''
单线程+多任务异步协程：pip install asyncio
- 特殊的函数
    - 如果一个函数被async修饰后，则该函数就变成一个特殊函数
    - 特殊之处：
        - 该特殊的函数被调用后，函数内部的实现语句不会被立即执行
        - 该特殊的函数被调用后，会返回一个协程对象
- 协程对象
    - 对象。通过调用特殊函数返回的一个协程对象
    - 协程 == 特殊函数 == 一组指定的操作
    - 协程 == 一组指定的操作
- 任务对象
    - 任务对象就是一个高级的协程对象。（任务对象就是对协程对象的进一步封装）
    - 任务对象 == 协程对象 == 特殊函数 == 一组指定的操作
    - 任务对象 == 一组指定的操作
    - 如何创建一个任务对象：
        - asyncio.ensure_future(协程对象)
    - 任务对象的高级之处：
        - 可以给任务对象绑定回调
            - task.add_done_callback(task_callback)
            - 回调函数的调用时机
                - 任务被执行结束后，才调用回调函数
            - 回调函数的参数只可以有一个：就是该回调函数的调用者（任务对象）
            - 使用回调函数的参数调用result()返回的就是其任务对象表示的特殊函数的return结果
- 事件循环对象
    - 对象。
    - 作用
        - 可以将多个任务对象注册/装载到事件循环对象中
        - 如果开启了事件循环后，则其内部注册/装载的任务对象表示的指定操作就会被基于异步的被执行
    - 创建方式：
        - loop = asyncio.get_event_loop()
    - 注册且启动的方式：
        - loop.run_until_complete(任务对象)
- asyncio.wait()的作用：
    - 将任务列表中的任务对象赋予可被挂起的权限。只有任务对象被赋予了可被挂起的权限后，该任务对象才可以被挂起
        - 挂起：将当前的任务对象交出cpu的使用权
- 注意事项（***）
    - 在特殊函数内部不能出现不支持异步模块对应的代码，否则会中断整个异步效果
- await关键字
    - 在特殊函数内部，凡是阻塞操作前都必须使用await进行修饰。await就可以保证阻塞操作
        在异步执行中不会被跳过！！！
'''


async def get_request(url):
    print('正在请求的url：', url)
    time.sleep(2)
    print('请求结束：', url)
    return 'huihuiya'


# 回调函数的封装
# 参数t：就是该回调函数的调用者（任务对象）
def task_callback(t):
    print('我是任务对象的回调函数，参数t：', t)
    # result返回的是特殊函数的返回值
    print('t.result返回的是：', t.result())


if __name__ == '__main__':
    # c就是一个协程对象（若特殊函数有自己的返回值，还是返回一个协程对象）
    c = get_request('www.baidu.com')
    # 任务对象就是对协程对象的进一步封装
    task = asyncio.ensure_future(c)
    # 给task绑定一个回调函数
    task.add_done_callback(task_callback)
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将任务对象注册到事件循环中，且开启事件循环
    loop.run_until_complete(task)
