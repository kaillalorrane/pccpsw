from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pedido
from .forms import PedidoForm

def index(request):
   pedidos = Pedido.objects.all()
   return render(request, 'pedido/index.html', {'pedidos': pedidos})
def create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/pedido/')
    else:
        form = PedidoForm()
    return render(request, 'pedido/criar.html', {'form': form})

def edit(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/pedido/')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido/atualizar.html', {'form': form})

def delete(request, pedido_id): 
    Pedido.objects.get(id=pedido_id) .delete()

    return HttpResponseRedirect('/pedido/') 

def detail(request, pedido_id):

    pedido = Pedido.objects.get(id=pedido_id)
    return render(request, 'pedido/detalhar.html', {'pedido': pedido})     
