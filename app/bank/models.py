from django.db import models


TYPE_PHONE =[
    ('1','Landline phone'),
    ('0','Mobile phone'),
]

class Bank(models.Model):
    
    name = models.CharField(max_length=250,null=False,unique=True)
    number = models.CharField(max_length=250,null=False,unique=True)
    
    class Meta:
        db_table = "Bank" 
    
    def __str__(self):
        
        return self.number+" - "+self.name 
    

class Agency(models.Model):
    
    bank_id = models.ForeignKey('Bank',on_delete=models.CASCADE)
    address = models.CharField(max_length=250,null=False)
    phone = models.BigIntegerField(unique=True,null=False)
    phonetype = models.IntegerField(choices=TYPE_PHONE,null=False)
    phone1 = models.BigIntegerField(blank=True)
    phonetype1 = models.IntegerField(choices=TYPE_PHONE,blank=True)
    agency = models.CharField(max_length=250,null=False)
    agency_name = models.CharField(max_length=250,null=False)
    
    class Meta:
        db_table = "Agency"
    
    def __str__(self):
        return self.agency_name
    

    
