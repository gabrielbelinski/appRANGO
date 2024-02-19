from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from RANGO.models import Produto, Pedido, ItemPedido


# Register your models here.

class ListaProdutos(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "quantidade", "imagem_tag", "edit_produto", "remove_produto")

    def imagem_tag(self, obj):
        url = obj.imagem.url
        return mark_safe(f'<a href="{url}" target="_blank"><img src="{url}" width="100" height="100" /></a>')

    imagem_tag.short_description = 'Imagem'

    def edit_produto(self, obj):
        url = reverse('admin:RANGO_produto_change', args=[obj.id])
        return mark_safe(f'<a href="{url}" target="_blank">Editar</a>')

    edit_produto.short_description = 'Editar'

    def remove_produto(self, obj):
        url = reverse('admin:RANGO_produto_delete', args=[obj.id])
        return mark_safe(f'<a href="{url}" target="_blank">Deletar</a>')

    remove_produto.short_description = 'Deletar'


admin.site.register(Produto, ListaProdutos)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido


class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ('id', 'cliente_nome', 'total', 'data', 'concluido', 'edit_pedido', 'remove_pedido')
    list_filter = ('concluido',)
    search_fields = ('cliente_nome',)

    def edit_pedido(self, obj):
        url = reverse('admin:RANGO_pedido_change', args=[obj.id])
        return mark_safe(f'<a href="{url}" target="_blank">Editar</a>')

    edit_pedido.short_description = 'Editar'

    def remove_pedido(self, obj):
        url = reverse('admin:RANGO_pedido_delete', args=[obj.id])
        return mark_safe(f'<a href="{url}" target="_blank">Deletar</a>')

    remove_pedido.short_description = 'Deletar'


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)

