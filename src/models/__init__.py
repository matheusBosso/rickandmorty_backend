from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from src.models.characters_model import Character  # Importing the Character model to ensure it's registered with SQLAlchemy
from src.models.location_model import Location  # Importing the Location model to ensure it's registered with SQLAlchemy
from src.models.episodes_model import Episode  # Importing the Episode model to ensure it's registered with SQLAlchemy
from src.models.character_episode_model import CharacterEpisode  # Importing the CharacterEpisode model to ensure it's registered with SQLAlchemy