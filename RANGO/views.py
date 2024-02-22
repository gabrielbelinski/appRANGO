from django.http import FileResponse, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

from RANGO.models import Produto, Pedido, ItemPedido
from appRANGO import settings


def index(request):
    return render(request, "index.html")


def lista_produtos(request):
    produtos = Produto.objects.filter(quantidade__gt=0).order_by('preco')
    return render(request, 'produto_list.html', {'produtos': produtos})


def lista_pedidos(request):
    pedidos = Pedido.objects.order_by('-data').filter(concluido=False)
    return render(request, 'pedidos_list.html', {'pedidos': pedidos})


def lista_pedidos_public(request):
    pedidos = Pedido.objects.order_by('-data')
    return render(request, 'pedidos_list_public.html', {'pedidos': pedidos})


def sucesso_pedido(request):
    return render(request, template_name='sucesso_pedido.html')


def adicionar_produtos(request):
    if request.method == 'POST':
        cliente_nome = request.POST['cliente_nome']
        observacoes = request.POST['observacoes']
        produtos_ids = request.POST.getlist('produtos')
        quantidades = {}
        for produto_id in produtos_ids:
            quantidade = int(request.POST['quantidade_' + produto_id])
            if quantidade > 0:
                quantidades[produto_id] = quantidade
        pedido = Pedido.objects.create(cliente_nome=cliente_nome, observacoes=observacoes)
        total = 0
        for produto_id, quantidade in quantidades.items():
            produto = Produto.objects.get(id=produto_id)
            total += produto.preco * quantidade
            produto.quantidade -= quantidade
            produto.save()
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade)
        pedido.total = total
        pedido.save()
        return redirect('RANGO:sucesso_pedido')
    else:
        return redirect('RANGO:lista_produtos')


@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    file = (settings.BASE_DIR / "static" / "favicon.ico").open("rb")
    return FileResponse(file)
