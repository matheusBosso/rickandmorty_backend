from flask import Blueprint
from src.controllers.episodes_controllers import EpisodesController

episodes_bp = Blueprint('episodes_bp', __name__)
episodes_controller = EpisodesController()

@episodes_bp.route('/episodes', methods=['GET'])
def get_episodes():
    return episodes_controller.get_episodes()