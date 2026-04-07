from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")  # from Render environment variables
print("MONGO_URI =", MONGO_URI)  # TEMPORARY
client = MongoClient(MONGO_URI)
db = client["purple_db"]

pl_collection = db["pl_data"]      # keywords + pincode
pdp_collection = db["pdp_data"]    # urls + pincode
logs_collection = db["logs_pruple"]   # <-- ADD THIS