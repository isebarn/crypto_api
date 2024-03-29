from flask_restx import Namespace, Resource, fields, marshal
import json
from ORM import Operations
from Auth import authenticate
from flask import request
from base64 import b64decode, b64encode
from Mail import send_email

api = Namespace("/users", description="Root path", path="/users")

user_post = api.model('user_post', {
  'name': fields.String,  
  'email': fields.String,  
  'password': fields.String, 
  'developer': fields.Boolean
})

@api.route("/", endpoint='users root path')
class UsersClass(Resource):
  @api.expect(user_post)
  def post(self):
    if Operations.SaveUser(api.payload):
      send_email(api.payload['email'],
                 'Welcome to primeplay.io!',
                 'This is a notification to let you know that your account was created sucessfully')
      return { 'code': 200, 'status': 'success', 'data': 1 }
    else:
      return { 'code': 200, 'status': 'success', 'data': 'User with this email exists' }

  def get(self):
    username, password = b64decode(request.headers['Authorization'].split('Bearer ')[1]).decode("utf-8").split(":")
    user = Operations.Login({ 'Username': username, 'Password': password})
    user.pop('Password')
    return user


user_login = api.model('user_login', {
  'Username': fields.String,  
  'Password': fields.String,
})

@api.route("/authenticate")
class UsersLoginClass(Resource):
  @api.expect(user_login)
  def post(self):
    user = Operations.Login(api.payload)
    if user is not None:
      auth_header = "{}:{}".format(api.payload['Username'], api.payload['Password'])
      return {
        "id": user['Id'],
        "token": b64encode(auth_header.encode('ascii')).decode('ascii')
      }
