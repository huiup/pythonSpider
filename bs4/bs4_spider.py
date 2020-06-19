# coding:utf-8
from bs4 import BeautifulSoup
import lxml
import re
'''
bs4解析原理：
	- 实例化一个BeautifulSoup的对象，且将待解析的页面源码数据加载到该对象中
	- 调用BeautifulSoup对象中相关方法或者属性进行标签定位和文本数据的提取
解析器：'lxml'/'html.parser'
'''

'''
标签定位：
	- soup.tagName：只可以定位到第一次出现的tagName标签
	- soup.find('tagName',attrName='value')：属性定位(单个)
	- soup.find_all():跟find()一样用作属性定位，只不过find_all()返回的是列表(多个)
	- soup.select('选择器')：
		-类选择器
		-id选择器
		-层级选择
			- >(大于号)：表示一个层级
			- 空格：表示多个层级
取数据：
	.text：返回的是该标签下所有的文本内容
	.get_text():同上
	.string：返回的是该标签直系的文本内容
取属性值：
	tag['attrName']
'''

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://examples.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="end">...</p>
</body></html>
"""
soup = BeautifulSoup(html_doc, 'lxml')
test = soup.findAll('a')
print(test[1].text)
print(soup.find('a',class_='story'))
print(soup.find('a',id='link2'))
print(soup.find_all('a',id='link2'))
print(soup.select('.story > a'))
print(soup.select('.story a'))


# print('获取所有的链接：')
# links = soup.find_all('a')
# for link in links:
#     print(link.name, link['href'], link.get_text())
# # 1.获取节点的名字、2.获取属性的内容、3.获取节点的文字
# print('获取Elsie的链接：')
# link_node = soup.find('a', href='http://example.com/lacie')
# print(link_node.name, link_node['href'], link_node.get_text())

# print('正则匹配：')
# link_node = soup.find('a', href=re.compile(r'lli'))
# print(link_node.name, link_node['href'], link_node.get_text())

# print('获取p段落文字：')
# # 为了区别于class关键字，此处规定为class_
# p_node = soup.find('p', class_='title')
# print(p_node.name, p_node['class'], p_node.string)
