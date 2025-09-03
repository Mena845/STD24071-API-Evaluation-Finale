from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# a: GET /health
@app.get("/health")
def health():
    return "Ok"


class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    id: int
    brand: str
    model: str
    characteristics: Characteristic

phones_db: List[Phone] = []

# b: POST /phones
@app.post("/phones", status_code=201, response_model=Phone)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return phone