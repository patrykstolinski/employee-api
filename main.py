# Library imports
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# App imports
from database import get_db
from models import Employee, EmployeeCreate, EmployeeUpdate
import crud

app = FastAPI(
    title = "Employee Management API",
    description = "Adding, reading, updating and deleting employees from Postgres DB.",
    version = "1.0"
)

@app.get("/health")
def health_check():
    return {"status":"all good and dandy"}


# Create employee
@app.post("/employees", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee_endpoint(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        db_employee = crud.create_employee(db = db, employee = employee)
        return db_employee
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Read all employees

# Read one employee

# Update employee

# Delete employee


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)