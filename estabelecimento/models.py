from django.db import models
from usuario.models import Usuario

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

