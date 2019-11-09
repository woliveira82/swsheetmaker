from app import app
from app.controllers.Scenarios import Scenarios

view_scenarios = Scenarios.as_view('scenarios')
app.add_url_rule('/scenarios', view_func=view_scenarios, methods=['GET'])
# app.add_url_rule('/scenarios/<int:scenario_id>', view_func=view_scenarios, methods=['GET'])
