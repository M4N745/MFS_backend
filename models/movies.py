from db import db

class MoviesModel(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    cover_id = db.Column(db.Integer, db.ForeignKey('covers.id'), unique=False, nullable=True)

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "cover_id": self.cover_id
        }