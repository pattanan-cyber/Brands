from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Brands(Base):
    __tablename__ = "brands"

    name = Column(String(20), primary_key=True)
    value = Column(Integer)
    change = Column(Integer)
    origin = Column(String(20))


    def __repr__(self):
        return f"{self.name} has {self.value} Brand value, change in 2020 about {self.change} and it come from {self.origin}"


class Ads(Base):
    __tablename__ = 'movie'
    name = Column(String(20), ForeignKey('IMDB.name'))
    year = Column(Integer)
    danger = Column(String(10))
    url = Column(String(255))

    def __repr__(self):
        return f"{self.name} produce ads in {self.year}, url is {self.url}.This ads has danger = {self.danger}"
