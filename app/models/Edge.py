from app import db
from app.inc import Dao


class Edge(db.Model, Dao):

    __tablename__ = 'edge'

    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(120), unique=True, nullable=False)
    __description = db.Column('description', db.Text())
    __rank = db.Column('rank', db.Integer, db.ForeignKey('scenario.id'), nullable=False)
    # __requirements = db.Column('requirements')


    def __init__(self, name, improved):
        self.id = id
        self.name = name
        self.improved = improved


    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'improved': self.description,
            'rank': self.rank,
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


    @property
    def rank(self):
        return self.__rank


    @rank.setter
    def rank(self, rank):
        self.__rank = rank
