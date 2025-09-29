from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from sistema.models import Activos
from .forms import ActivoForm


# Create your views here.

def computer(request):
    activos = Activos.objects.all()
    return render(request, "computer.html", {"activos": activos})


def crear_activo(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computer')  # vuelve a la lista
    else:
        form = ActivoForm()
    return render(request, 'crear_activo.html', {'form': form})
