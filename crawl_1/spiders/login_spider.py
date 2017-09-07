import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login_spider'

    def start_requests(self):
        yield scrapy.Request('http://eamtest.midea.com:9080/sit/commonAction.do', self.after_login,'POST',
                             body='funid=login&eventcode=login&pagetype=login&user_code=dongci&user_pass=@midea2014@',
                             headers={'Content-Type':'application/x-www-form-urlencoded'})

    def parse(self, response):
        print(response.body)

    def after_login(self,response):
        print(response.body)
        yield scrapy.Request('http://eamtest.midea.com:9080/sit/commonAction.do?eventcode=query_data&funid=queryevent&pagetype=editgrid&query_funid=sys_user&user_id=IU11199837',self.parse,'POST',
                             headers={'Content-Type':'application/x-www-form-urlencoded'},
                             body='start=0&limit=50')
