from app import app
from app.controllers.ScenariosView import ScenariosView

view_scenarios = ScenariosView.as_view('scenarios')
app.add_url_rule('/scenarios', view_func=view_scenarios, methods=['GET', 'POST'])
app.add_url_rule('/scenarios/<int:scenario_id>', view_func=view_scenarios, methods=['GET', 'PUT', 'DELETE'])

