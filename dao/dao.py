from utils.dao.dao import Dao
from model.artist import ArtistsModel
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import sessionmaker

class DaoBrands(Dao):
    """Dao for artist's model."""

    def __init__(self, session: Session) -> None:
        self.__session = session

    @property
    def session(self):
        return self.__session

