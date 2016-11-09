# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field

class Crawl1Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # address = Field();
    # text = Field();
    image_urls = Field()
    images = Field()
