from pymongo import MongoClient


MONGO_URI = os.getenv("MONGO_URI")  # from Render environment variables

client = MongoClient(MONGO_URI)
db = client["purple_db"]

pl_collection = db["pl_data"]      # keywords + pincode
pdp_collection = db["pdp_data"]    # urls + pincode