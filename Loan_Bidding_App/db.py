import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB connection string from .env
MONGO_URI = os.getenv("MONGO_URI")

# Ensure MONGO_URI is not None
if not MONGO_URI:
    raise ValueError("❌ ERROR: MONGO_URI is not set in .env file!")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["debt_auction_db"]

# Create collections
users_collection = db["users"]
loans_collection = db["loans"]
bids_collection = db["bids"]

print("✅ Connected to MongoDB successfully!")
