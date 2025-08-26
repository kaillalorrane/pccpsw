from django import forms
from .models import Estabelecimento

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['nome', 'responsavel', 'cnpj','telefone', 'rua', 'numero', 'bairro']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'maxlength': 18, 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'maxlength': 100, 'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'maxlength': 10, 'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'maxlength': 50, 'class': 'form-control'}),
        }
class EstabelecimentoUpdateForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['nome', 'responsavel', 'cnpj', 'telefone', 'rua', 'numero', 'bairro']
        widgets = {
            'nome': forms.TextInput(attrs={'maxlength': 30, 'class': 'form-control'}),
            'responsavel': forms.Select(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'maxlength': 18, 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'maxlength': 100, 'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'maxlength': 10, 'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'maxlength': 50, 'class': 'form-control'}),
        }              