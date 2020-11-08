from flask import Blueprint
from flask_restx import Api, fields
from .users import api as users_api
from .games import api as games_api
from .developers import api as developers_api

blueprint = Blueprint('', __name__)
authorizations = {
  'Basic Auth': {
      'type': 'basic',
      'in': 'header',
      'name': 'Authorization'
  },
}
api = Api(blueprint, authorizations=authorizations, security='Basic Auth')
api.add_namespace(users_api)
api.add_namespace(developers_api)
api.add_namespace(games_api)

@api.errorhandler(Exception)
def default_error_handler(error):
  return { 'code': 400, 'status': 'failure', 'message': str(error)}, 400