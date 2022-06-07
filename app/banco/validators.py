from django.core.exceptions import ValidationError
from django import forms

def nome_validator(value):
    if not len(value) > 7:
        raise forms.ValidationError('Insira um nome válido')
    else:
        return value

