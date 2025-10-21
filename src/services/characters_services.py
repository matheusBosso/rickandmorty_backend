from src.repositories.characters_repository import CharactersRepository  # Add this import
import math

class CharactersService: 

    def __init__(self):
        self.characters_repository = CharactersRepository()  # Initialize the repository
    
    def get_characters(self, page: int, name: str):

        limit = 20  # Number of items per page
        offset = (page - 1) * limit  # Calculate offset

        all_characters, characters_count = self.characters_repository.get_characters_by_name(name, limit, offset)  # Fetch all matching characters

        page_count = math.ceil(characters_count / limit)  # Calculate total number of pages

        return {
            "page": page,
            "per_page": limit,
            "page_count": page_count,
            "results": all_characters
        }
    
    def get_character_by_id(self, character_id: int):
        character = self.characters_repository.get_character_by_id(character_id)
        if not character:
            return None
        return character