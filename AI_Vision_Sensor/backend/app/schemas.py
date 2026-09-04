from pydantic import BaseModel


class DeviceRegistration(BaseModel):
    device_id: str
    device_name: str
    ip_address: str