from lxml import etree

'''
解析原理：
	-1.实例化一个etree对象，且将待解析的页面源码数据加载到该对象中
	-2.调用etree对象的xpath方法结合这不同的xpath表达式
实例化etree对象：
	-一般使用etree.HTML(page_text):解析html类数据
标签定位：
	-最左侧的/：如果xpath表达式罪左侧是以/开头则表示该xpath表达式一定要从根标签开始定位指定标签(一般不用)
	-非最左侧的/：表示一个层级
	-非左侧的//：表示多个层级
	-最左侧的//：xpath表达式可以从任意位置进行标签定位
属性定位：
	-tagName[@attrName='value']
索引定位：
	-tag[index]:索引是从1开始的
取范围：(取该ul下的第2到第6个li)
	"//*[@id='nav']/ul/li[position()>1 and position()<7]"
模糊匹配(不常用)：
	-//div[contains(@class,"ng")]
	-//div[starts-with(@class,"ta")]
取文本：
	-/text():取直系文本内容
	-//text()：取所有的文本内容
取属性：
	-/@attrName
局部数据解析：
	-将定位到的页面标签再次使用xpath解析
	-在局部数据解析的时候，xpath表达式中要使用./的操作，./表示的就是当前的局部数据
使xpath表达式更具有通用性：
	- |：在xpath表达式中使用管道符( | )分割，它表示 | 两边的子xpath表达式同时生效或一个生效
'''
fp = open('test.html','r',encoding='utf-8')
text = fp.read()
tree = etree.HTML(text)
# print(text)
# t = tree.xpath('/html/head/title')
# t = tree.xpath('//div[@id="top_left_menu"]/ul/li[8]/a/text()')
# t = tree.xpath('//div[@id="top_left_menu"]/ul/li//text()')
t = tree.xpath('//div[@id="top_left_menu"]/ul/li[8]/a/@href')
print(t)
