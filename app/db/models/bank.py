from pandas import notnull
from db.base_class import Base
from sqlalchemy import BigInteger, Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Bank(Base):
    __tablename__ = "Bank"
    id = Column(Integer, primary_key=True, index=True, notnull=True)
    nome = Column(String, unique=False, nullable=False, notnull=True)
    numero = Column(String, nullable=False, unique=False, index=True, notnull=True)