from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def minhahistoria(request):
    x = mh.objects.all()
    context = {'x': x}
    return render(request, 'minhahistoria.html', context)

def curso(request):
    x = c.objects.all()
    context = {'x': x}
    return render(request, 'curso.html', context)

def habilidades(request):
    x = h.objects.all()
    context = {'x': x}
    return render(request, 'habilidades.html', context)

def estagio(request):
    x = e.objects.all()
    context = {'x': x}
    return render(request, 'estagio.html', context)

def trabalhos(request):
    x = t.objects.all()
    context = {'x': x}
    return render(request, 'trabalhos.html', context)

def memorias(request):
    x = m1.objects.all()
    context = {'x': x}
    return render(request, 'memorias.html', context)