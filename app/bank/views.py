from django.views.generic import ListView
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from bank.forms import BankForm
from bank.forms import AgencyForm
from bank.models import Agency

class PaginaInicial(TemplateView):
    template_name = 'bank/home.html'
    
class Adicionar(TemplateView):
    template_name = 'bank/add.html'
    

def addAgency(request):
    if request.method == "GET":
        form = AgencyForm()
        context={
            'form': form
        }
        return render(request,'bank/agency_add.html',context=context)
    
    else:
        form=AgencyForm(request.POST)
        if form.is_valid():
            agency = form.save()
            form = AgencyForm()
            
        context={
        'form': form
        }
        return render(request,'bank/agency_add.html',context=context)
            
    
def addBank(request):
    if request.method == "GET":
        form = BankForm()
        context={
            'form': form
        }
        return render(request,'bank/bank_add.html',context=context)
    
    else:
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save()
            form = BankForm()
            
            context={
            'form': form
        }
        return render(request,'bank/bank_add.html',context=context)
    