from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
import time


Base = declarative_base()


class DailyTrade(Base):
    __tablename__ = 'real_estate_daily_trade'
    id = Column(Integer, primary_key=True)
    town_name = Column(String(63))
    trade_num = Column(Integer)
    trade_area = Column(Float)
    amounts = Column(Float)
    add_date = Column(Date)
    modify_date = Column(Date)

    def __init__(self, townName, tradeNum, tradeArea, amounts):
        self.town_name = townName
        self.trade_num = tradeNum
        self.trade_area = tradeArea
        self.amounts = amounts
        self.add_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.modify_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class HouseProject(Base):
    __tablename__ = 'house_project'

    id = Column(Integer,primary_key=True)
    project_name = Column(String)
    avg_price = Column(Float)
    presale_licence = Column(String)
    company_name = Column(String)
    house_num = Column(Integer)
    land_area = Column(Float)
    building_area = Column(Float)
    presale_date = Column(String)
    presale_end_date = Column(String)
    add_date = Column(Date)
    modify_date = Column(Date)

    def __init__(self,**fields):
        self.project_name = fields['project_name']
        self.avg_price = fields['avg_price']
        self.presale_licence = fields['presale_licence']
        self.company_name = fields['company_name']
        self.house_num = fields['house_num']
        self.land_area = fields['land_area']
        self.building_area = fields['building_area']
        self.presale_date = fields['presale_date']
        self.presale_end_date = fields['presale_end_date']
        self.add_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.modify_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
