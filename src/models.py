from config import db
from flask_sqlalchemy import SQLAlchemy

TIPO_PHONE=[
    ('0','Celular'),
    ('1','Fixo'),
]

class Agencia(db.Model):
    __tablename__='Agencia'

    id=db.Column(db.Integer,primary_key=True,null=False,autoincrement=True)
    id_banco=db.Column(db.String(200),null=False)
    endereco=db.Column(db.String(200))
    tipo=db.Column(db.Integer,choice=TIPO_PHONE)
    fone=db.Column(db.String(200))
    tipo1=db.Column(db.Integer,choice=TIPO_PHONE,nullable=True)
    fone1=db.Column(db.String(200),nullable=True)
    agencia=db.Column(db.String(200))
    nome_agencia=db.Column(db.String(200))
    
    def __init__(self, id_banco,endereco,tipo,fone,tipo1,fone1,agencia,nome_agencia):
        self.id_banco=id_banco
        self.endereco=endereco
        self.tipo=tipo
        self.fone=fone
        self.tipo1=tipo1
        self.fone1=fone1
        self.agencia=agencia
        self.nome_agencia=nome_agencia
        
        
class Banco(db.Model):
    __tablename__='Banco'
    
    id=db.Column(db.Integer,primary_key=True,null=False,autoincrement=True)
    nome=db.Coumn(db.String(200))
    numero=db.Column(db.String(200))

    def __init__(self,nome,numero):
        self.nome=nome
        self.numero=numero

db.create_all()