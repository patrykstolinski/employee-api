from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


DATABASE_URL = "postgresql://api_user:secure_password_123@localhost:5432/employees_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Model (Employee)

class EmployeeDB(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique = True, nullable = False, index = True)
    position = Column(String(100), nullable = True)
    start_date = Column(DateTime, nullable = True)
    salary = Column(Float, nullable = True)
    created_at = Column(DateTime, default = datetime.utcnow)
    updated_at = Column(DateTime, nullable = True)

# Create Tables
Base.metadata.create_all(bind=engine)

# start dependancies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

