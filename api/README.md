
We're going to build this:

```text
                    Client / Browser
                           │
                           ▼
                      FastAPI API
                           │
                           ▼
                    CRUD Functions
                           │
                           ▼
                       SQLAlchemy
                           │
                           ▼
                         psycopg
                           │
                           ▼
                      PostgreSQL
```

And by the end you'll have:

```text
GET    /students
GET    /students/{id}
POST   /students
PUT    /students/{id}
DELETE /students/{id}
```

---

# 1. First: Your Stack Builder Screen

You showed this:

![Stack Builder](attachment)

You're currently in **PostgreSQL Stack Builder**.

### What is Stack Builder?

Stack Builder is an optional PostgreSQL utility for installing additional components such as:

```text
Database Drivers
Spatial Extensions
Additional Tools
Web Development Components
```

For **this FastAPI + PostgreSQL project, you don't need Stack Builder**.

You already need:

* PostgreSQL Server
* pgAdmin
* Python
* FastAPI
* SQLAlchemy
* psycopg

So at this screen:

### 👉 Click `Cancel`

Don't install anything from:

```text
Database Drivers
Database Server
Spatial Extensions
Web Development
```

We're going to install the Python PostgreSQL driver ourselves:

```bash
pip install psycopg
```

That's cleaner for this project.

---

# 2. What We Are Building

Our final project will be:

```text
student-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Don't worry if this looks complicated.

Each file has **one main responsibility**.

---

# 3. Understand the Files First

This is the architecture:

```text
main.py
   │
   │ API endpoints
   ▼
crud.py
   │
   │ Database operations
   ▼
models.py
   │
   │ Database structure
   ▼
database.py
   │
   │ SQLAlchemy connection
   ▼
PostgreSQL
```

And:

```text
schemas.py
```

handles the data coming **into and out of the API**.

So:

| File               | Responsibility                             |
| ------------------ | ------------------------------------------ |
| `main.py`          | FastAPI routes                             |
| `database.py`      | PostgreSQL connection + SQLAlchemy session |
| `models.py`        | Database table structure                   |
| `schemas.py`       | API request/response validation            |
| `crud.py`          | Create, Read, Update, Delete operations    |
| `.env`             | Database credentials                       |
| `.gitignore`       | Files Git should ignore                    |
| `requirements.txt` | Python dependencies                        |

This separation is much better than putting everything into `main.py`.

---

# 4. Step 1 — Create Your Project Folder

Open VS Code.

Create a folder:

```text
student-api
```

Open it in VS Code.

Then create:

```text
student-api/
│
├── app/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Inside `app`, create:

```text
app/
│
├── __init__.py
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py
```

Your VS Code Explorer should look like:

```text
student-api
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 5. Step 2 — Create Your Conda Environment

Since you've already learned Miniconda, let's use it.

Open the VS Code terminal:

```bash
conda create -n student-api python=3.12
```

Then:

```bash
conda activate student-api
```

Check:

```bash
python --version
```

You should see something similar to:

```text
Python 3.12.x
```

---

# 6. Step 3 — Install the Required Packages

Run:

```bash
pip install fastapi uvicorn sqlalchemy psycopg python-dotenv
```

These packages have different jobs.

### FastAPI

```text
fastapi
```

Creates our REST API.

### Uvicorn

```text
uvicorn
```

Runs the FastAPI application.

### SQLAlchemy

```text
sqlalchemy
```

Handles database interaction / ORM.

### psycopg

```text
psycopg
```

Allows Python/SQLAlchemy to communicate with PostgreSQL.

### python-dotenv

```text
python-dotenv
```

Loads environment variables from `.env`.

---

# 7. Save Dependencies

Run:

```bash
pip freeze > requirements.txt
```

Now `requirements.txt` will contain your installed packages.

Don't manually type versions unless you have a reason to.

---

# 8. Step 4 — Create PostgreSQL Database

Open **pgAdmin**.

You should have something similar to:

```text
Servers
└── PostgreSQL
    ├── Databases
    ├── Login/Group Roles
    └── ...
```

Right-click:

```text
Databases
```

Then:

```text
Create
   ↓
Database
```

Set:

```text
Database name:
student_db
```

Then click **Save**.

Now you have:

```text
PostgreSQL Server
       │
       └── student_db
```

---

# 9. Step 5 — Database User

For learning, PostgreSQL probably has a user such as:

```text
postgres
```

However, I don't want you to build the application using the PostgreSQL superuser permanently.

Remember:

```text
postgres
   ↓
Superuser
   ↓
Extremely broad privileges
```

That's exactly what the warning in your screenshot is referring to.

For this learning project, you can initially use your PostgreSQL account to get everything working, but we'll create a dedicated application role.

---

# 10. Create an Application Role

In pgAdmin:

```text
student_db
   ↓
Query Tool
```

Run:

```sql
CREATE ROLE student_api_user
WITH LOGIN
PASSWORD 'YOUR_PASSWORD';
```

Replace:

```text
YOUR_PASSWORD
```

with a password you choose.

For example, don't literally use:

```text
YOUR_PASSWORD
```

---

# 11. Give the Application User Access

Still connected to `student_db`, run:

```sql
GRANT CONNECT
ON DATABASE student_db
TO student_api_user;
```

Then:

```sql
GRANT USAGE, CREATE
ON SCHEMA public
TO student_api_user;
```

For this learning project, we're allowing the application user to create the tables.

Later, in production, you'd normally use a proper migration/deployment role rather than letting the application create its own schema.

---

# 12. Step 6 — Create `.env`

Now go back to VS Code.

Open:

```text
.env
```

Put:

```env
DATABASE_URL=postgresql+psycopg://student_api_user:YOUR_PASSWORD@localhost:5432/student_db
```

Replace:

```text
YOUR_PASSWORD
```

with the password you created.

For example, conceptually:

```env
DATABASE_URL=postgresql+psycopg://student_api_user:MyPassword@localhost:5432/student_db
```

⚠️ **Don't commit this file to GitHub.**

---

# 13. Step 7 — Create `.gitignore`

Open:

```text
.gitignore
```

Put:

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/

# Conda
conda-meta/

# Environment variables
.env

# IDE
.vscode/

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/

# Distribution
dist/
build/
*.egg-info/
```

The most important one here is:

```text
.env
```

because it contains your database credentials.

---

# 14. Step 8 — `database.py`

Now we're going to build the database connection.

Open:

```text
app/database.py
```

Put:

```python
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# Load variables from .env
load_dotenv()


# Get database URL
DATABASE_URL = os.getenv("DATABASE_URL")


# Make sure DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")


# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# Create database session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

---

# 15. Understand `database.py`

This is important.

### `load_dotenv()`

```python
load_dotenv()
```

loads:

```text
.env
```

---

### `DATABASE_URL`

```python
DATABASE_URL = os.getenv("DATABASE_URL")
```

gets:

```text
postgresql+psycopg://...
```

---

### `create_engine()`

```python
engine = create_engine(DATABASE_URL)
```

creates the SQLAlchemy engine that manages communication with PostgreSQL.

Conceptually:

```text
FastAPI
   ↓
SQLAlchemy Engine
   ↓
psycopg
   ↓
PostgreSQL
```

---

### `SessionLocal`

```python
SessionLocal = sessionmaker(...)
```

creates database sessions.

Think of a session as the object through which our application performs database work.

---

### `Base`

```python
class Base(DeclarativeBase):
    pass
```

is the base class our SQLAlchemy models will inherit from.

---

# 16. Step 9 — `models.py`

Now we define our database table.

Open:

```text
app/models.py
```

Put:

```python
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    age: Mapped[int | None] = mapped_column(
        nullable=True
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    score: Mapped[float | None] = mapped_column(
        Numeric(5, 2),
        nullable=True
    )
```

---

# 17. What Does This Model Mean?

This:

```python
class Student(Base):
```

represents:

```text
students
```

And:

```python
id
```

becomes:

```text
id
```

in PostgreSQL.

So:

```python
name
```

becomes:

```text
name
```

and:

```python
age
```

becomes:

```text
age
```

etc.

The resulting database table looks approximately like:

```text
students
──────────────────────────────
id
name
age
email
score
```

---

# 18. Understanding the Constraints

This:

```python
primary_key=True
```

means:

```text
id = Primary Key
```

This:

```python
nullable=False
```

means:

```text
name cannot be NULL
```

This:

```python
unique=True
```

means:

```text
Two students cannot have the same email
```

This:

```python
index=True
```

creates an index for that column.

--- -->

<!-- # 19. Step 10 — `schemas.py`

Now we need to define what data the API accepts and returns.

Open:

```text
app/schemas.py
```

Put:

```python
from pydantic import BaseModel, ConfigDict, Field


class StudentBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    age: int | None = Field(
        default=None,
        ge=0,
        le=150
    )

    email: str

    score: float | None = Field(
        default=None,
        ge=0,
        le=100
    )


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    age: int | None = Field(
        default=None,
        ge=0,
        le=150
    )

    email: str | None = None

    score: float | None = Field(
        default=None,
        ge=0,
        le=100
    )


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
```

---

# 20. Why Do We Need Schemas?

This is the difference:

```text
models.py
     ↓
Database structure
```

while:

```text
schemas.py
     ↓
API data validation
```

For example, someone sends:

```json
{
    "name": "Janusha",
    "age": 28,
    "email": "janusha@example.com",
    "score": 95
}
```

FastAPI/Pydantic checks whether the data matches the expected schema.

---

# 21. Example Validation

We specified:

```python
score: float | None = Field(
    default=None,
    ge=0,
    le=100
)
```

So:

```text
score = 95
```

✅ Valid.

But:

```text
score = 150
```

❌ Invalid.

Because the score must be between:

```text
0 → 100
```

That's one of the reasons API schemas are useful.

---

# 22. Step 11 — `crud.py`

Now we implement the actual database operations.

Open:

```text
app/crud.py
```

Put:

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Student
from .schemas import StudentCreate, StudentUpdate


def get_students(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    statement = (
        select(Student)
        .offset(skip)
        .limit(limit)
    )

    return db.scalars(statement).all()


def get_student(
    db: Session,
    student_id: int
):
    statement = select(Student).where(
        Student.id == student_id
    )

    return db.scalars(statement).first()


def create_student(
    db: Session,
    student: StudentCreate
):
    db_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        score=student.score
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    update_data = student_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(
    db: Session,
    student_id: int
):
    db_student = get_student(db, student_id)

    if db_student is None:
        return None

    db.delete(db_student)
    db.commit()

    return db_student
```

---

# 23. What Does `crud.py` Mean?

CRUD:

```text
C → Create
R → Read
U → Update
D → Delete
```

Our functions are:

```text
get_students()
     ↓
READ

get_student()
     ↓
READ

create_student()
     ↓
CREATE

update_student()
     ↓
UPDATE

delete_student()
     ↓
DELETE
```

This keeps database logic out of `main.py`.

---

# 24. Step 12 — `main.py`

🔥 This is where we create our API.

Open:

```text
app/main.py
```

Put:

```python
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud
from .database import Base, engine, get_db
from .schemas import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="Student API",
    description="A FastAPI application connected to PostgreSQL",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Student API is running"
    }


@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_students(
        db,
        skip=skip,
        limit=limit
    )


@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(
        db,
        student_id
    )

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(
        db,
        student
    )


@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(
        db,
        student_id,
        student
    )

    if updated_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return updated_student


@app.delete(
    "/students/{student_id}"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    deleted_student = crud.delete_student(
        db,
        student_id
    )

    if deleted_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }
```

---

# 25. This `main.py` Might Look Scary

Don't worry.

Let's break it down.

---

## Creating FastAPI

```python
app = FastAPI(
    title="Student API"
)
```

creates the API application.

---

## GET `/students`

```python
@app.get("/students")
```

means:

```text
GET /students
```

will execute:

```python
get_students()
```

---

## GET `/students/{student_id}`

```python
@app.get("/students/{student_id}")
```

means:

```text
GET /students/1
GET /students/2
GET /students/3
```

---

## POST

```python
@app.post("/students")
```

creates a new student.

---

## PUT

```python
@app.put("/students/{student_id}")
```

updates a student.

---

## DELETE

```python
@app.delete("/students/{student_id}")
```

deletes a student.

---

# 26. What Is `Depends(get_db)`?

This is an important FastAPI concept.

We have:

```python
db: Session = Depends(get_db)
```

FastAPI essentially says:

> "Before running this endpoint, give me a database session."

So:

```text
Request
   ↓
FastAPI
   ↓
get_db()
   ↓
Database Session
   ↓
Endpoint
   ↓
CRUD
   ↓
PostgreSQL
```

After the request is finished:

```python
finally:
    db.close()
```

closes the session.

---

# 27. Step 13 — `__init__.py`

For now:

```text
app/__init__.py
```

can simply be empty.

You don't need to put anything inside it.

Its presence helps Python treat `app` as a package and supports imports such as:

```python
from . import crud
```

---

# 28. Step 14 — Run the API

Open the terminal in the **project root**:

```text
student-api/
```

Make sure your Conda environment is activated:

```bash
conda activate student-api
```

Then run:

```bash
uvicorn app.main:app --reload
```

You should see something similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

🎉 Your API is running.

---

# 29. Open the API

Open your browser:

```text
http://127.0.0.1:8000
```

You should get:

```json
{
    "message": "Student API is running"
}
```

---

# 30. The Best Part — Swagger UI

FastAPI automatically gives you interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You'll see:

```text
Student API

GET     /students
GET     /students/{student_id}
POST    /students
PUT     /students/{student_id}
DELETE  /students/{student_id}
```

This is where we're going to test everything.

---

# 31. Test POST First

In Swagger:

```text
POST /students
```

Click:

```text
Try it out
```

Enter:

```json
{
    "name": "Janusha",
    "age": 28,
    "email": "janusha@example.com",
    "score": 88.5
}
```

Click:

```text
Execute
```

You should receive something like:

```json
{
    "name": "Janusha",
    "age": 28,
    "email": "janusha@example.com",
    "score": 88.5,
    "id": 1
}
```

Now the data exists in PostgreSQL.

---

# 32. Test GET

Open:

```text
GET /students
```

Click:

```text
Try it out
```

Then:

```text
Execute
```

You should get:

```json
[
    {
        "name": "Janusha",
        "age": 28,
        "email": "janusha@example.com",
        "score": 88.5,
        "id": 1
    }
]
```

Your flow is now:

```text
Swagger
   ↓
FastAPI
   ↓
CRUD
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
PostgreSQL
```

🔥 That's a real backend application.

---

# 33. Test GET by ID

Try:

```text
GET /students/{student_id}
```

Enter:

```text
1
```

Execute.

You should get:

```json
{
    "name": "Janusha",
    "age": 28,
    "email": "janusha@example.com",
    "score": 88.5,
    "id": 1
}
```

---

# 34. Test Non-Existing Student

Try:

```text
GET /students/999
```

You should get:

```json
{
    "detail": "Student not found"
}
```

with:

```text
404 Not Found
```

This is good API behavior.

---

# 35. Test PUT

Try:

```text
PUT /students/1
```

Body:

```json
{
    "name": "Janusha",
    "age": 28,
    "email": "janusha@example.com",
    "score": 95
}
```

Execute.

You should receive:

```json
{
    "name": "Janusha",
    "age": 28,
    "email": "janusha@example.com",
    "score": 95,
    "id": 1
}
```

---

# 36. Test DELETE

Try:

```text
DELETE /students/1
```

Execute.

You should receive:

```json
{
    "message": "Student deleted successfully",
    "student_id": 1
}
```

Then run:

```text
GET /students
```

The student should no longer appear.

---

# 37. Verify Directly in PostgreSQL

Now open pgAdmin.

Go to:

```text
student_db
   ↓
Schemas
   ↓
public
   ↓
Tables
   ↓
students
```

You should see your table.

Right-click:

```text
students
   ↓
View/Edit Data
   ↓
All Rows
```

Now you can see the same data that your FastAPI application is manipulating.

That's the important connection:

```text
FastAPI
     ↕
PostgreSQL
```

---

# 38. Your Final Project Structure

After completing everything:

```text
student-api/
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── main.py
│   │
│   ├── database.py
│   │
│   ├── models.py
│   │
│   ├── schemas.py
│   │
│   └── crud.py
│
├── .env
│
├── .gitignore
│
├── requirements.txt
│
└── README.md
```

---

# 39. How Everything Connects

This is the most important diagram to understand:

```text
                         CLIENT
                           │
                           │ HTTP
                           ▼
                    ┌───────────────┐
                    │    FastAPI    │
                    │   main.py     │
                    └───────┬───────┘
                            │
                            │
                            ▼
                    ┌───────────────┐
                    │     CRUD      │
                    │    crud.py    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  SQLAlchemy   │
                    │   database.py │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    psycopg    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  PostgreSQL   │
                    │  student_db   │
                    └───────────────┘
```

And:

```text
models.py
    ↓
defines database structure

schemas.py
    ↓
validates API data

database.py
    ↓
connects application to PostgreSQL

crud.py
    ↓
performs database operations

main.py
    ↓
exposes REST API endpoints
```

---

# 40. One Important Professional Improvement

For this **learning project**, this is okay:

```python
Base.metadata.create_all(bind=engine)
```

It automatically creates the tables.

But in a professional application, you would generally use a migration tool such as **Alembic** to manage schema changes.

Your later architecture will become:

```text
SQLAlchemy Models
       ↓
Alembic Migrations
       ↓
PostgreSQL
```

Don't add Alembic yet. **First understand this project.**

---

# 41. Your Learning Checklist

Don't move to the next PostgreSQL practical until you can do these yourself:

* [ ] Create `student_db`
* [ ] Create `student_api_user`
* [ ] Create `.env`
* [ ] Create Conda environment
* [ ] Install FastAPI
* [ ] Install SQLAlchemy
* [ ] Install psycopg
* [ ] Understand `database.py`
* [ ] Understand `models.py`
* [ ] Understand `schemas.py`
* [ ] Understand `crud.py`
* [ ] Understand `main.py`
* [ ] Run Uvicorn
* [ ] Open `/docs`
* [ ] Create a student with POST
* [ ] Retrieve students with GET
* [ ] Retrieve one student
* [ ] Update a student
* [ ] Delete a student
* [ ] Verify the data in pgAdmin
* [ ] Explain the complete request → database flow

---

# 🎯 What I Want You to Do Now

**Don't create all the files and paste everything blindly at once.** That will make this another copy-paste project and you won't really learn it.

Let's do it in stages:

```text
STEP 1
Create project + Conda environment
        ↓
STEP 2
Install packages
        ↓
STEP 3
Create PostgreSQL database + user
        ↓
STEP 4
Create .env + .gitignore
        ↓
STEP 5
Build database.py
        ↓
STEP 6
Build models.py
        ↓
STEP 7
Build schemas.py
        ↓
STEP 8
Build crud.py
        ↓
STEP 9
Build main.py
        ↓
STEP 10
Run FastAPI
        ↓
STEP 11
Test Swagger
        ↓
STEP 12
Verify PostgreSQL
```

### **For your current screen:**

Just **click `Cancel` on Stack Builder**. You don't need to install anything there for this project.

Then create the `student-api` folder in VS Code and the Conda environment. Once that's done, the next thing to build is **`database.py`**, because everything else depends on establishing the PostgreSQL connection correctly. --> 
