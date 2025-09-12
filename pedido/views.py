from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pedido
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required, permission_required   

@login_required
@permission_required('pedido.view_pedido', raise_exception=True)
def index(request):
   pedidos = Pedido.objects.all()
   return render(request, 'pedido/index.html', {'pedidos': pedidos})

@login_required
@permission_required('pedido.add_pedido', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/pedido/')
    else:
        form = PedidoForm()
    return render(request, 'pedido/criar.html', {'form': form})

@login_required
@permission_required('pedido.change_pedido', raise_exception=True)
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

@login_required
@permission_required('pedido.delete_pedido', raise_exception=True)
def delete(request, pedido_id): 
    Pedido.objects.get(id=pedido_id) .delete()

    return HttpResponseRedirect('/pedido/') 

@login_required
@permission_required('pedido.view_pedido', raise_exception=True)
def detail(request, pedido_id):

    pedido = Pedido.objects.get(id=pedido_id)
    return render(request, 'pedido/detalhar.html', {'pedido': pedido})     
