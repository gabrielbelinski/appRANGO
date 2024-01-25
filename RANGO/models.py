from django.db import models


# Create your models here.

class Produto(models.Model):
    nome = models.CharField(blank=False, max_length=50)
    preco = models.DecimalField(blank=False, decimal_places=2, max_digits=5, default=0)
    descricao = models.CharField(blank=False, max_length=500)
    quantidade = models.IntegerField(blank=False, default=0)
    disponibilidade = models.BooleanField(blank=False, default=True)
