from django.urls import path
from . import views
from RANGO.views import adicionar_produtos, lista_produtos, lista_pedidos

app_name = 'RANGO'

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionarprodutos/', adicionar_produtos, name='adicionar_produtos'),
    path('listapedidos/', lista_pedidos, name='lista_pedidos'),
    path('listaprodutos/', lista_produtos, name='lista_produtos')
]