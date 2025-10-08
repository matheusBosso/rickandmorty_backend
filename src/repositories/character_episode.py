from src.models import db
from src.models.character_episode_model import CharacterEpisode

class CharacterEpisodeRepository:
    def get_all(self):
        try:
            return CharacterEpisode.query.all()
        except Exception:
            db.session.rollback()
            raise