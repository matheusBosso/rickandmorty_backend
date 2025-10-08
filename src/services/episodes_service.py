from src.repositories.episodes_repositories import EpisodesRepository

class EpisodesService:
    def __init__(self):
        self.episodes_repository = EpisodesRepository()
    
    def get_episodes(self):
        return self.episodes_repository.get_episodes()