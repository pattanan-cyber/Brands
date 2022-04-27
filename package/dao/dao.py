from abc import ABC
from sqlalchemy.orm.session import Session


class Dao(ABC):
    def __init__(self, session: Session):
        self.__session = session

    @property
    def session(self):
        return self.__session