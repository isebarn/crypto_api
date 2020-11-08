from flask import request
from bcrypt import checkpw
from functools import wraps
from base64 import b64decode, b64encode
from ORM import Operations
import json

#requests.get('http://127.0.0.1:5000/product?prod_ids=T2191,T2199', 
#headers={'Authorization': 'Basic MDEyMjMwMTIzNDg6bGFkeXNvbmRvcw=='})
#res = client.get('/order/', headers={'Authorization': 'Basic 01223012348:ladysondos'})

def authenticate(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    if request.headers.get('Authorization', None) is not None:
      auth_header = request.headers['Authorization'].split()[1]
    else:
      data = json.loads(request.data)
      auth_header = "{}:{}".format(data['Username'], data['Password'])

    # User logged in w. username/pw, so we return token
    if ':' in auth_header:
      username, password = auth_header.split(":")

      user = Operations.Login(username, password)
      print(user['Id'])
      print(b64encode(auth_header.encode('ascii')).decode('ascii'))
      return {
        "Id": user['Id'],
        "Token": b64encode(auth_header.encode('ascii')).decode('ascii')
      }

    else:
      username, password = b64decode(auth_header).decode("utf-8").split(":")
      user = Operations.Login(username, password)
      user.pop('Password')
      return user

  return wrapper