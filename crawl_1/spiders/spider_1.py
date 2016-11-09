# -*- coding:utf-8 -*-

import scrapy
from crawl_1.items import Crawl1Item


class spider_1(scrapy.Spider):
    name = "spider_1"

    title_urls = []

    all_urls = []

    def start_requests(self):
        urls = ['http://www.dazui88.com/tag/aiss/']
        for url in urls:
            yield scrapy.Request(url, self.get_title_urls)

    def parse(self, response):
        for a in response.xpath('//div/p/img'):
            item = Crawl1Item()
            next_url = a.xpath('@src').extract()
            urls = []
            for url in next_url:
                urls.append(url.replace(' ', ''))
            self.logger.info(urls)
            item['image_urls'] = urls
            item['images'] = a.xpath('@src').re(r'[^/]*.[jpg|png|gif]$')
            yield item
        next_page = response.xpath('//div[@id="eFramePic"]/div/ul/li/a/@href').reverse().extract_first()
        yield scrapy.Request(next_page, self.parse)

    def get_title_urls(self, response):
        for a in response.xpath('//body/div/ul/li/a'):
            title_url = response.urljoin(a.xpath('@href').extract_first())
            yield scrapy.Request(title_url, self.get_all_urls)

    def get_all_urls(self, response):
        for a in response.xpath('//body/div/div/div/div/p/a'):
            next_url = response.urljoin(a.xpath('@href').extract_first())
            yield scrapy.Request(next_url, self.parse)
