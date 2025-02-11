# database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://jalalpuraks:D2StUbv0HUcwNBgv@cluster0.1lac9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("schoolDB")


# Function to check connection
def check_mongo_connection():
    try:
        client.admin.command("ping")  # Ping MongoDB
        return True
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        return False