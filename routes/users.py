from fastapi import APIRouter, HTTPException
from models import User
from database import db
from bson import ObjectId  # Required for ObjectId conversion

router = APIRouter()

def serialize_user(user):
    """Convert MongoDB document to JSON serializable format."""
    user["_id"] = str(user["_id"])
    return user

@router.post("/users/")
async def create_user(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_dict = user.dict()
    await db.users.insert_one(user_dict)
    return {"message": "User created successfully"}

@router.get("/users/")
async def get_users():
    users = await db.users.find().to_list(100)  # Get first 100 users
    return [serialize_user(user) for user in users]  # Convert all users
