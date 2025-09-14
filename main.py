# Library imports
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# App imports
from database import get_db

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status":"all good and dandy"}