from flask import Blueprint, request
from src.controllers.characters_controller import CharactersController

characters_bp = Blueprint('characters_bp', __name__)
characters_controller = CharactersController()

@characters_bp.route('/', methods=['GET'])
def get_characters():
   page = request.args.get('page', default=1, type=int)
   name = request.args.get('name', default=None, type=str)
   return characters_controller.get_characters(page, name)