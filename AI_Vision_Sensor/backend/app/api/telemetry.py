from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.schemas import TelemetryCreate
from app.services.telemetry import create_telemetry

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def receive_telemetry(telemetry: TelemetryCreate, db: Session = Depends(get_db)):
    return create_telemetry(db, telemetry)