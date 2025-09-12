from django.db import models
from usuario.models import Usuario
from estabelecimento.models import Estabelecimento

class Pedido(models.Model):

    STATUS = (
        ('Pendente', 'Pendente'),
        ('Em Preparação', 'Em Preparação'),
        ('Entrega em Andamento', 'Entrega em Andamento'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
        
    )
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='vendedor_estabelecimentos')
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    dt_hora = models.DateTimeField(auto_now_add=True, verbose_name='Data e Hora do Pedido')
    status = models.CharField(max_length=20, choices=STATUS, default='Pendente')

    def __str__(self):
        return f'Cliente:{self.cliente.usuario}/Estabelecimento:{self.estabelecimento.nome} ({self.status})'