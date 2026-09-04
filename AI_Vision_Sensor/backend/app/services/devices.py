from sqlalchemy.orm import Session

from app.database.models import Device


def register_device(db: Session, device):
    new_device = Device(
        device_id=device.device_id,
        device_name=device.device_name,
        ip_address=device.ip_address
    )

    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return new_device