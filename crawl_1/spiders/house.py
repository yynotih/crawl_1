# -*- coding:utf-8 -*-

import scrapy
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crawl_1.db.DomainObject import DailyTrade, Base



class HouseSpider(scrapy.Spider):
    name = 'house_spider'

    def start_requests(self):
        url = 'http://house.shunde.gov.cn/servlet/list'
        yield scrapy.Request(url, self.parse, 'POST', body='o=getJSON&p=1&template_type=jrcjbb', headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def parse(self, response):
        engine = create_engine('mysql://scrapy:scrapy@localhost:3310/scrapy?charset=utf8', encoding='utf-8')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        html = eval(response.body)['html']
        result = scrapy.selector.Selector(text=re.sub('\\\\', '', html))
        for row in result.xpath("//table/tbody/tr"):
            datas = row.xpath(".//td/text()").extract()
            townName = re.sub('[\\\\n\\\\t]', '', row.xpath(".//td/a/text()").extract_first())
            if(len(datas) == 3):
                tradeNum = re.sub('[\\\\n\\\\t]', '', datas[0])
                tradeArea = re.sub('[\\\\n\\\\t]', '', datas[1])
                amounts = re.sub('[\\\\n\\\\t]', '', datas[2])
                dailyTrade = DailyTrade(townName=townName, tradeNum=tradeNum, tradeArea=tradeArea, amounts=amounts)
                session.add(dailyTrade)
        session.commit()
