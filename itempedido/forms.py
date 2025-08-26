from django import forms
from .models import Itempedido

class ItempedidoForm(forms.ModelForm):
    class Meta:
        model = Itempedido
        fields = ['pedido', 'produto', 'qtd']
        widgets = {
            'pedido': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control', 'id': 'id_produto'}),
            'qtd': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto')
        qtd = cleaned_data.get('qtd')

        if produto and qtd:
            if produto.estoque <= 0:
                raise forms.ValidationError(f"O produto '{produto.nome}' está esgotado.")
            if qtd > produto.estoque:
                raise forms.ValidationError(
                    f"Quantidade solicitada ({qtd}) é maior que o estoque disponível ({produto.estoque})."
                )

        return cleaned_data        