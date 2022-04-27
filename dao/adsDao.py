import movie.model as model
from movie.persistence.dao import Dao
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import sessionmaker


class AdsDao(Dao):