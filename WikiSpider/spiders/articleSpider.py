from scrapy.contrib.spiders import CrawlSpider, Rule
from WikiSpider.items import Article
from scrapy.contrib.linkextractors import LinkExtractor


class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["www.tvmao.com"]
    start_urls = ["https://www.tvmao.com/program" ]
    rules = [Rule(LinkExtractor(allow=('(/program/)((?!:).)*$'), ),
                  callback="parse_item", follow=True)]

    def parse_item(self, response):
        item = Article()
        program = response.xpath('//div[@class="pbar"]/text()')[0].extract()
        print("title is: " + program)
        item["program"] = program
        return item
