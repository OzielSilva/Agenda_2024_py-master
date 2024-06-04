from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from contatos.models import Contato

# Create your views here.

def contato(request, info_id):
    contato = get_object_or_404(Contato, pk=info_id)
    return render(request, 'contatos/det_contato.html', {"contato": contato})

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def cadastrar(request):
    return render(request, 'usuarios/cadastrar.html')
