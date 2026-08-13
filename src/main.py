import psycopg

# ============================================
# Connect to PostgreSQL
# ============================================

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="student_db",
    user="postgres",
    password="YOUR_PASSWORD"
    #password=""
)

print("Connected to PostgreSQL!")


# ============================================
# Create the students table
# ============================================

with conn.cursor() as cur:

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER,
            email VARCHAR(150) UNIQUE,
            score NUMERIC(5,2)
        );
    """)

conn.commit() #Because you're making a database change.

print("Students table created!")


# ============================================
# Insert a student
# ============================================

with conn.cursor() as cur:

    cur.execute("""
        INSERT INTO students
        (name, age, email, score)
        VALUES (%s, %s, %s, %s)
    """, (
        "Janusha",
        28,
        "janusha@example.com",
        88.5
    ))
 #We're using parameters instead of constructing SQL using string concatenation.

   # This is important for preventing SQL injection.

     # Don't do:

     # query = f"INSERT INTO students VALUES ('{name}')"

  # Use parameterized queries.
conn.commit()

print("Student inserted successfully!")


# ============================================
# Close connection
# ============================================

conn.close()

print("Database connection closed.")