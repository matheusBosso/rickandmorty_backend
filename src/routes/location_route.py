from flask import Blueprint
from src.controllers.location_controllers import LocationController

location_bp = Blueprint('location_bp', __name__)
location_controller = LocationController()

# Define the route for getting locations
@location_bp.route('/', methods=['GET'])
def get_locations():
    return location_controller.get_locations()