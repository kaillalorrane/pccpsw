from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm, UsuarioUpdateForm

def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/usuario/')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/criar.html', {'form': form})

def edit(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/usuario/')
    else:
        form = UsuarioUpdateForm(instance=usuario)
    return render(request, 'usuario/atualizar.html', {'form': form})
def delete(request, usuario_id): 
    Usuario.objects.get(id=usuario_id) .delete()

    return HttpResponseRedirect('/usuario/') 

def detail(request, usuario_id):

    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'usuario/detalhar.html', {'usuario': usuario})     
