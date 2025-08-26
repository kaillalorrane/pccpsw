from django.db import models
from pedido.models import Pedido
from produto.models import Produto

class Itempedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=10, decimal_places=2, editable=False, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, blank=True)

    def __str__(self):
        return f"{self.qtd}x {self.produto.nome} (R${self.preco})"

    def save(self, *args, **kwargs):
        if self.produto:
            self.preco = self.produto.preco

        self.total = self.preco * self.qtd
        
        super().save(*args, **kwargs)