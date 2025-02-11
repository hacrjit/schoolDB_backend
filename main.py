from fastapi import FastAPI
from database import db,check_mongo_connection  # Import db from database.py
from routes.users import router as user_router  # Import users router
from routes.notices import router as notice_router  # Import notice router
# from routes.finance import router as finance_router  # Import finance router
from routes.classroutine import router as classroutine_router  # Import class routine router

app = FastAPI()
app.include_router(user_router)
app.include_router(notice_router)
# app.include_router(finance_router)
app.include_router(classroutine_router)


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods including OPTIONS
    allow_headers=["*"],
)




# Health check endpoint
@app.get("/health/mongodb")
async def check_mongodb():
    is_connected = check_mongo_connection()
    if is_connected:
        return {"status": "MongoDB is connected"}
    else:
        return {"status": "MongoDB connection failed"}, 500