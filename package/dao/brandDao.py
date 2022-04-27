from typing import List, Any
from sqlalchemy.orm.query import Query
from package.dao.dao import Dao
from models.modelbrand_ads import Brand, Ads


class BrandDao(Dao):
    def all_brands(self):
        brands = self.session.query(Brand).all()
        return brands


    def name_eqaul(self, brand):
        sol = self.session.query(Brand).filter(Brand.brand == brand).all().pop()
        return sol

