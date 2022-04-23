from pandas import notnull
from db.base_class import Base
from sqlalchemy import BigInteger, Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Agencia(Base):
    __tablename__ = "Agencia"
    id = Column(Integer, primary_key=True, index=True, notnull=True)
    id_banco = Column(String, unique=False, nullable=False, notnull=True)
    endereco = Column(String, nullable=False, unique=False, index=True)
    fone = Column(BigInteger, nullable=False)
    tipo = Column(Integer, nullable=False)
    fone1 = Column(BigInteger, nullable=False)
    tipo1 = Column(Integer, default=False)
    agencia = Column(String, notnull=True)
    nome_agencia = Column(String, nullable=False)