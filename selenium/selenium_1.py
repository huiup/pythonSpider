# coding:utf-8
from selenium import webdriver
from time import sleep
'''
selenium
- 概念：基于浏览器自动化的模块
- 自动化：可以通过代码指定一些列的行为动作，然后将其作用到浏览器中。
- pip install selenium
- selenium和爬虫之间的关联
	- 1.便捷的捕获到任意形式动态加载的数据（可见即可得）
	- 2.实现模拟登录
-谷歌驱动下载： http://chromedriver.storage.googleapis.com/index.html（我用的2.43）
-服务器检测：
	-在浏览器中打开开发者工具输入window.navigator.webdriver时会显示true,
	说明被服务器检测到了,通常情况下会显示undefined
-规避检测(selenium接管本地浏览器)：
from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#实例化一个浏览器对象
bro = webdriver.Chrome(executable_path='your driver path',options=option)
bro.get('https://www.taobao.com/')

- 无头浏览器（无可视化界面的浏览器）
	-谷歌无头浏览器（详情请查看第4个py文件）

'''
# 1.基于浏览器的驱动程序实例化一个浏览器对象
bro = webdriver.Chrome(executable_path='./chromedriver')
# 2.对目的网站发起请求
bro.get('https://www.jd.com/')
# 标签定位(id、xpath、class)
search_text = bro.find_element_by_xpath('//*[@id="key"]')
# 向标签中录入数据
search_text.send_keys('笔记本')
# 定位到搜索按钮
btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(2)
# 在搜索结果页面进行滚轮向下滑动的操作（执行js操作：js注入(滑动到底部)）
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# bro.quit()