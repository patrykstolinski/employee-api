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
def get_employee(db: Session, employee_id: int):
    return db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()

# READ all employees
def get_employees(db: Session, skip: 0, limit: int = 100):
    return db.query(EmployeeDB).offset(skip).limit(limit).all()

# Update an employee
def update_employee(db: Session, employee_id: int, employee_update: EmployeeUpdate):
    
    db_employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    # check if ID exists
    if not db_employee:
        return None
    # check if employee email exists and is the same
    if employee_update.email and employee_update.email != db_employee.email:
        existing = db.query(EmployeeDB).filter(EmployeeDB.email == employee_update.email).first()
    # if not, throw error
        if existing:
            raise ValueError("Email bereits vergeben")
    # define updated data as only the fields included in update_employee
    update_data = employee_update.model_dump(exclude_unset=True)
    # for each key given in the update_employee, replace the value
    for key, value in update_data.items():
        setattr(db_employee, key, value)

    # Update the required fields
    db_employee.updated_at = datetime.utcnow()

    try:
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        raise ValueError("Fehler beim aktualisieren")

# DELETE an employee
def delete_employee(db: Session, employee_id: int):
    # define the employee and find him in the database
    db_employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
    # delete the entry and commit the changes

    if db_employee:
        db.delete(db_employee)
        db.commit()
    # return affirmative
        return True
    return False