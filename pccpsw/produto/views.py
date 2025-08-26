from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto
from .forms import ProdutoForm, ProdutoUpdateForm

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/index.html', {'produtos': produtos})
def create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/produto/')
    else:
        form = ProdutoForm()
    return render(request, 'produto/criar.html', {'form': form})

def edit(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoUpdateForm(request.POST, instance=produto)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/produto/')
    else:
        form = ProdutoUpdateForm(instance=produto)
    return render(request, 'produto/atualizar.html', {'form': form})

def delete(request, produto_id): 
    Produto.objects.get(id=produto_id) .delete()

    return HttpResponseRedirect('/produto/') 

def detail(request, produto_id):

    produto = Produto.objects.get(id=produto_id)
    return render(request, 'produto/detalhar.html', {'produto': produto})     


