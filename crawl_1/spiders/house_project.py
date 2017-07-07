import scrapy
from scrapy.selector import Selector
from crawl_1.db.DomainObject import HouseProject, CellInfo, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re


class HouseProjectSpider(scrapy.Spider):

    name = 'house_project'
    url_template = 'o=getJSON&p=%s&template_type=lpxs_ys_lpld_list'
    url = 'http://house.shunde.gov.cn/servlet/list'
    base_url = 'http://house.shunde.gov.cn/'
    engine = create_engine('mysql://scrapy:scrapy@localhost:3310/scrapy?charset=utf8', encoding='utf-8')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    def start_requests(self):
        body = self.url_template % 1
        yield scrapy.Request(self.url,self.parse,'POST',body=body,headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def parse(self,response):
        page = eval(response.body)['page']
        totalPage = eval(response.body)['totalPage']
        html = eval(response.body)['html']
        html = re.sub('\\\\','',html)
        selector = Selector(text=html)

        for row in selector.xpath('//table/tbody/tr'):
            data = row.xpath('.//td/text()').extract()
            project = HouseProject(presale_licence=data[0],project_name=row.xpath('.//td/a/text()').extract()[0],
                                   company_name=row.xpath('.//td/a/text()').extract()[1], house_num=data[1],
                                   land_area=data[2],building_area=data[3],presale_date=data[4],presale_end_date=data[5])
            self.session.add(project)
            self.session.commit()

            for cells in row.xpath('.//td/a'):
                if(cells.xpath('@href').extract_first().startswith('dy_list.jsp')):
                    request = scrapy.Request(self.base_url+cells.xpath('@href').extract_first(),
                                                   self.cellsParse,'GET',headers={'Content-Type':'application/x-www-form-urlencoded'})
                    request.meta['project_id'] = project.id
                    yield request

        body = self.url_template % str(page+1)
        if(page<totalPage):
            yield scrapy.Request(self.url,self.parse,'POST',body=body,headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def cellsParse(self,response):
        for cellLink in response.xpath('//table[contains(@class,"table_dy_info")]/tr/td/a'):
            request = scrapy.Request(self.base_url+cellLink.xpath('@href').extract_first(),self.cellParse,
                                 'GET',headers={'Content-Type':'application/x-www-form-urlencoded'})
            request.meta['project_id'] = response.meta['project_id']
            yield request

    def cellParse(self,response):
        project_id = response.meta['project_id']
        trs = response.xpath('//body/table/tr/td/table/tbody/tr')
        no = trs[0].xpath('./td/text()').extract()[1]
        name = trs[0].xpath('./td/text()').extract()[3]
        address = trs[1].xpath('./td/text()').extract()[1]
        town_name = trs[1].xpath('./td/text()').extract()[3]
        useage = trs[2].xpath('./td/text()').extract()[1]
        structure = trs[2].xpath('./td/text()').extract()[3]
        building_area = trs[3].xpath('./td/text()').extract()[1]
        share_area = trs[3].xpath('./td/text()').extract()[3]
        build_base_area = trs[4].xpath('./td/text()').extract()[1]
        inner_area = trs[4].xpath('./td/text()').extract()[3]
        land_share_area = trs[5].xpath('./td/text()').extract()[1]
        status = trs[5].xpath('./td/table/tbody/tr/td/text()').extract()[0]
        price = trs[6].xpath('./td/div/text()').extract_first()
        cellInfo = CellInfo(project_id=project_id,no=no,name=name,address=address,town_name=town_name,
                            useage=useage,structure=structure,building_area=build_base_area,share_area=share_area,
                            build_base_area=build_base_area,inner_area=inner_area,land_share_area=land_share_area,
                            status=status,price=price)
        self.session.add(cellInfo)
        self.session.commit()




