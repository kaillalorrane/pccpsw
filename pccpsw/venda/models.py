from django.db import models
from usuario.models import Usuario
from estabelecimento.models import Estabelecimento

class Venda(models.Model):
    cliente = models.ForeignKey(Usuario, related_name='compras', on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Usuario, related_name='vendas', on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.pk}"
