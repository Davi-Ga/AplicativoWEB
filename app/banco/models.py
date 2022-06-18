from django.db import models
from django.core.validators import RegexValidator
from .validators import nome_validator

TYPE_PHONE =[
    ('0','Fixo'),
    ('1','Celular'),
]

TYPE_PERMITIONS=[
    ('m','Moderador'),
    ('c','Comum')
]

class Banco(models.Model):
    
    nome = models.CharField(max_length=250,null=False,unique=True,validators=[nome_validator])
    numero = models.CharField(max_length=250,null=True,unique=True,)
     
    class Meta:
        db_table = "Banco" 
           
    def __str__(self):
        
        return self.numero+" - "+self.nome 
    

class Agencia(models.Model):
    
    id_banco = models.ForeignKey('Banco',on_delete=models.CASCADE)
    endereco = models.CharField(max_length=100,null=False)
    fone = models.BigIntegerField(unique=True,blank=True)
    tipo = models.CharField(max_length=1,choices=TYPE_PHONE,blank=True)
    fone1 = models.BigIntegerField(blank=True)
    tipo1 = models.CharField(max_length=1,choices=TYPE_PHONE,blank=True)
    agencia = models.CharField(max_length=100,null=False)
    nome_agencia = models.CharField(max_length=100,null=False)
    
    class Meta:
        db_table = "Agencia"
    
    def __str__(self):
        return self.nome_agencia

    def numero(self,*args,**kwargs):
        fone=self.cleaned_data.get('fone')
        fone1=self.cleaned_data.get('fone1')
    