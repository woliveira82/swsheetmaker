from flask.views import MethodView
from app.models import Scenario
from flask import jsonify
from flask_restful import reqparse
from app.inc import Response


class ScenariosView(MethodView):


    def get(self, scenario_id=None):
        if not scenario_id:
            response = Scenario.read_all()
            scenario_list = [scenario for scenario in response['response']]
            return Response(scenario_list).status(response['status'])
        
        scenario = Scenario.read(scenario_id)
        return Response(scenario['response']).status(scenario['status'])


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        scenario = Scenario(data['name'], data['description'])
        result = scenario.create()

        return Response(result['response']).status(result['status'])


    def put(self, scenario_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json')
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        none_values = [k for k, v in data.items() if not v]
        [data.pop(key) for key in none_values]

        if len(data) == 0:
            return Response('').status(400, 'No valid variables sent')

        data.update({'id': scenario_id})
        scenario = Scenario(data['name'], data['description'], data['id'])
        result = scenario.update()
        return Response(result['response']).status(result['status'])


    def delete(self, scenario_id):
        result = Scenario.delete(scenario_id)
        return Response(result['response']).status(result['status'], 'Successful deleted')