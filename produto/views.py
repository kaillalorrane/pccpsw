from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto
from .forms import ProdutoForm, ProdutoUpdateForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('produto.view_produto', raise_exception=True)
def index(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/index.html', {'produtos': produtos})

@login_required
@permission_required('produto.add_produto', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/produto/')
    else:
        form = ProdutoForm()
    return render(request, 'produto/criar.html', {'form': form})

@login_required
@permission_required('produto.change_produto', raise_exception=True)
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

@login_required
@permission_required('produto.delete_produto', raise_exception=True)
def delete(request, produto_id): 
    Produto.objects.get(id=produto_id) .delete()

    return HttpResponseRedirect('/produto/') 

@login_required
@permission_required('produto.view_produto', raise_exception=True)
def detail(request, produto_id):

    produto = Produto.objects.get(id=produto_id)
    return render(request, 'produto/detalhar.html', {'produto': produto})     


