from django import forms

from banco.models import Agencia
from banco.models import Banco

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'

class AgenciaForm(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = '__all__'