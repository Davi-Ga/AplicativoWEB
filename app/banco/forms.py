from pydoc import getpager
from django import forms
from django.forms import ValidationError

from banco.models import Agencia
from banco.models import Banco
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = '__all__'
        
class AgenciaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AgenciaForm, self).__init__(*args, **kwargs)
        self.fields['idbanco'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = Agencia
        fields = '__all__'
        
class CadastroUsuarioForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(CadastroUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={
            'username':None,
            'password1':None,
            'password2':None,
        }
        

        