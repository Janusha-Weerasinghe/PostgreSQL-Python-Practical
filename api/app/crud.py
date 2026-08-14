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