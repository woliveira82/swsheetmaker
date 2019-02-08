from app import db


class CharacterHindrance(db.Model):
    
    __tablename__ = 'character_hindrance'
    
    id = db.Column(db.Integer, primary_key = True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    hindrance_id = db.Column(db.Integer, db.ForeignKey('hindrance.id'))


    def __init__(self, id, character_id, hindrance_id):
        self.id = id
        self.character_id = character_id
        self.hindrance_id = hindrance_id

