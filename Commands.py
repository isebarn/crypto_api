# Methods in here directly used by endpoints
import os
from src.MongoConnection import MongoConnection

def connect():
  return MongoConnection(user=os.environ.get('MONGO_USER'),
                               password=os.environ.get('MONGO_PASSWORD'),
                               db=os.environ.get('DB'))

def add_order(order):
  '''
  @order: json dictionary that will be inserted into collection orders
  In addition, 3 fields will be generated

  order.isExternal = True
  order.orderNum = generated from sequence
  order.orderID = order.TagerId + / + order.orderNum
  '''
  if len(order['productIds']) != len(order['productPrices']) \
    or len(order['productPrices']) != len(order['productQuantities']):

    raise Exception("Number of product IDs, product prices and product quantities, differ")

  connection = connect()
  order_num = connection.get_new_order_id()

  order['isExternal'] = True
  order['orderNum'] = order_num
  order['orderID'] = '{}/{}'.format(order['TagerID'], order_num)

  try:
    order = connection.save_document('orders', order)

  except Exception as e:
    raise Exception(str(e))

  return order
