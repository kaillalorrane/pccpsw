from django import forms
from .models import Itempedido

class ItempedidoForm(forms.ModelForm):
    class Meta:
        model = Itempedido
        fields = ['pedido', 'produto', 'quantidade']
        widgets = {
            'pedido': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control', 'id': 'id_produto'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto')
        quantidade = cleaned_data.get('qtd')

        if produto and quantidade:
            if produto.estoque <= 0:
                raise forms.ValidationError(f"O produto '{produto.nome}' está esgotado.")
            if quantidade > produto.estoque:
                raise forms.ValidationError(
                    f"Quantidade solicitada ({quantidade}) é maior que o estoque disponível ({produto.estoque})."
                )

        return cleaned_data        