from django.shortcuts import render, redirect
from RANGO.models import Produto, Pedido, ItemPedido

def index(request):
    return render(request, "index.html")

def lista_produtos(request):
    produtos = Produto.objects.filter(quantidade__gt=0)
    return render(request, 'produto_list.html', {'produtos': produtos})

def lista_pedidos(request):
    pedidos = Pedido.objects.filter(concluido=False)
    return render(request, 'pedidos_list.html', {'pedidos': pedidos})

def adicionar_produtos(request):
    if request.method == 'POST':
        produtos_ids = request.POST.getlist('produtos')
        quantidades = {}
        for produto_id in produtos_ids:
            quantidade = int(request.POST['quantidade_' + produto_id])
            if quantidade > 0:
                quantidades[produto_id] = quantidade
        pedido = Pedido.objects.create(cliente_nome='Nome do cliente')
        total = 0
        for produto_id, quantidade in quantidades.items():
            produto = Produto.objects.get(id=produto_id)
            preco_unitario = produto.preco
            total += preco_unitario * quantidade
            produto.quantidade -= quantidade
            produto.save()
            ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=quantidade, preco_unitario=preco_unitario)
        pedido.total = total
        pedido.save()
        return redirect('RANGO:lista_pedidos')
    else:
        return redirect('RANGO:lista_produtos')