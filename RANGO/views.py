from django.shortcuts import render
from django.urls import reverse_lazy
from RANGO.forms import CriaProdutoForm

from RANGO.models import Produto
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
# Create your views here.
class ListaProdutos(ListView):
    template_name = "produto_list.html"
    model = Produto
    context_object_name = "produtos"

class AtualizaProduto(UpdateView):
    template_name = "produto_update.html"
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy(ListaProdutos)

class CriarProduto(CreateView):
    template_name = "produto_create.html"
    model = Produto
    form_class = CriaProdutoForm
    sucess_url = reverse_lazy('produto_list.html')
    get_success_url = reverse_lazy('produto_list.html')