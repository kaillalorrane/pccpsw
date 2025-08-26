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