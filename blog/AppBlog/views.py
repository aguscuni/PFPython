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


def busqueda_jugador(request):
    return render(request, "AppBlog/busqueda_jugador.html")


def buscar_jugador(request):
    if not request.GET["jugador"]:
        return HttpResponse("No enviaste datos")

    else:
        jugador_a_buscar = request.GET["jugador"]
        jugadores = Jugador.objects.filter(
            surname=jugador_a_buscar
        ) or Jugador.objects.filter(country=jugador_a_buscar)

        contexto = {"jugador": jugador_a_buscar, "jugadores_encontrados": jugadores}

        return render(request, "AppBlog/resultado_busqueda_jugador.html", contexto)


def busqueda_entrenador(request):
    return render(request, "AppBlog/busqueda_entrenador.html")


def buscar_entrenador(request):
    if not request.GET["entrenador"]:
        return HttpResponse("No enviaste datos")

    else:
        entrenador_a_buscar = request.GET["entrenador"]
        entrenadores = Entrenador.objects.filter(
            surname=entrenador_a_buscar
        ) or Entrenador.objects.filter(country=entrenador_a_buscar)

        contexto = {
            "entrenador": entrenador_a_buscar,
            "entrenadores_encontrados": entrenadores,
        }

        return render(request, "AppBlog/resultado_busqueda_entrenador.html", contexto)


def busqueda_equipo(request):
    return render(request, "AppBlog/busqueda_equipo.html")


def buscar_equipo(request):
    if not request.GET["equipo"]:
        return HttpResponse("No enviaste datos")

    else:
        equipo_a_buscar = request.GET["equipo"]
        equipos = Equipo.objects.filter(name=equipo_a_buscar) or Equipo.objects.filter(
            country=equipo_a_buscar
        )

        contexto = {"equipo": equipo_a_buscar, "equipos_encontrados": equipos}

        return render(request, "AppBlog/resultado_busqueda_equipo.html", contexto)


def listar_equipos(request):

    todos_los_equipos = Equipo.objects.all()

    contexto = {"equipos_encontrados": todos_los_equipos}

    return render(request, "AppBlog/listar_equipos.html", contexto)


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class Jugadorlist(ListView):
    model = Jugador
    template_name = "AppBlog/jugadores_list.html"


class JugadorDetail(DetailView):
    model = Jugador
    template_name = "AppBlog/jugadores_detalle.html"


from django.urls import reverse


class JugadorCreate(CreateView):
    model = Jugador
    success_url = "/AppBlog/jugador/list"
    fields = ["name", "surname", "position", "country", "birth"]


class JugadorUpdate(UpdateView):
    model = Jugador
    success_url = "/AppBlog/jugador/list"
    fields = ["name", "surname", "position", "country", "birth"]


class JugadorDelete(DeleteView):
    model = Jugador
    success_url = "/AppBlog/jugador/list"
