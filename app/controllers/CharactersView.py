from flask.views import MethodView
from app.models import Character
from flask import jsonify
from flask_restful import reqparse
from app.inc import Response, Functions
from exception import ResponseException


class CharactersView(MethodView):


    def get(self, character_id=None):
        if not character_id:
            character_list = Character.read_all()
            return Response(character_list).to_dict()
        
        character = Character.read(character_id)
        return Response(character).to_dict()


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('scenario_id', location='json', required=False, type=int)
        parser.add_argument('description', location='json', default='')
        parser.add_argument('xp', location='json', default=0, type=int)
        parser.add_argument('agility', location='json', default=2, type=int)
        parser.add_argument('smarts', location='json', default=2, type=int)
        parser.add_argument('spirit', location='json', default=2, type=int)
        parser.add_argument('strength', location='json', default=2, type=int)
        parser.add_argument('vigor', location='json', default=2, type=int)
        parser.add_argument('pace', location='json', default=2, type=int)
        parser.add_argument('parry', location='json', default=2, type=int)
        parser.add_argument('toughness', location='json', default=2, type=int)
        parser.add_argument('charisma', location='json', default=0, type=int)
        parser.add_argument('wounds', location='json', default=0, type=int)
        parser.add_argument('fatigue', location='json', default=0, type=int)
        data = parser.parse_args()

        character = Character(**data)
        print(character.as_dict())
        print('--'*34)
        character.create()
        return Response(character, 201).to_dict()


    def put(self, character_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('scenario_id', location='json', required=True, type=int)
        parser.add_argument('description', location='json', required=True)
        parser.add_argument('xp', location='json', required=True, type=int)
        parser.add_argument('agility', location='json', required=True, type=int)
        parser.add_argument('smarts', location='json', required=True, type=int)
        parser.add_argument('spirit', location='json', required=True, type=int)
        parser.add_argument('strength', location='json', required=True, type=int)
        parser.add_argument('vigor', location='json', required=True, type=int)
        parser.add_argument('pace', location='json', required=True, type=int)
        parser.add_argument('parry', location='json', required=True, type=int)
        parser.add_argument('toughness', location='json', required=True, type=int)
        parser.add_argument('charisma', location='json', required=True, type=int)
        parser.add_argument('wounds', location='json', required=True, type=int)
        parser.add_argument('fatigue', location='json', required=True, type=int)
        data = parser.parse_args()

        data.update({'id': character_id})
        character = Character(**data)
        character.update()
        return Response(character, 200, 'Successfuly updated').to_dict()


    def delete(self, character_id):
        result = Character.delete(character_id)
        return Response(result, 200, 'Successfuly deleted').to_dict()
