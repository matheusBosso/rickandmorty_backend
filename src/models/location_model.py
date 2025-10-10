from src.models import db

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    dimension = db.Column(db.String(50), nullable=False)


    #linkando as tabelas
    origin_characters = db.relationship('Character', foreign_keys='Character.origin_id', back_populates='origin', uselist=True, lazy=True)
    residing_characters = db.relationship('Character', foreign_keys='Character.location_id', back_populates='location', uselist=True, lazy=True)

    def __repr__(self):
        return f"<Location {self.name}>"