from flask import Blueprint
from src.controllers.characters_controller import CharactersController

characters_bp = Blueprint('characters_bp', __name__)
characters_controller = CharactersController()

@characters_bp.route('/', methods=['GET'])
def get_characters():
   return characters_controller.get_characters()