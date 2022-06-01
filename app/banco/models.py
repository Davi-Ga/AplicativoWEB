from django.db import models
from django.core.validators import RegexValidator
from .validators import nome_validator


TYPE_PHONE =[
    ('1','Fixo'),
    ('0','Celular'),
]



class Banco(models.Model):
    
    nome = models.CharField(max_length=250,null=False,unique=True,validators=[nome_validator])
    numero = models.CharField(max_length=250,null=False,unique=True,)
     
    class Meta:
        db_table = "Banco" 
        
    
    
    def __str__(self):
        
        return self.numero+" - "+self.nome 
    

class Agencia(models.Model):
    
    id_banco = models.ForeignKey('Banco',on_delete=models.CASCADE)
    endereco = models.CharField(max_length=250,null=False)
    fone = models.BigIntegerField(unique=True,blank=True,verbose_name="Telefone")
    tipo = models.IntegerField(choices=TYPE_PHONE,blank=True)
    fone1 = models.BigIntegerField(blank=True)
    tipo1 = models.IntegerField(choices=TYPE_PHONE,blank=True)
    agencia = models.CharField(max_length=250,null=False)
    nome_agencia = models.CharField(max_length=250,null=False)
    
    class Meta:
        db_table = "Agencia"
    
    def __str__(self):
        return self.nome_agencia
    

    
