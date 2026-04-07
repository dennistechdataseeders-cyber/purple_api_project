from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["purple_db"]

pl_collection = db["pl_data"]      # keywords + pincode
pdp_collection = db["pdp_data"]    # urls + pincode