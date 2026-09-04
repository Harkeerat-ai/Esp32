from sqlalchemy import Column, String

from app.database.connection import Base

class Device(Base):
    __tablename__ = "devices"

    device_id = Column(String, primary_key=True)
    device_name = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    