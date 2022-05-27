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
    
def listarAgencia(request):
    agencias= Agencia.objects.all()
    return (request,'banco/agencia_list.html',{'Agencias':agencias})
    

def adicionarAgencia(request):
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
            
    
def adicionarBanco(request):
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
    