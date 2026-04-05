# Finance Backend API

A FastAPI-based backend application that provides CRUD operations for managing users. This project demonstrates REST API development, database integration, and validation handling using modern Python tools.

## 🚀 Features

- Create User
- Get User by ID
- Search Users by Name
- Update User
- Delete User
- Unique Email Validation
- SQLite Database Integration
- Swagger UI for API testing

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## 📂 Project Structure

```
finance-backend/
│── main.py
│── models.py
│── schemas.py
│── crud.py
│── database.py
│── requirements.txt
│── finance.db
```

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/finance-backend.git
cd finance-backend
```

2. Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

5. Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST | /users | Create user |
| GET | /users/{user_id} | Get user |
| GET | /users/search | Search users |
| PUT | /users/{user_id} | Update user |
| DELETE | /users/{user_id} | Delete user |

## ⚠️ Notes

- Email field is unique
- Duplicate emails will throw an error
- SQLite database is used for simplicity

## 🎯 Future Improvements

- Add authentication (JWT)
- Deploy on cloud (Render / AWS)
- Add pagination
- Add frontend integration

## 👩‍💻 Author

Preksha Rajaram Naik