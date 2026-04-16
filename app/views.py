from django.shortcuts import render
from .forms import ProfesionalForm, ServicioForm, EntregableForm, BusquedaServicio
from .models import Servicio


# 🏠 Inicio
def inicio(request):
    return render(request, "app/inicio.html")


# 👨‍🏫 Crear Profesional
def crear_profesional(request):
    if request.method == "POST":
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "app/inicio.html")
    else:
        form = ProfesionalForm()

    return render(request, "app/formulario.html", {"form": form})


# 📚 Crear Servicio
def crear_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "app/inicio.html")
    else:
        form = ServicioForm()

    return render(request, "app/formulario.html", {"form": form})


# 📦 Crear Entregable
def crear_entregable(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "app/inicio.html")
    else:
        form = EntregableForm()

    return render(request, "app/formulario.html", {"form": form})


# 🔍 Buscar Servicio
def buscar_servicio(request):
    if request.method == "POST":
        form = BusquedaServicio(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            servicios = Servicio.objects.filter(nombre__icontains=nombre)
            return render(request, "app/resultados.html", {"servicios": servicios})
    else:
        form = BusquedaServicio()

    return render(request, "app/buscar.html", {"form": form})
