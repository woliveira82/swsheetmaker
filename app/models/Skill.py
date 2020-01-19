from app import db


class Skill(db.Model):
    
    __tablename__ = 'skill'
    
    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(32), unique=True, nullable=False)
    __attribute = db.Column('attribute', db.String(8), nullable=False)
    __description = db.Column('description', db.Text)


    def __init__(self, name, attribute, description=None):
        self.__id = id
        self.__name = name
        self.__attribute = attribute
        self.__description = description


    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'attribute': self.attribute,
            'description': self.description,
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
    def attribute(self):
        return self.__attribute


    @attribute.setter
    def attribute(self, attribute):
        self.__attribute = attribute


    @property
    def description(self):
        return self.__description


    @description.setter
    def description(self, description):
        self.__description = description


