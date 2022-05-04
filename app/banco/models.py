from django.db import models

TIPO_PHONE =[
    ('0','Fixo'),
    ('1','Celular'),
]

class Banco(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nome = models.CharField(max_length=250,null=False)
    numero = models.CharField(max_length=250)
    
    def __init__(self,nome,numero):
        self.nome=nome
        self.numero=numero


class Agencia(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    id_banco = models.ForeignKey(Banco.id,null=False)
    endereco = models.CharField(max_length=250)
    fone = models.BigIntegerField(max_length=11,unique=True)
    tipo = models.IntegerField(choices=TIPO_PHONE,max_length=1,min_length=0)
    fone1 = models.BigIntegerField(blank=True,max_length=11)
    tipo1 = models.IntegerField(choices=TIPO_PHONE,max_length=1,min_length=0)
    agencia = models.CharField(max_length=250)
    nome_agencia = models.CharField(max_length=250)
    
    def __init__(self, id_banco,endereco,tipo,fone,tipo1,fone1,agencia,nome_agencia):
        self.id_banco=id_banco
        self.endereco=endereco
        self.tipo=tipo
        self.fone=fone
        self.tipo1=tipo1
        self.fone1=fone1
        self.agencia=agencia
        self.nome_agencia=nome_agencia

    

    
