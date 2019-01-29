from app import db

class Skill(db.Model):
    
    __tablename__ = 'skill'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    attribute = db.Column(db.String(120))
    description = db.Column(db.Text)


    def __init__(self, name, attribute):
        self.id = id
        self.name = name
        self.attribute = attribute

