from app import db

class EdgeType(db.Model):
    
    __tablename__ = 'edge_type'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    description = db.column(db.Text)


    def __init__(self, name, description):
        self.id = id
        self.name = name
        self.description = description
