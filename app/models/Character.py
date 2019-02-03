from app import db


class Character(db.Model):
    
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    

    def __init__(self, name, skills, edges, hindrances):
        self.name = name
        self.skills = skills
        self.edges = edges
        self.hindrances = hindrances
