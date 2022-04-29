from config import db
from flask_sqlalchemy import SQLAlchemy

TIPO_PHONE=[
    ('0','Celular'),
    ('1','Fixo'),
]

class Agencia(db.Model):
    __tablename__ = 'Agencia'

    id = db.Column(db.Integer, primary_key=True,null=False,autoincrement=True)
    id_banco = db.Column(db.String(),null=False)
    endereco = db.Column(db.String())
    tipo = db.Column(db.Integer,choice=TIPO_PHONE)
    fone = db.Column(db.String())
    tipo1 = db.Column(db.Integer,choice=TIPO_PHONE)
    fone1 = db.Column(db.String())
    agencia = db.Column(db.String())
    nome_agencia = db.Column(db.String())
    

    def __init__(self, id_banco,endereco,tipo,fone,tipo1,fone1,agencia,nome_agencia):
        self.id_banco = id_banco
        self.endereco = endereco
        self.tipo = tipo
        self.fone=fone
        self.tipo1=tipo1
        self.fone1=fone1
        self.agencia=agencia
        self.nome_agencia=nome_agencia

    