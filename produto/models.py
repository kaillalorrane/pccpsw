from django.db import models
from estabelecimento.models import Estabelecimento

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=10)
    estoque = models.IntegerField()
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    categoria = models.ForeignKey('categoria.Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    

