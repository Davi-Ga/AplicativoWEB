from django.views.generic import ListView
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from banco.forms import BancoForm
from banco.forms import AgenciaForm
from banco.models import Agencia

class PaginaInicial(TemplateView):
    template_name = 'banco/home.html'
    
class Adicionar(TemplateView):
    template_name = 'banco/add.html'
    

def adicionarAgencia(request):
    form = AgenciaForm()
    context={
        'form': form
    }
    return render(request,'banco/agencia_add.html',context=context)
    
def adicionarBanco(request):
    form = BancoForm()
    context={
        'form': form
    }
    return render(request,'banco/banco_add.html',context=context)
    