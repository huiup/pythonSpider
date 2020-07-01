import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib
#转为汉字

class HtmlParser(object):
    def get_new_urls(self, page_url, soup):
        new_urls = set()
        # href = "/item/%E8%AF%BE%E7%A8%8B"
        links = soup.find_all('a', href=re.compile("/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            # 用urllib.parse.unquote()方法把乱码转为汉字,但url无法访问
            # new_full_url = urllib.parse.unquote(new_full_url)
            new_urls.add(new_full_url)
        return new_urls


    def get_new_data(self, page_url, soup):
        res_data = dict()
        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="para" label-module="para">
        summary_node = soup.find('div', class_='para')
        res_data['summary'] = summary_node.get_text()
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data



