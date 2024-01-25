from django import forms

from RANGO.models import Produto


class CriaProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto

        fields = [
            'nome',
            'descricao',
            'preco',
            'quantidade',
            'disponibilidade'
        ]

