from django.shortcuts import redirect, render
from banco.forms import BancoForm
from banco.forms import AgenciaForm
from banco.models import Agencia
from banco.models import Banco
from django.core.paginator import Paginator


def pagina_inicial(request):
    return render(request,'banco/home.html')
    
#CRUD do Banco

#CREATE  
def adicionar_banco(request):
    if request.method == 'GET':
        form = BancoForm()
        context={
            'form': form
        }
        return render(request,'banco/banco_adicionar.html',context=context)
    
    else:
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            form = BancoForm()
            
        context={
        'form': form
        }
        return render(request,'banco/banco_adicionar.html',context=context)
     
#READ
def listar_banco(request):
    bancos_list=Banco.objects.all()
    paginator= Paginator(bancos_list,3)
    
    page=request.GET.get('page')
    
    bancos=paginator.get_page(page)
    context={
        'bancos': bancos
    }
    return render(request,'banco/banco_list.html',context=context)
    
#UPDATE
def alterar_banco(request,banco_id):
    banco_id=int(banco_id)
    try:
        bancos=Banco.objects.get(id=banco_id)
    except Banco.DoesNotExist:
        return redirect('listarBanco')
    form=BancoForm(request.POST or None, instance=bancos)
    
    if form.is_valid():
        form.save()
        return redirect('listarBanco')
    
    context={
        'form': form
    }
    return render(request,'banco/banco_adicionar.html',context=context)
    
#DELETE
def deletar_banco(banco_id):
    banco_id=int(banco_id)  
    
#CRUD da Agência

#CREATE
def adicionar_agencia(request):
    if request.method == 'GET':
        form = AgenciaForm()
        context={
            'form': form
        }
        return render(request,'banco/agencia_adicionar.html',context=context)
    
    else:
        form=AgenciaForm(request.POST)
        if form.is_valid():
            form.save()
            form = AgenciaForm()
            
        context={
        'form': form
        }
        return render(request,'banco/agencia_adicionar.html',context=context)

#READ
def listar_agencia(request):
    agencias= Agencia.objects.all()
    context={
        'agencias': agencias
    }
    return render(request,'banco/agencia_list.html',context=context)

#UPDATE
def alterar_agencia(request,agencia_id):
    agencia_id=int(agencia_id)
    try:
        agencias = Agencia.objects.get(id = agencia_id)
    except Agencia.DoesNotExist:
        return redirect('listarAgencia')
    form = AgenciaForm(request.POST or None, instance=agencias)
    
    if form.is_valid():
        form.save()
        return redirect('listarAgencia')
    
    context={
        'form': form
    }
    return render(request,'banco/agencia_adicionar.html',context=context)

#DELETE
def deletar_agencia(request,agencia_id):
    agencia_id=int(agencia_id)
    try:
        agencias=Agencia.objects.get(id=agencia_id)
    except Agencia.DoesNotExist:
        return redirect('listarAgencia')
        
    agencias.delete()
    return redirect('listarAgencia')