# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from WikiSpider.items import Yellow
from scrapy.contrib.linkextractors import LinkExtractor
import urllib2
import time

def getImgFromUrl(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    request = urllib2.Request(url, None, header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
    response = urllib2.urlopen(request)
    with  open('D:\\gif\\'+str(time.time())+'.gif', 'wb') as f:
        f.write(response.read())
        f.close()

class YellowSpider(CrawlSpider):
    name = "yellow"
    # allowed_domains = ["www.1304q.com"]
    Urls=[]
    for i in range(60,127):
        Urls.append("https://www.1308y.com/Html/"+str(i))
    start_urls = Urls

    rules = [Rule(LinkExtractor(allow=('/Html/\d+/\d+.*'), ),
                  callback="parse_item", follow=True)]

    def parse_item(self, response):
        print(response.url)
        item = Yellow()
        title = response.xpath('//dd[@class="film_title"]/h1/text()')
        img=response.xpath("//dl/dt/img/@src")
        video=response.xpath('//ul[@class="downurl"]/a/font/text()')
        program=response.xpath("//dl/dd/span/text()")

        item["img"]=img.extract()[0]
        # getImg(i)下载图片
        item["program"] = program.extract()[0].encode("utf8")
        item["video"] = video.extract()[0]
        item["title"] = title.extract()[0].encode("utf8")
        yield item


