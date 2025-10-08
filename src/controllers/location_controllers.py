from flask import jsonify
from src.services.location_services import LocationServices

class LocationController:

    def __init__(self):
        self.location_services = LocationServices()
    
    def get_locations(self):
        try:
            data = self.location_services.get_locations()
            return jsonify(data)
        except Exception:
            return jsonify({
                'error': 'An error occurred while fetching locations.'
            }), 500