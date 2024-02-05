from django.urls import path
from . import views
from RANGO.views import *

app_name = 'RANGO'

urlpatterns = [
    path('', views.index, name='index'),
    path('listaprodutos/', ListaProdutos.as_view(), name='lista_produtos'),
    path('criaprodutos/', views.criar_produto, name='cria_produto')
]