from flask import jsonify
from src.services.characters_services import CharactersService

class CharactersController:

    def __init__(self):
        self.characters_service = CharactersService()
    
    def get_characters(self):
        try:
            data = self.characters_service.get_characters()
            return jsonify({
                'data': [
                    {
                        'id': character.id,
                        'name': character.name,
                        'status': character.status,
                        'species': character.species,
                        'type': character.type,
                    }
                    for character in data
                ]
            })
        except Exception:
            return jsonify({
                'error': 'An error occurred while fetching characters.'
            }), 500