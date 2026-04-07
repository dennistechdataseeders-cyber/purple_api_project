from pymongo import MongoClient
import os

client = MongoClient(os.getenv("mongodb://dennistechdataseeders_db_user:dennis09052003@ac-e63iz9w-shard-00-00.7xmrouw.mongodb.net:27017,ac-e63iz9w-shard-00-01.7xmrouw.mongodb.net:27017,ac-e63iz9w-shard-00-02.7xmrouw.mongodb.net:27017/?ssl=true&replicaSet=atlas-ogrfou-shard-0&authSource=admin&appName=Cluster0"))
db = client.test
print(db.list_collection_names())