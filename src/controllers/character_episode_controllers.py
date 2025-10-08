from flask import jsonify
from src.services.character_episode_service import CharacterEpisodeService

class CharacterEpisodeController:
    def __init__(self, db_session):
        self.character_episode_service = CharacterEpisodeService(db_session)
    
    def add_character_episode(self, character_id, episode_id):
        try:
            data = self.character_episode_service.add_character_episode(character_id, episode_id)
            return jsonify(data)
        except Exception:
            return jsonify({
                'error': 'An error occurred while adding character episode.'
            }), 500

    def get_episodes_by_character(self, character_id):
        try:
            data = self.character_episode_service.get_episodes_by_character(character_id)
            return jsonify(data)
        except Exception:
            return jsonify({
                'error': 'An error occurred while fetching episodes for the character.'
            }), 500