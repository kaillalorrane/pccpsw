from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['user', 'cpf', 'telefone', 'dt_nasc']
        widgets = {
            'senha': forms.PasswordInput(),
        }
    