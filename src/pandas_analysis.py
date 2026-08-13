# ============================================================
# PostgreSQL + Pandas Practical
# ============================================================

import pandas as pd
from sqlalchemy import create_engine

# ============================================================
# 1. Create Database Connection
# ============================================================

DATABASE_URL = (
    "postgresql+psycopg://postgres:YOUR_PASSWORD"
    "@localhost:5432/student_db"
)

engine = create_engine(DATABASE_URL)

print("Connected to PostgreSQL!")

