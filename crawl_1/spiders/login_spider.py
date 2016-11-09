# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
import logging


class LoginSpiderSpider(scrapy.Spider):

    name = "login_spider"
    allowed_domains = ["10.214.124.53:8090"]
    start_urls = (
        'http://10.214.124.53:8090/login.action?logout=true'
    )

    def parse(self, response):
        yield FormRequest.from_response(response, formdata={'os_username':'xuxiaobin5','os_password':'xuxiaobin5'},callback=self.after_login)

    @staticmethod
    def after_login(response):
        print response.body

