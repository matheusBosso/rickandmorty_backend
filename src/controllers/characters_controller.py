from flask import jsonify
from src.services.characters_services import CharactersService
from src.utils.api_response import ApiResponse
from werkzeug.exceptions import NotFound

class CharactersController:

    def __init__(self):
        self.characters_service = CharactersService()
    
    def get_characters(self, page, name):
        try:

            data = self.characters_service.get_characters(page, name)

            return ApiResponse.send(success=True, message='Characters fetched successfully.', data=data, status_code=200)
        except Exception:
            return ApiResponse.send(success=False, message='Failed to fetch characters.', data=None, status_code=500)
        
    def get_character_by_id(self, character_id):
        try:
                character = self.characters_service.get_character_by_id(character_id) # Fetch character by ID

                return ApiResponse.send(success=True, message='Character fetched successfully.', data=character, status_code=200)
        except NotFound:
            return ApiResponse.send(success=False, message='Character not found.', data=None, status_code=404)

        except Exception as e:
            return ApiResponse.send(success=False, message='Failed to fetch character.', data=None, status_code=500)