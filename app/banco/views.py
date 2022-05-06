from django.views.generic import ListView
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from banco.models import Agencia

class PaginaInicial(TemplateView):
    template_name = 'banco/home.html'
    
