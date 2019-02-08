from app import db


class CharacterSkill(db.Model):
    
    __tablename__ = 'character_skill'
    
    id = db.Column(db.Integer, primary_key = True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))


    def __init__(self, id, character_id, skill_id):
        self.id = id
        self.character_id = character_id
        self.skill_id = skill_id

