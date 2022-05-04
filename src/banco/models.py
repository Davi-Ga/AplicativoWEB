from banco import db


class Banco(db.Model):
    __tablename__='banco'
    
    id=db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    nome=db.Column(db.String(200))
    numero=db.Column(db.String(200))

    def __init__(self,nome,numero):
        self.nome=nome
        self.numero=numero
        
class Agencia(db.Model):
    TIPO_PHONE=[
        (u'0',u'Celular'),
        (u'1',u'Fixo'),
    ]
    __tablename__='agencia'

    id=db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
    id_banco=db.Column(db.Integer, db.ForeignKey('Banco.id'),nullable=False)
    endereco=db.Column(db.String(200))
    tipo=db.Column(ChoiceType=(TIPO_PHONE))
    fone=db.Column(db.BigInteger)
    tipo1=db.Column(db.Integer,nullable=True)
    fone1=db.Column(db.BigInteger,nullable=True)
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
  
agencia=type      

               
db.create_all()
