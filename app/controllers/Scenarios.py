from flask.views import MethodView
from app.models import Scenario


class Scenarios(MethodView):


    def get(self, scenarios_id=None):
        return 'ok'
        

