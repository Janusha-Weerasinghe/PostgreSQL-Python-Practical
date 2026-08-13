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