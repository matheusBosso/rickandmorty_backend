from flask import jsonify, request
from src.services.characters_services import CharactersService

class CharactersController:

    def __init__(self):
        self.characters_service = CharactersService()
    
    def get_characters(self):
        try:
            name = request.args.get('name', '')
            page = int(request.args.get('page', 1))

            data = self.characters_service.get_characters(name, page)

            characters = data.get('results', [])

            return jsonify({
                'page': data.get('page', 1),
                'per_page': data.get('per_page', 20),
                'total': data.get('total', len(characters)),
                'data': [
                    {
                        'id': character.id,
                        'name': character.name,
                        'status': character.status,
                        'species': character.species,
                        'type': character.type,
                    }
                    for character in characters
                ]
            })
        except Exception:
            return jsonify({
                'error': 'An error occurred while fetching characters.'
            }), 500