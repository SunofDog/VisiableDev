import pymongo
from time import time
from random import randint

db_name = "france"
#########新建Mongo客户端#########
client = MongoClient("localhost", 27017)
#client = MongoClient()
#client = MongoClient("monodb://localhost:27017")
print("Connected MongoDB")
db = client.get_database(db_name)
#db = client.[db_name]
print("Switch to %s"%db_name)
collection = db.index_1
#collection = db["index_1"]
start = time()
for i in range(100):
    db.index_1.insert({"user": "user_%s"%i, "major_data": "水",  "price": randint(0, 120)})
print(time() - start)
print("Insert Completed!")
