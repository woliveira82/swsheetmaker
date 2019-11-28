from flask.views import MethodView
from app.models import Scenario
from flask import jsonify
from flask_restful import reqparse


class ScenariosView(MethodView):


    def get(self, scenario_id=None):
        response = Scenario.read({'id': scenario_id}) if scenario_id else Scenario.read()
        if response['status'] != 200:
            return [], response['status']

        scenario_list = response['response']
        http_response = {'data': [scenario.as_dict() for scenario in scenario_list]}

        return http_response, response['status']


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('description', location='json')
        data = parser.parse_args()

        scenario = Scenario(data['name'], data['description'])
        result = scenario.create()

        return result['response'][0], result['status']
