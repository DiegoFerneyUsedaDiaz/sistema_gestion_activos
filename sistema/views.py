from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from sistema.models import Activos

# Create your views here.

def lista_activos(request):
    activos = Activos.objects.all()
    return render(request, "computer.html", {"activos": activos})
