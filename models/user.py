from enum import unique
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def get_json(self):
      return {
         "id": self.id,
         "username": self.username,
      }