from django.core.exceptions import ValidationError
from django import forms

def nome_validator(value):
        
        if not len(value) > 7:
            raise forms.ValidationError('Por favor insira um nome válido')
        else:
            return value
        