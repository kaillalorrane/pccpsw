from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'vendedor', 'estabelecimento', 'status']
        widgets = {
            'cliente': forms.Select(attrs={'maxlength': 30, 'class': 'form-control'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'estabelecimento': forms.Select(attrs={'maxlength': 18, 'class': 'form-control'}),
            'status': forms.Select(attrs={'maxlength': 20, 'class': 'form-control'}),
        }