# 🚀 Student Result Management System (SRMS) - Backend

A robust and modular **FastAPI** backend for managing students, courses, and results — built for speed, security, and scalability.

> 🛢️ Tech Stack: **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, **JWT Auth**, **Pydantic**, **Uvicorn**

---

## 📂 Folder Structure

```
server/
├── alembic/                       # DB migration scripts
├── config/                        # App and DB config
│   ├── database.py
│   └── env.py
├── controller/                    # All route handlers (API controllers)
│   ├── course_controller.py
│   ├── result_controller.py
│   ├── stats_controller.py
│   ├── student_controller.py
│   └── user_controller.py
├── db/                            # DB connection + decorators
│   ├── connect_db.py
│   └── decorator.py
├── logs/                          # Log files
│   └── app.log
├── middleware/                    # Custom auth middleware
│   └── auth_middleware.py
├── models/                        # SQLAlchemy ORM models
│   ├── course_model.py
│   ├── result_model.py
│   ├── student_model.py
│   └── user_model.py
├── schemas/                       # Pydantic request/response schemas
│   ├── course_schema.py
│   ├── result_schema.py
│   ├── student_schema.py
│   └── user_schema.py
├── service/                       # Business logic
│   ├── course_service.py
│   ├── result_service.py
│   ├── stats_service.py
│   ├── student_service.py
│   └── user_service.py
├── utils/                         # Utility modules
│   ├── auth.py
│   └── jwt.py
├── main.py                        # Entry point
├── alembic.ini                    # Alembic configuration
├── requirements.txt              # Python dependencies
├── .env                           # Environment variables
└── .gitignore
```

---

## ⚙️ Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/Purav2003/student-server
cd student-server
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root:

```env
DATABASE_URI=POSTGRESQL_URL
SECRET_KEY=YOUR_SECRET_KEY
ALGORITHM=YOUR_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=YOUR_TOKEN_EXPIRE_MINUTES
```

### 5. Start the FastAPI server

```bash
uvicorn main:app --reload
```

> 🚀 Server runs at: `http://localhost:8000`

> 📘 Docs available at: `http://localhost:8000/docs`

---

## 📮 Postman Collection

Use the following collection to test all backend routes with authentication.

> 🧪 **Download here**: [SRMS Postman Collection 🔗](https://www.postman.com/purav2003/purav-s-workspace/collection/zt1d64u/srms?action=share&creator=0)

---

## 🔐 Auth Flow (JWT)

- On login, user receives a `JWT` token.
- This token must be included in headers for all protected routes:

```
Authorization: Bearer <your-token>
```

---

## 🛠️ Dev Notes

- Built with **FastAPI's dependency injection**
- **Stateless auth** using JWT and custom middleware
- **PostgreSQL** with SQLAlchemy + Alembic for migrations
- Structured in **MVC + Service** style for clean separation

---

## 👤 Author

**Purav Shah**
📧 shahpurav308@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/purav308)
🌐 [Portfolio](https://purav-portfolio.vercel.app)

---

> Backend made with ❤️ using FastAPI, PostgreSQL, and JWT Auth
