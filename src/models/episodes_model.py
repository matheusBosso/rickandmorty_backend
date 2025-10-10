from src.models import db

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    air_date = db.Column(db.String(50), nullable=False)
    episode = db.Column(db.String(20), nullable=False)

    #relacao N para N
    characters = db.relationship('Character', secondary='character_episodes', back_populates='episodes', lazy=True)

    def __repr__(self):
        return f"<Episode {self.name}>"