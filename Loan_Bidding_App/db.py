import streamlit as st
from pymongo import MongoClient

MONGO_URI = st.secrets["MONGO_URI"]

client = MongoClient(MONGO_URI)
db = client["debt_auction_db"]

users_collection = db["users"]
loans_collection = db["loans"]
bids_collection = db["bids"]

if not MONGO_URI:
    raise ValueError("❌ ERROR: MONGO_URI is not set in .env file!")

client = MongoClient(MONGO_URI)
db = client["debt_auction_db"]

users_collection = db["users"]
loans_collection = db["loans"]
bids_collection = db["bids"]

print("✅ Connected to MongoDB successfully!")
