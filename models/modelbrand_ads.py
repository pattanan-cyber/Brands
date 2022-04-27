from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Brand(Base):
    __tablename__ = "brands"

    brand = Column(String(20), primary_key=True)
    value = Column(Integer)
    change = Column(Integer)
    category = Column(String(20))
    Rank_change = Column(Integer)
    origin = Column(String(20))


    def __repr__(self):
        return f"{self.name} has {self.value} Brand value, change in 2020 about " \
               f"{self.change}. The category is {self.category}, Rank change is {self.Rank_change} " \
               f"and it come from {self.origin}."


class Ads(Base):
    __tablename__ = 'ads'
    brand = Column(String(20), primary_key=True)
    year = Column(Integer)
    url = Column(String(255))
    youtube_url = Column(String(255))
    funny = Column(String(10))
    show_product_quickly = Column(String(10))
    patriotic = Column(String(10))
    celebrity = Column(String(10))
    danger = Column(String(10))
    animals = Column(String(10))
    use_sex = Column(String(10))


    def __repr__(self):
        return f"{self.name} produce ads in {self.year}, url is {self.url}." \
               f"and youtube url is {self.youtube_url}." \
               f"This ads funny = {self.danger}," \
               f"This ads show product quickly = {self.danger}," \
               f"This ads patriotic = {self.danger}," \
               f"This ads has celebrity = {self.danger}," \
               f"This ads has danger = {self.danger}," \
               f"This ads has animals = {self.danger}," \
               f"This ads use sex = {self.danger}."
