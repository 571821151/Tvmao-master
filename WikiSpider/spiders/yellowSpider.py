# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from WikiSpider.items import Yellow
from scrapy.contrib.linkextractors import LinkExtractor
import urllib2
import time,mongo_util

def getImg(url):
    name = url;
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    request = urllib2.Request(url, None, header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
    response = urllib2.urlopen(request)
    with  open('D:\\gif\\'+str(time.time())+'.gif', 'wb') as f:
        f.write(response.read())
        f.close()



    f.close()
class YellowSpider(CrawlSpider):
    name = "yellow"
    # allowed_domains = ["www.1304q.com"]
    a=[]
    for i in range(60,127):
        a.append("https://www.1308y.com/Html/"+str(i))
    start_urls = a

    rules = [Rule(LinkExtractor(allow=('/Html/\d+/\d+.*'), ),
                  callback="parse_item", follow=True)]

    def parse_item(self, response):
        sample_yellow = {}
        # print(response.url)
        item = Yellow()
        mongo_base = mongo_util()
        title = response.xpath('//dd[@class="film_title"]/h1/text()')
        img=response.xpath("//dl/dt/img/@src")
        video=response.xpath('//ul[@class="downurl"]/a/font/text()')
        program=response.xpath("//dl/dd/span/text()")
        if len(program):

            for i in img.extract():
                print(i)
                sample_yellow["img"]=i
                # getImg(i)下载图片
            for i in program.extract():
                print(i)
                sample_yellow["program"] = i.encode("utf8")
            for i in video.extract():
                print(i)
                sample_yellow["video"] = i
            for i in title.extract():
                print(i )
                sample_yellow["title"] = i.encode("utf8")
            print(sample_yellow)
            mongo_base.add_bjon(sample_yellow)
            item["program"] = program.extract()
            return item
        else:
            print( 'error---stop')
            return ""

