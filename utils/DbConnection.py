import os
import pymongo
from app_constants import databases
from multipledispatch import dispatch
from bson.objectid import ObjectId

def client():
  return pymongo.MongoClient(os.environ.get("DATABASE"))

def get_collection(collection_name):
  collection = databases.get(collection_name, None)
  if collection is not None:
    return client()[collection.get('database')][collection.get('collection')]


@dispatch(str, ObjectId)
def get_document(collection_name, _id):
  return get_collection(collection_name).find_one({'_id': _id})

@dispatch(str, str, str)
def get_document(collection_name, field, value):
  return get_collection(collection_name).find({field: value})