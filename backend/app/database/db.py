from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

from backend.app.config import settings


connect_args = {}

if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {
        "check_same_thread": False
    }


engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    department = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )

    salary = Column(
        Float,
        nullable=False
    )

    performance_score = Column(
        Float,
        nullable=False
    )


def init_db():

    Base.metadata.create_all(
        bind=engine
    )

    db = SessionLocal()

    try:

        if db.query(Employee).count() == 0:

            employees = [
                Employee(
                    name="Rahul",
                    department="Finance",
                    role="Financial Analyst",
                    salary=750000,
                    performance_score=8.5
                ),
                Employee(
                    name="Priya",
                    department="HR",
                    role="HR Specialist",
                    salary=650000,
                    performance_score=9.0
                ),
                Employee(
                    name="Arjun",
                    department="Engineering",
                    role="Software Engineer",
                    salary=950000,
                    performance_score=8.8
                ),
                Employee(
                    name="Sneha",
                    department="Finance",
                    role="Accountant",
                    salary=600000,
                    performance_score=7.8
                ),
                Employee(
                    name="Vikram",
                    department="HR",
                    role="Recruiter",
                    salary=550000,
                    performance_score=8.2
                )
            ]

            db.add_all(employees)
            db.commit()

    finally:

        db.close()