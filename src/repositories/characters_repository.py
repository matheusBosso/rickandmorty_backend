from src.models import db
from src.models.characters_model import Character

class CharactersRepository:
    def get_characters(self):
        try:
            return Character.query.all()
        except Exception:
            db.session.rollback()
            raise