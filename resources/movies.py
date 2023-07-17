from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint
from sqlalchemy import desc, asc

from db import db
from models import MoviesModel, CoversModel

blp = Blueprint('Movies', 'movies')

@blp.route('/movies')
class MoviesList(MethodView):
    @blp.paginate()
    def get(self, pagination_parameters):
        query = MoviesModel.query
        sort = request.args.get('sort')
        search_query = request.args.get('search')

        if search_query:
            query = query.filter(MoviesModel.title.ilike(f"%{search_query}%"))

    
        if sort != None and sort.startswith('-'):
            sort_column = sort[1:]
            sort_order = desc
        else:
            sort_column = 'title' if sort == None else sort
            sort_order = asc

        column = getattr(MoviesModel, sort_column)
        items = query.order_by(sort_order(column)).all()

        return {
            "items": [item.get_json() for item in items],
            "sort": 'desc' if sort == None or sort.startswith('-') else 'asc',
            "search": search_query,
        }, 200
        

@blp.route('/movies/<int:movie_id>')
class SpecificMovie(MethodView):
    def get(self, movie_id):
        get_movie = MoviesModel.query.get_or_404(movie_id)
        return MoviesModel.get_json(get_movie), 200