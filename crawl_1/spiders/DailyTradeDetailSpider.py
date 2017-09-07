# -*- coding:utf-8 -*-

import scrapy
import re
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crawl_1.db.DomainObject import DailyTradeDetail, Base

class DailyTradeDetailSpider(scrapy.Spider):

    name = 'daily_trade_detail_spider'

    baseUrl = 'http://house.shunde.gov.cn/'
    url = 'http://house.shunde.gov.cn/servlet/list'
    bodyTemplate = 'o=getJSON&p=%(page)s&template_type=lp_search_ys&z_name=%(z_name)s'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    engine = create_engine('mysql://scrapy:scrapy@localhost:3310/scrapy?charset=utf8', encoding='utf-8')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    def start_requests(self):
        yield scrapy.Request(self.url,self.parse,'POST',body = self.bodyTemplate % {'page':'1','z_name':'01'},headers=self.headers)

    def parse(self, response):
        html = eval(response.body)['html']
        currentPage = eval(response.body)['page']
        totalPage = eval(response.body)['totalPage']
        result = scrapy.selector.Selector(text=re.sub('[\\\\\\n\\t]', '', html))
        for project in result.xpath('//table/tbody'):
            links = project.xpath('.//tr/td/a')
            projectName = links[0].xpath('.//text()').extract_first(default='not_found')
            detailUrl = self.baseUrl + links[3].xpath('@href').extract_first()
            request = scrapy.Request(detailUrl,self.tradeDetailParse,'GET')
            request.meta['projectName'] = projectName
            yield request
        if(currentPage<totalPage):
            yield scrapy.Request(self.url,self.parse,'POST',body=self.bodyTemplate % {'page':str(currentPage+1),'z_name':'01'},headers=self.headers)

    def tradeDetailParse(self,response):
        projectName = response.meta['projectName']
        result = scrapy.selector.Selector(text=re.sub('[\\n\\t]','',str(response.body)))
        for table in result.xpath('//table'):
            tr = table.xpath('.//tr')
            if(len(tr)<2):
                continue
            texts = table.xpath('.//tr/td/text()')

            reserveNum = texts[1].root.split('/')[0]
            reserveArea = texts[1].root.split('/')[1]
            reserveMoney = texts[3].root
            reserveHouseNum = texts[5].root.split('/')[0]
            reserveHouseArea = texts[5].root.split('/')[1]
            reserveHouseMoney = texts[7].root


            tradeNum = texts[9].root.split('/')[0]
            tradeArea = texts[9].root.split('/')[1]
            tradeMoney = texts[11].root
            tradeHouseNum = texts[13].root.split('/')[0]
            tradeHouseArea = texts[13].root.split('/')[1]
            tradeHouseMoney = texts[15].root

            recordNum = texts[17].root.split('/')[0]
            recordArea = texts[17].root.split('/')[1]
            recordMoney = texts[19].root
            recordHouseNum = texts[21].root.split('/')[0]
            recordHouseArea = texts[21].root.split('/')[1]
            recordHouseMoney = texts[23].root

            detail = DailyTradeDetail(town_name='大良',reserve_num = reserveNum,reserve_area = reserveArea,reserve_money = reserveMoney,
                                      reserve_house_num = reserveHouseNum,reserve_house_area = reserveHouseArea,reserve_house_money = reserveHouseMoney,
                                      trade_num = tradeNum,trade_area = tradeArea,trade_money = tradeMoney,
                                      trade_house_num = tradeHouseNum,trade_house_area = tradeHouseArea,trade_house_money = tradeHouseMoney,
                                      record_num = recordNum,record_area = recordArea,record_money = recordMoney,
                                      record_house_num = recordHouseNum,record_house_area = recordHouseArea,record_house_money = recordHouseMoney,
                                      project_name = projectName)
            self.session.add(detail)
            self.session.commit()



