from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = 'banco/index.html'