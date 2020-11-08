# Methods in here directly used by endpoints
import os
from src.MongoConnection import MongoConnection

def connect():
  return MongoConnection(user=os.environ.get('MONGO_USER'),
                               password=os.environ.get('MONGO_PASSWORD'),
                               db=os.environ.get('DB'))

def get_user(username):
  connection = connect()

  user = next(connection.read_document('users', 'username', username), None)

  return user

def connect():
  return MongoConnection(user=os.environ.get('MONGO_USER'),
                               password=os.environ.get('MONGO_PASSWORD'),
                               db=os.environ.get('DB'))
'''
Get all Products from collection test.products.
Either all, or matching prod_ids list
We need to couple also with it categories from:
test.categories collection on CategoryId in test.products
'''
def products(prod_ids=None):
  connection = connect()

  categories_collection = connection.read_collection(collection_name='categories')
  categories = {str(category['_id']): category for category in categories_collection}

  if prod_ids == None:
    products = list(connection.read_collection(collection_name='products'))

  else:
    products = list(connection.read_document('products', 'prodID', prod_ids))

  if len(products) == 0:
    raise Exception("Product not found")

  for product in products:
      product['category'] = categories[str(product['categoryId'])]

  return products


def orders(tager_id):
  orders = list(connect().read_document('orders', 'TagerID', tager_id))
  return orders

def order(order_num, tager_id):
  orders = next(connect().read_document('orders', {'orderNum': order_num, 'TagerID': tager_id}), None)
  return orders

def get_current_order_id():
  connection = connect()
  return next(connection.read_document('counters', 'id', 'orderNum'))['seq']

def provinces():
  connection = connect()

  provinces = list(connection.read_collection('provinces'))
  if len(provinces) == 0:
    raise Exception("No provinces found")

  return provinces