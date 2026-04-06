from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

import models
import schemas
import crud

from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Backend API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id)


@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


@app.post("/transactions", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    role = "admin"
    if role != "admin":
        return {"error": "Not authorized"}
    return crud.create_transaction(db, transaction)


@app.get("/transactions", response_model=list[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)


@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return crud.delete_transaction(db, transaction_id)


@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_income = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "income").scalar() or 0
    total_expense = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "expense").scalar() or 0
    balance = total_income - total_expense
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
