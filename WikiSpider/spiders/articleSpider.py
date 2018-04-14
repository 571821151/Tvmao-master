# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from WikiSpider.items import Article
from scrapy.contrib.linkextractors import LinkExtractor

import urllib
import time
def download_img(url):
    path = str(time.time()) + ".gif"  # 给图片按先后顺序命名
    data = urllib.urlopen(url).read()  # 打开URL
    f = open('d:/gif/' + path, "wb")  # 读取，写入G盘的资料文件夹
    f.write(data)
    f.close()
class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["www.1300a.com"]
    start_urls = ["https://www.1300a.com/Html/60/" ]
    rules = [Rule(LinkExtractor(allow=('(/Html/)((?!:).)*$'), ),
                  callback="parse_item", follow=True)]

    def parse_item(self, response):
        item = Article()
        program = response.xpath('//h3/text()')
        img=response.xpath("//li/a/img/@src")
        if len(program):
            for i in img.extract():
                print(i)
                download_img(i)
            for i in program.extract():
                print(i)
                item["program"] = program.extract()
                return item
        else:
            return ""

