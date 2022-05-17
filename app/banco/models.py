from django.db import models


TIPO_PHONE =[
    ('1','Fixo'),
    ('0','Celular'),
]

class Banco(models.Model):
    

    nome = models.CharField(max_length=250,null=False)
    numero = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome


class Agencia(models.Model):
    
    
    id_banco = models.ForeignKey('Banco',on_delete=models.CASCADE)
    endereco = models.CharField(max_length=250)
    fone = models.CharField(max_length=11,unique=True)
    tipo = models.IntegerField(choices=TIPO_PHONE)
    fone1 = models.CharField(max_length=11,blank=True)
    tipo1 = models.IntegerField(choices=TIPO_PHONE,blank=True)
    agencia = models.CharField(max_length=250)
    nome_agencia = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome_agencia
    

    
