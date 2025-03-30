import streamlit as st
from pymongo import MongoClient

# ✅ Use Streamlit Secrets
MONGO_URI = st.secrets["MONGO_URI"]

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["debt_auction_db"]

# Collections
users_collection = db["users"]
loans_collection = db["loans"]
bids_collection = db["bids"]

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
