from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import EmployeeDB
from models import EmployeeCreate, EmployeeUpdate
from datetime import datetime

# CREATE an employee

def create_employee(db: Session, employee: EmployeeCreate):    
    # check if email exists
    existing = db.query(EmployeeDB).filter(EmployeeDB.email == employee.email).first()
    if existing:
        raise ValueError("Email bereits vergeben")

    # create a new entry for employee

    db_employee = EmployeeDB(
        name = employee.name,
        email = employee.email,
        position = employee.position,
        start_date = employee.start_date,
        salary = employee.salary,
        created_at = datetime.utcnow()
    )
    try:
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
    except IntegrityError:
        db.rollback()
        raise ValueError("Fehler beim speichern")
# READ single employee

# READ all employees

# Update an employee

    # check if email exists

    # Update the required fields

# DELETE an employee