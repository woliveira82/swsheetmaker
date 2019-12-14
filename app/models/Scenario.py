from app import db
from app.inc import Dao


class Scenario(db.Model, Dao):
    
    __tablename__ = 'scenario'

    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(120), nullable=False)
    __description = db.Column('description', db.Text)


    def __init__(self, name, description=None, id=None):
        self.__id = id
        self.__name = name
        self.__description = description
     
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
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
    def description(self):
        return self.__description


    @description.setter
    def description(self, description):
        self.__description = description
