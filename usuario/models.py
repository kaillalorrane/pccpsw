from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    dt_nasc = models.DateField()
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

   
