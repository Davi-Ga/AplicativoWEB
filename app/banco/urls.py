from django import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from banco import views


urlpatterns = [
    path('',views.Adicionar.as_view(),name='adicionar'),
    path('agencia/',views.adicionarAgencia,name='adicionarAgencia' ),
    path('banco/',views.adicionarBanco,name='adicionarBanco'),
]