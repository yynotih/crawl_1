import scrapy
from scrapy.selector import Selector
from crawl_1.db.DomainObject import HouseProject, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re


class HouseProjectSpider(scrapy.Spider):

    name = 'house_project'
    url_template = 'o=getJSON&p=%s&template_type=lpxs_ys_lpld_list'
    url = 'http://house.shunde.gov.cn/servlet/list'
    def start_requests(self):
        body = self.url_template % 1
        yield scrapy.Request(self.url,self.parse,'POST',body=body,headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def parse(self,response):
        engine = create_engine('mysql://scrapy:scrapy@localhost:3310/scrapy?charset=utf8', encoding='utf-8')
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        page = eval(response.body)['page']
        totalPage = eval(response.body)['totalPage']
        html = eval(response.body)['html']
        html = re.sub('\\\\','',html)
        selector = Selector(text=html)
        for row in selector.xpath('//table/tbody/tr'):
            data = row.xpath('.//td/text()').extract()
            project = HouseProject(presale_licence=data[0],project_name=row.xpath('.//td/a/text()').extract()[0],
                                   company_name=row.xpath('.//td/a/text()').extract()[1], house_num=data[1],
                                   land_area=data[2],building_area=data[3],presale_date=data[4],presale_end_date=data[5],avg_price=0)
            session.add(project)
        session.commit()
        body = self.url_template % str(page+1)
        if(page<totalPage):
            yield scrapy.Request(self.url,self.parse,'POST',body=body,headers={'Content-Type': 'application/x-www-form-urlencoded'})
