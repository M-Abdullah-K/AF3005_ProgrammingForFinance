import streamlit as st
from db import users_collection
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def login(username, password, user_type):
    """Handles login for users and admins separately."""
    user = users_collection.find_one({"username": username})

    if user:
        print(f"🟢 Found user: {user}")  # Debug log
        
        if user.get("role") == user_type and verify_password(password, user["password"]):
            return True
    
    return False


def signup(username, password):
    """Registers a new user (only non-admins)."""
    print(f"🟢 Signup Attempt: Username = {username}")  # Debug log

    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        print("❌ Username already exists!")  # Debug log
        return False

    hashed_password = hash_password(password)
    users_collection.insert_one({"username": username, "password": hashed_password, "role": "user"})
    
    print("✅ Signup successful!")  # Debug log
    return True

def ensure_admin_exists():
    """Ensures an admin account exists in the database."""
    admin_username = "admin123"  # Change this to your desired admin username
    admin_password = "securepassword"  # Change this to a strong password

    existing_admin = users_collection.find_one({"role": "admin"})

    if not existing_admin:
        print("🚀 Admin not found! Creating admin account...")
        hashed_password = hash_password(admin_password)
        users_collection.insert_one({
            "username": admin_username,
            "password": hashed_password,
            "role": "admin"
        })
        print("✅ Admin account created successfully!")
    else:
        print("✅ Admin already exists.")
