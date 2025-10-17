from src.models.characters_model import Character

class CharactersRepository:
    def get_characters_by_name(self, name: str, limit: int, offset: int):
            characters_query = Character.query.filter(Character.name.ilike(f'%{name}%'))

            characters = characters_query.limit(limit).offset(offset).all()
            characters_count = characters_query.count()
            

            
            return characters, characters_count
        