from app import db

class Hindrance(db.Model):
    
    __tablename__ = 'hindrance'

    id = db.Column(db.Integer, primary_key = True)
    hindrance = db.Column(db.String(120), unique = False)


    def __init__(self, hindrance):
        self.id = id
        self.hindrance = hindrance

        

