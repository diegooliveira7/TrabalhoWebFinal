from django.shortcuts import render
from app.models import *
# Create your views here.

def index(request):
    estudantes = Estudantes.objects.all()

    context = {
        'estudantes': estudantes,
    }
    return render(request, 'index.html', context)

# def estudantes(request):
#     estudantes = Estudantes.objects.all()

#     context = {
#         'estudantes': estudantes,
#     }
#     return render(request, 'index.html', context)

def estudante(request, id):
    estudante = Estudantes.objects.get(id=id)
    context = {
        'estudante': estudante,
    }
    return render(request, 'estudante.html', context)

