from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm, UsuarioUpdateForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})

@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/usuario/')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/criar.html', {'form': form})

@login_required
@permission_required('usuario.change_usuario', raise_exception=True)
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

@login_required
@permission_required('usuario.delete_usuario', raise_exception=True)
def delete(request, usuario_id): 
    Usuario.objects.get(id=usuario_id) .delete()

    return HttpResponseRedirect('/usuario/') 

@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def detail(request, usuario_id):

    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'usuario/detalhar.html', {'usuario': usuario})     
