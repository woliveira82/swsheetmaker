from app import db


class Scenario(db.Model):
    
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    description = db.Column(db.Text)


    def __init__(self, name, description):
        
        self.name = name
        self.description = description