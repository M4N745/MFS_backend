from flask import send_file
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models import CoversModel

blp = Blueprint('Covers', 'covers')

@blp.route('/covers/<int:cover_id>')
class Cover(MethodView):
    def get(self, cover_id):
        cover = CoversModel.query.get_or_404(cover_id)
        return send_file('storage/'+cover.path, mimetype='image/jpeg')