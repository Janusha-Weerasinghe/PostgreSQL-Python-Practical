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

# ============================================================
# 6. Calculate Average Score
# ============================================================

average_score = df["score"].mean()

print("\nAverage Score:")
print(average_score)

# ============================================================
# 7. Find High Performers
# ============================================================

high_performers = df[df["score"] >= 80]

print("\nHigh Performing Students:")
print(high_performers)

# ============================================================
# 7. Find High Performers (Descending order — Highest → Lowest)
# ============================================================


high_performers = df[df["score"] >= 80]

high_performers = high_performers.sort_values(
    by="score",
    ascending=False
)

print("\nHigh Performing Students:")
print(high_performers)

# ============================================================
# 7. Find High Performers (Ascending order — Lowest → Highest)
# ============================================================
high_performers = df[df["score"] >= 80]

high_performers = high_performers.sort_values(
    by="score",
    ascending=True
)

print("\nHigh Performing Students:")
print(high_performers)