from typing import List, Any
from sqlalchemy.orm.query import Query
from package.dao.dao import Dao
from models.modelbrand_ads import Brand, Ads


class AdsDao(Dao):

    def get_brand(self, brand):
        return self.session.query(Ads).filter(Ads.brand == brand)