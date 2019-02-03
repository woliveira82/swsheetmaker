from app import db


class Rank(db.Model):
    
    __tablename__ = 'rank'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    xp = db.Column(db.Integer, unique = True)


    def __init__(self, name, xp):
        self.id = id
        self.name = name
        self.xp = xp
