单线程+多任务异步协程：`pip install asyncio`
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
        - `asyncio.ensure_future`(协程对象)
    - 任务对象的高级之处：
        - 可以给任务对象绑定回调
            - `task.add_done_callback(task_callback)`
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
        - `loop = asyncio.get_event_loop()`
    - 注册且启动的方式：
        - `loop.run_until_complete(任务对象)`
- `asyncio.wait()`的作用：
    - 将任务列表中的任务对象赋予可被挂起的权限。只有任务对象被赋予了可被挂起的权限后，该任务对象才可以被挂起
        - 挂起：将当前的任务对象交出cpu的使用权
- 注意事项（***）
    - 在特殊函数内部不能出现不支持异步模块对应的代码，否则会中断整个异步效果
- await关键字
    - 在特殊函数内部，凡是阻塞操作前都必须使用await进行修饰。await就可以保证阻塞操作
        在异步执行中不会被跳过！！！

- loop执行过程

![image-20200630012321765](C:\Users\huihuiyo\AppData\Roaming\Typora\typora-user-images\image-20200630012321765.png)

##### aiohttp模块

- 一个支持异步的网络请求模块

- `pip install aiohttp `

- 使用代码：

  1. 先写出一个大致的架构

     - ```python
       async def get_request(url):
           # 实例化一个请求对象
           with aiohttp.ClientSession() as sess:
               # 调用get发起请求，返回一个响应对象
               # get/post(url,headers,params/data,proxy="http://ip:port")
               # 此处参数除了proxy的格式不同（proxies={'http':'ip:port'}），其它都与requests模块一样
               with sess.get(url=url) as response:
                   # text():获取字符串形式的响应数据
                   # read()：获取byte类型的响应数据
                   page_text = response.text()
       ```

  2. 补充细节

     - 在阻塞操作前加上`await`关键字

     - 在每一个`with`前加上`async`关键字

     - 一般在爬虫中，只有发请求和获取响应数据是阻塞操作

     - ```python
       async def get_request(url):
           async with aiohttp.ClientSession() as sess:
               async with await sess.get(url=url) as response:
                   page_text = await response.text()
       ```

##### 多任务爬虫的数据解析

- 一定要使用任务对象的回调函数实现数据解析
- 因为：
  - 多任务的架构中数据的爬取是封装在特殊函数中，我们一定要保证数据请求结束后，再实现数据解析。

##### 使用多任务的异步协程爬取数据实现套路

- 可以先使用`requests`模块将待请求数据对应的url封装到一个列表中（同步）
- 可以使用`aiohttp`模式将列表中的url进行异步请求I和解析（异步）