from app import db

class Edge(db.Model, Dao):
    
    __tablename__ = 'edge'
    
    __id = db.Column('id', db.Integer, primary_key = True)
    __name = db.Column('name', db.String(120), unique = True, nullable = False)
    __improved = db.Column('improved', db.String(120))


    def __init__(self, name, improved):
        self.id = id
        self.name = name
        self.improved = improved
        # self.requirement

    
    def as_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'improved': self.improved
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
    def improved(self):
        return self.__improved


    @improved.setter
    def improved(self, improved):
        self.__improved = improved
