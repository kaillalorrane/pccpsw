from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})
    # return render(request, 'html/layouts-container.html', {'usuarios': usuarios})
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/usuario/')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/criar.html', {'form': form})

def edit(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/usuario/')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/atualizar.html', {'form': form})
def delete(request, id_usuario): 
    Usuario.objects.get(id=id_usuario) .delete()

    return HttpResponseRedirect('/usuario/') 

def detail(request, id_usuario):

    usuario = Usuario.objects.get(id=id_usuario)
    return render(request, 'pessoa/detalhe.html', {'pessoa': usuario})     
