# Finance Backend API

A backend REST API built using FastAPI for managing user data with full CRUD operations.

---

## 🚀 Features

- Create User
- Get All Users
- Get User by ID
- Update User
- Delete User

---

## 🛠️ Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
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
│── README.md

---

## ⚙️ Installation & Setup

git clone https://github.com/preksharajaram/finance-backend.git  
cd finance-backend  
pip install -r requirements.txt  

---

## ▶️ Run the Server

uvicorn main:app --reload

---

## 📌 API Endpoints

GET    /users          → Get all users  
GET    /users/{id}     → Get user by ID  
POST   /users          → Create new user  
PUT    /users/{id}     → Update user  
DELETE /users/{id}     → Delete user  

---

## 📷 API Testing

Open in browser:  
http://127.0.0.1:8000/docs  

---

## ✨ Future Improvements

- Authentication (JWT)
- Search functionality
- Pagination
- Deployment

---

## 👩‍💻 Author

Preksha Rajaram Naik