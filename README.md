# Finance Backend API

A FastAPI-based backend application that provides CRUD operations for managing users and financial transactions, along with financial summary analytics. This project demonstrates REST API development, database integration, validation, and backend logic implementation.

---

## 🚀 Features

- User Management (CRUD)
- Transaction Management (CRUD)
- Financial Summary (Income, Expense, Balance)
- Unique Email Validation
- SQLite Database Integration
- Swagger UI for API testing
- Basic Role-based Access Control (simulated)

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

## 📂 Project Structure

finance-backend/
│── main.py  
│── models.py  
│── schemas.py  
│── crud.py  
│── database.py  
│── requirements.txt  
│── finance.db  
│── README.md  

---

## ⚙️ Setup & Run (Step-by-Step)

1. Clone the repository:

git clone https://github.com/YOUR-USERNAME/finance-backend.git  
cd finance-backend  

2. Create virtual environment:

python -m venv venv  

3. Activate environment:

venv\Scripts\activate  

4. Install dependencies:

pip install -r requirements.txt  

5. Run the server:

uvicorn main:app --reload  

6. Open Swagger UI:

http://127.0.0.1:8000/docs  

---

## 🧪 How to Test the API

### Create User

POST /users

{
  "name": "Preksha",
  "email": "preksha@gmail.com",
  "role": "admin",
  "status": "active"
}

---

### Get Users

GET /users

---

### Update User

PUT /users/{user_id}

{
  "name": "Preksha Updated",
  "email": "preksha_updated@gmail.com",
  "role": "admin",
  "status": "active"
}

---

### Delete User

DELETE /users/{user_id}

---

### Create Transaction (Income)

POST /transactions

{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "date": "2026-04-06",
  "description": "Monthly salary"
}

---

### Create Transaction (Expense)

POST /transactions

{
  "amount": 2000,
  "type": "expense",
  "category": "food",
  "date": "2026-04-06",
  "description": "Groceries"
}

---

### Get Transactions

GET /transactions

---

### Delete Transaction

DELETE /transactions/{id}

---

### Get Summary

GET /summary

Example Response:

{
  "total_income": 5000,
  "total_expense": 2000,
  "balance": 3000
}

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST | /users | Create user |
| GET | /users | Get all users |
| GET | /users/{user_id} | Get user |
| PUT | /users/{user_id} | Update user |
| DELETE | /users/{user_id} | Delete user |
| POST | /transactions | Create transaction |
| GET | /transactions | Get all transactions |
| DELETE | /transactions/{id} | Delete transaction |
| GET | /summary | Get financial summary |

---

## 🔐 Access Control

- Admin → Full access  
- Analyst → Read access  
- Viewer → Limited access  

---

## ⚠️ Notes

- Email field is unique  
- Duplicate emails will throw an error  
- SQLite database is used for simplicity  

---

## 🎯 Future Improvements

- Add authentication (JWT)
- Add pagination
- Add filtering
- Role-based middleware
- Deploy on cloud (Render / AWS)

---

## 👩‍💻 Author

Preksha Rajaram Naik

 