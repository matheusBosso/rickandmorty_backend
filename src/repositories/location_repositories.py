from src.models import db
from src.models.location_model import Location

class LocationRepository:
    def get_locations(self):
        try:
            return Location.query.all()
        except Exception:
            db.session.rollback()
            raise