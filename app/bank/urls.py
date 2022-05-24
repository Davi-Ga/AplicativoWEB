from django import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from bank import views


urlpatterns = [
    path('',views.Adicionar.as_view(),name='adicionar'),
    path('agency/',views.addAgency,name='addAgency' ),
    path('bank/',views.addBank,name='addBank'),
]