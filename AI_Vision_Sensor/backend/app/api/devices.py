from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.schemas import DeviceRegistration
from app.services.devices import register_device


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    device: DeviceRegistration,
    db: Session = Depends(get_db)
):
    return register_device(db, device)


@router.get("/")
def get_devices():
    return {
        "devices": []
    }