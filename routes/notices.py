from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import datetime
from database import db  # Import the database instance

router = APIRouter()

# Notice Pydantic Model
class Notice(BaseModel):
    subject: str
    details: str
    postedTo: str
    date: str  # Store as string (YYYY-MM-DD)

# Route to add a new notice
@router.post("/api/addNotice")
async def add_notice(notice: Notice):
    new_notice = {
        "subject": notice.subject,
        "details": notice.details,
        "postedTo": notice.postedTo,
        "date": notice.date,
        "created_at": datetime.utcnow(),  # Store timestamp
    }
    db.notices.insert_one(new_notice)  # Save to DB
    return {"message": "Notice added successfully"}

# Route to get all notices
@router.get("/api/getNotices", response_model=List[Notice])
async def get_notices():
    notices = await db.notices.find({}, {"_id": 0}).to_list(length=None)  # Exclude MongoDB ID
    if not notices:
        raise HTTPException(status_code=404, detail="No notices found")
    return notices
