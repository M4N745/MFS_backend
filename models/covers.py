from db import db

class CoversModel(db.Model):
    __tablename__ = 'covers'
    
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(100), nullable=False)