#coding=utf-8
from bs4 import BeautifulSoup
import urlparse
import re


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):

        new_urls = set()

        #查找网页所有匹配的链接
        # https://baike.baidu.com/item/Python
        links = soup.find_all('a', href=re.compile(r"/item/"))

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            return new_urls

    def _get_new_datas(self, page_url, soup):

        # 定义返回数据字典
        res_data = {}

        res_data['url'] = page_url

        # 获取网页词条名称
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text(strip=True)

        # 获取网页词条备注
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text(strip=True)

        return res_data

    def parse(self, page_url, html_cont):
        print "in html_parser def parse"
        if page_url is None or html_cont is None:
            return

        # 将网页源码放入解析
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        new_urls = self._get_new_urls(page_url, soup)
        new_datas = self._get_new_datas(page_url, soup)

        return new_urls, new_datas
