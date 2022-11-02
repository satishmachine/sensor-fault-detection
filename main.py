from pymongo import MongoClient
from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == '__main__':
    Mongodb_client = MongoDBClient()
    print(Mongodb_client.database.list_collection_names())