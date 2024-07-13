import pymongo
import pymongo.errors as mongo_error
import logging
import threading

class Store:
    database:any
    
    def __init__(self) -> None:
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.database = myclient["se"]
        self.init_tables()

    def init_tables(self):
        try:
            '''TODO:这里对mongodb进行初始化'''
            pass
        except mongo_error.PyMongoError as e:
            logging.error(e)

    def get_db_conn(self):
        return self.database

database_instance: Store = None
# global variable for database sync
init_completed_event = threading.Event()

def init_database(db_path):
    global database_instance
    database_instance = Store(db_path)

#¸ÄÎª·µ»Ødatabase£¨¶ø²»ÊÇconn£©
def get_db_conn():
    global database_instance
    return database_instance.get_db_conn()