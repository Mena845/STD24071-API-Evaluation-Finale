from fastapi import FastAPI , HTTPException
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


# c: GET /phones
@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones_db


# d: GET /phones/{id}
@app.get("/phones/{id}", response_model=Phone)
def get_phone(id: int):
    for phone in phones_db:
        if phone.id == id:
            return phone
    raise HTTPException(
        status_code=404,
        detail=f"Phone avec l'id {id} n'existe pas ou n'a pas été trouvé."
    )