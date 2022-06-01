from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from banco.forms import BancoForm
from banco.forms import AgenciaForm
from banco.models import Agencia
from banco.models import Banco

def pagina_inicial(request):
    return render(request,'banco/home.html')
    
    
def adicionar_agencia(request):
    if request.method == "GET":
        form = AgenciaForm()
        context={
            'form': form
        }
        return render(request,'banco/agencia_adicionar.html',context=context)
    
    else:
        form=AgenciaForm(request.POST)
        if form.is_valid():
            agencia = form.save()
            form = AgenciaForm()
            
        context={
        'form': form
        }
        return render(request,'banco/agencia_adicionar.html',context=context)
            
    
def adicionar_banco(request):
    if request.method == "GET":
        form = BancoForm()
        context={
            'form': form
        }
        return render(request,'banco/banco_adicionar.html',context=context)
    
    else:
        form = BancoForm(request.POST)
        if form.is_valid():
            banco = form.save()
            form = BancoForm()
            
        context={
        'form': form
        }
        return render(request,'banco/banco_adicionar.html',context=context)
    
def listar_agencia(request):
    agencias= Agencia.objects.all()
    context={
        'agencias': agencias
    }
    return render(request,'banco/agencia_list.html',context=context)

def listar_banco(request):
    bancos=Banco.objects.all()
    context={
        'bancos': bancos
        }
    return render(request,'banco/banco_list.html',context=context)
    
    