from django import forms
from .models import Produto
from categoria.models import Categoria
from estabelecimento.models import Estabelecimento

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descrição', 'categoria', 'preco', 'unidade', 'estoque', 'estabelecimento']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 100, 'class': 'form-control'}),
            'descrição': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidade': forms.TextInput(attrs={'maxlength': 10, 'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'estabelecimento': forms.Select(attrs={'class': 'form-control'}),
        }
class ProdutoUpdateForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descrição', 'categoria', 'preco', 'unidade', 'estoque', 'estabelecimento']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 100, 'class': 'form-control'}),
            'descrição': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'unidade': forms.TextInput(attrs={'maxlength': 10, 'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'estabelecimento': forms.Select(attrs={'class': 'form-control'}),
        }        