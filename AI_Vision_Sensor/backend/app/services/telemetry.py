from sqlalchemy.orm import Session

from app.database.models import Telemetry

def create_telemetry(db: Session, telemetry):
    new_telemetry = Telemetry(
        device_id = telemetry.device_id,
        uptime = telemetry.uptime,
        free_heap = telemetry.free_heap,
        wifi_rssi = telemetry.wifi_rssi
    )

    db.add(new_telemetry)
    db.commit()
    db.refresh(new_telemetry)

    return new_telemetry
