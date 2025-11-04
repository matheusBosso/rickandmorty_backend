from src.repositories.characters_repository import CharactersRepository  # Add this import
from src.models.characters_model import character_output_schema_get_all, character_output_schema_get_by_id
import math
from werkzeug.exceptions import NotFound

class CharactersService: 

    def __init__(self):
        self.characters_repository = CharactersRepository()  # Initialize the repository
    
    def get_characters(self, page: int, name: str):

        limit = 20  # Number of items per page
        offset = (page - 1) * limit  # Calculate offset

        all_characters, characters_count = self.characters_repository.get_characters_by_name(name, limit, offset)  # Fetch all matching characters

        page_count = math.ceil(characters_count / limit)  # Calculate total number of pages

        data = {
            "page": page,
            "per_page": limit,
            "page_count": page_count,
            "characters": all_characters
        }
        
        response_data = character_output_schema_get_all.dump(data)

        return response_data
    
    def get_character_by_id(self, character_id: int):
        character = self.characters_repository.get_character_by_id(character_id)
        if not character:
            raise NotFound
        character_data = character_output_schema_get_by_id.dump(character)
        return character_data