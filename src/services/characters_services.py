from src.repositories.characters_repository import CharactersRepository  # Add this import

class CharactersService: 

    def __init__(self):
        self.characters_repository = CharactersRepository()  # Initialize the repository
    
    def get_characters(self, name: str, page: int, items_per_page: int = 20):
        all_characters = self.characters_repository.get_characters_by_name(name)

        total = len(all_characters) # Total number of characters found
        start = (page - 1) * items_per_page # Calculate start index
        end = start + items_per_page # Calculate end index

        paginated = all_characters[start:end]

        return {
            "page": page,
            "per_page": items_per_page,
            "total": total,
            "results": paginated
        }