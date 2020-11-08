from flask_restx import Namespace, Resource, fields, marshal
import json
from ORM import Operations
from Auth import authenticate
from flask import request
from base64 import b64decode, b64encode

api = Namespace("/developers")

@api.route("/games/<developer_id>")
class DeveloperGameslass(Resource):
  def get(self, developer_id):
    return Operations.QueryDeveloperGames(developer_id)
