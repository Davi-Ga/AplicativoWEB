from typing import Optional
from pydantic import BaseModel



# shared properties
class AgencyBase(BaseModel):
    id: Optional[int] = None
    id_banco: Optional[str] = None
    endereco: Optional[str] = None
    fone: Optional[int] = None
    tipo: Optional[int] = None
    fone1: Optional[int] = None
    tipo1: Optional[int] = None
    agencia: Optional[str] = None
    nome_agencia: Optional[str] = None

# this will be used to validate data while creating a Agency
class AgencyCreate(AgencyBase):
    id: int
    id_banco: str
    endereco: str
    fone: int
    tipo: int
    fone1: int
    tipo1: int
    agencia: str
    nome_agencia: str

# this will be used to format the response to not to have id,owner_id etc
class ShowAgency(AgencyBase):
    id: int
    id_banco: str
    endereco: str
    fone: int
    tipo: int
    fone1:  Optional[int]
    tipo1: Optional[int]
    agencia: str
    nome_agencia: str


    class Config:  # to convert non dict obj to json
        orm_mode = True