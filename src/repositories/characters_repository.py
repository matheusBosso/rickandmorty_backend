import requests
from src.models.characters_model import Character

class CharactersRepository:
    def get_characters_by_name(self, name: str):
        all_characters = []
        page = 1

        while True:
            url = f"https://rickandmortyapi.com/api/character/?name={name}&page={page}"
            response = requests.get(url)

            if response.status_code != 200:
                break

            data = response.json()
            all_characters.extend(data['results'])

            if not data['info']['next']:
                break

            page += 1

        return all_characters