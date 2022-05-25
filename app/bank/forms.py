from django import forms

from bank.models import Agency
from bank.models import Bank

class BankForm(forms.ModelForm):
    
    class Meta:
        model = Bank
        fields = '__all__'

class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'