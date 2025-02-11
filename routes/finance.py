# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from typing import List
# from datetime import datetime
# from database import db

# router = APIRouter()

# class Expense(BaseModel):
#     id: str
#     name: str
#     expenseType: str
#     amount: float
#     status: str
#     phone: str
#     email: str
#     date: str

# @router.post("/api/addExpense")
# async def add_expense(expense: Expense):
#     new_expense = {
#         "id": expense.id,
#         "name": expense.name,
#         "expenseType": expense.expenseType,
#         "amount": expense.amount,
#         "status": expense.status,
#         "phone": expense.phone,
#         "email": expense.email,
#         "date": expense.date,
#         "created_at": datetime.utcnow(),
#     }
#     db.expenses.insert_one(new_expense)
#     return {"message": "Expense added successfully"}

# @router.get("/api/getExpenses", response_model=List[Expense])
# async def get_expenses():
#     expenses = await db.expenses.find({}, {"_id": 0}).to_list(length=None)
#     if not expenses:
#         raise HTTPException(status_code=404, detail="No expenses found")
#     return expenses