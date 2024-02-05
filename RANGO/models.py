from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(blank=False, max_length=50)
    preco = models.DecimalField(blank=False, decimal_places=2, max_digits=5, default=0)
    descricao = models.CharField(blank=False, max_length=500)
    quantidade = models.IntegerField(blank=False, default=0)
    disponibilidade = models.BooleanField(blank=False, default=True)
    imagem = models.ImageField(upload_to='static/images/imagens_produtos/', blank=True)

class Pedido(models.Model):
    cliente_nome = models.CharField(blank=False, max_length=50)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    total = models.DecimalField(blank=False, decimal_places=2, max_digits=5)
    data = models.DateTimeField(auto_now_add=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=False, default=0)
    preco_unitario = models.DecimalField(blank=False, decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade} unidades"