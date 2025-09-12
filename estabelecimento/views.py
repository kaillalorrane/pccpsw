from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .models import Estabelecimento
from .forms import EstabelecimentoForm, EstabelecimentoUpdateForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('estabelecimento.view_estabelecimento', raise_exception=True)
def index(request):
    estabelecimentos = Estabelecimento.objects.all()
    return render(request, 'estabelecimento/index.html', {'estabelecimentos': estabelecimentos})

@login_required
@permission_required('estabelecimento.add_estabelecimento', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/estabelecimento/')
    else:
        form = EstabelecimentoForm()
    return render(request, 'estabelecimento/criar.html', {'form': form})

@login_required
@permission_required('estabelecimento.change_estabelecimento', raise_exception=True)
def edit(request, estabelecimento_id):
    estabelecimento = Estabelecimento.objects.get(id=estabelecimento_id)
    if request.method == 'POST':
        form = EstabelecimentoUpdateForm(request.POST, instance=estabelecimento)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/estabelecimento/')
    else:
        form = EstabelecimentoUpdateForm(instance=estabelecimento)
    return render(request, 'estabelecimento/atualizar.html', {'form': form})

@login_required
@permission_required('estabelecimento.delete_estabelecimento', raise_exception=True)
def delete(request, estabelecimento_id): 
    Estabelecimento.objects.get(id=estabelecimento_id) .delete()

    return HttpResponseRedirect('/estabelecimento/') 

@login_required
@permission_required('estabelecimento.view_estabelecimento', raise_exception=True)
def detail(request, estabelecimento_id):

    estabelecimento = Estabelecimento.objects.get(id=estabelecimento_id)
    return render(request, 'estabelecimento/detalhar.html', {'estabelecimento': estabelecimento})     

