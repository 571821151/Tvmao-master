# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Yellow(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    program = Field()
    img=Field()
    title=Field()
    video=Field()
    pass
