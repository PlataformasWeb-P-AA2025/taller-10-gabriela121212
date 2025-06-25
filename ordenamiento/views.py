from django.shortcuts import render, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm


def parroquias_con_barrios(request):
    parroquias = Parroquia.objects.prefetch_related('mis_barrios').all()
    return render(request, 'parroquiasBarrios.html', {'parroquias': parroquias})


def lista_barrios(request,id):
    barrio = Barrio.objects.get(pk=id)
    barrios={'barrio':barrio}
    return render(request, 'lista_barrios.html',barrios)


def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barrios')
    else:
        form = ParroquiaForm()
    return render(request, 'form_parroquia.html', {'form': form})


def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barrios')
    else:
        form = BarrioForm()
    return render(request, 'form_barrio.html', {'form': form})
