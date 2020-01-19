from app import db
from app.inc import Dao


class Rank(db.Model, Dao):
    
    __tablename__ = 'rank'
    
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(16), unique=True, nullable=False)
    __xp = db.Column('xp', db.Integer, unique=True, nullable=False)


    def __init__(self, name, xp, id=None):
        self.__id = id
        self.__name = name
        self.__xp = xp

    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'xp': self.xp,
        }


    @property
    def id(self):
        return self.__id

    
    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def name(self):
        return self.__name

    
    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def xp(self):
        return self.__xp

    
    @xp.setter
    def xp(self, xp):
        self.__xp = xp
