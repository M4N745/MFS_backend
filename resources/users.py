from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
from wtforms import Form, StringField, PasswordField, validators
from flask import request
from werkzeug.datastructures import MultiDict
from db import db
from models import UserModel

blp = Blueprint('Users', 'users')

class NewUserForm(Form):
  username = StringField('username', [
    validators.InputRequired(),
    validators.Length(min=3, max=25)
  ])
  password = PasswordField('password', [
    validators.InputRequired(),
    validators.Length(min=8, max=50)
  ])
  repeat_password = PasswordField('repeat_password',[
    validators.InputRequired(),
    validators.EqualTo('password')
  ])

@blp.route('/users')
class Users(MethodView):
  def post(self):
    form_data = MultiDict(request.json)
    form = NewUserForm(formdata=form_data)
    if form.validate():
      if UserModel.query.filter(UserModel.username == form_data["username"]).first():
        return {"username": ["username already in use"]}, 422
  
      user = UserModel(
        username=form_data["username"],
        password=pbkdf2_sha256.hash(form_data["password"])
      )
  
      db.session.add(user)
      db.session.commit()
      return UserModel.get_json(user), 201
    else:
      errors = form.errors
      return errors, 422


@blp.route('/users/auth')
class Login(MethodView):
  def post(self):
    user_data = request.json
    user = UserModel.query.filter(UserModel.username == user_data["username"]).first()

    if user and pbkdf2_sha256.verify(user_data["password"], user.password):
      access_token = create_access_token(identity=user.id, fresh=True)
      
      return { "token": access_token }, 200
    return {"message": "Bad credentials."}, 422
  
  @jwt_required()
  def get(self):
    current_user = UserModel.query.get_or_404(get_jwt_identity())
    return UserModel.get_json(current_user), 200