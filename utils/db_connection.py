import pymongo
from pymongo import MongoClient
class MongoConnections:
    '''
    Create this client once for each process, and reuse it for all operations.
    It is a common mistake to create a new client for each request, which is very inefficient.
    '''

    g_db_connection = None
    def get_db_connection(self):
        """ get the database connection using env_constants.py"""
        #config_obj = config_parser_utility.ConfigParserUtility()
        #$config = config_obj.get_config_object()
        #db_connection = MongoClient(config['mongo_db']['host'], int(config['mongo_db']['port']),maxPoolSize=200)
        #if config['mongo_db'].get('username') and config['mongo_db'].get('password'):
        #    db_connection.the_database.authenticate(config['mongo_db']['username'],
        #                                        config['mongo_db']['password'], source='admin')
        return db_connection

    def connect(self,db_name,collection):
        self.intialize()
        database = self.db_connection[db_name]
        return database[collection]


    def  intialize(self):
        if MongoConnections.g_db_connection is None:
            MongoConnections.g_db_connection = self.get_db_connection()
        self.db_connection= MongoConnections.g_db_connection