# coding:utf-8
from chaojiying import transform_Img_Code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
from PIL import Image

'''
-定位到元素标签后，用.location获取坐标值时，出现较大的偏差原因和解决方法如下：
	-使用定位截图时出现这个问题的，之所以会出现这个坐标偏差是因为电脑上设置的显示缩放比例造成的，location获取的坐标是按显示100%时得到的坐标，而截图所使用的坐标却是需要根据显示缩放比例缩放后对应的图片所确定的，因此就出现了偏差。
	解决这个问题有四种方法：
		-修改电脑显示设置为100%。
		-缩放截取到的页面图片，即将截图的size缩放为宽和高都除以缩放比例后的大小（应该需要将缩放后的宽和高转化为int型）
		-修改Image.crop的参数，将参数元组的四个值都乘以缩放比例（应该也需要转化为int型）
		-使用无头浏览器

'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

url = 'https://kyfw.12306.cn/otn/login/init'
# 使用无头浏览器打开
# bro = webdriver.Chrome(executable_path='./chromedriver')
bro = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
bro.get(url)
sleep(1)
# 截取当前屏幕,并保存为main.png
bro.save_screenshot('main.png')
# 定位到验证码图片
code_img_ele = bro.find_element_by_xpath(
    '//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
# 获取验证码左上角位置
location = code_img_ele.location
print('location:', location)
# 获取图片区域的尺寸
size = code_img_ele.size
print('size:', size)
# 定制好截取图片的尺寸(电脑分辨率必须为100%等比缩放，否则选取的位置会出错)
rangle = (int(location['x']), int(location['y']), int(
    location['x'] + size['width']), int(location['y'] + size['height']))
# 打开main.png这张图片
img = Image.open('main.png')
# 创建截图图片名称
code_img_name = './code.png'
# 按指定尺寸截取
frame = img.crop(rangle)
# 保存截取的图片
frame.save(code_img_name)
# 用超级鹰识别验证码：返回图片的位置（x,y）
result = transform_Img_Code(code_img_name,9004)
print(result)

# 创建坐标数据结构
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)

# 移动光标进行点击验证码, 动作链移动光标
for lis in all_list:
    x = lis[0]
    y = lis[1]
    # 因为分辨率问题，需要定位到验证码图片这一标签，在进行移动
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    sleep(0.5)

# 获取到用户名输入框
bro.find_element_by_id('username').send_keys('15085628704')
sleep(1.5)
# 获取到密码输入框
bro.find_element_by_id('password').send_keys('19970411zhh')
sleep(1.5)
# 点击登录
bro.find_element_by_id('loginSub').click()
sleep(3)
bro.quit()
