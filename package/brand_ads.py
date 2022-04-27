from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from package.dao.adsDao import AdsDao
from package.dao.brandDao import BrandDao


class Brands:

    def __init__(self, url = "sqlite:///package.db"):
        engine = create_engine(url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()

    def brand(self):
        return BrandDao(self.__db_session)

    def ads(self):
        return AdsDao(self.__db_session)