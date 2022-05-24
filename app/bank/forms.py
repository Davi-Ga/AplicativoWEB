from django import forms

from bank.models import Agency
from bank.models import Bank

class BankForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Bank Name"}))
    number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Bank Number"}))
    
    class Meta:
        model = Bank
        fields = ['name','number']

class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'