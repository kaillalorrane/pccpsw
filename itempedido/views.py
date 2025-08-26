from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from produto.models import Produto
from pedido.models import Pedido
from .models import Itempedido
from .forms import ItempedidoForm
from django.contrib.auth.decorators import login_required

def index(request):
   itempedidos = Itempedido.objects.all()
   return render(request, 'itempedido/index.html', {'itempedidos': itempedidos})
@login_required
def create(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    pedido = Pedido.objects.get(cliente=request.user, status="aberto")
    if request.method == "POST":
        quantidade = int(request.POST.get("quantidade", 1))
        item = Itempedido.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=quantidade,
            total=produto.preco * quantidade
        )
        return redirect("index.html")  # ajuste para a rota da listagem

    return render(request, "itempedido/criar.html", {"produto": produto})

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