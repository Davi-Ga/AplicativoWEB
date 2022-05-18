from django.db import models


TIPO_PHONE =[
    ('1','Fixo'),
    ('0','Celular'),
]

class Banco(models.Model):
    
    nome = models.CharField(max_length=250,null=False)
    numero = models.CharField(max_length=250,null=False)
    
    class Meta:
        db_table = "Banco" 
    
    def __str__(self):
        
        return self.numero+" - "+self.nome 
    

class Agencia(models.Model):
    
    id_banco = models.ForeignKey('Banco',on_delete=models.CASCADE)
    endereco = models.CharField(max_length=250,null=False)
    fone = models.DecimalField(max_digits=11,decimal_places=0,unique=True,null=False)
    tipo = models.IntegerField(choices=TIPO_PHONE,null=False)
    fone1 = models.DecimalField(max_digits=11,decimal_places=0,blank=True)
    tipo1 = models.IntegerField(choices=TIPO_PHONE,blank=True)
    agencia = models.CharField(max_length=250,null=False)
    nome_agencia = models.CharField(max_length=250,null=False)
    
    class Meta:
        db_table = "Agencia"
    
    def __str__(self):
        return self.nome_agencia
    

    
