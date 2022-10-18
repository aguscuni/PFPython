from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.forms import JugadorFormulario, EntrenadorFormulario, EquipoFormulario
from AppBlog.models import Jugador, Entrenador, Equipo

# Create your views here.


def inicio(request):
    return render(request, "AppBlog/inicio.html")


def equipos(request):
    return render(request, "AppBlog/equipos.html")


def jugadores(request):
    return render(request, "AppBlog/jugadores.html")


def entrenadores(request):
    return render(request, "AppBlog/entrenadores.html")


def cargar_jugador(request):
    if request.method != "POST":
        mi_formulario = JugadorFormulario()

    else:
        mi_formulario = JugadorFormulario(request.POST)
        if mi_formulario.is_valid():
            information = mi_formulario.cleaned_data
            jugador = Jugador(
                name=information["name"],
                surname=information["surname"],
                position=information["position"],
                country=information["country"],
                birth=information["birth"],
            )
            jugador.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppBlog/cargar_jugador.html", contexto)


def cargar_entrenador(request):
    if request.method != "POST":
        mi_formulario = EntrenadorFormulario()

    else:
        mi_formulario = EntrenadorFormulario(request.POST)
        if mi_formulario.is_valid():
            information = mi_formulario.cleaned_data
            entrenador = Entrenador(
                name=information["name"],
                surname=information["surname"],
                country=information["country"],
                birth=information["birth"],
            )
            entrenador.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppBlog/cargar_entrenador.html", contexto)


def cargar_equipo(request):
    if request.method != "POST":
        mi_formulario = EquipoFormulario()

    else:
        mi_formulario = EquipoFormulario(request.POST)
        if mi_formulario.is_valid():
            information = mi_formulario.cleaned_data
            equipo = Equipo(
                name=information["name"],
                country=information["country"],
                foundation_year=information["foundation_year"],
            )
            equipo.save()
            return render(request, "AppBlog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppBlog/cargar_equipo.html", contexto)
