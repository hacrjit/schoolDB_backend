from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from database import db  # Replace with your actual DB connection

router = APIRouter()

# Store entire routine structure as JSON
class RoutineData(BaseModel):
    schedules: Dict[str, Any]

@router.post("/api/saveClassRoutine")
async def save_class_routine(data: RoutineData):
    # Upsert a single document storing the entire schedule
    db.classroutine.update_one(
        {"type": "complete_routine"},
        {"$set": {"data": data.schedules, "updated_at": datetime.utcnow()}},
        upsert=True
    )
    return {"message": "Class routine saved successfully"}

@router.get("/api/getClassRoutine")
async def get_class_routine():
    routine_doc = await db.classroutine.find_one({"type": "complete_routine"}, {"_id": 0})
    if not routine_doc:
        raise HTTPException(status_code=404, detail="No class routine found")
    return routine_doc.get("data", {})