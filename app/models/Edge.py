from app import db

class Edge(db.Model):
    
    __tablename__ = 'edge'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    improved = db.Column(db.String(120))


    def __init__(self, name, improved):
        self.id = id
        self.name = name
        self.improved = improved
        self.requirement

