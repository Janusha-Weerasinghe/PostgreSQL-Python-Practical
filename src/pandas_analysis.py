# ============================================================
# PostgreSQL + Pandas Practical
# ============================================================

import pandas as pd
from sqlalchemy import create_engine


# ============================================================
# 1. Create Database Connection
# ============================================================

DATABASE_URL = (
    #"postgresql+psycopg://postgres:Password"
    
    "@localhost:5432/student_db"
)

engine = create_engine(DATABASE_URL)

print("Database engine created.")

# High Important if password have "@" mark The problem is the @ character .In a PostgreSQL SQLAlchemy URL, @ has a special meaning: it separates the password from the host.
# So we need to URL-encode @ as %40.

# ============================================================
# 2. Load Data from PostgreSQL
# ============================================================

query = """
SELECT
    id,
    name,
    age,
    score
FROM students;
"""

df = pd.read_sql(query, engine)

print("Successfully connected to PostgreSQL!")

# ============================================================
# 3. Display Dataset
# ============================================================

print("\nStudent Dataset:")
print(df)

# ============================================================
# 4. Explore the Dataset
# ============================================================

print("\nFirst 5 Records:")
print(df.head())


print("\nDataset Information:")
df.info()


print("\nStatistical Summary:")
print(df.describe())

# ============================================================
# 5. Check Missing Values
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())

