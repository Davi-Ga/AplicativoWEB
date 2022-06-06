from pydoc import getpager
from django import forms
from django.forms import ValidationError
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
        
    def algum_numero(self):
        telefone=self.cleaned_data.get("fone")
        telefone1=self.cleaned_data.get("fone1")
        
        if telefone and telefone1 == "":
            raise forms.ValidationError("Insira algum número de telefone por favor")
        return telefone and telefone1

        