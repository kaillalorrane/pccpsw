from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'username', 'cpf', 'telefone', 'dt_nasc', 'rua', 'numero', 'bairro', 'password1', 'password2']

        
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'telefone', 'dt_nasc', 'rua', 'numero', 'bairro']
