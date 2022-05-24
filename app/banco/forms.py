from django import forms

from banco.models import Agencia
from banco.models import Banco

class BancoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Nome do Banco"}))
    numero = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Nome do Banco"}))
    
    class Meta:
        model = Banco
        fields = ['nome','numero']

class AgenciaForm(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = '__all__'