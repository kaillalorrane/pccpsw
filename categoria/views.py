from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Categoria
from .forms import CategoriaForm

def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/index.html', {'categorias': categorias})
def create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/categoria/')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/criar.html', {'form': form})

def edit(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/categoria/')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/atualizar.html', {'form': form})

def delete(request, categoria_id): 
    Categoria.objects.get(id=categoria_id) .delete()

    return HttpResponseRedirect('/categoria/') 

def detail(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    return render(request, 'pessoa/detalhe.html', {'pessoa': categoria})     
