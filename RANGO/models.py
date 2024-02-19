from django.db import models

# Create your models here.

class Produto(models.Model):

    nome = models.CharField(blank=False, max_length=50)
    preco = models.DecimalField(blank=False, decimal_places=2, max_digits=5, default=0)
    descricao = models.CharField(blank=False, max_length=500)
    quantidade = models.IntegerField(blank=False, default=0)
    imagem = models.ImageField(upload_to='static/images/imagens_produtos/', blank=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente_nome = models.CharField(blank=False, max_length=50)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    total = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    data = models.DateTimeField(auto_now_add=True)
    concluido = models.BooleanField(blank=False, default=False)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.cliente_nome

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return f"{self.produto.nome}"
