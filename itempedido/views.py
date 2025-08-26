from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from produto.models import Produto
from .models import Itempedido
from .forms import ItempedidoForm

def index(request):
   itempedidos = Itempedido.objects.all()
   return render(request, 'itempedido/index.html', {'itempedidos': itempedidos})
def create(request):
    if request.method == 'POST':
        form = ItempedidoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/itempedido/')
    else:
        form = ItempedidoForm()
    return render(request, 'itempedido/criar.html', {'form': form})

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

def delete(request, itempedido_id): 
    Itempedido.objects.get(id=itempedido_id) .delete()

    return HttpResponseRedirect('/itempedido/') 

def detail(request, itempedido_id):

    itempedido = Itempedido.objects.get(id=itempedido_id)
    return render(request, 'itempedido/detalhar.html', {'itempedido': itempedido})     

def get_preco_produto(request):
    produto_id = request.GET.get('produto_id')
    preco = 0
    if produto_id:
        produto = Produto.objects.get(id=produto_id)
        preco = produto.preco  
    return JsonResponse({'preco': preco})

def itempedido_create(request):
    if request.method == 'POST':
        form = ItempedidoForm(request.POST)
        if form.is_valid():
            itempedido = form.save(commit=False)   # ainda não salva no banco
            itempedido.preco = itempedido.produto.preco  # pega o preço do produto
            itempedido.save()
            return redirect('itempedido_list')  # ajuste para a sua rota de listagem
    else:
        form = ItempedidoForm()
    return render(request, 'itempedido/criar.html', {'form': form})
