from src.repositories.characters_repository import CharactersRepository  # Add this import

class CharactersService: 

    def __init__(self):
        self.characters_repository = CharactersRepository()  # Initialize the repository
    
    def get_characters(self):
        return self.characters_repository.get_characters()  # Fetch characters from the repository