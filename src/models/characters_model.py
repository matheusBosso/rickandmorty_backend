from src.models import db, ma

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(10), nullable=False)

    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)


    #linkando as tabelas
    origin = db.relationship('Location', foreign_keys=[origin_id], back_populates='origin_characters', uselist=False, lazy=True)
    location = db.relationship('Location', foreign_keys=[location_id], back_populates='residing_characters', uselist=False, lazy=True)

    # relacao N para N
    episodes = db.relationship('Episode', secondary='character_episode', back_populates='characters', lazy=True)

    def __repr__(self):
        return f"<Character {self.name}>"
    
    @property
    def last_episode(self):
        if not self.episodes:
            return None
        return max(self.episodes, key=lambda ep: ep.id)
    
#----------------------------Schemas----------------------------#

class CharacterSchema(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    image = ma.String()
    species = ma.String()

class CharacterSchemaGetAll(CharacterSchema):
    type = ma.String()
    gender = ma.String()
    location = ma.Nested("LocationSchema")
    last_episode = ma.Nested("EpisodeSchema", attribute="last_episode")
    origin = ma.String()

character_output_schema = CharacterSchema()   

character_output_schema_get_all = CharacterSchemaGetAll()