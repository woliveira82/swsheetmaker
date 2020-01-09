from app import app
from app.controllers.ScenariosView import ScenariosView
from app.controllers.CharactersView import CharactersView

view_scenarios = ScenariosView.as_view('scenarios')
app.add_url_rule('/scenarios', view_func=view_scenarios, methods=['GET', 'POST'])
app.add_url_rule('/scenarios/<int:scenario_id>', view_func=view_scenarios, methods=['GET', 'PUT', 'DELETE'])
view_characters = CharactersView.as_view('characters')
app.add_url_rule('/characters', view_func=view_characters, methods=['GET', 'POST'])
app.add_url_rule('/characters/<int:character_id>', view_func=view_characters, methods=['GET', 'PUT', 'DELETE'])

