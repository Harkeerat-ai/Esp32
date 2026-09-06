from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

from app.database.connection import Base

class Device(Base):
    __tablename__ = "devices"

    device_id = Column(String, primary_key=True)
    device_name = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String, nullable = False)
    uptime = Column(Integer, nullable= False)
    free_heap = Column(Integer, nullable= False)
    wifi_rssi = Column(Integer, nullable= False)
    timestamp = Column(DateTime, default= datetime.utcnow)
