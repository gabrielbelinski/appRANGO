from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.html import format_html

from RANGO.forms import CriaProdutoForm
from RANGO.models import Produto
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
# Create your views here.

class ListaProdutos(ListView):
        model = Produto
        template_name = 'produto_list.html'
        context_object_name = 'produtos'
        list_display = ('nome', 'preco', 'descricao', 'quantidade', 'disponibilidade', 'imagem_tag')

        def imagem_tag(self, obj):
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.imagem.url))

        imagem_tag.short_description = 'Image'

class AtualizaProduto(UpdateView):
    template_name = "produto_update.html"
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy(ListaProdutos)

def criar_produto(request):
    if request.method == 'POST':
        form = CriaProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listaprodutos')
    else:
        form = CriaProdutoForm()
    return render(request, 'produto_create.html', {'form': form})


def index(request):
    return render(request, "index.html")