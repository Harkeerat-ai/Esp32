from fastapi import FastAPI

from app.api import devices
from app.database.connection import Base,engine
from app.database.models import Device

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Smart Camera Station API is running"}

app.include_router(
    devices.router,
    prefix= "/api/devices"
)
