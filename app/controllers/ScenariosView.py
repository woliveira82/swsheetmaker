from flask.views import MethodView
from app.models import Scenario
from flask import jsonify
from flask_restful import reqparse


class ScenariosView(MethodView):


    def get(self, scenario_id=None):
        if not scenario_id:
            response = Scenario.read_all()
            scenario_list = response['response']
            return {'data': [scenario.as_dict() for scenario in scenario_list]}, response['status']
        
        response = Scenario.read(scenario_id)
        if response['status'] != 200:
            return {'data': []}, response['status']

        scenario = response['response']
        return {'data': scenario.as_dict()}, response['status']


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        scenario = Scenario(data['name'], data['description'])
        result = scenario.create()

        return result['response'], result['status']


    def put(self, scenario_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json')
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        none_values = [k for k, v in data.items() if not v]
        [data.pop(key) for key in none_values]

        if len(data) == 0:
            return jsonify({'message': 'No valid variables sent'}), 400

        data.update({'id': scenario_id})
        scenario = Scenario(data['name'], data['description'], data['id'])
        result = scenario.update()
        return result['response'], result['status']
