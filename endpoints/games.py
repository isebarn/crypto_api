from flask_restx import Namespace, Resource, fields, marshal
import json
from ORM import Operations
from Auth import authenticate
from flask import request
from base64 import b64decode, b64encode

api = Namespace("/games", description="Root path")

game_post = api.model('game_post', {
  'user_id': fields.Integer,
  'path': fields.String,
  'icon': fields.String,
  'name': fields.String,
  'github': fields.String
})


@api.route("/")
class GamesClass(Resource):
  def get(self):
    return Operations.QueryGames()

  @api.expect(game_post)
  def post(self):
    print(api.payload)
    Operations.SaveGame(api.payload)
    return 1
