import re
import requests
from lxml import etree
import os

# 爬取梨视频某模块下的热门视频
# 1.根据分类页找到热门视频的视频播放页链接
# 2.再在播放页找到动态加载的(隐藏在js中)视频链接（全局搜索）
dir_name = 'video_dir'
if not os.path.exists(dir_name):
	os.mkdir(dir_name)
main_url = 'https://www.pearvideo.com/category_59'
# main_url = 'https://www.pearvideo.com/category_130'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
page_text = requests.get(url=main_url,headers= headers).text
tree = etree.HTML(page_text)
video_num_list = tree.xpath('//ul[@id="listvideoListUl"]/li/div/a/@href')
for num in video_num_list:
	# 得到视频播放页url
	url = "https://www.pearvideo.com/"+num
	res_video_text = requests.get(url=url,headers=headers).text
	# print(res_video_text)
	ex = 'srcUrl="(.*?)",vdoUrl=srcUrl'
	# 得到视频具体链接
	video_url = re.findall(ex,res_video_text,re.S)[0]
	video_name = re.findall('<h1 class="video-tt">(.*?)</h1>',res_video_text)[0]
	video_data = requests.get(url=video_url,headers=headers).content
	video_path = dir_name+'/'+video_name+'.mp4'
	with open(video_path,'wb') as fp:
		fp.write(video_data)	
	