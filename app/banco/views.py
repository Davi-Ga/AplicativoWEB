from django.shortcuts import redirect, render
from django import forms
from banco.forms import AgenciaForm,BancoForm,CadastroUsuarioForm
from banco.models import Agencia,Banco
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def pagina_inicial(request):
    return render(request,'banco/home.html')



def pagina_login(request):
    if request.user.is_authenticated:
        return redirect('paginaInicial')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')
            
            user = authenticate(request,username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect('paginaInicial')
            else:
                return forms.ValidationError("Usuário ou senha estão incorretos")
        context={
            
        }
        return render(request,'usuario/login.html',context=context)
   
def deslogar(request):
    logout(request) 
    return redirect('paginaLogin')

def pagina_registro(request):
    if request.user.is_authenticated:
        return redirect('paginaInicial')
    else:
        form = CadastroUsuarioForm()
        if request.method=='POST':
            form = CadastroUsuarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('paginaLogin')
                
        context={
            'form':form
        }
        return render(request,'usuario/registro.html',context=context)

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
    paginator= Paginator(bancos_list,15)
    
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
    
    try:
        bancos=Banco.objects.get(id=banco_id)
    except Banco.DoesNotExist:
        return redirect('listarBanco')
    
    bancos.delete()
    return redirect('listarBanco')
#CRUD da Agência

#CREATE
def adicionar_agencia(request):
    if request.method == 'GET':
        form = AgenciaForm()
        result= Banco.objects.all
        context={
            'form': form,
            'bancos': result
        }
        return render(request,'banco/agencia_adicionar.html',context=context)
    
    else:
        form=AgenciaForm(request.POST)
        result= Banco.objects.all
        if form.is_valid():
            form.save()
            form = AgenciaForm()
            
        context={
            'form': form,
            'bancos': result
        }
        return render(request,'banco/agencia_adicionar.html',context=context)

#READ
def listar_agencia(request):
    agencias_list= Agencia.objects.all()
    paginator=Paginator(agencias_list,10)
    
    page=request.GET.get('page')
    
    agencias=paginator.get_page(page)
    context={
        'agencias': agencias
    }
    return render(request,'banco/agencia_list.html',context=context)

#UPDATE
@login_required
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
@login_required
def deletar_agencia(agencia_id):
    agencia_id=int(agencia_id)
    try:
        agencias=Agencia.objects.get(id=agencia_id)
    except Agencia.DoesNotExist:
        return redirect('listarAgencia')
        
    agencias.delete()
    return redirect('listarAgencia')