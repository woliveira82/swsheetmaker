from app import db
from app.inc import Dao


class Character(db.Model, Dao):
    
    __tablename__ = 'character'

    __id = db.Column('id', db.Integer, primary_key=True)
    __name = db.Column('name', db.String(127), nullable=False)
    __description = db.Column('description', db.String(255))
    __xp = db.Column('xp', db.SmallInteger, nullable=False, default=0)
    __agility = db.Column('agility', db.SmallInteger, nullable=False, default=4)
    __smarts = db.Column('smarts', db.SmallInteger, nullable=False, default=4)
    __spirit = db.Column('spirit', db.SmallInteger, nullable=False, default=4)
    __strength = db.Column('strength', db.SmallInteger, nullable=False, default=4)
    __vigor = db.Column('vigor', db.SmallInteger, nullable=False, default=4)
    __pace = db.Column('pace', db.SmallInteger, nullable=False, default=6)
    __parry = db.Column('parry', db.SmallInteger, nullable=False, default=2)
    __toughness = db.Column('toughness', db.SmallInteger, nullable=False, default=2)
    __charisma = db.Column('charisma', db.SmallInteger, nullable=False, default=0)
    __wounds = db.Column('wounds', db.SmallInteger, nullable=False, default=0)
    __fatigue = db.Column('fatigue', db.SmallInteger, nullable=False, default=0)
    __scenario_id = db.Column('scenario_id', db.Integer, db.ForeignKey('scenario.id'), nullable=False)
    # __skills = db.Column('skills', )
    # __edge = db.Column('edge', )
    # __hindrance = db.Column('hindrance', )
    

    def __init__(self, name, scenario_id, xp=0, agility=4, smarts=4, spirit=4, strength=4, vigor=4, pace=6, parry=2, toughness=2, charisma=0, wounds=0, fatigue=0, description=None, id=None):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__xp = xp
        self.__agility = agility
        self.__smarts = smarts
        self.__spirit = spirit
        self.__strength = strength
        self.__vigor = vigor
        self.__pace = pace
        self.__parry = parry
        self.__toughness = toughness
        self.__charisma = charisma
        self.__wounds = wounds
        self.__fatigue = fatigue
        self.__scenario_id = scenario_id


    def as_dict(self):
        return {
            'id': self.id,
            'scenario_id': self.scenario_id,
            'name': self.name,
            'description': self.description,
            'xp': self.xp,
            'agility': self.agility,
            'smarts': self.smarts,
            'spirit': self.spirit,
            'strength': self.strength,
            'vigor': self.vigor,
            'pace': self.pace,
            'parry': self.parry,
            'toughness': self.toughness,
            'charisma': self.charisma,
            'wounds': self.wounds,
            'fatigue': self.fatigue,
            # 'skills': self.skills,
            # 'edge': self.edge,
            # 'hindrance': self.hindrance,
        }

    
    @property
    def id(self):
        return self.__id


    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def scenario_id(self):
        return self.__scenario_id


    @scenario_id.setter
    def scenario_id(self, scenario_id):
        self.__scenario_id = scenario_id


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
    def vigor(self):
        return self.__vigor


    @vigor.setter
    def vigor(self, vigor):
        self.__vigor = vigor


    @property
    def agility(self):
        return self.__agility


    @agility.setter
    def agility(self, agility):
        self.__agility = agility


    @property
    def smarts(self):
        return self.__smarts


    @smarts.setter
    def smarts(self, smarts):
        self.__smarts = smarts


    @property
    def spirit(self):
        return self.__spirit


    @spirit.setter
    def spirit(self, spirit):
        self.__spirit = spirit


    @property
    def strength(self):
        return self.__strength


    @strength.setter
    def strength(self, strength):
        self.__strength = strength


    @property
    def xp(self):
        return self.__xp


    @xp.setter
    def xp(self, xp):
        self.__xp =xp


    @property
    def pace(self):
        return self.__pace


    @pace.setter
    def pace(self, pace):
        self.__pace = pace


    @property
    def parry(self):
        return self.__parry


    @parry.setter
    def parry(self, parry):
        self.__parry = parry


    @property
    def toughness(self):
        return self.__toughness


    @toughness.setter
    def toughness(self, toughness):
        self.__toughness = toughness


    @property
    def charisma(self):
        return self.__charisma


    @charisma.setter
    def charisma(self, charisma):
        self.__charisma = charisma


    @property
    def wounds(self):
        return self.__wounds


    @wounds.setter
    def wounds(self, wounds):
        self.__wounds = wounds


    @property
    def fatigue(self):
        return self.__fatigue


    @fatigue.setter
    def fatigue(self, fatigue):
        self.__fatigue = fatigue


    # @property
    # def skills(self):
    #     return self.__skills


    # @skills.setter
    # def skills(self, skills):
    #     self.__skills = skills


    # @property
    # def edge(self):
    #     return self.__edge


    # @edge.setter
    # def edge(self, edge):
    #     self.__edge = edge


    # @property
    # def hindrance(self):
    #     return self.__hindrance


    # @hindrance.setter
    # def hindrance(self, hindrance):
    #     self.__hindrance = hindrance
