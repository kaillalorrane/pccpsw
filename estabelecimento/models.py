from django.db import models
from django.contrib.auth.models import User

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

  
