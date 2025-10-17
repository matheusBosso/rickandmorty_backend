from flask import jsonify
from src.services.characters_services import CharactersService

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