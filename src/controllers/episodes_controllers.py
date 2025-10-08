from flask import jsonify
from src.services.episodes_service import EpisodesService

class EpisodesController:

    def __init__(self):
        self.episodes_service = EpisodesService()
    
    def get_episodes(self):
        try:
            data = self.episodes_service.get_episodes()
            return jsonify(data)
        except Exception:
            return jsonify({
                'error': 'An error occurred while fetching episodes.'
            }), 500