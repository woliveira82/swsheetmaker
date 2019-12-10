from flask.views import MethodView
from app.models import Scenario
from flask import jsonify
from flask_restful import reqparse
from app.inc import Response
from exception import ResponseException

class ScenariosView(MethodView):


    def get(self, scenario_id=None):
        if not scenario_id:
            response = Scenario.read_all()
            return Response(response).to_dict()
        
        scenario = Scenario.read(scenario_id)
        return Response(scenario).to_dict()


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        scenario = Scenario(data['name'], data['description'])
        result = scenario.create()

        return Response(result, 201).to_dict()


    def put(self, scenario_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json')
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        none_values = [k for k, v in data.items() if not v]
        [data.pop(key) for key in none_values]

        if len(data) == 0:
            raise ResponseException('', 400, 'No valid parameters sent')

        data.update({'id': scenario_id})
        scenario = Scenario(data['name'], data['description'], data['id'])
        result = scenario.update()
        return Response(result, 200, 'Successfuly updated').to_dict()


    def delete(self, scenario_id):
        result = Scenario.delete(scenario_id)
        return Response(result, 200, 'Successfuly deleted').to_dict()