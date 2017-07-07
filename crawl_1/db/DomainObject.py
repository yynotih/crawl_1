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
        self.presale_licence = fields['presale_licence']
        self.company_name = fields['company_name']
        self.house_num = fields['house_num']
        self.land_area = fields['land_area']
        self.building_area = fields['building_area']
        self.presale_date = fields['presale_date']
        self.presale_end_date = fields['presale_end_date']
        self.add_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.modify_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

class CellInfo(Base):
    __tablename__='cell_info'

    id = Column(Integer, primary_key=True)
    no = Column(String)
    name = Column(String)
    address = Column(String)
    town_name = Column(String)
    useage = Column(String)
    structure = Column(String)
    building_area = Column(String)
    share_area = Column(String)
    build_base_area = Column(String)
    inner_area = Column(String)
    land_share_area = Column(String)
    status = Column(String)
    price = Column(String)
    add_date = Column(Date)
    modify_date = Column(Date)
    project_id = Column(Integer)

    def __init__(self,**fields):
        self.no = fields['no']
        self.name = fields['name']
        self.address = fields['address']
        self.town_name = fields['town_name']
        self.useage = fields['useage']
        self.structure = fields['structure']
        self.building_area = fields['building_area']
        self.share_area = fields['share_area']
        self.build_base_area = fields['build_base_area']
        self.inner_area = fields['inner_area']
        self.land_share_area = fields['land_share_area']
        self.status = fields['status']
        self.price = fields['price']
        self.add_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.modify_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.project_id = fields['project_id']
