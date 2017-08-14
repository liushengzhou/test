# coding:utf-8
class UrlManager(object):
    def __init__(self):
        # 定义2个参数集合
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        print "in url_manager def add_new_url"

        # 如果为空就返回false
        if url is None:
            return

        # 如果不存在新url和老url中,则添加到新的url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

        return

    def add_new_urls(self, urls):
        print "in url_manager def add_new_urls"

        # 如果这个url为空或者url集合长度是0就返回false
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)
        return

    def has_new_url(self):
        print "in url_manager def has_new_url"
        return len(self.new_urls) != 0

    def get_new_url(self):
        print "in url_manager def get_new_url"
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
