from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.schemas import DeviceRegistration, DeviceResponse
from app.services.devices import register_device
from app.database.models import Device


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model= DeviceResponse)
def register(
    device: DeviceRegistration,
    db: Session = Depends(get_db)
):
    return register_device(db, device)


@router.get("/", response_model= list[DeviceResponse])
def get_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()

@router.get("/{device_id}", response_model=DeviceResponse)
def get_device(
    device_id: str,
    db: Session = Depends(get_db)
):
    device = db.query(Device).filter(Device.device_id == device_id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device