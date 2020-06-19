# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 用selenium打开无界面的chrome浏览器
#创建一个参数对象，用来控制chrome以无界面的方式打开
chrome_options = Options()
#后面的两个是固定写法
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#创建浏览器对象
browser = webdriver.Chrome(executable_path=r'D:\python_spider\selenium\chromedriver.exe',options=chrome_options)

url ='http://www.baidu.com/'

browser.get(url)
time.sleep(3)
browser.save_screenshot('baid.png')# 截图
print(browser.page_source)
browser.quit()
