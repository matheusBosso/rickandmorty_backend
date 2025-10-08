from src.repositories.location_repositories import LocationRepository

class LocationServices:
    def __init__(self):
        self.location_repository = LocationRepository()
    
    def get_locations(self):
        return self.location_repository.get_locations()