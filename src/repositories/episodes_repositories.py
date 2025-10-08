from src.models import db
from src.models.episodes_model import Episode

class EpisodesRepository:
    def get_episodes(self):
        try:
            return Episode.query.all()
        except Exception:
            db.session.rollback()
            raise