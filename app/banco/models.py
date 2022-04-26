from django.db import models


class Agencia(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    id_banco = models.IntegerField(null=False)
    endereco = models.CharField(max_length=250)
    fone = models.BigIntegerField()
    tipo = models.IntegerField()
    fone1 = models.BigIntegerField(blank=True)
    tipo1 = models.IntegerField(blank=True)
    agencia = models.CharField(max_length=250)
    nome_agencia = models.CharField(max_length=250)
    
class Banco(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nome = models.CharField(max_length=250,null=False)
    numero = models.CharField(max_length=250)
    
def __str__(self):
        return self.description
    
