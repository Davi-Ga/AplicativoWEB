from django import forms

from banco.models import Agencia

class AgenciaForm(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = '__all__'