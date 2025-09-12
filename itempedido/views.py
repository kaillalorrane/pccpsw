from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from produto.models import Produto
from pedido.models import Pedido
from .models import Itempedido
from .forms import ItempedidoForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('itempedido.view_itempedido', raise_exception=True)
def index(request):
   itempedidos = Itempedido.objects.all()
   return render(request, 'itempedido/index.html', {'itempedidos': itempedidos})

@login_required
@permission_required('itempedido.add_itempedido', raise_exception=True)
def create(request): 
    if request.method == 'POST':
        form = ItempedidoForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/itempedido/')
            except ValueError as e:
                # Captura o erro vindo do save() e adiciona no formulário
                form.add_error(None, str(e))
    else:
        form = ItempedidoForm()
    
    return render(request, 'itempedido/criar.html', {'form': form})

@login_required
@permission_required('itempedido.change_itempedido', raise_exception=True)
def edit(request, itempedido_id):
    itempedido = Itempedido.objects.get(id=itempedido_id)
    if request.method == 'POST':
        form = ItempedidoForm(request.POST, instance=itempedido)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/itempedido/')
    else:
        form = ItempedidoForm(instance=itempedido)
    return render(request, 'itempedido/atualizar.html', {'form': form})

@login_required
@permission_required('itempedido.delete_itempedido', raise_exception=True)
def delete(request, itempedido_id):
    Itempedido.objects.get(id=itempedido_id) .delete()

    return HttpResponseRedirect('/itempedido/')

@login_required
@permission_required('itempedido.view_itempedido', raise_exception=True)
def detail(request, itempedido_id):

    itempedido = Itempedido.objects.get(id=itempedido_id)
    return render(request, 'itempedido/detalhar.html', {'itempedido': itempedido})

@login_required
@permission_required('itempedido.view_itempedido', raise_exception=True)
def get_preco_produto(request):
    produto_id = request.GET.get('produto_id')
    preco = 0
    if produto_id:
        produto = Produto.objects.get(id=produto_id)
        preco = produto.preco
    return JsonResponse({'preco': preco})