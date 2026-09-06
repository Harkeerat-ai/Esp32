from pydantic import BaseModel


class DeviceRegistration(BaseModel):
    device_id: str
    device_name: str
    ip_address: str

class DeviceResponse(BaseModel):
    device_id: str
    device_name: str
    ip_address: str

    class Config:
        from_attributes = True

class TelemetryCreate(BaseModel):
    device_id: str
    uptime: int
    free_heap: int
    wifi_rssi: int