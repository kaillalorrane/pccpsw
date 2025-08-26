from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .models import Estabelecimento
from .forms import EstabelecimentoForm, EstabelecimentoUpdateForm

def index(request):
    estabelecimentos = Estabelecimento.objects.all()
    return render(request, 'estabelecimento/index.html', {'estabelecimentos': estabelecimentos})

def create(request):
    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST)
        
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/estabelecimento/')
    else:
        form = EstabelecimentoForm()
    return render(request, 'estabelecimento/criar.html', {'form': form})

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

def delete(request, estabelecimento_id): 
    Estabelecimento.objects.get(id=estabelecimento_id) .delete()

    return HttpResponseRedirect('/estabelecimento/') 

def detail(request, estabelecimento_id):

    estabelecimento = Estabelecimento.objects.get(id=estabelecimento_id)
    return render(request, 'estabelecimento/detalhar.html', {'estabelecimento': estabelecimento})     

