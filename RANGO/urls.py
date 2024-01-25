from django.urls import path
from . import views
from RANGO.views import *

app_name = 'RANGO'

urlpatterns = [
    path('listaprodutos/', ListaProdutos.as_view(), name='lista_produtos'),
    path('criaprodutos/', CriarProduto.as_view(), name='cria_produto'),
]