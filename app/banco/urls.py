from django import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from banco import views


urlpatterns = [
    
    path('agencia/',views.adicionar_agencia,name='adicionarAgencia' ),
    path('banco/',views.adicionar_banco,name='adicionarBanco'),
    
]