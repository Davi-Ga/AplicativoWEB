from typing import Optional
from pydantic import BaseModel



# shared properties
class BankBase(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    numero: Optional[str] = None

# this will be used to validate data while creating a Bank
class BankCreate(BankBase):
    id: Optional[int] = None
    nome: Optional[str] = None
    numero: Optional[str] = None

# this will be used to format the response to not to have id,owner_id etc
class Showbank(BankBase):
    id: Optional[int] = None
    nome: Optional[str] = None
    numero: Optional[str] = None


    class Config:  # to convert non dict obj to json
        orm_mode = True