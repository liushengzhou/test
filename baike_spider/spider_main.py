# coding=utf-8
from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        # 初始化URL管理器
        self.urls = url_manager.UrlManager()
        # 初始化下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 初始化解析器
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1  # 初始记录序号
        self.urls.add_new_url(root_url)  # 添加新的url
        # 如果存在新的url
        while self.urls.has_new_url():

            try:
                # 获取新的url地址
                new_url = self.urls.get_new_url()
                print "craw %d:%s" % (count, new_url)
                html_cont = self.downloader.download(new_url)

                # 解析网页和内容
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 100:
                    break
                count += 1
            except:
                print "crow failed"
        self.outputer.output_html()


if __name__ == "__main__":
    # 入口URL
    root_url = "https://baike.baidu.com/item/Python"
    # 爬虫总调度程序
    obj_spider = SpiderMain()
    # 执行爬虫抓取方法
    obj_spider.craw(root_url)
