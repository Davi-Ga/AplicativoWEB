from django.test import TestCase
import unittest
from .models import Agencia

class TestesApp(unittest.TestCase):
    
    def teste_aceitacao_agencia(self):
        Agencia.objects.create(endereco='Av.Madre Maria Dos Anjos',fone=62993794033,tipo='1',fone1=62993794033,tipo1='1',agencia='23a',nome_agencia='Agencia BrasilQ')
