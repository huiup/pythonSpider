# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

'''
-动作链(ActionChains)
	-动作链：
		-一系列连续的动作(滑动动作)
'''
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
bro = webdriver.Chrome(executable_path='D:\python_spider\selenium\chromedriver.exe')
bro.get(url)
sleep(1)
# 通过find系列的函数进行标签定位时，如果标签是存在与iframe下的，则会定位失败
# 解决方案：使用swith_to即可
bro.switch_to.frame('iframeResult')
div_tag = bro.find_elements_by_xpath('//*[@id="draggable"]')[0]


# 进行滑动操作
action = ActionChains(bro)
action.click_and_hold(div_tag)# 点击且长按

for i in range(6):
	action.move_by_offset(10,15).perform()
	sleep(0.5)
# 释放动作链
action.release()
bro.quit()
