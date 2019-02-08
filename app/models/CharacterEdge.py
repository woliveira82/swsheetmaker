from app import db


class CharacterEdge(db.Model):
    
    __tablename__ = 'character_edge'
    
    id = db.Column(db.Integer, primary_key = True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    edge_id = db.Column(db.Integer, db.ForeignKey('edge.id'))


    def __init__(self, id, character_id, edge_id):
        self.id = id
        self.character_id = character_id
        self.edge_id = edge_id

