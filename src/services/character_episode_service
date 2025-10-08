from src.models import CharacterEpisode

class CharacterEpisodeService:

    def __init__(self, db_session):
        self.db_session = db_session

    def add_character_episode(self, character_id, episode_id):
        character_episode = CharacterEpisode(character_id=character_id, episode_id=episode_id)
        self.db_session.add(character_episode)
        self.db_session.commit()
        return character_episode

    def get_episodes_by_character(self, character_id):
        return self.db_session.query(CharacterEpisode).filter_by(character_id=character_id).all()