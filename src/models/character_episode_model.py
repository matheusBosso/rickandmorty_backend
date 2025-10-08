from src.models import db

class CharacterEpisode(db.Model):
    __tablename__ = 'character_episodes'

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False, primary_key=True)

    def __repr__(self):
        return f"<CharacterEpisode Character ID: {self.character_id}, Episode ID: {self.episode_id}>"