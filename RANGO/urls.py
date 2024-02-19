from django.urls import path
from . import views
from RANGO.views import adicionar_produtos, lista_produtos, lista_pedidos, lista_pedidos_public, sucesso_pedido

app_name = 'RANGO'

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionarprodutos/', adicionar_produtos, name='adicionar_produtos'),
    path('listapedidos/', lista_pedidos, name='lista_pedidos'),
    path('listapedidospublic/', lista_pedidos_public, name='lista_pedidos_public'),
    path('sucessopedido/', sucesso_pedido, name='sucesso_pedido'),
    path('listaprodutos/', lista_produtos, name='lista_produtos')
]