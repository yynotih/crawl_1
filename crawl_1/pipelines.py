# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


# class Crawl1Pipeline(object):

# def __init__(self):
#     self.file = codecs.open('spider_1.json','awb',encoding='utf-8') #awb,a表示从文件末尾添加，不会覆盖原文件，w表示写，b表示二进制

# def process_item(self, item, spider):
#     line = json.dumps(dict(item))+'\n'
#     self.file.write(line.decode('unicode_escape'))
#     return item

class MyImagesPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        for image_url in item['image_uls']:
            self.log.info(image_url.replace(' ', ''))
            yield scrapy.Request(image_url.replace(' ', ''))

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
