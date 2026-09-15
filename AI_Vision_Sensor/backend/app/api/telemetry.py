from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models import Telemetry
from app.schemas import TelemetryCreate, TelemetryResponse
from app.services.telemetry import create_telemetry

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def receive_telemetry(telemetry: TelemetryCreate, db: Session = Depends(get_db)):
    return create_telemetry(db, telemetry)

@router.get("/", response_model=list[TelemetryResponse])
def get_telemetry(db: Session = Depends(get_db)):
    return db.query(Telemetry).all()

@router.get("/{device_id}", response_model = list[TelemetryResponse])
def get_device_telemetry(device_id: str, db: Session = Depends(get_db)):
    return db.query(Telemetry).filter(Telemetry.device_id == device_id).all()