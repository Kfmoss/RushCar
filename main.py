import pymongo
import pymongo.mongo_client

conn = pymongo.MongoClient("mongodb://localhost:27017/")

if conn:
    print("connection ok!!")
    db = conn['TestIM']
    print(db.list_collection_names())
else:
    print("error : ", pymongo.mongo_client.PyMongoError)


