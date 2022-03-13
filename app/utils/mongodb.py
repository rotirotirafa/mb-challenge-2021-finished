import pymongo

from app.settings import MONGODB_PORT, MONGODB_CLIENT, MONGODB_COLLECTION

mongo_client = pymongo.MongoClient(f'mongodb://localhost:{MONGODB_PORT}/')

db = mongo_client[MONGODB_CLIENT]

mms_collection = db[MONGODB_COLLECTION]

