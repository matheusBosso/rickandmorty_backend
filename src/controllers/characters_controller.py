from flask import jsonify
from src.services.characters_services import CharactersService
from src.models.characters_model import character_output_schema, character_output_schema_get_all

class CharactersController:

    def __init__(self):
        self.characters_service = CharactersService()
    
    def get_characters(self, page, name):
        try:

            data = self.characters_service.get_characters(page, name)

            characters = data.get('results', [])

            return jsonify({
                'page': data.get('page', 1),
                'per_page': data.get('per_page', 20),
                'page_count': data.get('page_count', 0),
                'data': [
                    {
                        'id': character.id,
                        'name': character.name,
                        'status': character.status,
                        'species': character.species,
                        'type': character.type,
                    }
                    for character in data.get('results', [])
                ]
            })
        except Exception:
            return jsonify({
                'error': 'An error occurred while fetching characters.'
            }), 500
        
    def get_character_by_id(self, character_id):
        try:
                character = self.characters_service.get_character_by_id(character_id) # Fetch character by ID
                if not character:
                    return jsonify({
                    'error': 'Character not found.'
                }), 404

                character_data = character_output_schema_get_all.dump(character)
                
                return jsonify({
                    'data': character_data
                })
    
        except Exception as e:
            import traceback
            print("❌ ERRO NO CONTROLLER ❌")
            print(traceback.format_exc())
            return jsonify({
                'error': str(e)
            }), 500