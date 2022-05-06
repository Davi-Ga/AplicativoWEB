from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import PaginaInicial

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
]